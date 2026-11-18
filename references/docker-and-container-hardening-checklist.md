# Docker and Container Hardening Checklist

## Image
- [ ] Multi-stage build; runtime image minimal.
- [ ] Base image pinned and updated on a schedule.
- [ ] Non-root `USER`; no sudo or shell tools unless needed.
- [ ] No secrets in layers, build args, or history.
- [ ] `.dockerignore` excludes `.git`, env files, local data.
- [ ] Image scanned; SBOM stored if required.

## Runtime
- [ ] Read-only root filesystem with explicit writable volumes.
- [ ] Capabilities dropped; no privileged mode; no host network unless justified.
- [ ] Memory and CPU limits; restart policy; PID limit if supported.
- [ ] Healthcheck defined; signal handling for graceful stop.
- [ ] Logs rotated or shipped.

## Network
- [ ] Only the reverse proxy publishes ports; databases on internal networks only.
- [ ] Docker socket never mounted into application containers.
- [ ] Egress limited where practical.

## Data
- [ ] Named volumes with backups and restore tests.
- [ ] Database upgrade procedure documented.

## Delivery
- [ ] Immutable tags by commit; previous image retained for rollback.
- [ ] Registry credentials scoped and rotated.
