# Data Migration Playbook

## Plan
Inventory sources, schema, volume, dependencies, owners, retention, and rollback requirements.

## Prepare
Back up and test restore, define invariants, write idempotent migration steps, test representative and worst-case data, and establish stop conditions.

## Execute
Use checkpoints, bounded batches, observability, and explicit cutover ownership. Avoid uncontrolled dual writes.

## Verify
Compare counts and invariants, test reads/writes, inspect downstream systems, and reconcile exceptions.

## Close
Remove compatibility layers only when safe, document evidence, monitor, and retain recovery artifacts according to policy.

## Application evidence

Resume from a partial checkpoint while representative concurrent writes occur. Reconcile domain invariants and dependent reads, and document the last reversible point before destructive contraction.

## Coexisting consumers

Inventory old and new application versions, jobs, reports and replicas before contracting a schema. Observe an agreed soak period after switching readers/writers, retain the reverse path where feasible, and stop on predefined correctness or saturation limits. [Database operations](../specialists/database-engineering.md) owns engine-specific locks, concurrent indexes and backfills.
