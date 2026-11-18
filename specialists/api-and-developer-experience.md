# API and Developer Experience Specialist

## Mission
Make the product understandable, predictable, secure, and pleasant to integrate with.

## Responsibilities
- Define resource models, endpoint or operation semantics, versioning, pagination, filtering, sorting, idempotency, and error conventions.
- Design authentication, authorization, scopes, quotas, rate limits, and safe credential lifecycle.
- Provide stable SDKs, typed clients, examples, webhooks, sandbox environments, and migration guidance where justified.
- Make errors actionable without leaking secrets or internal implementation details.
- Consider retries, duplicate delivery, ordering, timeouts, partial failure, and backwards compatibility.

## Deliverables
- API contract and versioning policy.
- Error model and representative examples.
- Authentication and authorization matrix.
- Webhook delivery and retry policy, if applicable.
- Developer onboarding and migration guide.

## Quality checks
Contracts are testable; examples run; breaking changes are explicit; secrets never appear in logs; rate limits and failure behavior are documented.

## Applied verification

Run a documented example against the supported API version and exercise pagination while records change. Verify stable ordering, no leaked forbidden records, and an actionable response when an idempotency key is reused with a different request.

## Contract lifecycle

Choose REST, RPC, GraphQL, event contracts or the existing API style from consumer needs. Define stable identifiers, null/absent fields, numeric precision, timestamps, filtering and deterministic pagination. Specify authentication separately from resource authorization. Establish request/body limits, quotas and a machine-readable error convention; do not reveal another tenant's resource existence through errors.

For retryable mutations, define idempotency scope, payload conflict behavior, retention and replayed results. For conditional writes, specify version/ETag semantics and conflict recovery. Distinguish accepted asynchronous work from completed work; return a durable operation reference where appropriate.

For webhooks, authenticate the exact supported payload representation, enforce freshness/replay rules, record delivery identity, deduplicate effects and support bounded redelivery. Reconcile ambiguous outbound outcomes. Validate pagination, cancellation, timeout and errors from an actual consumer, not only server unit tests.

When an outbound mutation may have succeeded but its response was lost, preserve the durable intent and expose a supported reconciliation path. Verify a candidate provider record against the original intent's relevant identity, amount, direction and destination fields before binding it. Missing evidence must remain distinguishable from a mismatch or proven non-submission; do not infer proof from the caller's current request or remove the block with a generic bypass. Keep monitoring accepted operations independent of failures in data needed only to admit new work.

Evolve contracts additively where possible. Define deprecation, overlap and migration with real consumers; test compatibility against the supported versions. Generate clients or documentation from a maintained contract only when they improve the workflow, and execute the published examples. Link to [backend delivery](../playbooks/BACKEND_DELIVERY_PLAYBOOK.md) for the full operating path.

## Protocol and asynchronous contracts

Compare transports using [API style selection](../references/api-style-selection-guide.md). For GraphQL, budget query cost and field-level authorization; for gRPC, check browser gateway and streaming constraints; for brokered contracts, define event versions and replay semantics. Preserve the project’s existing error format; RFC 9457 is an option when choosing one. A long-running HTTP operation can return 202 with an authorized status resource; define cancellation, expiry and partial failure instead of holding a request open. Document null, unknown-field, currency and timestamp semantics together.
