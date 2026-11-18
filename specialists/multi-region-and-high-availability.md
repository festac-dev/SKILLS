# Multi-Region and High Availability Specialist

## Mission
Raise availability with the lowest complexity that meets the target, and be honest about trade-offs.

## Ladder
Single node with fast recovery → redundant app nodes across zones → managed database with zone failover → read replicas / regional replicas → active-passive multi-region → active-active multi-region.

## Concerns
Failure domains (process, host, zone, region, provider, DNS, certificate, human), health-check design, leader election, quorum, replication modes (sync/async), conflict resolution, data residency, session/state handling, queue and cache replication, global load balancing, failover and failback testing, dependency availability (your uptime cannot exceed critical dependencies' without fallbacks), cost multiplier of redundancy.

## Principles
Avoid single points of failure that the target forbids; remove complexity that adds more failure than it prevents; test failover regularly; use CAP/PACELC reasoning explicitly for stateful systems; define degraded modes (read-only, queued writes, cached content).

## Failure modes
Untested failover, split-brain, replication lag data loss surprises, shared dependency outage across "independent" regions, config drift between regions.

## Deliverables
Availability target and error budget, failure-domain map, failover design and drill results, degraded-mode behavior.
