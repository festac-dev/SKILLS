# Observability Signal Catalogue

## Golden signals
Latency, traffic, errors, saturation. Track per service and per critical endpoint.

## Application
Request duration histograms, error rate by code, dependency call latency and failures, job duration and retries, queue depth and age, cache hit ratio, DB query time and pool usage.

## Infrastructure
CPU, memory, swap, disk usage and IOPS, inodes, network errors, open file descriptors, container restarts, OOM kills, certificate expiry days, backup age and last restore test.

## Business and product
Signup completions, checkout success, jobs completed, active sessions, feature usage, payment failures.

## Example SLOs (adapt)
- 99.9% of requests to key API succeed over 30 days.
- 95% of page loads complete core interaction under 2.5 seconds on a reference device.
- 99% of background jobs start within 60 seconds.
- Backups completed within 24 hours; restore test passes monthly.

## Alerting rules
Page on user-visible symptoms and imminent resource exhaustion; ticket for slow burns. Include runbook link, owner, severity and dashboard.

## Logging
Structured JSON, request/trace IDs, tenant and user IDs where lawful, no secrets, sampling for noisy events, retention matched to need.

## Cardinality warning
Never use unbounded values (user ID, URL with IDs) as metric labels.
