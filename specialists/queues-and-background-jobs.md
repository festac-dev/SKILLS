# Queues and Background Jobs

Use for durable asynchronous work, scheduled jobs, long-running tasks or worker operations. Skip a queue when a bounded in-process operation meets the requirement. Distributed-systems guidance owns cross-service consistency; this guide owns job lifecycle, admission, leases and replay.

## Define delivery and ownership

Start with a real job: accepted, pending, claimed, running, succeeded, retryable failure, terminal failure and cancellation as applicable. Define when the caller receives an acknowledgement and which state is durable at that point. Choose a queue or scheduler from ordering, delay, throughput, durability and hosting needs, not popularity.

Acknowledge only after the intended durable boundary. Expect redelivery. Store an idempotency key scoped to the operation and tenant, a request fingerprint and a durable outcome. Pair state changes with outbox publication when needed. Exactly-once delivery claims do not remove the need to reconcile external effects.

## Worker contract

- Bound concurrency, queue depth and per-tenant work. Use fair scheduling or separate capacity where one customer can starve others.
- Set deadlines, visibility/lease duration, heartbeat rules and retry budgets from measured job duration and failure modes. Fence stale workers when their late writes can corrupt state.
- Retry transient faults with backoff and jitter. Reject invalid work promptly. Limit attempts and total age; a dead-letter queue needs an owner and a diagnosed replay procedure.
- Check cancellation at safe boundaries. A cancelled request may already have caused an external effect; reconcile instead of announcing reversal.
- Drain on shutdown, stop claiming work, and renew or release existing leases within a bounded grace period.
- Preserve trace and causation IDs without copying secrets into job payloads. Prefer references to durable objects over large private payloads.

For schedules, define timezone, daylight-saving behavior, overlap policy, missed-run catch-up and clock assumptions. For recurring business periods, derive a stable period key so scheduler retries do not produce duplicate effects. Avoid claiming globally synchronized execution from wall-clock timestamps.

## Failure exercise

For an invoice notification job, crash after the invoice commit but before publication; recover the outbox. Crash after sending but before acknowledgement; reconcile the provider outcome or use its idempotency contract before sending again. Re-deliver an old event, run two workers after a lease expires, cancel mid-flight and replay a dead-letter item. Verify one intended business effect, truthful status and an inspectable history.

## Operations and verification

Measure oldest-job age, time-to-start, completion latency, retries, dead letters, lease loss and downstream saturation. Queue length alone is insufficient. Load-test admission and drain behavior with a representative job mix; scaling workers must respect database and provider limits.

Record the actual broker/scheduler, acknowledgement semantics, crash boundaries and replay outcomes. A unit test with an immediate synchronous mock does not establish durable recovery. Use [distributed systems](edge-and-distributed-systems.md), [backend](backend-and-data-engineering.md) and [observability](observability-and-incident-response.md) for related contracts.

## Event envelopes and schedules

Define event ID, producer, schema version, timestamp, correlation ID and tenant where applicable. A database table owned by another service is not an implicit event contract. For schedules, specify timezone/DST behavior, missed-run handling and coordination across replicas. Give long jobs a visible state, cancellation policy and heartbeat/lease renewal; poison messages must not block unrelated work. Use the [job specification](../templates/QUEUE_AND_JOB_SPEC.md) when these details need a shared contract.
