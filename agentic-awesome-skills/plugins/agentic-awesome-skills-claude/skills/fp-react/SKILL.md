---
name: agentic-awesome-fp-react-d54a162b
description: Practical patterns for using fp-ts with React - hooks, state, forms,
  data fetching. Includes version-specific React examples; verify framework/client
  boundaries.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-01-30'
    version: 2.0.0
    author: fp-ts-skills
    tags:
    - fp-ts
    - react
    - typescript
    - hooks
    - state-management
    - forms
    - data-fetching
    - remote-data
    - react-19
    - next-js
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Functional Programming in React

Practical patterns for React apps. Untested integration sketches; decode external data and verify lifecycle behavior.

---

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use What

| Situation | Use |
|-----------|-----|
| Value might not exist | `Option<T>` |
| Operation might fail (sync) | `Either<E, A>` |
| Async operation might fail | `TaskEither<E, A>` |
| Need loading/error/success UI | `RemoteData<E, A>` |
| Form with multiple validations | `Either` with validation applicative |
| Dependency injection | Context + `ReaderTaskEither` |
| Prevent re-renders with fp-ts | `useMemo` or `fp-ts-react-stable-hooks` |

---

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
