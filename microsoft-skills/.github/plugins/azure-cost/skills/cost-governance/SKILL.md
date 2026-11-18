---
name: microsoft-cost-governance
description: 'Govern Azure costs with budgets, alerts, tags, and policy restrictions.
  WHEN: "Azure budget health", "configured budget overrun", "list Azure budgets",
  "create Azure budget", "budget alerts", "budget coverage", "missing CostCenter tags",
  "allowed VM SKUs", "allowed Azure regions", "would this SKU be denied", "cost guardrails".
  DO NOT USE FOR: planning-target forecasts, bill investigations, pricing, rightsizing,
  or commitments.'
license: MIT
metadata:
  author: Microsoft
  version: 1.0.1
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Cost Governance

## Quick Reference

| Intent | Workflow | Primary tools |
|--------|----------|---------------|
| Check budget status | [Budget health](references/budget-health.md) | `list_budgets`, `forecast_costs`, `query_costs`, `list_alerts` |
| Configure a budget | [Budget setup](references/budget-setup.md) | Cost tools, `create_budget` |
| Review guardrails | [Guardrails](references/guardrails.md) | Resource Graph, `list_budgets` |

## When to Use This Skill

Use for budgets, alerts, tags, and policy.

## MCP Tools

Use cost tools for budgets; Resource Graph for guardrails. Writes need
confirmed scope, amount, thresholds, and recipients. Fallback:
[API mappings](references/tool-fallback.md).

## Workflow

1. Confirm scope and load the matching workflow.
2. Never transform MCP results in a shell or interpreter; request tool-side
   filtering or bounded follow-up queries.
3. Distinguish access failures from empty results.
4. Report gaps without implying budgets cap spend.

## Error Handling

| Error | Action |
|-------|--------|
| Access denied | Name missing permission. |
| No budget or forecast | Report unavailable data, not zero. |
| Multiple currencies | Never sum or compare across currencies. |
| Write conflict | Preserve the budget. |
| Server error | Retry once; then stop with the trace ID. |
