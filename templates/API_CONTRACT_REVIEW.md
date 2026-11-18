# API Contract Review

## Interface
- Audience and primary use cases:
- Resources/operations:
- Authentication and authorization:
- Versioning and compatibility:
- Pagination, filtering, sorting:
- Idempotency and concurrency:
- Rate limits and quotas:

## Error behavior
| Condition | Status/code | Safe message | Retryable? | Recovery guidance |
|---|---|---|---|---|
| | | | | |

## Webhooks (if applicable)
- Signature and timestamp validation:
- Delivery IDs and deduplication:
- Retry schedule and expiry:
- Ordering guarantees:
- Replay tooling:

## Acceptance
- [ ] Contract is machine-readable or unambiguous.
- [ ] Examples are executable.
- [ ] Authorization is tested per resource.
- [ ] Breaking changes and migration path are documented.

## Execution record

Keep only fields relevant to this artifact.

- Executable example and supported contract version:
- Conflicting idempotency payload and expected response:
- Pagination behavior during concurrent changes:
