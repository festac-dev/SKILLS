---
name: alireza-business-growth-skills
description: "Use when a growth request needs routing between customer-success-manager, sales-engineer, revenue-operations, contract-and-proposal-writer and support-ops."
license: MIT
metadata:
  version: 2.9.0
  author: Alireza Rezvani
  tags:
    - business
    - customer-success
    - sales
    - revenue-operations
    - growth
  agents:
    - claude-code
    - codex-cli
    - openclaw
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Business & Growth Skills — Router

This plugin bundles **5 skills** (this router is the 6th folder under `business-growth/skills/`). Each skill is self-contained.

## Routing table

Match the request, then load `business-growth/skills/<skill>/SKILL.md`. If multiple rows match, ask one clarifying question first.

| Request signals | Skill | Path |
|---|---|---|
| Customer health scores, churn risk, expansion plays | customer-success-manager | `skills/customer-success-manager/` |
| RFP/RFI coverage, competitive positioning, PoC plans | sales-engineer | `skills/sales-engineer/` |
| Pipeline coverage, forecast accuracy (MAPE), GTM efficiency | revenue-operations | `skills/revenue-operations/` |
| Proposals, contracts, statements of work, DPAs | contract-and-proposal-writer | `skills/contract-and-proposal-writer/` |
| Support SLAs, agent staffing (Erlang C), ticket deflection | support-ops | `skills/support-ops/` |

## Quick start

```bash
# Example: route an account-health request
cat business-growth/skills/customer-success-manager/SKILL.md
python3 business-growth/skills/customer-success-manager/scripts/health_score_calculator.py --help
```

## Rules

- Route to exactly one skill, then follow that skill's workflow. This router ships no tools of its own.
- Use the skills' Python scorers for metrics, not manual estimates; deal/contract outputs are drafts for human legal/commercial review.
