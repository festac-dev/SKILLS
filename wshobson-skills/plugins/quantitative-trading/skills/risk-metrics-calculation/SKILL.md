---
name: wshobson-risk-metrics-calculation
description: Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino,
  and drawdown analysis. Use when measuring portfolio risk, implementing risk limits,
  or building risk monitoring systems.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Risk Metrics Calculation

Comprehensive risk measurement toolkit for portfolio management, including Value at Risk, Expected Shortfall, and drawdown analysis.

## When to Use This Skill

- Measuring portfolio risk
- Implementing risk limits
- Building risk dashboards
- Calculating risk-adjusted returns
- Setting position sizes
- Regulatory reporting

## Core Concepts

### 1. Risk Metric Categories

| Category          | Metrics         | Use Case             |
| ----------------- | --------------- | -------------------- |
| **Volatility**    | Std Dev, Beta   | General risk         |
| **Tail Risk**     | VaR, CVaR       | Extreme losses       |
| **Drawdown**      | Max DD, Calmar  | Capital preservation |
| **Risk-Adjusted** | Sharpe, Sortino | Performance          |

### 2. Time Horizons

```
Intraday:   Minute/hourly VaR for day traders
Daily:      Standard risk reporting
Weekly:     Rebalancing decisions
Monthly:    Performance attribution
Annual:     Strategic allocation
```

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices

### Do's

- **Use multiple metrics** - No single metric captures all risk
- **Consider tail risk** - VaR isn't enough, use CVaR
- **Rolling analysis** - Risk changes over time
- **Stress test** - Historical and hypothetical
- **Document assumptions** - Distribution, lookback, etc.

### Don'ts

- **Don't rely on VaR alone** - Underestimates tail risk
- **Don't assume normality** - Returns are fat-tailed
- **Don't ignore correlation** - Increases in stress
- **Don't use short lookbacks** - Miss regime changes
- **Don't forget transaction costs** - Affects realized risk
