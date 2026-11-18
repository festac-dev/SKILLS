# Cost and Capacity Engineering Specialist

## Mission
Keep the product sustainable and responsive as usage, data, and complexity grow.

## Responsibilities
- Establish cost per user, task, request, workflow, tenant, or business outcome where useful.
- Identify infrastructure, storage, egress, model inference, third-party, and operational cost drivers.
- Model expected, peak, and failure-mode demand.
- Use budgets, quotas, caching, batching, backpressure, and graceful degradation appropriately.
- Avoid premature optimization; measure before adding complexity.

## Deliverables
Capacity assumptions, cost model, scaling triggers, budget alerts, and optimization backlog.

## Agent and inference budgets

### When to use
Use when AI/tool workloads risk exceeding latency, token, concurrency, or monetary limits.

### Core principles
Budget per successful user outcome, not per call alone. Count retries, failed runs, context growth, retrieval, storage, and tool execution. User-supplied limits override defaults.

### Step-by-step procedure
1. Record required quality and hard limits for elapsed time, steps, tool calls, input/output tokens, and spend.
2. Measure a representative baseline and p95 latency/cost. Separate provider time, queues, retrieval, and tools.
3. Reserve budget for verification and recovery. Set an early warning before the hard stop; a starting policy is warn at 80%, stop at the specified cap.
4. Cache only where identity, freshness, permissions, and correctness permit. Minimize irrelevant context before reducing evidence.
5. On budget exhaustion, stop new expensive work, reconcile pending mutations, and provide a resumable checkpoint.

### Checklist
- [ ] Retries fit both deadline and spend limits.
- [ ] Fallback models/providers preserve data policy and quality requirements.
- [ ] Parallelism is bounded by downstream capacity.
- [ ] Prices and token counts come from observed usage/current sources.

### Common failure modes
Cheap calls produce expensive retries; logs hide tool costs; all budget is consumed before tests; cached answers leak between tenants; silent quality downgrades mislead users.

### Concrete examples
If a run permits 20 tool calls, warn at 16 and reserve the remaining calls for verification/reconciliation rather than starting an unrelated feature. These are example limits, not universal quotas.

### Verification
Compare estimated and observed cost/latency per successful task, count aborted/failed runs, and test the budget-stop path.

### Related skills
[Agent runtime](../playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md), [context](../references/agent-context-and-handoffs.md), [unit economics](financial-planning-and-unit-economics.md).

## Applied verification

Model idle, expected and burst load with measured unit consumption. Include retries, replicas, background work and egress; compare the estimate to observed usage and state which assumptions dominate uncertainty.

## Saturation and scaling triggers

State the observed limiting component and workload, such as concurrent requests or writes per second, with the measurement environment. Compare query fixes, caching, batching and vertical capacity before choosing replicas or partitioning; none is a universal sequence. App-tier autoscaling can overload a shared database, so budget aggregate connections, failover headroom, scale ceilings and cost alerts together. Use the [capacity review](../templates/CAPACITY_AND_SCALING_REVIEW.md) and [load plan](../templates/LOAD_TEST_PLAN.md).
