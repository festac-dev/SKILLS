---
name: agentic-awesome-ddd-tactical-patterns
description: Apply DDD tactical patterns in code using entities, value objects, aggregates,
  repositories, and domain events with explicit invariants.
metadata:
  aas-risk: safe
  aas-source: self
  aas-tags: '[ddd, tactical, aggregates, value-objects, domain-events]'
  aas-date-added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# DDD Tactical Patterns

## Use this skill when

- Translating domain rules into code structures.
- Designing aggregate boundaries and invariants.
- Refactoring an anemic model into behavior-rich domain objects.
- Defining repository contracts and domain event boundaries.

## Do not use this skill when

- You are still defining strategic boundaries.
- The task is only API documentation or UI layout.
- Full DDD complexity is not justified.

## Instructions

1. Identify invariants first and design aggregates around them.
2. Model immutable value objects for validated concepts.
3. Keep domain behavior in domain objects, not controllers.
4. Emit domain events for meaningful state transitions.
5. Keep repositories at aggregate root boundaries.

If detailed checklists are needed, open `references/tactical-checklist.md`.

## Example

```typescript
class Order {
  private status: "draft" | "submitted" = "draft";

  submit(itemsCount: number): void {
    if (!Number.isInteger(itemsCount) || itemsCount <= 0) throw new Error("Order cannot be submitted empty");
    if (this.status !== "draft") throw new Error("Order already submitted");
    this.status = "submitted";
  }
}
```

## Limitations

- This skill does not define deployment architecture.
- It does not choose databases or transport protocols.
- It should be paired with testing patterns for invariant coverage.
