# Server Hardening Checklist

Host: ______ OS/version: ______ Owner: ______ Date: ______

- [ ] Admin accounts named; root SSH login disabled; key-only SSH.
- [ ] Firewall default-deny; open ports match the intended list.
- [ ] Database/cache/admin ports not publicly reachable.
- [ ] Automatic security updates configured; reboot plan documented.
- [ ] Services run as unprivileged users with sandbox options.
- [ ] Secrets stored outside the repo with restricted permissions.
- [ ] TLS valid with automatic renewal and expiry alert.
- [ ] Time sync, log rotation, and disk alerts configured.
- [ ] Monitoring and alert routing confirmed with a test alert.
- [ ] Off-host encrypted backups running; restore tested on ______.
- [ ] Rebuild-from-scratch procedure documented/scripted.
- [ ] Out-of-band access method confirmed.
- [ ] End-of-life dates for OS/runtimes recorded.

Evidence (commands run, outputs summarized, not secrets):
Exceptions and accepted risks:
