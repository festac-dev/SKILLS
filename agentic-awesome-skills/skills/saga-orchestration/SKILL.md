---
name: agentic-awesome-saga-orchestration-f9315be4
description: Patterns for managing distributed transactions and long-running business
  processes.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Saga Orchestration

Patterns for managing distributed transactions and long-running business processes.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## Do not use this skill when

- The task is unrelated to saga orchestration
- You need a different domain or tool outside this scope

## Use this skill when

- Coordinating multi-service transactions
- Implementing compensating transactions
- Managing long-running business workflows
- Handling failures in distributed systems
- Building order fulfillment processes
- Implementing approval workflows

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Example

After inventory reservation succeeds, a payment timeout is an unknown outcome.
Query the provider using the original idempotency key before charging again or
releasing inventory; record the resolution and retry compensation durably.
