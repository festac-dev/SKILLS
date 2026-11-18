---
name: openai-efo-ontology-skill
description: Submit compact EFO OLS4 requests for search, term lookup, children, and descendants. Use when a user wants concise EFO resolution or ontology-expansion summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/rest_request.py` for all OLS4 and EFO API calls.
- Use `base_url=https://www.ebi.ac.uk/ols4/api`.
- Search, children, and descendant endpoints are better with `max_items=10`; single term lookups usually do not need `max_items`.
- Use the smallest ontology expansion that answers the question.
- Re-run requests in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Prefer these paths: `search`, `ontologies/efo/terms/<double-encoded-iri>`, and the corresponding `children` or `descendants` paths.
- If the user needs the full payload, set `save_raw=true` and report the saved file path.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common OLS4 patterns:
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"search","params":{"q":"asthma","ontology":"efo"},"record_path":"response.docs","max_items":10}`
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0000270"}`
  - `{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0000270/descendants","record_path":"_embedded.terms","max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"base_url":"https://www.ebi.ac.uk/ols4/api","path":"search","params":{"q":"asthma","ontology":"efo"},"record_path":"response.docs","max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
