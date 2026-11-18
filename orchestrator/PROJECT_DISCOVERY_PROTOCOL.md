# Project Discovery Protocol

## Inspection order

1. Repository status and recent changes.
2. README, docs, contribution instructions and project-specific agent instructions.
3. Package manifests, lockfiles, runtime versions and scripts.
4. Application entry points, route definitions and major modules.
5. Existing tests, fixtures and CI configuration.
6. Environment examples, infrastructure and deployment configuration.
7. Existing design assets, tokens, copy, screenshots and product flows.
8. Data model, API contracts, permissions and integrations.

## Record

| Area | Findings | Evidence | Confidence | Action |
|---|---|---|---|---|
| Purpose | | | | |
| Users | | | | |
| Stack | | | | |
| Architecture | | | | |
| Design language | | | | |
| Content voice | | | | |
| Core journeys | | | | |
| Security | | | | |
| Accessibility | | | | |
| Performance | | | | |
| Deployment | | | | |

## Rules

- Never infer the entire product from its homepage or README alone.
- Do not assume a missing artifact means a feature is required.
- Treat existing tests and implementation as evidence, but verify their relevance.
- Identify conflicting instructions and follow the most specific, current, authorized requirement.
- Mark unknowns explicitly.
- Do not change the project's identity as a side effect of a technical task.

## Current-task application

For multi-project work, inspect each project’s identity, runtime, routes and integration limits independently. Record current preview artifact/process state and latest user corrections; a shared parent directory does not imply a shared design system.
