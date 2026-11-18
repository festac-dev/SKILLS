---
name: openai-minimal-skill
description: Minimal example skill for plugin-eval tests. Use when the user wants a compact demonstration of a well-structured skill.
license: MIT
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Minimal Skill

Use this fixture to verify that skill evaluation works on a small but valid example.

## Workflow

1. Read the target file.
2. Summarize the important structure.
3. Reference deeper details only when needed.

## Reference

- `references/details.md`
