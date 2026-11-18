# Database Schema Review

## Context
- Store(s) and version:
- Access patterns (top reads/writes, volume, growth):
- Consistency and transaction needs:

## Model
- Entities, relationships, cardinality, ownership:
- Constraints (PK/FK/unique/check/not-null):
- Public identifiers vs internal keys:
- Money, time, enum, JSON usage:
- Tenant isolation approach:

## Performance
| Query | Frequency | Index/plan | Expected latency |
|---|---|---|---|
| | | | |

## Lifecycle
- Retention, deletion, archival, audit/history:
- Migration plan (expand/contract) and rollback:
- Backup/restore and last restore test:

## Acceptance
- [ ] Integrity enforced by the database where practical.
- [ ] Indexes justified by real queries.
- [ ] Migrations tested on realistic data volume.
- [ ] Restore verified.

## Migration plan details
- Engine/version and reason:
- Lock and downtime assessment:
- Backfill plan (batch size, resumability):
- Rollback or forward-fix plan:
- Backup taken and verified before change (evidence):
- Test results on realistic data volume:
