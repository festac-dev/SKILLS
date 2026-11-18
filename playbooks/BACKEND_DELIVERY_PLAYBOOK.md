# Backend Delivery Playbook

Use for a new service, a substantial backend change or a requested production-readiness review. For a narrow defect, load the relevant specialist and repair that boundary directly. This playbook adds no deployment or external-mutation authorization.

## Start with one real operation

Inspect the current architecture, runtime, data stores, integration contracts, deployment target and operating owner. Define the actor, request, permission, invariant, durable result and failure response for one critical operation. Keep the existing supported stack unless a concrete constraint defeats it. Record consequential alternatives through [technology selection](../orchestrator/TECHNOLOGY_SELECTION.md).

| Concern | Owning guidance | Evidence that changes confidence |
|---|---|---|
| Boundaries and trade-offs | [Architecture](../specialists/architecture-and-systems-design.md) | Traced write path and recovery owner |
| Request/response and integrations | [API](../specialists/api-and-developer-experience.md) | Contract compatibility and a working consumer example |
| Persistent invariants and capacity | [Database](../specialists/database-engineering.md) | Competing transactions, representative query plans, migration compatibility |
| Identity and permissions | [Identity](../specialists/identity-and-access-management.md) | Denied cross-tenant and revoked-session access |
| Durable asynchronous work | [Queues](../specialists/queues-and-background-jobs.md) | Crash/redelivery/replay with one intended effect |
| Shared timely state | [Realtime](../specialists/realtime-and-collaboration.md) | Reconnect, authorization change and slow-consumer behavior |
| Host and traffic path | [Server operations](../specialists/network-and-server-operations.md) | Correct ingress, TLS, restart and resource limits |
| Builds and release | [DevOps](../specialists/devops-and-release.md) | Exact artifact, migration order, staged rollout and rollback |
| Service health | [Observability](../specialists/observability-and-incident-response.md) | A failure correlated to user impact and a usable alert |
| Recovery | [Backups](../specialists/backup-and-disaster-recovery.md) | Isolated restore with domain invariants and measured recovery window |

Load only rows the accepted task needs. A static site does not need queues, tenants, a cluster or disaster-recovery infrastructure simply because they appear here.

## Implement and challenge the slice

Keep server-side authorization and schema constraints authoritative. Bound inputs, uploads, request deadlines, downstream calls, connection pools and concurrency. Expose actionable errors without revealing protected resources. Reconcile an ambiguous timeout before retrying a side effect.

Test the slice under success, unauthorized access, invalid input, concurrent requests, duplicate delivery and a dependency failure at the relevant commit boundary. Assert final state as well as responses. Use the actual engine or provider boundary when its semantics are under test; clearly label fixtures and simulation.

Broaden to additional operations after the first path and its failure recovery work. Shared abstractions need actual repeated behavior, not forecast features. Record contracts, unusual invariants and operational decisions; omit comments that merely narrate code.

## Ship and operate within scope

Build once and identify the immutable artifact. Validate configuration names, secrets injection, schema compatibility, readiness, graceful shutdown and intended network exposure. Rehearse migration and rollback against representative data. For remote rollout, verify the current target and existing authorization, then follow the project's change procedure.

Confirm the running artifact through a meaningful operation and telemetry, not just a listening port. Measure observed capacity and recovery; do not turn an installation, a linter pass or an HTTP 200 into a production-readiness claim. Deliver the requested artifact, concise operating instructions and material limitations. Use existing [operational readiness](../templates/OPERATIONAL_READINESS_REVIEW.md) and [release evidence](../templates/RELEASE_AND_EVIDENCE_REPORT.md) templates only when they add value.

## Reference implementation

The [backend reference example](../examples/backend-reference/README.md) provides a local, testable service slice. Its persistence and deployment limits are part of the example; adapt the design to the real system of record and use [backend/API gates](../quality-gates/BACKEND_AND_API_GATE.md) only for applicable service requirements.
