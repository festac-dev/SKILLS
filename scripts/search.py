#!/usr/bin/env python3
"""
Fast Skill Search & Discovery CLI for AI Models and Developers.

Searches 19,573 skills across 115 collections in <50ms without context bloat.

Usage:
  python3 search.py "<keywords>"
  python3 search.py --category cloud-devops "terraform"
  python3 search.py --limit 10 "react hooks"
  python3 search.py --json "fastapi"
  python3 search.py --info <skill-id>
  python3 search.py --categories
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path


def find_skills_root():
    # 1. Environment variable if set
    if "SKILLS_DIR" in os.environ and Path(os.environ["SKILLS_DIR"]).is_dir():
        return Path(os.environ["SKILLS_DIR"]).resolve()

    current = Path(__file__).resolve().parent

    # Check upward paths
    for p in [current, current.parent, current.parent.parent]:
        if (p / "runtime" / "indexes" / "skills.db").exists():
            return p
        if (p / "SKILLS" / "runtime" / "indexes" / "skills.db").exists():
            return p / "SKILLS"

    # Standard fallback
    fallback = Path("/data/home/SKILLS")
    if fallback.exists():
        return fallback

    return current


ROOT = find_skills_root()
INDEX_DIR = ROOT / "runtime" / "indexes"
DB_PATH = INDEX_DIR / "skills.db"
TSV_PATH = INDEX_DIR / "skills_quickref.tsv"


def clean_fts_query(query):
    words = re.findall(r"[\w-]+", query)
    if not words:
        return ""
    # Search with prefix matching for high recall
    tokens = [f'"{w}"*' for w in words]
    return " OR ".join(tokens)


def search_db(query, category=None, collection=None, limit=5):
    if not DB_PATH.exists():
        return search_tsv(query, category, collection, limit)

    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    fts_q = clean_fts_query(query) if query else ""

    conditions = []
    params = []

    if fts_q:
        conditions.append("skills_fts MATCH ?")
        params.append(fts_q)

    if category:
        conditions.append("category = ?")
        params.append(category)

    if collection:
        conditions.append("collection = ?")
        params.append(collection)

    where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
    order_clause = " ORDER BY rank " if fts_q else " ORDER BY name "

    sql = f"""
        SELECT id, name, category, collection, path, description
        FROM skills_fts
        {where_clause}
        {order_clause}
        LIMIT ?;
    """
    params.append(limit)

    try:
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    except sqlite3.OperationalError:
        # Fallback to standard LIKE matching if query has complex syntax
        like_conds = []
        like_params = []
        for word in query.split():
            like_conds.append("(id LIKE ? OR name LIKE ? OR description LIKE ?)")
            like_params.extend([f"%{word}%", f"%{word}%", f"%{word}%"])
        if category:
            like_conds.append("category = ?")
            like_params.append(category)
        if collection:
            like_conds.append("collection = ?")
            like_params.append(collection)
        where_like = " WHERE " + " AND ".join(like_conds) if like_conds else ""
        cursor.execute(f"SELECT id, name, category, collection, path, description FROM skills {where_like} LIMIT ?;", like_params + [limit])
        rows = cursor.fetchall()

    conn.close()

    results = []
    for r in rows:
        results.append({
            "id": r[0],
            "name": r[1],
            "category": r[2],
            "collection": r[3],
            "path": r[4],
            "description": r[5],
        })
    return results


def search_tsv(query, category=None, collection=None, limit=5):
    if not TSV_PATH.exists():
        return []

    tokens = [t.lower() for t in query.split() if t]
    matches = []

    with open(TSV_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split("\t")
            if len(parts) < 6:
                continue
            sid, name, cat, col, path, desc = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]

            if category and cat != category:
                continue
            if collection and col != collection:
                continue

            row_text = f"{sid} {name} {cat} {col} {desc}".lower()
            if not tokens or any(t in row_text for t in tokens):
                matches.append({
                    "id": sid,
                    "name": name,
                    "category": cat,
                    "collection": col,
                    "path": path,
                    "description": desc,
                })
                if len(matches) >= limit:
                    break

    return matches


def show_info(identifier):
    conn = sqlite3.connect(str(DB_PATH)) if DB_PATH.exists() else None
    skill = None
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, name, category, collection, path, description, sha256 FROM skills WHERE id = ? OR name = ? OR path = ? LIMIT 1;",
            (identifier, identifier, identifier)
        )
        row = cursor.fetchone()
        if not row:
            # Try partial match
            cursor.execute(
                "SELECT id, name, category, collection, path, description, sha256 FROM skills WHERE id LIKE ? LIMIT 1;",
                (f"%{identifier}%",)
            )
            row = cursor.fetchone()
        if row:
            skill = {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "collection": row[3],
                "path": row[4],
                "description": row[5],
                "sha256": row[6],
            }
        conn.close()

    if not skill:
        print(f"Skill '{identifier}' not found in index.")
        return

    full_path = ROOT / skill["path"]
    print("=" * 70)
    print(f"SKILL ID   : {skill['id']}")
    print(f"NAME       : {skill['name']}")
    print(f"CATEGORY   : {skill['category']}")
    print(f"COLLECTION : {skill['collection']}")
    print(f"PATH       : {full_path}")
    print("=" * 70)
    print("\nDESCRIPTION:\n" + skill["description"] + "\n")

    if full_path.exists():
        print("-" * 70)
        print("PREVIEW (First 40 lines of SKILL.md):")
        print("-" * 70)
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                lines = [f.readline() for _ in range(40)]
                print("".join(lines).strip())
        except Exception as e:
            print(f"Could not read preview: {e}")
    else:
        print(f"(File at {full_path} is not locally present)")
    print("=" * 70)


def list_categories():
    if DB_PATH.exists():
        conn = sqlite3.connect(str(DB_PATH))
        cursor = conn.cursor()
        cursor.execute("SELECT category, COUNT(*) FROM skills GROUP BY category ORDER BY COUNT(*) DESC;")
        rows = cursor.fetchall()
        conn.close()
        print(f"{'CATEGORY':<28} | {'COUNT':<6} | {'INDEX FILE'}")
        print("-" * 75)
        for cat, cnt in rows:
            print(f"{cat:<28} | {cnt:<6} | {ROOT}/runtime/indexes/categories/{cat}.md")
    else:
        print("Index database not found.")


def main():
    parser = argparse.ArgumentParser(
        description="Search 19,573 skills across 115 collections in <50ms without context bloat."
    )
    parser.add_argument("query", nargs="?", default="", help="Keywords or topic to search for")
    parser.add_argument("--category", "-c", help="Filter by category slug (e.g., cloud-devops, ai-agents)")
    parser.add_argument("--collection", help="Filter by collection name (e.g., openai-plugins, aws-agent-toolkit-for-aws)")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Maximum results to return (default: 5)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")
    parser.add_argument("--info", "-i", help="Display full details and preview for a skill ID or path")
    parser.add_argument("--categories", action="store_true", help="List all 20 categories and counts")

    args = parser.parse_args()

    if args.categories:
        list_categories()
        return

    if args.info:
        show_info(args.info)
        return

    if not args.query and not args.category and not args.collection:
        parser.print_help()
        return

    results = search_db(args.query, category=args.category, collection=args.collection, limit=args.limit)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print(f"No skills found matching '{args.query}'.")
        print(f"Tip: Try broader search terms or browse {ROOT}/runtime/indexes/SKILLS_INDEX.md.")
        return

    print(f"\nFound {len(results)} matching skill(s) for query '{args.query}':\n")
    for i, r in enumerate(results, 1):
        full_path = ROOT / r["path"]
        print(f"{i}. [{r['category']}] {r['id']}")
        print(f"   Collection : {r['collection']}")
        print(f"   Path       : {full_path}")
        desc_snippet = r["description"][:200] + ("..." if len(r["description"]) > 200 else "")
        print(f"   Summary    : {desc_snippet}\n")

    print("Tip: To preview instructions for any skill above without reading the whole file, run:")
    print(f"python3 /data/home/search_skills.py --info '{results[0]['id']}'\n")


if __name__ == "__main__":
    main()
