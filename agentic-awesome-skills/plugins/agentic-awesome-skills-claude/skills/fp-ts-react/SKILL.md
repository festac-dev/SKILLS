---
name: agentic-awesome-fp-ts-react-47c509be
description: Practical patterns for using fp-ts with React - hooks, state, forms,
  data fetching. Use when building React apps with functional programming patterns.
  Includes version-specific React patterns requiring project verification.
metadata:
  upstream_headers:
    risk: safe
    source: https://github.com/whatiskadudoing/fp-ts-skills
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Functional Programming in React

Practical patterns for React apps. Untested integration sketches; validate external JSON and request lifecycle behavior.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use This Skill

- When building React apps with fp-ts for type-safe state management
- When handling loading/error/success states in data fetching
- When implementing form validation with error accumulation
- When using React 18/19 or Next.js 14/15 with functional patterns

---

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
