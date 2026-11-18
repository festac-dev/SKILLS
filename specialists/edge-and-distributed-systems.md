# Edge and Distributed Systems Specialist

## Mission
Make behavior correct across regions, devices, unreliable networks, and independently failing components.

## Work
- Define consistency, ordering, time, identity, replication, partition, and conflict semantics.
- Account for clock skew, duplicate delivery, delayed messages, partial availability, and network partitions.
- Use leases, fencing tokens, idempotency, durable queues, and reconciliation where justified.
- Define data residency, locality, latency, and failover requirements.
- Avoid assuming exactly-once delivery or perfectly synchronized clocks.

## Deliverables
Consistency model, communication contracts, failure matrix, replication/failover plan, and chaos-test scenarios.

## Consistency, sagas, outbox, and overload

### When to use
Use when a workflow spans processes, regions, independent datastores, or disconnected clients.

### Core principles
State consistency guarantees per operation. During a network partition, a distributed read/write operation cannot guarantee both linearizable consistency and availability; CAP is not a menu from which a whole product simply picks two. Local invariants still need explicit enforcement.

### Step-by-step procedure
1. Identify authoritative owners, transaction boundaries, idempotency keys, ordering scope, and tolerated staleness.
2. Use a transactional outbox when a database commit must produce a message: persist the business change and outbox record atomically, then publish asynchronously.
3. Expect duplicate delivery. Deduplicate consumers using a durable unique event key in the same transaction as effects.
4. Model multi-step workflows as states with compensations. A saga compensation is a new business action, not a guaranteed reversal of the past.
5. Use CRDTs only for operations with understood merge semantics. Authorization, deletion, and invariant constraints still need design.
6. Bound queues, retries, request deadlines, and per-tenant work. Shed load or defer visibly rather than exhaust memory.
7. Test partitions, stale leaders, delayed messages, clock skew, duplicate deliveries, and reconnect reconciliation.

### Checklist
- [ ] Retry budgets fit inside the caller deadline.
- [ ] Poison messages have ownership and replay rules.
- [ ] Leases use fencing where a stale worker could corrupt state.
- [ ] Reconciliation can detect missed or divergent effects.

### Common failure modes
“Exactly once” obscures external side effects; dual writes split state; last-write-wins loses user edits; autoscaling producers floods a fixed-capacity database; wall-clock order is mistaken for causal order.

### Concrete examples
For “create order and send notification,” commit the order and outbox row together. Crash after commit but before publish: the publisher must recover the row. Crash after publish but before marking sent: the consumer must ignore the duplicate event ID. Both cases belong in integration tests.

### Verification
Inject each crash at a controlled boundary and assert business invariants after recovery. Measure queue age, retry amplification, rejected work, and reconciliation discrepancies.

### Related skills
[Backend](backend-and-data-engineering.md), [realtime](realtime-and-collaboration.md), [formal methods](formal-methods-and-invariants.md).

## Applied verification

Simulate duplicate delivery and a partition during an acknowledged write. Verify each declared consistency guarantee, bound queued work, and reconcile after reconnect without claiming global exactly-once execution.
