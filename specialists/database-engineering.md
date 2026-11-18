# Database Engineering

Use for persistent data modeling, transactions, query performance, database operations or schema evolution. Skip adding a database when project state does not need one. Backend owns business operations; this guide owns storage semantics and capacity; the recovery specialist owns restore drills.

## Choose from the workload

Inspect the existing engine, supported versions, topology and access layer. Identify invariants, read/write paths, expected data volume, concurrent writers, search/analytics needs, retention, residency and recovery objectives. Compare embedded, relational, document, key-value, search and analytical stores only where their trade-offs matter. A database marketed as distributed does not remove transaction, conflict or operating decisions.

Define keys and ownership before tables or collections. Use enforced uniqueness, foreign keys or equivalent constraints where supported. Distinguish entity identity from display order. Specify precision, currency, timezone, nullable state, immutable history and deletion behavior. Choose tenant isolation from the threat model and operating cost; a client-supplied tenant ID never establishes authority.

## Prove transaction behavior

Write the invariant and competing operations. Choose isolation, conditional updates, row locks, optimistic versions or serialization based on the actual engine. Establish a consistent lock order and bounded lock/statement timeouts. Retry only recognized transient failures, with a bounded policy and an idempotent operation. Keep external calls outside long transactions and use an outbox when commit must cause an external effect.

Test races with independent connections against the supported database. Verify both caller outcomes and final state. An in-memory substitute or a sequential test does not establish production isolation. For example, two buyers racing for the last unit must produce one successful reservation and a nonnegative stock balance, including after a lost response and retry.

## Read paths and capacity

Use representative data and an actual query plan before adding indexes. Check selectivity, ordering, covering/index-only behavior, write cost, N+1 access, unbounded exports and pathological filters. Paginate with a stable tie-breaker; decide how concurrent changes affect the traversal. Inspect replica lag before routing read-after-write work to replicas.

Budget connections across every replica, worker, migration process and operator reserve. Bound request concurrency upstream of the database. Monitor pool wait, lock wait, slow-query distribution, disk growth, replication lag and maintenance work. Do not log query parameters that contain private data. Verify caching and invalidation separately from database correctness.

## Change and recover safely

Use additive migrations and a compatibility window when old and new binaries overlap. Backfill in resumable bounded batches with checkpoints; rehearse large-table locking behavior. Distinguish application rollback from irreversible data transformation. Validate new constraints against existing rows before enforcing them where the engine supports staged validation.

Use engine-supported consistent backups. Test restore with encryption keys, schema version and a real application operation in an isolated target. Replication is not protection against propagated corruption. Use [migration](../playbooks/DATA_MIGRATION_PLAYBOOK.md) and [recovery](backup-and-disaster-recovery.md) for detailed rollout/drill procedures.

## Verification

Record engine/version, topology, representative data, transaction races, duplicate/retry outcomes, query plans, migration compatibility and restore evidence. Verify logical invariants as well as row counts. Mark untested failover, scale and recovery objectives as unverified.

## Engine-specific operations

Check the installed engine/version before assuming a column default, constraint validation or index build is online: these operations may scan, rewrite or lock a large table. Set lock and statement timeouts, rehearse concurrent readers and writers, and observe replication lag while backfilling. Keep schema changes compatible until every deployed consumer has migrated; use shadow reads or sampled comparisons where counts alone cannot prove equivalence. Verify the maintenance policy for vacuum/analyze, storage growth and major version upgrades. The [schema review](../templates/DATABASE_SCHEMA_REVIEW.md) and [SQL examples](../references/sql-and-data-patterns.md) supply concrete evidence formats.
