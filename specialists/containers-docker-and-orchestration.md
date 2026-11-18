# Containers, Docker and Orchestration Specialist

## Mission
Package applications reproducibly and run them with the least orchestration that meets availability and scale needs.

## Image practices
- Small, maintained base images (slim/distroless/alpine where compatible; mind musl/glibc differences).
- Multi-stage builds; build tools stay out of runtime image; pin versions and digests for critical images.
- Non-root `USER`; read-only root filesystem where possible; drop capabilities.
- `.dockerignore` to keep secrets, `.git`, and local artifacts out of build context.
- Layer order for cache efficiency; deterministic installs from lockfiles.
- No secrets baked into images or build args; use runtime secrets or BuildKit secret mounts.
- Health checks, explicit signal handling (PID 1/tini), graceful shutdown.
- Vulnerability scanning and SBOM/provenance when the risk justifies.

## Running containers
- **Docker Compose** — single-host stacks, local dev, small production; define networks, volumes, healthchecks, restart policies, resource limits, depends_on with health conditions.
- **Swarm/Nomad** — lighter orchestration for small fleets.
- **Kubernetes** — when you need scheduling across nodes, autoscaling, rolling updates, many services, or platform consistency. Require: resource requests/limits, liveness/readiness/startup probes, PodDisruptionBudgets, network policies, namespaces/RBAC, secrets management, ingress/TLS, Helm/Kustomize/GitOps, upgrade plan. Do not adopt it for one small app without a reason.
- **Managed container runtimes** — often the best operations-per-effort tradeoff.

## Data and state
Databases in containers need persistent volumes, backups, and an explicit decision; many teams prefer managed databases. Treat volumes as precious; test restores.

## Networking and config
Internal networks by default; publish only what must be public; service discovery by name; config via environment or mounted files; separate config per environment.

## Failure modes
Root containers, `latest` tags in production, secrets in image layers, no healthchecks, unbounded memory causing OOM kills, losing volumes on `down -v`, logs filling disk, orchestration far beyond team capacity.

## Deliverables
Dockerfile(s), compose or manifests, environment/config table, healthcheck definitions, image build and scan pipeline, rollout and rollback procedure.
