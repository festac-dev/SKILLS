# Third-Party Integration Playbook

1. Define why the integration is needed and what happens without it.
2. Review provider reliability, security, data use, permissions, pricing, support, and exit.
3. Define contract, versioning, authentication, quotas, and data mapping.
4. Implement timeouts, idempotency, bounded retries, signature verification, and reconciliation.
5. Test provider outages, malformed data, duplicates, and credential rotation.
6. Monitor health, cost, schema changes, and usage.
7. Document ownership, support escalation, and replacement/export procedure.

## Application evidence

Exercise signed/authorized input, duplicate delivery, unavailable provider and uncertain commit with the supported contract version. Verify recovery and revoke disposable credentials when appropriate; mock outcomes establish only the boundary behavior they simulate.

Before reporting an integration as enabled, check the relevant [configuration layer](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md#configuration-and-external-account-state): code, effective runtime configuration, provider account setting, or observed operation. Record the account/project and environment without exposing credentials. A working SDK client alone cannot confirm account-level collection, billing, consent or feature activation.
