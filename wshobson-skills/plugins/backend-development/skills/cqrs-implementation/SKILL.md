---
name: wshobson-cqrs-implementation
description: Implement Command Query Responsibility Segregation for scalable architectures.
  Use when separating read and write models, optimizing query performance, or building
  event-sourced systems.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# CQRS Implementation

Comprehensive guide to implementing CQRS (Command Query Responsibility Segregation) patterns.

## When to Use This Skill

- Separating read and write concerns
- Scaling reads independently from writes
- Building event-sourced systems
- Optimizing complex query scenarios
- Different read/write data models needed
- High-performance reporting requirements

## Core Concepts

### 1. CQRS Architecture

```
                    ┌─────────────┐
                    │   Client    │
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │  Commands   │          │   Queries   │
       │    API      │          │    API      │
       └──────┬──────┘          └──────┬──────┘
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │  Command    │          │   Query     │
       │  Handlers   │          │  Handlers   │
       └──────┬──────┘          └──────┬──────┘
              │                         │
              ▼                         ▼
       ┌─────────────┐          ┌─────────────┐
       │   Write     │─────────►│    Read     │
       │   Model     │  Events  │   Model     │
       └─────────────┘          └─────────────┘
```

### 2. Key Components

| Component           | Responsibility                  |
| ------------------- | ------------------------------- |
| **Command**         | Intent to change state          |
| **Command Handler** | Validates and executes commands |
| **Event**           | Record of state change          |
| **Query**           | Request for data                |
| **Query Handler**   | Retrieves data from read model  |
| **Projector**       | Updates read model from events  |

## Templates and detailed worked examples

Full template library and detailed worked examples live in `references/details.md`. Read that file when you need the concrete templates.

## Best Practices

### Do's

- **Separate command and query models** - Different needs
- **Use eventual consistency** - Accept propagation delay
- **Validate in command handlers** - Before state change
- **Denormalize read models** - Optimize for queries
- **Version your events** - For schema evolution

### Don'ts

- **Don't query in commands** - Use only for writes
- **Don't couple read/write schemas** - Independent evolution
- **Don't over-engineer** - Start simple
- **Don't ignore consistency SLAs** - Define acceptable lag
