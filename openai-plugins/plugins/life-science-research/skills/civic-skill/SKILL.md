---
name: openai-civic-skill
description: Submit compact CIViC GraphQL requests for cancer variant interpretation schema inspection and targeted evidence retrieval. Use when a user wants concise CIViC summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/civic_graphql.py` for all CIViC GraphQL work.
- Keep selection sets narrow and start with schema or targeted entity queries.
- Use `query_path` for longer GraphQL documents instead of pasting large inline queries.
- Re-run requests in long conversations instead of relying on older tool output.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return raw JSON only if the user explicitly asks for machine-readable output.
- Prefer sanity, schema, and targeted evidence queries over broad graph dumps.

## Input
- Read one JSON object from stdin.
- Required field: `query` or `query_path`
- Optional fields: `variables`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common CIViC patterns:
  - `{"query":"query { __typename }"}`
  - `{"query":"query { __schema { queryType { fields { name } } } }","max_items":20}`

## Output
- Success returns `ok`, `source`, `top_keys`, a compact `summary`, and `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` such as `invalid_json`, `invalid_input`, `network_error`, `invalid_response`, or `graphql_error`.

## Execution
```bash
echo '{"query":"query { __typename }"}' | python scripts/civic_graphql.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/civic_graphql.py`.
