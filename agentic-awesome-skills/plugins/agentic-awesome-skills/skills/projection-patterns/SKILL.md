---
name: agentic-awesome-projection-patterns-afe07e85
description: Build read models and projections from event streams. Use when implementing
  CQRS read sides, building materialized views, or optimizing query performance in
  event-sourced systems.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Projection Patterns

Comprehensive guide to building projections and read models for event-sourced systems.

## Use this skill when

- Building CQRS read models
- Creating materialized views from events
- Optimizing query performance
- Implementing real-time dashboards
- Building search indexes from events
- Aggregating data across streams

## Do not use this skill when

- The task is unrelated to projection patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Example

For `OrderItemAdded` at position 42, apply the increment and persist checkpoint 42
in one transaction. Replay position 42 and verify no second increment; crash
before commit and verify both the row update and checkpoint roll back together.
