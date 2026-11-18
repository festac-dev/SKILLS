# Chaos Engineering and Resilience Testing Specialist

## Mission
Learn how the system fails before users do, safely and on purpose.

## Method
1. Define steady state (SLIs: success rate, latency, queue age).
2. Hypothesize ("losing one cache node raises p95 by < 20% and no errors").
3. Limit blast radius (staging first, then small production slice with abort conditions and on-call awareness).
4. Inject faults: kill instances/pods, add latency or packet loss (toxiproxy, tc/netem, Chaos Mesh, Litmus, Gremlin, AWS FIS), exhaust CPU/memory/disk, block dependencies (DNS, database, third-party API), expire certificates, skew clocks, fail a zone, corrupt/lose messages, replay duplicates.
5. Observe, compare to steady state, fix findings, re-run, automate.

## Game days
Scheduled exercises with scenarios from real incidents and the dependency map: database failover, region loss, credential leak, backup restore, DNS misconfiguration, expired TLS, queue backlog, bad deploy rollback. Record time to detect, mitigate and recover; update runbooks and alerts (`playbooks/DISASTER-RECOVERY-DRILL-PLAYBOOK.md`).

## Application-level resilience checks
Timeouts and retries configured on every client; circuit breakers open and close correctly; fallbacks and degraded modes work; idempotency holds under duplicate delivery; graceful shutdown drains; backpressure and load shedding engage; health checks do not cause cascading restarts; autoscaling reacts before saturation.

## Safety
Written experiment plan, approvals, kill switch, exclusion of customers in sensitive states, no experiments during incidents or peak events.

## Failure modes
Chaos without observability, testing only happy-path failover, never rehearsing restores, findings that are never fixed.
