---
name: agentic-awesome-unity-ecs-patterns
description: Production patterns for Unity's Data-Oriented Technology Stack (DOTS)
  including Entity Component System, Job System, and Burst Compiler.
metadata:
  upstream_headers:
    risk: safe
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Unity ECS Patterns

Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler.

## Use this skill when

- Building high-performance Unity games
- Managing thousands of entities efficiently
- Implementing data-oriented game systems
- Optimizing CPU-bound game logic
- Converting OOP game code to ECS
- Using Jobs and Burst for parallelization

## Do not use this skill when

- The task is unrelated to unity ecs patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Example

```text
Implement Speed plus a MovementSystem using the pinned Entities package. Profile a fixed entity cohort before/after; verify movement once per frame and job dependencies before enabling parallel execution.
```

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
