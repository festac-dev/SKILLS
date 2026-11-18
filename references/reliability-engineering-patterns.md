# Reliability Engineering Patterns

## Design for failure
- Set timeouts on remote calls.
- Retry only transient failures, with bounded exponential backoff and jitter.
- Use idempotency for operations that may be repeated.
- Apply circuit breakers, bulkheads, queues, and backpressure when justified.
- Define behavior for dependency outages and partial success.
- Avoid retry storms and unbounded work queues.

## Data and workflow correctness
Use explicit state machines, durable checkpoints, deduplication, reconciliation, and repair procedures for long-running or financial workflows.

## Service objectives
Choose service-level indicators that reflect user outcomes. Set objectives only after understanding the service's importance and realistic operating conditions.

## Evidence
Load tests, fault injection, restore exercises, incident reviews, and production telemetry should support reliability claims.

## SLOs, error budgets, capacity, and controlled faults

### When to use
Use for service reliability objectives, operational readiness, scaling, or a measured reliability regression.

### Core principles
Define reliability through user outcomes. An SLI needs an explicit numerator, denominator, exclusions, and window. Error budgets guide decisions; they are not permission to ignore severe failures.

### Step-by-step procedure
1. Select critical journeys and measurable availability, latency, freshness, or durability indicators.
2. Set an SLO from user/business requirements and current evidence. For a 99.9% request-success SLO, the allowed bad fraction is 0.001 over the agreed window.
3. Alert on burn rate: observed bad fraction divided by allowed bad fraction. Combine fast and sustained windows to avoid paging on noise or missing persistent degradation.
4. Attach an owner, user impact, and runbook to each page. Route informational signals to lower urgency.
5. Forecast capacity using measured resource cost per request/job plus headroom for failover and recovery.
6. Exercise faults first in isolated environments. Define scope, abort thresholds, rollback, and observation before any authorized production experiment.
7. Review incidents and repeated toil; track corrective actions through verification.

### Checklist
- [ ] SLI exclusions do not hide dependency failures users experience.
- [ ] Saturation and queue age accompany request error/latency metrics.
- [ ] A dependency outage has bounded degradation.
- [ ] Restore/failover procedures have execution evidence.

### Common failure modes
Healthy containers can serve failed journeys; aggregate metrics hide one tenant; high-cardinality labels overload monitoring; autoscaling reacts too slowly to prevent connection exhaustion; chaos without an abort path is uncontrolled failure.

### Concrete examples
If 99.9% success is the objective and observed errors are 1%, burn rate is `0.01 / 0.001 = 10`. That number alone does not set a paging threshold; select windows and traffic minimums from detection and response needs. A queue SLI can measure the fraction of accepted jobs completed within the promised deadline.

### Verification
Exercise an alert end-to-end to its responder, validate the SLI query against known events, and record recovery time and lost-data exposure from drills.

### Related skills
[Observability](../specialists/observability-and-incident-response.md), [backups](../specialists/backup-and-disaster-recovery.md), [performance](../playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md).

## Application evidence

Combine a timeout with a duplicate retry in an isolated failure exercise and inspect final state. Bound queues and catch-up after suspension; distinguish degraded but correct service from a fabricated success fallback.
