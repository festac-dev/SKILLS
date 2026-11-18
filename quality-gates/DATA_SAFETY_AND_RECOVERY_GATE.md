# Data Safety and Recovery Gate

- [ ] RPO/RTO agreed.
- [ ] Backups automated, encrypted, off-host, versioned.
- [ ] Restore drill completed with recorded time and verification.
- [ ] Backup credentials cannot delete history; access logged.
- [ ] Retention and deletion policy implemented and tested.
- [ ] Migrations backed up and rehearsed.
- [ ] Personal and sensitive data inventory and minimization reviewed.
- [ ] Disaster scenarios (disk loss, region loss, credential compromise, bad deploy, accidental delete) have runbooks.

## Deep guidance (v4)
Evidence to attach: last successful backup timestamp, last **restore drill** date with measured RTO and RPO, backup encryption and off-site/immutable copy proof, access list to backups, retention schedule, deletion propagation test.
**Fail the gate when:** backups exist but were never restored; the only copy lives in the same account/region/credentials as production; restore steps live in one person's head; encryption keys are not recoverable independently of the data; RPO/RTO were never agreed with the owner.
**Spot checks:** restore into a scratch environment and run an application smoke test against it; verify a deleted-user request removes data from primary, replicas, search, caches and analytics (or documents expiry).
