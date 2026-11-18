---
name: openai-ensembl-skill
description: Submit compact Ensembl REST API requests for lookup, overlap, cross-reference, and variation endpoints. Use when a user wants concise Ensembl summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/rest_request.py` for all Ensembl API calls.
- Use `base_url=https://rest.ensembl.org`.
- The script accepts `max_items`; object lookups usually do not need it, but `overlap` and `xrefs` are better with `max_items=10`.
- Send JSON-friendly headers such as `Accept: application/json` and `Content-Type: application/json`.
- Re-run requests in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not part of the true request.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return the script JSON verbatim only if the user explicitly asks for machine-readable output.
- Prefer these paths: `lookup/id/<id>`, `overlap/region/<species>/<region>`, `xrefs/id/<id>`, and `variation/<species>/<id>`.
- Use `save_raw=true` when the user needs the full payload.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common Ensembl patterns:
  - `{"base_url":"https://rest.ensembl.org","path":"lookup/id/ENSG00000141510","headers":{"Accept":"application/json","Content-Type":"application/json"}}`
  - `{"base_url":"https://rest.ensembl.org","path":"overlap/region/homo_sapiens/1:1000000-1002000","params":{"feature":"gene"},"headers":{"Accept":"application/json","Content-Type":"application/json"},"max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"base_url":"https://rest.ensembl.org","path":"lookup/id/ENSG00000141510","headers":{"Accept":"application/json","Content-Type":"application/json"}}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
