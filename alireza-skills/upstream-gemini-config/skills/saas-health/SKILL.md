---
name: alireza-saas-health
description: 'Calculate SaaS health metrics (ARR, MRR, churn, CAC, LTV, NRR) and benchmark
  against industry standards. Usage: /saas-health <metrics|quick-ratio|simulate> [options]'
metadata:
  upstream_headers:
    argument-hint: <metrics|quick-ratio|simulate> [options]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /saas-health

Calculate SaaS financial health metrics from raw business numbers, benchmark against industry standards, and project forward.

## Usage

```
/saas-health metrics --mrr <amount> [--customers <n>] [--churned <n>] [--json]
/saas-health quick-ratio --new-mrr <amount> --churned <amount> [--expansion <amount>]
/saas-health simulate --mrr <amount> --growth <pct> --churn <pct> --cac <amount> [--json]
```

## Examples

```
/saas-health metrics --mrr 80000 --customers 200 --churned 3 --new-customers 15 --sm-spend 25000
/saas-health quick-ratio --new-mrr 10000 --expansion 2000 --churned 3000 --contraction 500
/saas-health simulate --mrr 50000 --growth 10 --churn 3 --cac 2000
```

## Scripts
- `finance/skills/saas-metrics-coach/scripts/metrics_calculator.py` — Core SaaS metrics (ARR, MRR, churn, CAC, LTV, NRR, payback)
- `finance/skills/saas-metrics-coach/scripts/quick_ratio_calculator.py` — Growth efficiency ratio
- `finance/skills/saas-metrics-coach/scripts/unit_economics_simulator.py` — 12-month forward projection

## Skill Reference
→ `finance/skills/saas-metrics-coach/SKILL.md`

## Related Commands
- `/financial-health` — Traditional financial analysis (ratios, DCF, budgets)
