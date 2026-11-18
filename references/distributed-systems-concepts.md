# Distributed Systems Concepts

Use these ideas to reason about trade-offs; do not apply distributed patterns to problems a single database transaction already solves.

- **Fallacies to avoid**: the network is reliable, latency is zero, bandwidth is infinite, topology never changes, there is one administrator, transport cost is zero.
- **CAP / PACELC**: during partition choose consistency or availability; otherwise latency vs consistency.
- **Consistency models**: strong/linearizable, sequential, causal, read-your-writes, monotonic reads, eventual. Pick per operation.
- **Idempotency and exactly-once**: practical systems are at-least-once plus idempotent processing.
- **Ordering and clocks**: wall clocks drift; use logical/vector clocks, sequence numbers, or database ordering; hybrid logical clocks in some stores.
- **Consensus and leader election**: Raft/Paxos, quorums; use proven implementations (etcd, ZooKeeper, database primitives) rather than inventing them.
- **Replication**: single-leader, multi-leader, leaderless; sync vs async; lag and failover data-loss windows.
- **Partitioning**: hash, range, directory; hot keys; rebalancing cost.
- **Transactions across services**: avoid when possible; otherwise sagas (orchestration or choreography) with compensations, outbox, and idempotent steps. Two-phase commit has availability costs.
- **CRDTs / OT**: for collaborative state with offline edits.
- **Failure handling**: timeouts, retries with backoff and jitter, circuit breakers, bulkheads, load shedding, hedged requests (carefully), graceful degradation.
- **Backpressure**: bounded queues, concurrency limits, reject early instead of collapsing.
- **Observability**: correlation IDs, distributed traces, RED/USE metrics, structured logs.
- **Deployment safety**: canary, blue/green, feature flags, automated rollback, backward-compatible schemas and APIs.
- **Testing**: failure injection, partition simulation, soak tests, game days.
