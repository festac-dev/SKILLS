#!/usr/bin/env python3
"""
Build the AI Model Navigation Index for SKILLS.

Generates:
1. runtime/indexes/skills.db (SQLite with FTS5 search)
2. runtime/indexes/skills_quickref.tsv (Grep-friendly single-line TSV)
3. runtime/indexes/categories/*.md (20 domain-specific markdown indexes)
4. runtime/indexes/collections.md (Directory of all collections)
5. runtime/indexes/SKILLS_INDEX.md (Master navigation guide for AI agents)
"""

import json
import os
import re
import sqlite3
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).resolve().parents[1]
INDEXES_DIR = ROOT / "runtime" / "indexes"
CATEGORIES_DIR = INDEXES_DIR / "categories"

CATEGORY_META = {
    "ai-agents": {
        "title": "AI Agents, Autonomous Workflows & Orchestration",
        "desc": "Autonomous agents, subagents, multi-agent swarms, tool calling, memory, and orchestration.",
    },
    "ai-prompts-llms": {
        "title": "Prompt Engineering, LLM Interfaces & Fine-Tuning",
        "desc": "System prompts, task prompting, persona prompts, OpenAI/Anthropic APIs, RAG, and embeddings.",
    },
    "cloud-devops": {
        "title": "Cloud Platforms, Infrastructure as Code & DevOps",
        "desc": "AWS, GCP, Azure, Terraform, CloudFormation, Ansible, CI/CD pipelines, and cloud operations.",
    },
    "containers-kubernetes": {
        "title": "Docker, Containers, Kubernetes & Orchestration",
        "desc": "Dockerfiles, container builds, Kubernetes pods/deployments/ingress, Helm charts, and container runtimes.",
    },
    "security-appsec": {
        "title": "Application Security, Vulnerability Analysis & Exploits",
        "desc": "AppSec, CVE vulnerability analysis, penetration testing, exploit detection, fuzzing, and secure coding.",
    },
    "security-auditing": {
        "title": "Security Audits, Hardening, Compliance & Threat Modeling",
        "desc": "RedHat ProdSec, SlowMist, Trail of Bits, IAM policies, compliance (SOC2/HIPAA), hardening, and firewall rules.",
    },
    "web-frontend": {
        "title": "Frontend Development, React, Vue, Next.js & Frameworks",
        "desc": "React, Vue, Svelte, Next.js, Nuxt, Angular, Astro, TypeScript frontend, DOM, and client state.",
    },
    "web-styling-ui": {
        "title": "UI/UX Design Systems, Tailwind, CSS & Components",
        "desc": "Tailwind CSS, design systems, Shadcn UI, CSS animations, responsive layouts, icons, and UX patterns.",
    },
    "backend-apis": {
        "title": "Backend Development, REST APIs, GraphQL & Microservices",
        "desc": "FastAPI, Express, Django, Flask, Spring, REST endpoints, GraphQL schemas, gRPC, and webhooks.",
    },
    "databases-storage": {
        "title": "Databases, SQL, PostgreSQL, Supabase, Prisma & Caching",
        "desc": "PostgreSQL, MySQL, SQLite, Supabase, Neon, Prisma ORM, Redis caching, migrations, and query tuning.",
    },
    "testing-qa": {
        "title": "Testing, QA, Automation, Playwright, Jest & Cypress",
        "desc": "End-to-end testing, Playwright CLI, Cypress, unit tests (pytest/Jest), test mocks, and QA verification.",
    },
    "graphics-3d-motion": {
        "title": "3D Modeling, Blender, Three.js, WebGL & Canvas",
        "desc": "Three.js scenes, Blender scripting, WebGL shaders, 3D meshes, procedural graphics, and spatial rendering.",
    },
    "media-video-audio": {
        "title": "Video Production, Audio Processing, TTS & Media Generation",
        "desc": "Motion Studio, Remotion, FFmpeg video editing, ElevenLabs TTS, audio ducking, subtitles, and media pipelines.",
    },
    "mobile-apps": {
        "title": "Mobile App Development, React Native, Flutter, iOS & Android",
        "desc": "React Native, Expo, Flutter, Swift, SwiftUI, Kotlin, Android SDK, and cross-platform mobile patterns.",
    },
    "product-management": {
        "title": "Product Strategy, PRDs, Roadmaps & Feature Specs",
        "desc": "Product requirements documents (PRDs), user journeys, feature roadmaps, OKRs, and discovery protocols.",
    },
    "marketing-growth": {
        "title": "Marketing, SEO, Copywriting & Content Growth",
        "desc": "Content marketing, copywriting, SEO optimization, growth tactics, email campaigns, and analytics.",
    },
    "blockchain-web3": {
        "title": "Smart Contracts, Solana, Ethereum & Web3",
        "desc": "Solana development, Ethereum Solidity contracts, DeFi protocols, token standards, and Web3 SDKs.",
    },
    "data-science-scientific": {
        "title": "Data Science, Scientific Computing, Bioinformatics & NCBI",
        "desc": "Scientific computing, bioinformatics, NCBI datasets, genomics, chemistry modeling, pandas, and data analytics.",
    },
    "software-architecture": {
        "title": "Software Architecture, Clean Code, Git & Monorepos",
        "desc": "Architectural design patterns, clean code principles, refactoring, Git workflows, and monorepo management.",
    },
    "programming-languages": {
        "title": "Programming Languages, CLI Tools, Compilers & Utilities",
        "desc": "Python, TypeScript, Go, Rust, C++, shell scripting, CLI tools, algorithms, and developer utilities.",
    },
}


def classify(s):
    text = (s.get("id", "") + " " + s.get("name", "") + " " + s.get("path", "") + " " + s.get("description", "")).lower()
    col = s.get("path", "").split("/")[0]

    if col in ("slowmist-security", "redhat-security", "unitone-security", "clawsec", "cloudflare-security-audit-skill"):
        return "security-auditing"
    if col in ("cybersecurity-skills", "trailofbits-skills", "zero-lab-security"):
        return "security-appsec"
    if col in ("solana-foundation-solana-dev-skill",):
        return "blockchain-web3"
    if col in ("blender-skills", "origami-3d", "threejs-full-stack", "arjun988-blender-skills"):
        return "graphics-3d-motion"
    if col in ("motionmaxxing", "motion-studio", "media2threejs", "mediagen", "manim-skills", "manim-render-review", "video-cut-skills", "video-shotcraft", "heygen-com-hyperframes", "heygen-com-hyperframes-additional", "elevenlabs-skills"):
        return "media-video-audio"
    if col in ("mobile-mcp-skills", "expo-skills", "flutter-agent-plugins"):
        return "mobile-apps"
    if col in ("microsoft-playwright-cli",):
        return "testing-qa"
    if col in ("supabase-skills", "prisma-skills", "neondatabase-agent-skills", "neondatabase-agent-skills-additional"):
        return "databases-storage"
    if col in ("shadcn-ui", "nextlevelbuilder-ui-ux-pro-max-skill", "nextlevelbuilder-ui-ux-pro-max-skill-additional", "greensock-gsap-skills", "emilkowalski-skills", "emilkowalski-skills-additional", "leonxlnx-taste-skill"):
        return "web-styling-ui"
    if col in ("scientific-agent-skills",):
        return "data-science-scientific"
    if col in ("kostja94-marketing-skills", "marketing-skills", "aaron-he-zhu-aaron-marketing-skills"):
        return "marketing-growth"
    if col in ("pm-phuryn", "pm-on-purpose", "deanpeters-product-manager-skills"):
        return "product-management"
    if col in ("aws-agent-toolkit-for-aws", "hashicorp-skills", "devops-cli-skills", "devops-lgbarn", "devops-notharshhaa", "cc-devops-skills", "azure-devops-skills"):
        if any(k in text for k in ["docker", "kubernetes", "k8s", "container", "helm"]):
            return "containers-kubernetes"
        return "cloud-devops"
    if col in ("anthropics-knowledge-work-plugins", "agent-browser-skills", "mastra-ai-skills", "orchestra-research-ai-research-skills"):
        return "ai-agents"
    if col in ("aj-geddes-useful-ai-prompts", "openai-plugins", "anthropic-skills"):
        if any(k in text for k in ["prompt", "rewrite", "critique", "translate", "summarize"]):
            return "ai-prompts-llms"
        return "ai-agents"

    if re.search(r"\b(solidity|smart contract|ethereum|web3|solana|defi|token|erc20)\b", text):
        return "blockchain-web3"
    if re.search(r"\b(bioinformatics|genomics|protein|chemistry|scientific|biology|physics|ncbi)\b", text):
        return "data-science-scientific"
    if re.search(r"\b(cve|exploit|penetration test|xss|sql injection|payload|vulnerability|malware|fuzzing)\b", text):
        return "security-appsec"
    if re.search(r"\b(security audit|compliance|hardening|soc2|hipaa|iam policy|firewall|rbac|threat model)\b", text):
        return "security-auditing"
    if re.search(r"\b(playwright|cypress|jest|pytest|unit test|integration test|mocking|e2e test|selenium|qa)\b", text):
        return "testing-qa"
    if re.search(r"\b(kubernetes|k8s|docker|dockerfile|helm|containerd|podman)\b", text):
        return "containers-kubernetes"
    if re.search(r"\b(aws|azure|gcp|terraform|ansible|cloudformation|ci\/cd|github actions|serverless|devops)\b", text):
        return "cloud-devops"
    if re.search(r"\b(postgres|postgresql|mongodb|mysql|sqlite|supabase|prisma|redis|dynamodb|sql|orm|migration)\b", text):
        return "databases-storage"
    if re.search(r"\b(tailwind|css|sass|styling|design system|shadcn|component library|theme|icons|figma)\b", text):
        return "web-styling-ui"
    if re.search(r"\b(react|vue|svelte|next\.js|nuxt|angular|astro|remix|frontend|dom|jsx|tsx)\b", text):
        return "web-frontend"
    if re.search(r"\b(three\.js|blender|webgl|shader|3d mesh|geometry|animation|keyframes|canvas)\b", text):
        return "graphics-3d-motion"
    if re.search(r"\b(video edit|audio|tts|speech synthesis|remotion|ffmpeg|voice|transcription|video)\b", text):
        return "media-video-audio"
    if re.search(r"\b(react native|flutter|expo|ios|android|swiftui|kotlin mobile|xcode)\b", text):
        return "mobile-apps"
    if re.search(r"\b(product manager|prd|user story|roadmap|user journey|feature specification|okr)\b", text):
        return "product-management"
    if re.search(r"\b(seo|copywriting|marketing|growth|campaign|analytics|conversion rate|ad copy)\b", text):
        return "marketing-growth"
    if re.search(r"\b(fastapi|express|django|flask|spring boot|graphql|rest api|microservice|grpc|endpoint|webhook)\b", text):
        return "backend-apis"
    if re.search(r"\b(agent|orchestration|tool calling|function calling|subagent|multi-agent|workflow)\b", text):
        return "ai-agents"
    if re.search(r"\b(llm|prompt|system prompt|openai|anthropic|claude|rag|embeddings|fine-tune|huggingface)\b", text):
        return "ai-prompts-llms"
    if re.search(r"\b(clean code|refactoring|design pattern|git|monorepo|architecture|code review)\b", text):
        return "software-architecture"

    return "programming-languages"


def build_all():
    print("Loading runtime/index.json...")
    with open(ROOT / "runtime/index.json") as f:
        skills = json.load(f)["skills"]
    print(f"Loaded {len(skills)} skills.")

    INDEXES_DIR.mkdir(parents=True, exist_ok=True)
    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)

    # Classify each skill
    classified_skills = []
    category_buckets = defaultdict(list)
    collection_buckets = defaultdict(list)

    for s in skills:
        cat = classify(s)
        col = s.get("path", "").split("/")[0]
        desc_clean = " ".join(s.get("description", "").split())
        item = {
            "id": s["id"],
            "name": s.get("name", s["id"]),
            "category": cat,
            "collection": col,
            "path": s["path"],
            "description": desc_clean,
            "sha256": s.get("sha256", ""),
        }
        classified_skills.append(item)
        category_buckets[cat].append(item)
        collection_buckets[col].append(item)

    # 1. Build SQLite database with FTS5
    db_path = INDEXES_DIR / "skills.db"
    if db_path.exists():
        db_path.unlink()
    print(f"Creating SQLite FTS5 database at {db_path}...")
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE skills (
            id TEXT PRIMARY KEY,
            name TEXT,
            category TEXT,
            collection TEXT,
            path TEXT,
            description TEXT,
            sha256 TEXT
        );
    """)
    cursor.execute("CREATE INDEX idx_skills_cat ON skills(category);")
    cursor.execute("CREATE INDEX idx_skills_col ON skills(collection);")
    cursor.execute("""
        CREATE VIRTUAL TABLE skills_fts USING fts5(
            id,
            name,
            category,
            collection,
            description,
            path,
            content='skills',
            content_rowid='rowid'
        );
    """)

    cursor.executemany("""
        INSERT INTO skills (id, name, category, collection, path, description, sha256)
        VALUES (:id, :name, :category, :collection, :path, :description, :sha256);
    """, classified_skills)

    cursor.execute("""
        INSERT INTO skills_fts (rowid, id, name, category, collection, description, path)
        SELECT rowid, id, name, category, collection, description, path FROM skills;
    """)
    conn.commit()
    conn.close()
    print(f"Database built successfully ({db_path.stat().st_size // (1024*1024)} MB).")

    # 2. Build skills_quickref.tsv (plain text, grep-friendly)
    tsv_path = INDEXES_DIR / "skills_quickref.tsv"
    print(f"Generating TSV quickref at {tsv_path}...")
    with open(tsv_path, "w", encoding="utf-8") as f:
        f.write("# id\tname\tcategory\tcollection\tpath\tdescription\n")
        for s in classified_skills:
            desc_short = s["description"][:160].replace("\t", " ")
            f.write(f"{s['id']}\t{s['name']}\t{s['category']}\t{s['collection']}\t{s['path']}\t{desc_short}\n")
    print(f"TSV quickref built successfully ({tsv_path.stat().st_size // (1024*1024)} MB).")

    # 3. Build collections.md
    print("Generating collections directory...")
    collections_data = []
    if (ROOT / "COLLECTIONS.json").exists():
        try:
            with open(ROOT / "COLLECTIONS.json") as f:
                c_json = json.load(f)
                collections_data = c_json.get("collections", [])
        except Exception:
            pass

    col_meta_map = {c["directory"]: c for c in collections_data}
    col_md_path = INDEXES_DIR / "collections.md"
    with open(col_md_path, "w", encoding="utf-8") as f:
        f.write("# SKILLS Collections Directory\n\n")
        f.write("This directory lists all collections included in the SKILLS library. Use this to locate which collection owns specific domain capabilities.\n\n")
        f.write("| Collection Folder | Source Repository | Skills Count | Primary Domains |\n")
        f.write("|---|---|---|---|\n")
        for col_name, items in sorted(collection_buckets.items(), key=lambda x: -len(x[1])):
            source_repo = col_meta_map.get(col_name, {}).get("repository", col_name)
            col_cats = Counter(i["category"] for i in items).most_common(2)
            domains_str = ", ".join(f"`{c[0]}` ({c[1]})" for c in col_cats)
            f.write(f"| `{col_name}` | [{source_repo}](https://github.com/{source_repo}) | {len(items)} | {domains_str} |\n")

    # 4. Build individual category markdown indexes
    print("Generating category markdown indexes...")
    for cat_slug, meta in CATEGORY_META.items():
        cat_file = CATEGORIES_DIR / f"{cat_slug}.md"
        items = category_buckets[cat_slug]
        items.sort(key=lambda x: (x["collection"], x["name"]))

        with open(cat_file, "w", encoding="utf-8") as f:
            f.write(f"# Category: {meta['title']}\n\n")
            f.write(f"> **Overview**: {meta['desc']}\n")
            f.write(f"> **Total Skills**: {len(items)}\n\n")
            f.write("### Quick Search Commands\n")
            f.write("```bash\n")
            f.write(f"# Search specifically within this category:\n")
            f.write(f"python3 /data/home/SKILLS/scripts/search.py --category {cat_slug} '<query>'\n\n")
            f.write(f"# Or grep this category from the quickref TSV:\n")
            f.write(f"grep '{cat_slug}' /data/home/SKILLS/runtime/indexes/skills_quickref.tsv | grep -i '<topic>' | head -n 10\n")
            f.write("```\n\n")
            f.write("### Skills Table\n\n")
            f.write("| Skill ID | Collection | Path | Description |\n")
            f.write("|---|---|---|---|\n")

            # For very large categories, show top 500 or paginate gracefully
            display_items = items[:600] if len(items) > 600 else items
            for it in display_items:
                desc_snippet = it["description"][:180].replace("|", "\\|")
                f.write(f"| `{it['id']}` | `{it['collection']}` | [{it['path']}](../../{it['path']}) | {desc_snippet} |\n")

            if len(items) > 600:
                f.write(f"\n*...and {len(items) - 600} more skills in this category. Use `python3 /data/home/SKILLS/scripts/search.py --category {cat_slug} '<query>'` or `skills.db` for full access.*\n")

    # 5. Build SKILLS_INDEX.md
    print("Generating master AI navigation guide SKILLS_INDEX.md...")
    master_index_path = INDEXES_DIR / "SKILLS_INDEX.md"
    with open(master_index_path, "w", encoding="utf-8") as f:
        f.write("# SKILLS Index & Fast Lookup Guide for AI Models\n\n")
        f.write("> **IMPORTANT NOTICE FOR AI MODELS**:\n")
        f.write("> **DO NOT** attempt to scan all directories or parse `COLLECTIONS.json` (83MB) or `runtime/index.json` (9.2MB). Doing so will exhaust your context window.\n")
        f.write("> This repository contains **19,573 skills**. Use one of the fast, targeted methods below to find and load only the specific skill you need.\n\n")

        f.write("## 1. Instant CLI Search (Recommended)\n\n")
        f.write("Run the search tool from your shell / command execution tool. It searches all 19,573 skills in milliseconds and returns exact paths and summaries:\n\n")
        f.write("```bash\n")
        f.write("# 1. Keyword search (fast full-text ranking):\n")
        f.write("python3 /data/home/SKILLS/scripts/search.py 'kubernetes ingress deploy'\n\n")
        f.write("# 2. Search filtered by domain category:\n")
        f.write("python3 /data/home/SKILLS/scripts/search.py --category cloud-devops 'terraform aws'\n\n")
        f.write("# 3. Inspect a skill and view its instructions without reading the entire file:\n")
        f.write("python3 /data/home/SKILLS/scripts/search.py --info <skill-id>\n\n")
        f.write("# 4. Machine-readable JSON output (for automated parsing):\n")
        f.write("python3 /data/home/SKILLS/scripts/search.py --json --limit 5 'react tailwind'\n")
        f.write("```\n\n")

        f.write("## 2. Instant Grep Quickref (Zero Dependencies)\n\n")
        f.write("A single-line TSV index of all 19,573 skills (`id`, `name`, `category`, `collection`, `path`, `summary`):\n\n")
        f.write("```bash\n")
        f.write("grep -i 'fastapi' /data/home/SKILLS/runtime/indexes/skills_quickref.tsv | head -n 10\n")
        f.write("```\n\n")

        f.write("## 3. SQLite Full-Text Search (FTS5)\n\n")
        f.write("The database `/data/home/SKILLS/runtime/indexes/skills.db` is indexed with SQLite FTS5 for sub-millisecond queries:\n\n")
        f.write("```bash\n")
        f.write("sqlite3 /data/home/SKILLS/runtime/indexes/skills.db \\\n")
        f.write("  \"SELECT id, category, path, description FROM skills_fts WHERE skills_fts MATCH 'postgres' LIMIT 5;\"\n")
        f.write("```\n\n")

        f.write("## 4. Browse by Domain Categories\n\n")
        f.write("If you need to explore available skills for a specific domain, read ONLY the corresponding category index file:\n\n")
        f.write("| Category | Skills | Description | Category File |\n")
        f.write("|---|---|---|---|\n")

        for cat_slug, meta in sorted(CATEGORY_META.items(), key=lambda x: -len(category_buckets[x[0]])):
            count = len(category_buckets[cat_slug])
            f.write(f"| **{meta['title']}** | {count} | {meta['desc']} | [categories/{cat_slug}.md](categories/{cat_slug}.md) |\n")

        f.write("\n## 5. Collections Directory\n\n")
        f.write(f"To see all 115 imported upstream collections and which domains they cover, consult [collections.md](collections.md).\n\n")

        f.write("## 6. How to Load and Apply a Skill\n\n")
        f.write("Once you identify the relevant skill path (e.g. `openai-plugins/plugins/adobe/skills/adobe-create-mockups/SKILL.md`):\n")
        f.write("1. Read **only** that specific `SKILL.md` file using your file read tool.\n")
        f.write("2. Apply the instructions to the user's project.\n")
        f.write("3. Never read entire collection folders or unneeded files.\n")

    print("Master AI navigation guide generated.")

if __name__ == "__main__":
    build_all()
