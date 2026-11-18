# Playbook: Containerize and Deploy

1. Confirm the project benefits (reproducibility, environment parity, deployment target requires it).
2. Write a multi-stage Dockerfile, `.dockerignore`, non-root user, healthcheck, graceful shutdown.
3. Build locally; run with production-like config; test failure and restart.
4. Define Compose (or manifests) with networks, volumes, resource limits, secrets handling.
5. Add CI: build, scan, tag with immutable version, push to registry.
6. Choose runtime: single-host Compose, managed container service, or Kubernetes (justify).
7. Deploy to staging; run smoke tests; verify logs/metrics; rehearse rollback.
8. Production rollout with health-gated replacement; watch error rate and latency; keep previous image available.
9. Document operations: logs, shell access policy, upgrades, base-image patch cadence, volume backups.
