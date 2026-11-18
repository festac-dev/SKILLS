# Data Platform and Pipeline Specialist

## Mission
Make data movement, transformation, quality, and lineage dependable.

## Responsibilities
- Define source contracts, schemas, ownership, freshness, lineage, retention, and access.
- Plan batch/stream processing, retries, deduplication, late events, backfills, and dead-letter handling.
- Add quality checks for completeness, validity, uniqueness, consistency, and timeliness.
- Separate operational data from analytical workloads where useful.
- Make pipeline failures observable and replay safe.

## Deliverables
Data flow diagram, schema contracts, quality rules, recovery plan, and ownership map.

## ETL, ELT, vector data, and model serving

### When to use
Use for ingestion, transformations, analytical models, embeddings, feature pipelines, training data, or inference serving.

### Core principles
Choose ETL when transformation must happen before the destination trust boundary; choose ELT when governed warehouse processing fits the workload. Version schema, transformation, and model/embedding configuration. Track provenance and deletion across derived data.

### Step-by-step procedure
1. Define source ownership, keys, event time versus processing time, freshness, retention, access, and schema-change policy.
2. Design incremental processing with watermarks, late-event handling, idempotent writes, bounded retries, and replay checkpoints.
3. In dbt projects, inspect installed adapters and project configuration before selecting commands. Test uniqueness, nullability, relationships, and business invariants, not only SQL compilation.
4. Keep training and evaluation splits separate by the leakage boundary: user, time, session, or entity. Version features and label availability.
5. For vector stores, bind each embedding to source ID, version, model, dimensions, ACL, and deletion state. Model changes generally require a versioned re-embedding/reindex plan.
6. For serving, record model version, feature compatibility, rollout, latency/cost budgets, drift signals, and rollback.

### Checklist
- [ ] Replaying a partition does not duplicate authoritative records.
- [ ] Late and deleted source data propagate correctly.
- [ ] Data/model versions are reconstructable.
- [ ] Online and offline feature meanings agree.

### Common failure modes
A timestamp-only watermark misses equal-time records; re-embedding mixes incompatible vector spaces; training leakage exaggerates accuracy; backfills starve production; deleted PII remains in vectors or caches.

### Concrete examples
In an installed dbt project, inspect `dbt --version` and `dbt build --help` before running the project's approved build selection. Validate duplicates with `SELECT source_id, COUNT(*) FROM events GROUP BY source_id HAVING COUNT(*) > 1;` against a disposable dataset whose schema includes those fields.

### Verification
Reprocess a bounded partition and compare keys, row counts, aggregates, freshness, and lineage. Test deletion and schema evolution through all derived stores. Use held-out inference data for quality claims.

### Related skills
[Data governance](data-governance-and-compliance.md), [search](search-relevance-and-recommendations.md), [migration](migration-and-compatibility.md).

## Applied verification

Interrupt a batch after some writes, replay its checkpoint, and process a late correction. Reconcile source-to-sink counts and domain totals, reject incompatible schema drift, and verify lineage still identifies the original input.

## Analytical stores and lineage

Compare ELT/warehouse, lakehouse, CDC and streaming approaches using required freshness, data volume and ownership. Keep production transaction capacity separate from analytical scans when they contend. Give incremental watermarks, backfills and schema changes an explicit replay policy; test freshness, volume anomalies and key constraints. Define shared metrics once, with lineage from raw data through staging to consumer models.
