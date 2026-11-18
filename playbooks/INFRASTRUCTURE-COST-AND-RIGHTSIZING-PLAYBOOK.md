# Playbook: Infrastructure Cost and Rightsizing

1. Tag/attribute costs by service, environment, and owner.
2. List top spend drivers (compute, database, egress, storage, observability, third-party APIs).
3. Check utilization against allocation; identify idle and oversized resources.
4. Quick wins: delete orphaned resources, schedule non-prod shutdown, lifecycle storage, compress/caching to reduce egress, review log retention and metric cardinality.
5. Structural options: reserved/committed use, spot for tolerant workloads, different provider/region, managed vs self-hosted trade-offs, architecture simplification.
6. Validate that reliability and security are not degraded.
7. Set budgets, anomaly alerts, and monthly review.
