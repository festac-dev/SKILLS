---
name: alireza-sprint-health
description: 'Sprint health scoring and velocity analysis for agile teams. Usage:
  /sprint-health <analyze|velocity> [options]'
metadata:
  upstream_headers:
    argument-hint: <analyze|velocity> [options]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /sprint-health

Score sprint health across delivery, quality, and team metrics with velocity trend analysis.

## Usage

```
/sprint-health analyze <sprint_data.json>                    Full sprint health score
/sprint-health velocity <sprint_data.json>                   Velocity trend analysis
```

## Input Format

```json
{
  "sprint_name": "Sprint 24",
  "committed_points": 34,
  "completed_points": 29,
  "stories": {"total": 12, "completed": 10, "carried_over": 2},
  "blockers": [{"description": "API dependency", "days_blocked": 3}],
  "ceremonies": {"planning": true, "daily": true, "review": true, "retro": true}
}
```

## Examples

```
/sprint-health analyze sprint-24.json
/sprint-health velocity last-6-sprints.json
/sprint-health analyze sprint-24.json --format json
```

## Scripts
- `project-management/skills/scrum-master/scripts/sprint_health_scorer.py` — Sprint health scorer (`<data_file> [--format text|json]`)
- `project-management/skills/scrum-master/scripts/velocity_analyzer.py` — Velocity analyzer (`<data_file> [--format text|json]`)

## Skill Reference
> `project-management/skills/scrum-master/SKILL.md`
