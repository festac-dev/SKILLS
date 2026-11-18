# Playbook: Deploy to a VPS / Single Server

Only with explicit authorization to touch the server. Keep provider-console access open throughout.

1. **Inspect** — OS, resources, existing services, open ports, users, disk, backups, DNS. Record the starting state.
2. **Snapshot or backup** if the server holds anything of value.
3. **Harden** — create admin user, SSH keys, disable root/password login (verify in a second session), firewall, automatic security updates, time sync, log limits (`SERVER_HARDENING_CHECKLIST.md`).
4. **Runtime** — install the language runtime or container engine; create unprivileged service user; directories with correct permissions.
5. **App** — deploy artifact by version; env file with restricted mode; systemd unit or Compose stack with healthchecks and restart policy.
6. **Data** — database local (small) or managed; never exposed publicly; configure backups before go-live.
7. **Proxy and TLS** — reverse proxy, HTTP→HTTPS, ACME certificate with renewal test, security headers, body/timeouts, static caching.
8. **DNS** — lower TTL ahead of time, point records, verify propagation and email records if relevant.
9. **Observability** — uptime probe, resource and disk alerts, log access, certificate expiry alert, test alert delivery.
10. **Release procedure** — atomic switch or rolling replacement, smoke test, rollback command documented and tested.
11. **Restore drill** — rebuild or restore on a fresh machine from backups and scripts; record time.
12. **Document** — runbook, access list, update calendar.

Common pitfalls: forgetting swap/OOM behavior, logs filling disk, exposed database ports, unrenewed certificates, snapshots mistaken for backups, undocumented hand edits.

Smoke test and then lightly load test. Complete `templates/SERVER_HARDENING_CHECKLIST.md`, document in `templates/INFRASTRUCTURE_TOPOLOGY.md` and `templates/RUNBOOK.md`, then run `quality-gates/INFRASTRUCTURE_AND_OPERATIONS_GATE.md`.
