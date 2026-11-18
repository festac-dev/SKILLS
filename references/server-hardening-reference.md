# Server and Infrastructure Hardening Reference

Apply proportionally to the threat model. Verify each control; document exceptions.

## Access
- SSH keys only, no root login, named admin accounts, MFA on cloud consoles and registrars.
- Admin interfaces (databases, dashboards, Kubernetes API, monitoring) never exposed publicly; reach them via VPN/zero-trust/bastion.
- Offboarding revokes keys, tokens, and console access promptly.

## Network
- Default-deny firewalls; least open ports; private network for data tier; egress filtering for sensitive systems; rate limiting and WAF at edge when exposed.

## Host
- Patch OS and runtimes on schedule; remove unused packages and services; unattended security updates; kernel and reboot strategy.
- Mandatory access controls (AppArmor/SELinux) where practical; run services unprivileged; separate users per service.
- File integrity and audit logging (auditd or equivalent) for high-risk hosts.
- Time synchronization; disk encryption where required.

## Application runtime
- Dedicated service accounts, restricted file permissions, sandboxed systemd units or containers, resource limits, read-only filesystems where practical.

## Data
- Encryption in transit everywhere; at rest per risk; protected and tested backups; restricted database users per application with least privilege; no shared superuser credentials in apps.

## Supply chain
- Pinned dependencies and images, trusted registries, vulnerability scanning, signed artifacts where feasible, protected CI secrets.

## Detection
- Centralized logs off-host, alerts for auth failures, privilege changes, new listening ports, unexpected outbound traffic, certificate expiry, disk and resource anomalies, backup failure.

## Recovery
- Rebuild from code and configuration; rotate credentials after incidents; tested incident response with contacts and decision authority.

## Compliance note
Mapping to CIS Benchmarks, NIST, ISO 27001, SOC 2, PCI DSS, HIPAA, or other frameworks requires qualified review; this reference does not certify compliance.

## Linux host notes
Always keep a second SSH session and provider-console access open while changing SSH or firewall settings. Apply firewall rules to IPv4 and IPv6. Databases, queues, and admin tools listen on private interfaces or localhost. Use service accounts without a shell. Provider account and registrar need MFA.
