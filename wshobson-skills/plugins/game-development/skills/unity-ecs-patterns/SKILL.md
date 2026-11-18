---
name: wshobson-unity-ecs-patterns
description: Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst
  for high-performance game development. Use when building data-oriented games, optimizing
  performance, or working with large entity counts.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Unity ECS Patterns

Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler.

## When to Use This Skill

- Building high-performance Unity games
- Managing thousands of entities efficiently
- Implementing data-oriented game systems
- Optimizing CPU-bound game logic
- Converting OOP game code to ECS
- Using Jobs and Burst for parallelization

## Core Concepts

### 1. ECS vs OOP

| Aspect      | Traditional OOP   | ECS/DOTS        |
| ----------- | ----------------- | --------------- |
| Data layout | Object-oriented   | Data-oriented   |
| Memory      | Scattered         | Contiguous      |
| Processing  | Per-object        | Batched         |
| Scaling     | Poor with count   | Linear scaling  |
| Best for    | Complex behaviors | Mass simulation |

### 2. DOTS Components

```
Entity: Lightweight ID (no data)
Component: Pure data (no behavior)
System: Logic that processes components
World: Container for entities
Archetype: Unique combination of components
Chunk: Memory block for same-archetype entities
```

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices

### Do's

- **Use ISystem over SystemBase** - Better performance
- **Burst compile everything** - Massive speedup
- **Batch structural changes** - Use ECB
- **Profile with Profiler** - Identify bottlenecks
- **Use Aspects** - Clean component grouping

### Don'ts

- **Don't use managed types** - Breaks Burst
- **Don't structural change in jobs** - Use ECB
- **Don't over-architect** - Start simple
- **Don't ignore chunk utilization** - Group similar entities
- **Don't forget disposal** - Native collections leak
