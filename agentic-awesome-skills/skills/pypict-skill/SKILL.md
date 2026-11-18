---
name: agentic-awesome-pypict-skill-2c945b40
description: Pairwise test generation
metadata:
  upstream_headers:
    risk: safe
    source: https://github.com/omkamal/pypict-claude-skill/blob/main/SKILL.md
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Pypict Skill

## Overview

Pairwise test generation

## When to Use

Design a small test matrix covering every pair of values across discrete factors,
when exhaustive combinations are too costly and pairwise coverage is appropriate.

## Procedure

1. Define factors, permitted values and real invalid-combination constraints.
2. Inspect an actual installed pairwise generator and its supported input format;
   this entrypoint does not bundle a Python package or executable.
3. Generate candidate rows and independently enumerate covered valid value pairs.
   Missing pairs must remain visible; constraints must not be invented to hide them.
4. Convert rows into tests with expected behavior, not just input combinations.

For three binary factors, this illustrative matrix covers all two-factor pairs:

```json
[[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
```

Pair coverage is not correctness or coverage of three-way interactions. Add known
boundary, authorization and failure cases separately.

## Example

**User request:**

> Use @pypict-skill for this task: Pairwise test generation.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
