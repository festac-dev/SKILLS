# Integration and Operations Gate

Before release, verify all applicable items:
- [ ] Every external integration has a clear purpose and owner.
- [ ] Permissions are least-privilege and revocable.
- [ ] Webhooks are authenticated, replay-resistant and idempotent where applicable.
- [ ] Timeouts, retries, rate limits and provider outages are handled.
- [ ] Sensitive data is minimized and redacted from telemetry.
- [ ] Operators can understand service health and investigate failures.
- [ ] Backup and restore procedures are documented and tested where required.
- [ ] Production changes have authorization, rollback and evidence.
- [ ] User-visible status reflects actual persisted/confirmed state.
- [ ] Claims about provider activation, data collection or account permissions use evidence from the owning account/environment; unknown state is not reported as disabled.

## Application evidence

Separate local server health, populated workflow checks and real-provider communication. Verify a provider failure has a truthful usable state and does not silently become demo data.
