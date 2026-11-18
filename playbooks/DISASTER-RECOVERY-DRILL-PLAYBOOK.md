# Playbook: Disaster Recovery Drill

1. Choose a scenario (deleted database, region loss, compromised credentials, corrupt deploy).
2. Set scope, safety rules, participants, and success criteria (RTO/RPO).
3. Use an isolated environment unless an authorized production drill is planned.
4. Start the clock; follow the runbook exactly as written by someone who did not write it.
5. Record every missing permission, unclear step, stale document, and surprise.
6. Verify restored data and application behavior.
7. Compare measured times to targets.
8. Fix documentation, automation, and gaps; schedule the next drill.
9. File results in `BACKUP_RESTORE_TEST_LOG.md` and `DISASTER_RECOVERY_PLAN.md`.
