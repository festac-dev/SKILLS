---
name: microsoft-azure-advisor-actionability
description: 'Get remediation instructions for selected Azure Advisor recommendations.
  WHEN: fix a selected recommendation, generate remediation commands. DO NOT USE FOR:
  unused-resource discovery, savings or deletion prevalidation (use azure-advisor-cost-optimization).'
license: MIT
metadata:
  author: Microsoft
  version: 1.0.2
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Azure Advisor Actionability

## Quick reference

Present remediation for the customer to run; never execute without explicit confirmation. Require the `recommendationTypeId` GUID and complete affected `resourceId`; reuse known values, ask for missing values, never guess.

Get `resourceId` from the user or an exact `advisor_recommendation_list` affected-resource record. Ask which resource if ambiguous; never use a recommendation instance ID.

## Workflow

1. Call `advisor_remediation_get` once with only `recommendationTypeId`, never `resourceId`, before generating guidance or substituting values.
2. For `RemediationNotFound`, empty responses, or no usable remediation, state that Advisor remediation is unavailable. Retrieve relevant public Microsoft Learn documentation; ask for the recommendation description if unknown. If none is available, say so; never invent guidance. Report other tool errors without internals, not as empty results.
3. Use only returned remediation or retrieved Learn guidance, including warnings and verification.
4. After retrieval, substitute unambiguous placeholders from the exact affected `resourceId` or confirmed context: subscription, resource group, resource names, full resource ID. Preserve and describe unresolved placeholders.
5. Preserve step order; separate Azure CLI and PowerShell.

For Advisor `guidance`, do not generate commands. For `hybrid` or `executable`, include every manual, decision, and command step. Omit raw JSON and internal labels.

## Final response

Label the source: "Guidance source: Azure Advisor remediation tool" or "Guidance source: publicly available Microsoft Learn documentation" with retrieved `learn.microsoft.com` citations. Never attribute fallback guidance to Advisor or claim execution.
