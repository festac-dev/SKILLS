---
name: agentic-awesome-n8n-node-configuration-0350d992
description: Operation-aware node configuration guidance. Use when configuring nodes,
  understanding property dependencies, determining required fields, choosing between
  get_node detail levels, or learning common configuration patterns by node type.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-01-30'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# n8n Node Configuration

Expert guidance for operation-aware node configuration with property dependencies.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
- You need to configure an n8n node correctly for a specific resource and operation.
- The task involves required fields, property dependencies, or choosing the right `get_node` detail level.
- You are troubleshooting node setup rather than overall workflow architecture.

---

## Configuration safety

Read and preserve the existing workflow, credentials references and node versions before targeted updates. Configure in a draft/test workflow with synthetic inputs; publishing or activating may trigger scheduled runs and external messages/writes. Confirm intended recipients and approval before those effects. Do not paste credentials into JSON or execution logs. HTTP targets must be scoped and validated rather than taken directly from untrusted items.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
