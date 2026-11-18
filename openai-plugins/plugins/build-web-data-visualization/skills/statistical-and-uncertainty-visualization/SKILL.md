---
name: openai-statistical-and-uncertainty-visualization
description: Design statistically honest and uncertainty-aware visualizations. Use when the user needs help showing distributions, intervals, confidence, missingness, sampling effects, or analytical rigor in charts and dashboards.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Statistical and Uncertainty Visualization

## Overview

Use this skill when the risk is analytical distortion rather than rendering difficulty. This skill focuses on distributions, intervals, uncertainty, missingness, aggregation effects, and common statistical storytelling failures.

Default assumption: if a claim depends on variability, estimation, sampling, or model uncertainty, the visualization should show that explicitly.

## Working Pattern

1. Identify whether the viewer needs exact values, distributions, intervals, or model-derived estimates.
2. Choose encodings that show spread, uncertainty, missingness, or sample size honestly.
3. Avoid summarizing away the variation that matters to the decision.
4. Pair concise explanations with the view when the uncertainty concept is nontrivial.

## Output Expectations

- Name the statistical question, not just the chart type.
- Explain why the chosen encoding is more truthful than the tempting alternative.
- Call out when aggregation, smoothing, or interval choice can mislead.

## References

- Shared theory:
  - `../../references/foundations/task-abstraction-and-chart-selection.md`
  - `../../references/foundations/perception-color-and-encoding.md`
- Skill references:
  - `./references/distribution-and-summary-choices.md`
  - `./references/uncertainty-encodings.md`
  - `./references/experimental-and-analytical-pitfalls.md`
  - `./references/missingness-and-confidence.md`

## Representative Prompts

- "What chart should I use to show uncertainty here?"
- "Should this be a histogram, box plot, violin plot, or density plot?"
- "How do I show confidence intervals without misleading people?"
- "This dashboard hides variability. How should I fix it?"
- "Help me visualize missing data and sample size honestly."
