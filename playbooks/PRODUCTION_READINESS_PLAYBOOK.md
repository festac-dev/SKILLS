# Production Readiness Playbook

## Product
Clear user journeys, support paths, truthful claims, accessible interaction, and documented limitations.

## Engineering
Reproducible builds, configuration validation, migration safety, dependency hygiene, secure defaults, and tested recovery.

## Operations
Service ownership, SLO-relevant signals, alert routing, runbooks, capacity, backups, incident response, and release rollback.

## Governance
Data inventory, retention, access review, vendor review, auditability, and qualified legal/regulatory review where required.

## Release
Preflight checklist, staged rollout, success/stop criteria, communications, post-release verification, and post-launch review.

Readiness is evidence-based and proportionate to product risk.

## Application evidence

Tie readiness to the candidate artifact, required environments and an exercised recovery path. Keep localhost smoke tests, browser fixtures and real-provider verification separate; missing required environments remain explicit gaps.

For systems that move value, bind any live canary to exact reviewed terms, strict amounts, fees, destination, profile and build. Persist submission intent before the external call, serialize concurrent attempts and reconcile an ambiguous response instead of retrying it. Verify a resulting receipt with the owning system; status labels and balance growth alone are insufficient. If only valueless test tokens are available, exercise the real adapters and recovery path while retaining funded production evidence as pending.

For traffic containment, distinguish configured proxies, synthetic leak probes and the actual deployed process tree. Record namespace/firewall enforcement, dropped capabilities, DNS/IPv4/IPv6 probes, proxy outage behavior and bounded packet captures. Kernel privileges and filesystem/Unix-socket boundaries matter; an unprivileged compatibility runtime does not supply native firewall enforcement.

Load the distributed configuration example through the actual application parser. Testing only small handcrafted examples can miss renamed options or documented settings that startup rejects. For strict adapter validation, distinguish client payload fields from metadata inserted by an SDK/parser; exercise the real parsing path while retaining rejection of unexpected client fields. Bump runtime compatibility when a running integration must restart to receive a correctness fix.
