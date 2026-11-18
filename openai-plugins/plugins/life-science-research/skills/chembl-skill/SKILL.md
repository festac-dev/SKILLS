---
name: openai-chembl-skill
description: Submit compact ChEMBL API requests for activity, molecule, target, mechanism, and text-search endpoints. Use when a user wants concise ChEMBL summaries
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## Operating rules
- Use `scripts/rest_request.py` for all ChEMBL API calls.
- Use `base_url=https://www.ebi.ac.uk/chembl/api/data`.
- The script accepts `max_items`; for activity, mechanism, and text-search collections, start with API `limit=10` and `max_items=10`.
- Single molecule or target lookups usually do not need `max_items`.
- Re-run requests in long conversations instead of relying on older tool output.
- Treat displayed `...` in tool previews as UI truncation, not literal request content.

## Execution behavior
- Return concise markdown summaries from the script JSON by default.
- Return the script JSON verbatim only if the user explicitly asks for machine-readable output.
- Prefer these paths: `activity.json`, `molecule/<id>.json`, `target/<id>.json`, `mechanism.json`, and `molecule/search.json`.
- Use `record_path` to target list fields like `activities`, `mechanisms`, or `molecules`.

## Input
- Read one JSON object from stdin.
- Required fields: `base_url`, `path`
- Optional fields: `method`, `params`, `headers`, `json_body`, `form_body`, `record_path`, `response_format`, `max_items`, `max_depth`, `timeout_sec`, `save_raw`, `raw_output_path`
- Common ChEMBL patterns:
  - `{"base_url":"https://www.ebi.ac.uk/chembl/api/data","path":"activity.json","params":{"molecule_chembl_id":"CHEMBL25","limit":10},"record_path":"activities","max_items":10}`
  - `{"base_url":"https://www.ebi.ac.uk/chembl/api/data","path":"molecule/CHEMBL25.json"}`
  - `{"base_url":"https://www.ebi.ac.uk/chembl/api/data","path":"molecule/search.json","params":{"q":"imatinib","limit":10},"record_path":"molecules","max_items":10}`

## Output
- Success returns `ok`, `source`, `path`, `method`, `status_code`, `warnings`, and either compact `records` or a compact `summary`.
- Use `raw_output_path` when `save_raw=true`.
- Failure returns `ok=false` with `error.code` and `error.message`.

## Execution
```bash
echo '{"base_url":"https://www.ebi.ac.uk/chembl/api/data","path":"activity.json","params":{"molecule_chembl_id":"CHEMBL25","limit":10},"record_path":"activities","max_items":10}' | python scripts/rest_request.py
```

## References
- No additional runtime references are required; keep the import package limited to this file and `scripts/rest_request.py`.
