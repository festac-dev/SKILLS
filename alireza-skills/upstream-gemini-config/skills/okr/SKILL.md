---
name: alireza-okr
description: "Generate OKR cascades from company strategy to team objectives. Usage: /okr generate <strategy>"
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /okr

Generate cascaded OKR frameworks from company-level strategy down to team-level key results.

## Usage

```
/okr generate <strategy>                                     Generate OKR cascade
```

Supported strategies: `growth`, `retention`, `revenue`, `innovation`, `operational`

## Input Format

Pass a strategy keyword directly. The generator produces company, department, and team-level OKRs aligned to the chosen strategy.

## Examples

```
/okr generate growth
/okr generate retention
/okr generate revenue
/okr generate innovation
/okr generate operational
/okr generate growth --json
```

## Scripts
- `product-team/skills/product-strategist/scripts/okr_cascade_generator.py` — OKR cascade generator (`<strategy> [--teams "A,B,C"] [--contribution 0.3] [--json]`)

## Skill Reference
> `product-team/skills/product-strategist/SKILL.md`
