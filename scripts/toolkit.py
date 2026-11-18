#!/usr/bin/env python3
"""Maintain and validate the toolkit without dependencies or external actions."""

import argparse
import importlib.util
from collections import Counter
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = {"orchestrator", "specialists", "references", "templates", "quality-gates", "playbooks", "scripts", "tests", "reports", "evals", "examples", "motion-studio", ".codex-plugin", ".agents"}
ROOT_FILES = {"README.md", "SKILL.md", "AGENTS.md", "CLAUDE.md", "CATALOG.md", "manifest.json", ".gitignore", "COLLECTIONS.md", "COLLECTION_RULES.md", "COLLECTIONS.json", "LICENSE", "NOTICE.md", ".gitattributes", "install.sh", "native-skills.tsv"}
SKIP = {".git", "__pycache__", ".pytest_cache", "dist", "node_modules", ".native", "skills-library", "runtime"}
DRY_RUNS = [
    ("Build a keyboard-driven TUI on Termux with no mouse.", "cli"),
    ("Fix duplicate webhook processing in the backend API.", "backend"),
    ("Review Foundry proxy storage and Solidity reentrancy before a testnet release.", "solidity"),
    ("Repair a responsive form and frontend focus at high zoom.", "frontend"),
    ("Migrate a shared package through a monorepo codemod.", "monorepo"),
]


def source_files(root):
    imported = set()
    if (root / "COLLECTIONS.json").exists():
        collection_records = json.loads((root / "COLLECTIONS.json").read_text())["collections"]
        imported = {r["directory"] for r in collection_records}
        if not imported or len(imported) != len(collection_records) or any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in DIRECTORIES for name in imported):
            raise ValueError("Invalid imported collection directories")
    files = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if rel.parts[0] in imported or any(part in SKIP for part in rel.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink is not a toolkit source: {rel}")
        if not path.is_file():
            continue
        if rel.parts[0] not in DIRECTORIES and str(rel) not in ROOT_FILES:
            raise ValueError(f"Unexpected root file: {rel}")
        allowed = {".md", ".json", ".py", ".gitignore"}
        if rel.parts[0] in {"scripts", "tests"} or str(rel) in {"install.sh", "native-skills.tsv"}:
            allowed |= {".sh", ".tsv", ".mjs"}
        if rel.parts[0] == "motion-studio":
            allowed |= {".sh", ".ts", ".tsx", ".css", ".html", ".js", ".yaml"}
        if rel.parts[0] == "examples":
            allowed |= {".html", ".js", ".css", ".svg"}
        if path.suffix not in allowed and path.name not in {".gitignore", "LICENSE", ".gitattributes"}:
            raise ValueError(f"Unexpected source type: {rel}")
        files.append(rel.as_posix())
    return files


def prose(text):
    """Ignore fenced code when interpreting headings and Markdown links."""
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def headings(text):
    return re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", prose(text), re.M)


def local_target(root, origin, target):
    target = target.strip().strip("<>")
    parts = urlsplit(target)
    if parts.scheme or parts.netloc:
        if parts.scheme not in {"https", "http", "mailto"}:
            raise ValueError(f"Unsupported link scheme: {target}")
        return None
    raw = unquote(parts.path)
    if raw.startswith("/") or "\\" in raw:
        raise ValueError(f"Non-portable local path: {target}")
    candidate = (root / origin).parent / raw if raw else root / origin
    resolved = candidate.resolve()
    try:
        rel = resolved.relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError(f"Path escapes toolkit: {target}") from exc
    if not resolved.is_file():
        raise ValueError(f"Broken link from {origin}: {target}")
    if parts.fragment:
        anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings(resolved.read_text(encoding="utf-8"))}
        if unquote(parts.fragment) not in anchors:
            raise ValueError(f"Missing anchor from {origin}: {target}")
    return rel


def registry(root):
    data = json.loads((root / "orchestrator/ROUTES.json").read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("routes"), list):
        raise ValueError("Unsupported route registry")
    ids = set()
    for route in data["routes"]:
        if not isinstance(route, dict):
            raise ValueError("Each route must be an object")
        identifier = route.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
            raise ValueError("Invalid route ID")
        if identifier in ids:
            raise ValueError(f"Duplicate route ID: {identifier}")
        ids.add(identifier)
        for key in ("keywords", "resources", "gates"):
            values = route.get(key)
            if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
                raise ValueError(f"Route {identifier}: {key} must be a nonempty string list")
            if len(values) != len(set(v.casefold() for v in values)):
                raise ValueError(f"Route {identifier}: duplicate {key}")
        for key in ("when_to_load", "skip", "overlap"):
            if not isinstance(route.get(key), str) or not route[key].strip():
                raise ValueError(f"Route {identifier}: missing {key}")
    return data["routes"]


def route_task(task, routes):
    scores = []
    for index, route in enumerate(routes):
        hits = [word for word in route["keywords"] if re.search(r"(?<!\w)" + re.escape(word) + r"(?!\w)", task, re.I)]
        if hits:
            scores.append((sum(len(word.split()) for word in hits), -index, route, hits))
    # Host constraints supplement a task; they must not outscore its actual goal.
    substantive = [entry for entry in scores if entry[2]["id"] != "environment"]
    if substantive:
        scores = substantive
    if not scores:
        return {"task": task, "primary": "catalogue", "matched": [], "resources": ["orchestrator/PROJECT_DISCOVERY_PROTOCOL.md", "CATALOG.md"], "gates": [], "candidates": [], "selection": "keyword heuristic; interpret the brief before loading"}
    _, _, selected, hits = max(scores, key=lambda entry: (entry[0], entry[1]))
    resources = list(selected["resources"])
    if selected["id"] != "environment":
        environment = next((r for r in routes if r["id"] == "environment"), None)
        if environment and any(re.search(r"(?<!\w)" + re.escape(word) + r"(?!\w)", task, re.I) for word in environment["keywords"]):
            resources = environment["resources"] + resources
    return {"task": task, "primary": selected["id"], "matched": hits, "resources": list(dict.fromkeys(resources)), "gates": selected["gates"], "candidates": [entry[2]["id"] for entry in sorted(scores, key=lambda entry: (entry[0], entry[1]), reverse=True)], "skip": selected["skip"], "overlap": selected["overlap"], "selection": "keyword heuristic; interpret the brief before loading"}


def search_resources(root, query, limit=8):
    """Search all guidance, including subjects without a dedicated route."""
    words = set(re.findall(r"[\w-]+", query.casefold()))
    results = []
    for name in source_files(root):
        if not name.endswith(".md") or name.startswith("reports/") or name in {"CATALOG.md", "README.md"}:
            continue
        body = (root / name).read_text(encoding="utf-8")
        hs = headings(body)
        title = hs[0] if hs else name
        title_words = set(re.findall(r"[\w-]+", (name.replace("-", " ") + " " + title).casefold()))
        body_words = set(re.findall(r"[\w-]+", prose(body).casefold()))
        score = 5 * len(words & title_words) + len(words & body_words)
        if score:
            results.append({"resource": name, "title": title, "score": score})
    return sorted(results, key=lambda row: (-row["score"], row["resource"]))[:limit]


def audit(root):
    files = source_files(root)
    suites = json.loads((root / "evals/SKILL_EVALS.json").read_text())["suites"]
    return {"kind": "static inventory; not behavioral execution", "sources": len(files),
            "groups": dict(sorted(Counter(PurePosixPath(p).parts[0] if "/" in p else "entrypoints" for p in files).items())),
            "behavioral_statuses": dict(Counter(case["status"] for suite in suites for case in suite["cases"])),
            "files": [{"path": name, "bytes": (root / name).stat().st_size,
                       "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()} for name in files]}


def routing_checks(root, routes):
    data = json.loads((root / "evals/ROUTING_EVALS.json").read_text())
    if not isinstance(data, dict) or data.get("schema_version") != 1 or not isinstance(data.get("cases"), list) or not data["cases"]:
        raise ValueError("Invalid routing evaluations")
    results, ids = [], set()
    for case in data["cases"]:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"] or case["id"] in ids:
            raise ValueError("Invalid or duplicate routing case ID")
        ids.add(case["id"])
        if not isinstance(case.get("prompt"), str) or not isinstance(case.get("primary"), str):
            raise ValueError(f"Invalid routing case: {case['id']}")
        result = route_task(case["prompt"], routes)
        errors = []
        if result["primary"] != case["primary"]:
            errors.append(f"primary {result['primary']} != {case['primary']}")
        for key in ("includes", "excludes"):
            values = case.get(key, [])
            if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
                raise ValueError(f"Invalid {key} in routing case {case['id']}")
            for value in values:
                present = value in result["resources"]
                if present != (key == "includes"):
                    errors.append(f"{key}: {value}")
        results.append({"id": case["id"], "primary": result["primary"], "passed": not errors, "errors": errors})
    return results


def catalogue(root, files, routes):
    text = "# Complete Resource Catalogue\n\nGenerated by `python scripts/toolkit.py index`. Start with [project routing](orchestrator/PROJECT_ROUTING.md); load only the relevant entries. Core source files are listed here; imported collections and their full supporting-file inventory are listed in [COLLECTIONS.md](COLLECTIONS.md). Keywords are discovery hints, not permission or mandatory scope.\n"
    for folder in ["."] + sorted(DIRECTORIES):
        entries = [p for p in files if (str(PurePosixPath(p).parent) == "." if folder == "." else p.startswith(folder + "/")) and p != "CATALOG.md"]
        if not entries:
            continue
        text += f"\n## {folder if folder != '.' else 'Entrypoints'}\n\n| Resource | Load for / routes | Skip and overlap |\n|---|---|---|\n"
        for name in entries:
            body = (root / name).read_text(encoding="utf-8") if name.endswith(".md") else ""
            hs = headings(body) if name.endswith(".md") else []
            title = (hs[0] if hs else PurePosixPath(name).name).replace("|", "/")
            owners = [r["id"] for r in routes if name in r["resources"] or name in r["gates"]]
            reason = ", ".join(owners) if owners else title.lower()
            policy = "Use for the named task; follow route exclusions" if owners else "Load only when the named subject/artifact is needed; reuse its owning resource"
            if folder in {"scripts", "tests", "reports", "evals"}:
                policy = "Toolkit maintenance/evidence only; skip in ordinary product work"
            if folder == "scripts" and owners:
                policy = "Runnable helper for the owning route; inspect inputs and permitted effects"
            text += f"| [{title}]({name}) | {reason} | {policy} |\n"
    return text


def machine_manifest(root, files):
    return {
        "schema_version": 1,
        "name": "professional-product-creation",
        "generated_by": "python scripts/toolkit.py index",
        "files": [
            {"path": name, "bytes": (root / name).stat().st_size,
             "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()}
            for name in files if name != "manifest.json"
        ],
    }


def index(root):
    routes = registry(root)
    builder_spec = importlib.util.spec_from_file_location("build_library", root / "scripts/build_library.py")
    builder = importlib.util.module_from_spec(builder_spec)
    builder_spec.loader.exec_module(builder)
    builder.build(root)
    (root / "native-skills.tsv").write_text("# name\tSKILL.md path\tcollection\nskills-library\tskills-library/SKILL.md\tmcp-entrypoint\n", encoding="utf-8")
    plugin_path = root / ".codex-plugin/plugin.json"
    plugin_path.parent.mkdir(parents=True, exist_ok=True)
    plugin = {
        "name": "complete-skills", "version": "1.4.0",
        "description": "Search and read the external SKILLS dataset through bounded MCP tools.",
        "skills": ["./skills-library"],
    }
    plugin_path.write_text(json.dumps(plugin, indent=2) + "\n", encoding="utf-8")
    marketplace_path = root / ".agents/plugins/marketplace.json"
    marketplace_path.parent.mkdir(parents=True, exist_ok=True)
    marketplace_path.write_text(json.dumps({
        "name": "festac-skills", "plugins": [{"name": "complete-skills", "source": "./"}],
    }, indent=2) + "\n", encoding="utf-8")
    (root / "orchestrator/PROJECT_ROUTING.md").write_text(routing_guide(routes), encoding="utf-8")
    files = sorted(set(source_files(root)) | {"CATALOG.md", "manifest.json"})
    (root / "CATALOG.md").write_text(catalogue(root, files, routes), encoding="utf-8")
    (root / "manifest.json").write_text(json.dumps(machine_manifest(root, files), indent=2) + "\n", encoding="utf-8")
    return len(files)


def routing_guide(routes):
    text = """# Project Routing

Generated from [ROUTES.json](ROUTES.json) by `python scripts/toolkit.py index`.

## Select resources

Interpret the actual task and current project evidence. Choose one primary route and add supporting resources only for dependencies the work needs. A compound request may need brand, graphics and frontend guidance together; it does not require loading the whole library or spawning agents.

Use the table below to choose a route and read its linked resources directly. Environment constraints supplement the actual task and cannot replace it. Negation and unfamiliar wording require judgment. The optional maintainer command `python scripts/toolkit.py route 'your task'` reports a deterministic keyword suggestion; it is not required to use these skills.

For subjects outside the routes, browse [the catalogue](../CATALOG.md) or select an installed native skill. Read the chosen resource before applying it. Existing user authorization persists; route selection adds no external-action permission.

## Routes and ownership

| Route / triggers | Ordered resources | Applicable gates | Exclusion and overlap |
|---|---|---|---|
"""
    for route in routes:
        links = lambda names: ", ".join(f"[{PurePosixPath(name).stem}](../{name})" for name in names)
        text += f"| **{route['id']}**: {', '.join(route['keywords'])} | {links(route['resources'])} | {links(route['gates'])} | {route['skip']} {route['overlap']} |\n"
    return text + """
## Verify selection

Run `python scripts/toolkit.py dry-run` for deterministic cases, including compound environment constraints, design requests and exclusions. [Behavioral evaluations](../evals/SKILL_EVALS.json) remain separate: routing success does not demonstrate that an agent implements the selected guidance correctly.
"""


def validate(root, preserve_baseline=False):
    errors = []
    try:
        files = source_files(root)
        routes = registry(root)
        baseline = json.loads((root / "reports/MERGE_BASELINE.json").read_text())["files"]
        evaluations = json.loads((root / "evals/SKILL_EVALS.json").read_text())
        suites = evaluations["suites"]
        if evaluations.get("schema_version") != 1 or not isinstance(suites, list):
            raise ValueError("Unsupported behavioral evaluations")
        routing_results = routing_checks(root, routes)
        errors.extend(f"Routing case failed: {row['id']}: {row['errors']}" for row in routing_results if not row["passed"])
        import_path = root / "reports/CLAUDE_MERGE_MAP.json"
        imports = json.loads(import_path.read_text()) if import_path.exists() else {}
        imported = set()
        for entry in imports.get("importedResources", []):
            target = entry.get("target")
            if (not isinstance(target, str) or PurePosixPath(target).is_absolute()
                    or ".." in PurePosixPath(target).parts):
                raise ValueError(f"Invalid imported resource target: {target}")
            if target not in files:
                errors.append(f"Invalid imported resource target: {target}")
            if not re.fullmatch(r"[a-f0-9]{64}", entry.get("sourceSha256", "")):
                raise ValueError(f"Missing import provenance: {target}")
            imported.add(target)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [str(exc)]
    if (root / "COLLECTIONS.json").exists():
        spec = importlib.util.spec_from_file_location("skill_collections", root / "scripts/skill_collections.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        errors.extend(module.validate(root, deep=False))
    imported_files = set()
    if (root / "COLLECTIONS.json").exists():
        imported_files = {f["path"] for c in json.loads((root / "COLLECTIONS.json").read_text())["collections"] for f in c["files"]}
    available = set(files)
    graph = {p: set() for p in files}
    resource_titles = {}
    fingerprints = {}
    for name in files:
        try:
            body = (root / name).read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"Non-UTF-8 source {name}: {exc}")
            continue
        digest = hashlib.sha256(body.strip().encode()).hexdigest()
        if body.strip() and digest in fingerprints:
            errors.append(f"Duplicate content: {name} and {fingerprints[digest]}")
        fingerprints[digest] = name
        if not name.startswith("reports/") and name != "COLLECTIONS.json":
            for retired in imports.get("retiredAliases", {}):
                if retired in body:
                    errors.append(f"Retired resource reference: {name} -> {retired}")
        if not name.endswith(".md"):
            continue
        hs = headings(body)
        if len(re.findall(r"^# ", prose(body), re.M)) != 1:
            errors.append(f"Expected one H1: {name}")
        duplicate = [h for h, count in Counter(h.casefold() for h in hs).items() if count > 1]
        if duplicate:
            errors.append(f"Duplicate headings in {name}: {duplicate}")
        if name.startswith(("specialists/", "references/")) and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.md", PurePosixPath(name).name):
            errors.append(f"Inconsistent lowercase name: {name}")
        if name.startswith(("orchestrator/", "playbooks/", "quality-gates/", "templates/", "reports/")) and not re.fullmatch(r"[A-Z0-9_-]+\.md", PurePosixPath(name).name):
            errors.append(f"Inconsistent uppercase name: {name}")
        if name.startswith(("specialists/", "references/")) and hs:
            title = re.sub(r"\bspecialist\b|[^\w ]", "", hs[0].lower()).strip()
            key = (PurePosixPath(name).parts[0], title)
            if key in resource_titles:
                errors.append(f"Duplicate resource title: {name} and {resource_titles[key]}")
            resource_titles[key] = name
        if body.startswith("---\n"):
            if name not in {"SKILL.md", "motion-studio/SKILL.md"}:
                errors.append(f"Unexpected frontmatter in plain resource: {name}")
            front = body.split("---\n", 2)
            if len(front) != 3:
                errors.append(f"Unclosed frontmatter: {name}")
            else:
                fields = dict(re.findall(r"^([a-z_-]+): (.+)$", front[1], re.M))
                if not re.fullmatch(r"[a-z0-9-]{1,63}", fields.get("name", "")) or not fields.get("description"):
                    errors.append(f"Invalid skill name/description: {name}")
        elif name == "SKILL.md":
            errors.append("Missing SKILL.md frontmatter")
        for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", prose(body)):
            try:
                dest = local_target(root, name, target)
                if dest:
                    if dest not in available and dest not in imported_files:
                        errors.append(f"Link to unlisted source: {name} -> {dest}")
                    graph[name].add(dest if dest in available else "COLLECTIONS.json")
            except ValueError as exc:
                errors.append(str(exc))
    for name, original in baseline.items():
        data = (root / name).read_bytes() if name in available else b""
        if name not in available:
            errors.append(f"Baseline resource is missing: {name}")
        if preserve_baseline and hashlib.sha256(data[:original["bytes"]]).hexdigest() != original["sha256"]:
            errors.append(f"Original content is not preserved: {name}")
    ids = set()
    for route in routes:
        if route.get("id") in ids:
            errors.append(f"Duplicate route ID: {route.get('id')}")
        ids.add(route.get("id"))
        for key in ("id", "keywords", "when_to_load", "skip", "overlap", "resources", "gates"):
            if not route.get(key):
                errors.append(f"Missing route field {key}: {route.get('id')}")
        for name in route.get("resources", []) + route.get("gates", []):
            if name not in available or PurePosixPath(name).is_absolute() or ".." in PurePosixPath(name).parts:
                errors.append(f"Invalid route target: {name}")
    expected = catalogue(root, files, routes)
    if "CATALOG.md" not in available or (root / "CATALOG.md").read_text() != expected:
        errors.append("Catalogue is missing/stale; run index")
    if (root / "orchestrator/PROJECT_ROUTING.md").read_text() != routing_guide(routes):
        errors.append("Project routing guide is stale; run index")
    if "manifest.json" in available:
        try:
            if json.loads((root / "manifest.json").read_text()) != machine_manifest(root, files):
                errors.append("Machine manifest is stale; run index")
        except (ValueError, OSError) as exc:
            errors.append(f"Invalid machine manifest: {exc}")
    else:
        errors.append("Machine manifest is missing; run index")
    for retired, target in imports.get("retiredAliases", {}).items():
        if retired in available:
            errors.append(f"Retired resource was recreated: {retired}")
        if target not in available:
            errors.append(f"Missing consolidation target: {target}")
    visited, pending = set(), ["README.md", "SKILL.md"]
    while pending:
        node = pending.pop()
        if node not in visited:
            visited.add(node)
            pending.extend(graph.get(node, set()) - visited)
    if available - visited:
        errors.append(f"Resources not reachable from entrypoints: {sorted(available - visited)}")
    new_guides = {p for p in available if p.endswith(".md") and p not in baseline and p not in imported and not p.startswith("reports/") and p not in {"CATALOG.md", "NOTICE.md"}}
    seen, case_ids = set(), set()
    for suite in suites:
        if not isinstance(suite, dict):
            errors.append("Each behavioral suite must be an object")
            continue
        name = suite.get("resource")
        if not isinstance(name, str):
            errors.append("Invalid eval resource type")
            continue
        if name not in available or name in seen:
            errors.append(f"Invalid or duplicate eval target: {name}")
        seen.add(name)
        cases = suite.get("cases", [])
        if not isinstance(cases, list) or not cases:
            errors.append(f"Expected behavioral cases: {name}")
            continue
        for case in cases:
            if not isinstance(case, dict) or not isinstance(case.get("id"), str):
                errors.append(f"Invalid eval case: {name}")
                continue
            if case.get("id") in case_ids:
                errors.append(f"Duplicate eval case ID: {case.get('id')}")
            case_ids.add(case.get("id"))
            if any(not case.get(k) for k in ("id", "prompt", "expected_behaviors", "failure_signs", "status")):
                errors.append(f"Incomplete eval case: {name}")
            status = case.get("status")
            if not isinstance(status, str) or status not in {"not_run", "passed", "failed", "blocked"}:
                errors.append(f"Invalid eval status: {case['id']}")
            if status != "not_run":
                evidence = case.get("evidence")
                if not isinstance(evidence, str) or not evidence.strip():
                    errors.append(f"Executed eval needs evidence: {case['id']}")
                else:
                    try:
                        local_target(root, "evals/SKILL_EVALS.json", evidence)
                    except ValueError as exc:
                        errors.append(str(exc))
    if new_guides - seen:
        errors.append(f"New guidance without evaluations: {sorted(new_guides - seen)}")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["index", "validate", "dry-run", "route", "search", "audit"])
    parser.add_argument("task", nargs="?")
    parser.add_argument("--preserve-baseline", action="store_true", help="Check original append-only merge prefixes; not required for authorized revisions")
    args = parser.parse_args(argv)
    try:
        routes = registry(ROOT)
        if args.command == "index":
            print(f"Indexed {index(ROOT)} source files")
        elif args.command == "validate":
            errors = validate(ROOT, preserve_baseline=args.preserve_baseline)
            for error in errors:
                print(error, file=sys.stderr)
            if errors:
                return 1
            print(f"PASS: {len(source_files(ROOT))} sources; {len(routes)} routes; links, structure, routing cases, and evaluation records")
        elif args.command in {"route", "search"}:
            if not args.task:
                parser.error(f"{args.command} requires a task description")
            result = route_task(args.task, routes) if args.command == "route" else search_resources(ROOT, args.task)
            print(json.dumps(result, indent=2))
        elif args.command == "audit":
            print(json.dumps(audit(ROOT), indent=2))
        else:
            results = routing_checks(ROOT, routes)
            print(json.dumps({"kind": "routing simulation; no agent execution", "results": results}, indent=2))
            return int(any(not row["passed"] for row in results))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
