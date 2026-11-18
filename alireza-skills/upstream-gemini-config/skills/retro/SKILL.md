---
name: alireza-retro
description: "Analyze sprint retrospectives for patterns and action item tracking. Usage: /retro analyze <retro_data.json>"
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /retro

Analyze retrospective data for recurring themes, sentiment trends, and action item effectiveness.

## Usage

```
/retro analyze <retro_data.json>                             Full retrospective analysis
```

## Input Format

```json
{
  "sprint_name": "Sprint 24",
  "went_well": ["CI pipeline improvements", "Pair programming sessions"],
  "improvements": ["Too many meetings", "Flaky integration tests"],
  "action_items": [
    {"description": "Reduce standup to 10 min", "owner": "SM", "status": "done"},
    {"description": "Fix flaky tests", "owner": "QA Lead", "status": "in_progress"}
  ],
  "participants": 8
}
```

## Examples

```
/retro analyze sprint-24-retro.json
/retro analyze sprint-24-retro.json --format json
```

## Scripts
- `project-management/skills/scrum-master/scripts/retrospective_analyzer.py` — Retrospective analyzer (`<data_file> [--format text|json]`)

## Skill Reference
> `project-management/skills/scrum-master/SKILL.md`
