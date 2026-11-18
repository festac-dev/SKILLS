---
name: agentic-awesome-domain-driven-design-2dee9402
description: Plan and route Domain-Driven Design work from strategic modeling to tactical
  implementation and evented architecture patterns.
metadata:
  upstream_headers:
    risk: safe
    source: self
    tags: '[ddd, domain, bounded-context, architecture]'
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Domain-Driven Design

## Use this skill when

- You need to model a complex business domain with explicit boundaries.
- You want to decide whether full DDD is worth the added complexity.
- You need to connect strategic design decisions to implementation patterns.
- You are planning CQRS, event sourcing, sagas, or projections from domain needs.

## Do not use this skill when

- The problem is simple CRUD with low business complexity.
- You only need localized bug fixes.
- There is no access to domain knowledge and no proxy product expert.

## Instructions

1. Run a viability check before committing to full DDD.
2. Produce strategic artifacts first: subdomains, bounded contexts, language glossary.
3. Route to specialized skills based on current task.
4. Define success criteria and evidence for each stage.

### Viability check

Use full DDD only when at least two of these are true:

- Business rules are complex or fast-changing.
- Multiple teams are causing model collisions.
- Integration contracts are unstable.
- Auditability and explicit invariants are critical.

### Routing map

- Strategic model and boundaries: `@ddd-strategic-design`
- Cross-context integrations and translation: `@ddd-context-mapping`
- Tactical code modeling: `@ddd-tactical-patterns`
- Read/write separation: `@cqrs-implementation`
- Event history as source of truth: `@event-sourcing-architect` and `@event-store-design`
- Long-running workflows: `@saga-orchestration`
- Read models: `@projection-patterns`
- Decision log: `@architecture-decision-records`

If templates are needed, open `references/ddd-deliverables.md`.

## Output requirements

Always return:

- Scope and assumptions
- Current stage (strategic, tactical, or evented)
- Explicit artifacts produced
- Open risks and next step recommendation

## Examples

```text
Use @domain-driven-design to assess if this billing platform should adopt full DDD.
Then route to the right next skill and list artifacts we must produce this week.
```

## Limitations

- This skill does not replace direct workshops with domain experts.
- It does not provide framework-specific code generation.
- It should not be used as a justification to over-engineer simple systems.
