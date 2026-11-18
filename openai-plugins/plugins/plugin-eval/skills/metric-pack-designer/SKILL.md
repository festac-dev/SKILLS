---
name: openai-metric-pack-designer
description: Design custom metric packs for plugin-eval so teams can add local evaluation rubrics that emit schema-compatible checks and metrics. Use when the user wants their own evaluation criteria or visualizations.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Metric Pack Designer

Use this skill when the user wants to extend `plugin-eval` with a local rubric.

## Workflow

1. Clarify the custom rubric categories and target kinds.
2. Define the smallest useful `checks[]` and `metrics[]` payload.
3. Create a metric-pack manifest plus a script that prints JSON to stdout.
4. Run the pack through `plugin-eval analyze <path> --metric-pack <manifest.json>`.

## Design Rules

- Keep IDs stable across runs so comparisons stay meaningful.
- Emit only `checks[]`, `metrics[]`, and optional `artifacts[]`.
- Do not try to overwrite the core score or summary.
- Prefer deterministic local signals over subjective text generation.

## Reference

- `../../references/metric-pack-manifest.md`
