# Specialist: Backend and Data Engineering

Define service boundaries, API contracts, data models, validation, authorization, migrations, concurrency, retries, idempotency and failure recovery.

Use least privilege, safe query patterns, appropriate transactions and explicit data lifecycle policies. Avoid speculative microservices and premature abstraction. Document operational assumptions and migration/rollback plans.

## Service implementation, contracts, and production correctness

### When to use
Use for APIs, server operations, persistent models, background jobs, authentication integration, or a backend production-readiness review.

### Core principles
Keep a modular service or monolith unless independent scaling, ownership, or isolation justifies distribution. The server owns validation, authorization, and authoritative state. Use database constraints for invariants even when application validation exists.

### Step-by-step procedure
1. Trace one critical journey through request, identity, permission, transaction, side effect, response, and telemetry. Define latency/availability goals and sensitive data boundaries.
2. Design resource/operation contracts: input limits, error codes, pagination order, rate limits, versioning, idempotency, optimistic concurrency, and compatibility. Use OpenAPI, GraphQL schemas, protobuf, or the project's existing contract format as appropriate.
3. Build a permission matrix for roles, resource ownership, tenant boundary, support access, and privileged actions. Check each protected operation, including reads, exports, search, jobs, and realtime subscriptions.
4. Model keys, constraints, transaction isolation, deletion, audit, and retention. Use decimal or integer minor units for money. Document timestamp/time-zone semantics.
5. Use parameterized database access. Measure query plans on representative data; prevent N+1 queries and unbounded scans. Bound connection pools against total database capacity across replicas.
6. Make retryable commands idempotent with scope, request fingerprint, retention, and durable result handling. Reject reuse of a key with a conflicting payload. Handle commit-success/response-loss without repeating the effect.
7. Use an outbox for atomic state-and-event publication. Bound worker concurrency, retry attempts, exponential backoff with jitter, and poison-message handling. Define cancellation and reconciliation.
8. Add request IDs, structured redacted logs, low-cardinality metrics, traces across dependencies, timeouts, overload behavior, and graceful shutdown.
9. Rehearse expand/contract migrations, backups, restores, and binary rollback compatibility. Release only after the critical failure paths have evidence.

### Checklist
- [ ] Two users/tenants cannot access each other's resources by guessing IDs.
- [ ] Concurrent requests cannot violate stock, uniqueness, balance, or state-transition rules.
- [ ] Retries cannot duplicate money, orders, notifications, or jobs.
- [ ] Uploads are bounded, validated, quarantined when required, and never executed as code.
- [ ] Caches have ownership, invalidation, TTL, and permission-aware keys.
- [ ] Realtime reconnect resumes safely or explicitly requests a full resync.

### Common failure modes
Checking authorization only in the UI; read-then-write races; long transactions across network calls; “exactly once” claims over external systems; retry storms; databases exposed to the public Internet; backups that have never restored.

### Concrete examples
A SQLite concurrency invariant can be exercised without a server:
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE stock (id INTEGER PRIMARY KEY, qty INTEGER NOT NULL CHECK(qty >= 0))")
db.execute("INSERT INTO stock VALUES (1, 1)")
first = db.execute("UPDATE stock SET qty = qty - 1 WHERE id = 1 AND qty > 0").rowcount
second = db.execute("UPDATE stock SET qty = qty - 1 WHERE id = 1 AND qty > 0").rowcount
assert (first, second) == (1, 0)
assert db.execute("SELECT qty FROM stock WHERE id = 1").fetchone()[0] == 0
```
This demonstrates an atomic conditional update; it does not prove the production database's concurrent transaction behavior. Add a competing-client test against that database.

### Verification
Run contract, permission-negative, concurrency, duplicate-request, timeout-after-commit, migration, and restore checks applicable to the service. Record exact environment, dataset, results, and untested assumptions.

### Related skills
[API review](../templates/API_CONTRACT_REVIEW.md), [identity](identity-and-access-management.md), [distributed systems](edge-and-distributed-systems.md), [DevOps](devops-and-release.md), [data integrity](../references/data-modeling-and-integrity-guide.md).

## Applied verification

Race two legitimate callers against the same constrained resource in the actual database engine. Assert the final invariant and each caller’s outcome, then retry a request whose response was lost after commit; an in-memory substitute cannot prove database locking.

## Capacity and boundary behavior

Carry an end-to-end deadline through downstream calls, and bound retries within it. Limit body size, decompression, upload streams, query complexity and concurrent work before dependencies are saturated. Use backpressure, a durable accepted operation or an explicit rejection; unbounded in-memory buffering is not a queue.

Design cache keys around tenant, permission, version and relevant request variation. Specify invalidation and acceptable staleness; account for stampedes and negative-cache behavior. Never let a cached response bypass authorization. For files and object storage, define ownership, access expiry, content validation, retention and consistency with the authoritative record.

Use [database engineering](database-engineering.md), [queues](queues-and-background-jobs.md) and [server operations](network-and-server-operations.md) for those concrete boundaries rather than duplicating their operating contracts here.

## Implementation references


For concrete service and storage examples, use [backend code patterns](../references/backend-code-patterns.md), [SQL patterns](../references/sql-and-data-patterns.md) and the [runnable backend reference](../examples/backend-reference/README.md). These are conditional examples, not a required stack. Use [caching](caching-and-backend-performance.md), [service testing](backend-testing-and-verification.md) and [serverless runtimes](serverless-and-edge-runtimes.md) only when the actual operation needs their trade-offs.

## Reviewed operations and partial completion

Define which configuration values are defaults, persisted user preferences or forced operator overrides. Validate limits at the trusted boundary before persisting and again before committing an operation. Include legacy data in migration checks; a missing field must not silently remove an established constraint.

When several independent providers or resources fulfill a requested total, distinguish planned, reserved, submitted and confirmed quantities. Bound concurrent work and account for commitments that an external status response may not yet reflect. Do not imply whole-group atomicity when individual operations have separate outcomes.

Persist intent before an external side effect, use stable operation IDs and classify unstarted items separately from uncertain submissions. A lost response cannot establish that nothing happened. Reconcile through authoritative evidence before retrying; formatted display data may omit the fields required to prove an exact match. Apply this to payments, inventory reservations, notifications, imports and other mutations according to their actual contracts.

For capacity shortfalls, implement the authorized partial, waiting or cancellation policy explicitly. A durable waiting intent is not permission to perform a later changed operation without its required review. Keep domain-specific units, provider parameters and project defaults in that project's documentation, not in global reusable instructions.

A waiting target remains unfinished while work is only reserved or submitted. Count authoritative completion toward fulfillment, and return cancelled or refunded reservations to the unmet target when the domain permits another attempt. Stopping future allocation must not imply cancellation of work already committed. Exercise both directions of a reversible workflow with partial capacity, pending work, a returned reservation and final completion.

When a client adds a provider or publishing role, verify the native create, list, accept and cancellation contracts separately from the user interface. Track offered capacity and accepted commitments, keep optional pricing adjustments off by default when requested, and bind uncertain mutations to authoritative records before retrying. Reuse a common lifecycle only where both roles have the same verified state contract.
