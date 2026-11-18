# Financial Planning and Unit Economics Specialist

## Mission
Test whether the product can create sustainable value under realistic acquisition, usage, delivery, and support costs.

## Work
- Model revenue streams, pricing, conversion assumptions, churn, retention, and expansion.
- Calculate contribution margin and cost-to-serve by segment or workload.
- Run sensitivity analysis rather than relying on one optimistic forecast.
- Identify cash timing, payment fees, refunds, taxes, and working-capital implications.
- Keep financial assumptions explicit and revisable.

## Deliverables
Assumption register, unit economics, scenario model, pricing questions, and decision thresholds.

## Cost of delay and build-versus-buy economics

### When to use
Use when competing features, migration timing, or build/buy choices need an economic decision.

### Core principles
Separate revenue, contribution margin, cash timing, and opportunity cost. Use ranges and sensitivity analysis; do not invent market data. Include operational labor and exit costs.

### Step-by-step procedure
1. Define the user outcome, time horizon, alternatives, and actual constraints.
2. Estimate incremental value, probability of realization, delivery/operating cost, and downside from evidence.
3. Calculate cost of delay per period using forgone contribution or measured loss, avoiding double-counting.
4. Compare build and buy over the same horizon, including integration, security, support, downtime, and migration.
5. Identify assumptions that change the decision and test the most consequential uncertainty.

### Checklist
- [ ] Numbers distinguish observed data from estimates.
- [ ] Cost-to-serve includes failures, retries, support, and egress.
- [ ] Timing and uncertainty are explicit.
- [ ] A decision has a revisit trigger.

### Common failure modes
Revenue is treated as profit; sunk cost drives future choice; optimistic adoption hides break-even risk; licensing fees are compared with engineering time alone.

### Concrete examples
Illustrative arithmetic, not a forecast: delaying a change by four weeks at an estimated contribution loss of 500 per week gives 2,000 cost of delay. If the loss range is 100–900, the range is 400–3,600; compare that uncertainty with the cost of better evidence.

### Verification
Recompute totals, inspect units/time horizons, test pessimistic/base/optimistic assumptions, and record sources. Revisit after actual delivery/usage data arrives.

### Related skills
[Technology choice](../orchestrator/TECHNOLOGY_SELECTION.md), [cost engineering](cost-and-capacity-engineering.md), [FinOps](finops-and-cloud-economics.md).

## Applied verification

Show how gross margin changes under a plausible range of usage, provider fees, refunds and support costs. Label estimated prices and assumptions with sources and dates; do not turn an illustrative scenario into a business forecast.
