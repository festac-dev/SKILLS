#!/usr/bin/env python3
"""Register SKILLS in agent skill directories without copying the library."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ("codex", "claude-code", "opencode")


def agent_directories(home, project=None):
    if project is not None:
        return {
            "codex": project / ".agents/skills",
            "claude-code": project / ".claude/skills",
            "opencode": project / ".opencode/skills",
        }
    return {
        "codex": Path(os.environ.get("CODEX_HOME", home / ".codex")) / "skills",
        "claude-code": Path(os.environ.get("CLAUDE_CONFIG_DIR", home / ".claude")) / "skills",
        "opencode": Path(os.environ.get("XDG_CONFIG_HOME", home / ".config")) / "opencode/skills",
    }


def detected_agents(home):
    profiles = {
        "codex": Path(os.environ.get("CODEX_HOME", home / ".codex")),
        "claude-code": Path(os.environ.get("CLAUDE_CONFIG_DIR", home / ".claude")),
        "opencode": Path(os.environ.get("XDG_CONFIG_HOME", home / ".config")) / "opencode",
    }
    commands = {"codex": "codex", "claude-code": "claude", "opencode": "opencode"}
    return [agent for agent in AGENTS if profiles[agent].is_dir() or shutil.which(commands[agent])]


def available_skills(root, include_collections=True):
    skills = {
        "professional-product-creation": root,
        "motion-studio": root / "motion-studio",
    }
    registry_path = root / "COLLECTIONS.json"
    if include_collections and registry_path.is_file():
        for row in json.loads(registry_path.read_text(encoding="utf-8"))["skills"]:
            name = row["name"]
            source = (root / row["path"]).resolve()
            if not re.fullmatch(r"[a-z0-9-]{1,64}", name) or name in skills:
                raise ValueError(f"Invalid or duplicate skill name: {name}")
            if not source.is_relative_to(root.resolve()) or source.name != "SKILL.md":
                raise ValueError(f"Invalid skill source: {row['path']}")
            skills[name] = source.parent
    return skills


def install_links(skills, destinations, dry_run=False):
    planned = []
    # Check every destination before changing any of them.
    for directory in destinations:
        for name, source in skills.items():
            source = source.resolve()
            if not (source / "SKILL.md").is_file():
                raise ValueError(f"Missing SKILL.md: {source}")
            target = directory / name
            if source == target.resolve():
                continue
            if target.is_symlink() or target.exists():
                raise ValueError(f"Existing skill left untouched: {target}. Choose another --dest or remove it yourself.")
            if directory.resolve().is_relative_to(source):
                raise ValueError(f"Destination is inside the skill source: {directory}. Choose another --dest.")
            planned.append((target, source))
    for target, source in planned:
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(source, target_is_directory=True)
        print(f"{'Would link' if dry_run else 'Linked'} {target} -> {source}")
    return len(planned)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agent", nargs="?", choices=("auto", *AGENTS, "all"), default="auto")
    parser.add_argument("--skill", action="append", help="Name to install; repeat for several skills")
    parser.add_argument("--all", action="store_true", help="Install all registered skills")
    parser.add_argument("--project", action="store_true", help="Install in the current project")
    parser.add_argument("--dest", type=Path, help="Custom skill directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned links without writing")
    args = parser.parse_args(argv)
    if args.all and args.skill:
        parser.error("Choose --all or --skill")
    if args.dest and args.project:
        parser.error("Choose --dest or --project")
    try:
        include_collections = args.all or any(name not in {"professional-product-creation", "motion-studio"} for name in args.skill or [])
        available = available_skills(ROOT, include_collections=include_collections)
        names = list(available) if args.all else args.skill or ["professional-product-creation"]
        unknown = set(names) - available.keys()
        if unknown:
            raise ValueError("Unknown skill: " + ", ".join(sorted(unknown)) + ". Find names in COLLECTIONS.md.")
        selected = {name: available[name] for name in names}
        home = Path.home()
        if args.dest:
            destinations = [args.dest.expanduser().absolute()]
        else:
            agents = list(AGENTS) if args.agent == "all" else detected_agents(home) if args.agent == "auto" else [args.agent]
            if not agents:
                raise ValueError("No supported agent detected. Run ./install.sh codex, ./install.sh claude-code, or ./install.sh opencode.")
            directories = agent_directories(home, Path.cwd() if args.project else None)
            destinations = list(dict.fromkeys(directories[agent] for agent in agents))
        count = install_links(selected, destinations, args.dry_run)
        if not args.dry_run:
            print(f"Ready: {len(selected)} skill(s), {count} new link(s). Start a new agent session to load them.")
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
