---
name: alireza-tech-debt
description: 'Scan, prioritize, and report technical debt. Usage: /tech-debt <scan|prioritize|report>
  [options]'
metadata:
  upstream_headers:
    argument-hint: <scan|prioritize|report> [options]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /tech-debt

Scan codebases for technical debt, score severity, and generate prioritized remediation plans.

## Usage

```
/tech-debt scan <project-dir>           Scan for debt indicators
/tech-debt prioritize <inventory.json>  Prioritize debt backlog
/tech-debt report <project-dir>         Full dashboard with trends
```

## Examples

```
/tech-debt scan ./src
/tech-debt scan . --format json
/tech-debt report . --format json --output debt-report.json
```

## Scripts
- `engineering/skills/tech-debt-tracker/scripts/debt_scanner.py` — Scan for debt patterns (`debt_scanner.py <directory> [--format json] [--output file]`)
- `engineering/skills/tech-debt-tracker/scripts/debt_prioritizer.py` — Prioritize debt backlog (`debt_prioritizer.py <inventory.json> [--framework cost_of_delay|wsjf|rice] [--format json]`)
- `engineering/skills/tech-debt-tracker/scripts/debt_dashboard.py` — Generate debt dashboard (`debt_dashboard.py [files...] [--input-dir dir] [--period weekly|monthly|quarterly] [--format json]`)

## Skill Reference
→ `engineering/skills/tech-debt-tracker/SKILL.md`
