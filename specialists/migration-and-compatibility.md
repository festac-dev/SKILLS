# Migration and Compatibility Specialist

## Mission
Change systems without losing data, breaking users, or creating unmanageable transition states.

## Responsibilities
- Inventory current schemas, APIs, data, integrations, and consumers.
- Prefer additive, reversible steps and expand/contract migrations.
- Define backfills, checkpoints, validation, dual-read/write risks, cutover, and rollback.
- Preserve identifiers and user-visible history when required.
- Test realistic data volumes and interrupted migration scenarios.

## Deliverables
Migration plan, compatibility matrix, validation queries, rollback criteria, and post-migration checks.

## Strangler migration and zero-downtime cutover

### When to use
Use when replacing a legacy component, evolving data/contracts, or moving traffic between implementations.

### Core principles
Keep one clear source of truth during each phase. Prefer expand/contract and a strangler boundary over an unbounded rewrite. Zero downtime is an outcome to test, not a property of a diagram.

### Step-by-step procedure
1. Inventory consumers, data invariants, capacity, compatibility windows, and rollback limits.
2. Introduce an additive interface/schema and a routing seam. Keep old readers/writers compatible.
3. Backfill in bounded resumable batches from a consistent position. Validate keys, counts, constraints, and business aggregates.
4. If dual writes are necessary, define authority, atomicity limits, retry, deduplication, and repair. Prefer outbox/change capture over unrelated best-effort writes.
5. Shadow read-only traffic after removing external side effects and sensitive duplication. Compare semantic results, not raw incidental fields.
6. Cut over incrementally with measurable divergence/latency/error stop thresholds. Keep the old path recoverable for the stated window.
7. Contract/remove old state only after consumer telemetry and recovery evidence justify it.

### Checklist
- [ ] Backfill and live writes cannot create silent gaps.
- [ ] Deletions and schema changes propagate.
- [ ] Rollback accounts for data written after cutover.
- [ ] Shadow traffic cannot bill, email, or mutate twice.

### Common failure modes
Dual writes diverge; shadow requests trigger side effects; old consumers still depend on removed fields; schema rollback loses new data; retries restart a backfill from zero.

### Concrete examples
For renaming a field, add the new field, support both readers, backfill with checkpoints, switch writes/read preference, measure old-field usage, and remove it only after the compatibility window. A successful row-count comparison alone cannot prove semantic equality.

### Verification
Rehearse interruption, restart, concurrent writes, cutover, and rollback on representative data. Compare invariants and consumer behavior in both paths.

### Related skills
[Migration runbook](../templates/MIGRATION_RUNBOOK.md), [distributed systems](edge-and-distributed-systems.md), [cross-repo changes](monorepo-and-cross-repo-engineering.md).

## Applied verification

Resume a backfill from a partial checkpoint while both supported client versions write. Verify one source of authority and the business invariants before cutover; record whether recovery requires rollback or a forward repair.
