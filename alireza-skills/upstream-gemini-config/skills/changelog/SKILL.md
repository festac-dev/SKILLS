---
name: alireza-changelog
description: 'Generate changelogs from git history and validate conventional commits.
  Usage: /changelog <generate|lint> [options]'
metadata:
  upstream_headers:
    argument-hint: <generate|lint> [options]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /changelog

Generate Keep a Changelog entries from git history and validate commit message format.

## Usage

```
/changelog generate [--from-tag <tag>] [--to-tag <tag>]    Generate changelog entries
/changelog lint [--from-ref <ref>] [--to-ref <ref>]       Lint commit messages
```

## Examples

```
/changelog generate --from-tag v2.0.0
/changelog lint --from-ref main --to-ref dev
/changelog generate --from-tag v2.0.0 --to-tag v2.1.0 --format markdown
```

## Scripts
- `engineering/skills/changelog-generator/scripts/generate_changelog.py` — Parse commits, render changelog (`--from-tag`, `--to-tag`, `--from-ref`, `--to-ref`, `--format markdown|json`)
- `engineering/skills/changelog-generator/scripts/commit_linter.py` — Validate conventional commit format (`--from-ref`, `--to-ref`, `--strict`, `--format text|json`)

## Skill Reference
→ `engineering/skills/changelog-generator/SKILL.md`
