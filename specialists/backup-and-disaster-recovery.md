# Backup and Disaster Recovery Specialist

## Mission
Make recovery possible, tested, and proportionate to business impact.

## Responsibilities
- Define recovery time objective (RTO) and recovery point objective (RPO) with stakeholders.
- Identify data, secrets, configuration, infrastructure, and dependencies that must be recoverable.
- Protect backups with encryption, access controls, separation, and retention policies.
- Test restoration, integrity, partial recovery, and recovery under compromised credentials.
- Document ownership, runbooks, communication, and decision authority.

## Deliverables
Recovery objectives, backup matrix, restore runbook, test evidence, and gap register.

## Restore drill procedure

### When to use
Use before claiming recoverability and after material data, encryption, storage, or deployment changes.

### Core principles
A successful backup job is not proof of recovery. Define RPO as tolerated data loss and RTO as tolerated recovery time; include detection, access, keys, infrastructure, and validation in the exercise.

### Step-by-step procedure
1. Inventory databases, object storage, configuration, encryption keys, secrets recovery, and external dependencies.
2. Choose a representative restore point and isolated target with approved synthetic or protected data.
3. Restore without overwriting the source. Measure time and identify missing permissions or keys.
4. Validate domain invariants, record counts, relationships, application reads/writes, and external reconnections.
5. Reconcile events after the restore point; prevent replay from duplicating financial or notification effects.
6. Record achieved RPO/RTO, gaps, ownership, and the next drill.

### Checklist
- [ ] Backups are separated from primary compromise/failure paths.
- [ ] Key retention permits authorized recovery.
- [ ] Restore procedures work without relying on one person's laptop.
- [ ] Validation checks meaning, not only archive integrity.

### Common failure modes
A backup cannot decrypt; replicas copy corruption; restored queues replay side effects; credentials point the drill at production; row counts match while relationships are broken.

### Concrete examples
SQLite snapshot mechanics in an isolated fixture can use its Python backup API: create a temporary database, copy through `sqlite3.Connection.backup`, then run `PRAGMA integrity_check` and application invariants against the copy. Verify the installed database's supported backup method before applying this pattern elsewhere.

### Verification
Retain restore start/end times, source point, target, integrity results, business checks, measured loss window, and unresolved recovery dependencies.

### Related skills
[Backend](backend-and-data-engineering.md), [incident response](../playbooks/INCIDENT_RESPONSE_PLAYBOOK.md), [operational readiness](../templates/OPERATIONAL_READINESS_REVIEW.md).

## Applied verification

Run the restored application against the isolated restore target and verify a representative user record with its related objects. Check that restored workers cannot send old notifications or charge again before enabling their external connections.

## Recovery independence

Include provider-account lockout, loss of encryption keys and corruption discovered after a backup in recovery scenarios. A snapshot inside the failed account is not an independent recovery path. Where the risk warrants it, use separately controlled immutable or versioned copies, restrict backup credentials from deleting history, and retain a tested recovery path for configuration and keys. Select backup/restore, pilot light or standby from measured RPO/RTO and operating cost; document failback and split-brain prevention. Record actual restoration in the [restore log](../templates/BACKUP_RESTORE_TEST_LOG.md) and [recovery plan](../templates/DISASTER_RECOVERY_PLAN.md).
