# Performance Investigation Playbook

1. Define the user-visible symptom and affected journey.
2. Capture a representative baseline and environment.
3. Profile before optimizing; identify the dominant bottleneck.
4. Check network, rendering, database, memory, CPU, media, third parties, and background work.
5. Form one testable hypothesis at a time.
6. Change the smallest relevant area and compare under equivalent conditions.
7. Add a regression guard and document trade-offs.
8. Verify on representative devices and network conditions.

## Reproducible profiling and load experiments

### When to use
Use when users experience latency, resource exhaustion, queue lag, or an approaching capacity limit. Establish a measured bottleneck before optimizing.

### Core principles
Compare identical workloads and report distributions, not averages alone. Separate offered throughput from completed throughput and failures. Never load-test a shared or production target without scoped authorization.

### Step-by-step procedure
1. Choose a user journey, baseline, target, representative data volume, and resource limits.
2. Profile CPU, allocations, I/O, lock contention, database plans, and dependency time on that path.
3. Design normal, peak, burst, sustained, and degraded scenarios. Include cold/warm caches and realistic request mixes.
4. Set stop thresholds for latency, errors, saturation, and downstream impact before executing.
5. Change one bottleneck, repeat the same workload, and compare p50/p95/p99, throughput, error rate, cost, and resource headroom.
6. Check recovery after overload: queues drain, memory stabilizes, and useful work resumes.

### Checklist
- [ ] The load generator is not itself saturated.
- [ ] Timeouts and rejected work count in results.
- [ ] Data size and connection pools resemble the intended environment.
- [ ] Benchmarks record versions, seeds, warm-up, duration, and hardware.

### Common failure modes
Closed-loop generators can hide overload through coordinated omission; tiny datasets hide index costs; unbounded retries amplify failure; a faster median can conceal worse tail latency.

### Concrete examples
Python CPU diagnosis: `python -m cProfile -s cumulative scripts/toolkit.py --help` once that script exists. For Go use `go test -help` to verify benchmark/profile flags, then select actual package benchmarks. A queue worker experiment must measure oldest-message age as well as jobs per second.

### Verification
Provide the baseline and changed measurements with the same workload and explain tradeoffs. If only a local microbenchmark ran, keep production claims unverified.

### Related skills
[Performance budgets](../templates/PERFORMANCE_BUDGET.md), [reliability patterns](../references/reliability-engineering-patterns.md), [cost engineering](../specialists/cost-and-capacity-engineering.md).

## Application evidence

Repeat baseline and candidate measurements under the same cache, data and device conditions. Retain the trace identifying the bottleneck, report relevant percentiles and check that a faster path preserves correctness.

## Layer-specific measurements

Locate the slow interval before choosing a tool: browser trace and resource waterfall; network TTFB/cache behavior; server CPU/allocation profile; database plan and lock waits; host I/O, memory or CPU steal; external dependency duration. Record query-plan commands that execute work before running them on shared data. Consult [performance budgets](../references/performance-budgets-and-benchmarks.md), then update capacity triggers after a measured improvement.
