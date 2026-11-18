# Reference Architectures by Scale (Illustrative)

Select by evidence. Each stage is a plausible shape, not a destination.

## Stage 0 — Prototype / MVP
One deployable app (or static site + functions), one managed database, managed auth if needed, object storage for files, logging to the platform, daily backups verified once.

## Stage 1 — Early product (hundreds to thousands of users)
Modular monolith, CI/CD, staging environment, error tracking, uptime checks, queue/worker for slow tasks, CDN for assets, migrations discipline, backup restore tested.

## Stage 2 — Growing product
Read replicas or caching where measured, dedicated workers, rate limiting, WAF/CDN protections, structured observability with SLOs, feature flags, IaC, secrets manager, load tests, runbooks, on-call.

## Stage 3 — Scaled product
Selective service extraction for proven boundaries, partitioning of hot data, search infrastructure, event streams, multi-AZ high availability, regional redundancy if justified, platform team practices, cost governance, disaster recovery drills.

## Stage 4 — Large/global
Multi-region data strategy, edge compute, advanced traffic management, compliance and data residency architecture, chaos engineering, capacity planning, internal developer platform.

## Heuristics
Do not skip operations basics to chase scale. Do not build Stage 4 for Stage 1 traffic. Each added component must have an owner, monitoring, backup/restore story, and removal criteria.
