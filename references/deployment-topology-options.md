# Deployment Topology Options

Pick the smallest topology that meets requirements, with an upgrade path.

1. **Single VPS, all-in-one**: proxy, app, database, worker on one host. Cheapest. Risks: single point of failure, resource contention. Mitigate with backups, monitoring, fast rebuild.
2. **Single VPS + managed database/object storage**: reduces data risk and operations.
3. **Two or more app nodes behind a load balancer, managed database**: availability and rolling deploys.
4. **PaaS**: git push or image deploy; platform handles TLS, scaling, health. Check limits, cost curve and portability.
5. **Containers on managed orchestration**: many services or autoscaling needs; accept platform complexity.
6. **Serverless + managed data**: spiky workloads; watch cold starts and connection limits.
7. **Multi-region active-passive**: disaster tolerance; define data replication and failover test.
8. **Multi-region active-active**: global low latency; hard consistency and cost problems; justify with evidence.
9. **Edge-first**: static and edge compute with central data; careful with data locality.

## Decision inputs
Availability target, RTO/RPO, traffic, budget, team skills, compliance and data residency, vendor risk, operational capacity.

## Upgrade triggers
Define measurable signals for moving up a level, such as sustained CPU or memory saturation, deploy downtime becoming unacceptable, or recovery objectives not being met.
