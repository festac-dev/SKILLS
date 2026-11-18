# Domain Model and State Machine

## Domain
- Core entities and ownership:
- Roles and permissions:
- Authoritative data sources:
- Invariants:
- Lifecycle boundaries:

## State model
| Current state | Event/command | Preconditions | Next state | Side effects | Failure/retry |
|---|---|---|---|---|---|
| | | | | | |

## Concurrency and recovery
- Duplicate command behavior:
- Competing updates:
- Idempotency key:
- Transaction boundary:
- Audit history:
- Reconciliation/repair:

Include a diagram when it clarifies the lifecycle; keep this table as the source of truth.

## Execution record

Keep only fields relevant to this artifact.

- Authoritative constraint or transaction enforcing each invariant:
- Competing command and timeout-after-commit outcome:
- Historical-version interpretation after transition changes:
