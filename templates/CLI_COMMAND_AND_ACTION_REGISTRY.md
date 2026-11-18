# CLI Command and Action Registry

Define commands/actions once and derive execution, help, completion, and UI discovery from the same validated registry where practical.

| Stable ID | Display label | Description | Arguments/schema | Required capability | Permission | CLI route | TUI presentation |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Registry rules
- Stable identifiers are separate from human-readable labels.
- Validate schemas before execution.
- Do not execute arbitrary discovered content without authorization and validation.
- Hide or disable unavailable capabilities with a useful explanation.
- Keep user-provided extensions isolated and permission-scoped.
- Do not hard-code a fixed list of providers, models, actions, or plugins when discovery is supported.
- Do not invent capabilities that an integration does not expose.
- Generate help and completion from the same source to prevent drift.

## Change management
Document compatibility, deprecation, migration, and error behavior for registry changes.
