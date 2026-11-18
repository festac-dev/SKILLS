# Backend and API Gate

- [ ] Contract exists (machine-readable or unambiguous) and matches behavior.
- [ ] All inputs validated at boundaries with size/time limits.
- [ ] Authorization enforced server-side per object and tenant; negative tests exist.
- [ ] Errors use a consistent safe shape with correlation IDs.
- [ ] Idempotency/retry behavior defined for creates, payments, and webhooks.
- [ ] Pagination bounded; list endpoints cannot return unbounded data.
- [ ] Database constraints, indexes, and migrations reviewed; migration rollback or expand/contract plan exists.
- [ ] External calls have timeouts, retries with backoff, and failure behavior.
- [ ] Background work is idempotent with dead-letter handling.
- [ ] Rate limits/quotas and abuse controls exist where exposure warrants.
- [ ] Secrets are outside the repo; config validated at startup.
- [ ] Logs are structured and free of secrets/unnecessary personal data.
- [ ] Tests actually run and results are reported accurately.
