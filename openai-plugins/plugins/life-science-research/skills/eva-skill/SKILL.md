---
name: openai-eva-skill
description: Submit compact EVA REST requests for species metadata and archived variant lookups. Use when a user wants concise European Variation Archive summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/rest_request.py` for all EVA calls.
- Use `base_url=https://www.ebi.ac.uk/eva/webservices/rest/v1`.
- Prefer metadata and targeted variant lookups over broad genomic window pulls.
- Keep region queries narrow by species, assembly, or small coordinate windows when possible.
- Re-run requests in long conversations instead of relying on older tool output.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return raw JSON only if the user explicitly asks for machine-readable output.
- Prefer these paths: `meta/species/list` and targeted variant or region routes from the EVA REST API.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common EVA patterns:
  - `{"base_url":"https://www.ebi.ac.uk/eva/webservices/rest/v1","path":"meta/species/list","record_path":"response.0.result","max_items":10}`
  - `{"base_url":"https://www.ebi.ac.uk/eva/webservices/rest/v1","path":"variants/rs699","max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"base_url":"https://www.ebi.ac.uk/eva/webservices/rest/v1","path":"meta/species/list","record_path":"response.0.result","max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
