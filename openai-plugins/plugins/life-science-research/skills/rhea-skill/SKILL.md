---
name: openai-rhea-skill
description: Submit compact Rhea reaction search requests for biochemical reactions and reaction IDs. Use when a user wants concise Rhea summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/rest_request.py` for all Rhea calls.
- Use `base_url=https://www.rhea-db.org`.
- Start with the `rhea` search endpoint plus `format=json`.
- Keep queries narrow by reaction ID, compound name, EC number, or free-text reaction term.
- Re-run requests in long conversations instead of relying on older tool output.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return raw JSON only if the user explicitly asks for machine-readable output.
- Prefer these patterns: reaction search by `query`, targeted ID search via `query=RHEA:<id>`, and small result windows.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common Rhea patterns:
  - `{"base_url":"https://www.rhea-db.org","path":"rhea","params":{"query":"caffeine","format":"json"},"record_path":"results","max_items":10}`
  - `{"base_url":"https://www.rhea-db.org","path":"rhea","params":{"query":"RHEA:47148","format":"json"},"record_path":"results","max_items":5}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"base_url":"https://www.rhea-db.org","path":"rhea","params":{"query":"caffeine","format":"json"},"record_path":"results","max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
