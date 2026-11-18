---
name: alireza-rice
description: "RICE feature prioritization with scoring and capacity planning. Usage: /rice prioritize <features.csv> [options]"
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /rice

Prioritize features using RICE scoring (Reach, Impact, Confidence, Effort) with optional capacity constraints.

## Usage

```
/rice prioritize <features.csv>                              Score and rank features
/rice prioritize <features.csv> --capacity 20                Rank with effort capacity limit
```

## Input Format

```csv
feature,reach,impact,confidence,effort
Dark mode,5000,2,0.8,3
API v2,12000,3,0.9,8
SSO integration,3000,2,0.7,5
Mobile app,20000,3,0.5,13
```

## Examples

```
/rice prioritize features.csv
/rice prioritize features.csv --capacity 20
/rice prioritize features.csv --output json
```

## Scripts
- `product-team/skills/product-manager-toolkit/scripts/rice_prioritizer.py` — RICE prioritizer (`<input.csv> [--capacity N] [--output text|json|csv]`)

## Skill Reference
> `product-team/skills/product-manager-toolkit/SKILL.md`
