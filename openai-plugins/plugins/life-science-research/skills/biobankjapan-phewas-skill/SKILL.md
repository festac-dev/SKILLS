---
name: openai-biobankjapan-phewas-skill
description: Fetch compact BioBank Japan PheWAS summaries for single variants by accepting rsID, GRCh38, or GRCh37 input and resolving to the required GRCh37 query. Use when a user wants concise BBJ association results for one variant
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/biobankjapan_phewas.py` for all BioBank Japan PheWAS lookups.
- Accept exactly one of `rsid`, `grch37`, `grch38`, or `variant`; resolve to the canonical GRCh37 `chr:pos-ref-alt` query before calling BioBank Japan.
- The script accepts `max_results`; start with `max_results=10` and only increase it if the first slice is insufficient.
- Re-run the lookup in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.
- If the user needs the full association payload, set `save_raw=true` and report `raw_output_path` instead of pasting large arrays into chat.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return the JSON verbatim only if the user explicitly asks for machine-readable output.
- Surface the canonical queried variant, total association count, and whether the results were truncated.
- Increase `max_results` gradually instead of asking for large association dumps in one call.

## Input
- Read one JSON object from stdin, or a single JSON string containing the variant.
- Required input: exactly one of `rsid`, `grch37`, `grch38`, or `variant`
- Optional fields: `max_results`, `save_raw`, `raw_output_path`, `timeout_sec`
- Common patterns:
  - `{"grch37":"10:114758349-C-T","max_results":10}`
  - `{"grch38":"10:112998590-C-T","max_results":10}`
  - `{"rsid":"rs7903146","max_results":10}`
  - `{"variant":"10:114758349:C:T","max_results":25,"save_raw":true}`

## Output
- Success returns `ok`, `source`, `input`, `query_variant`, `max_results_applied`, `association_count`, `association_count_total`, `truncated`, `associations`, `variant`, `variant_url`, `raw_output_path`, and `warnings`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"grch37":"10:114758349-C-T","max_results":10}' | python scripts/biobankjapan_phewas.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/biobankjapan_phewas.py`.
