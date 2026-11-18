---
name: wshobson-nx-workspace-patterns
description: Configure and optimize Nx monorepo workspaces. Use when setting up Nx,
  configuring project boundaries, optimizing build caching, or implementing affected
  commands.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Nx Workspace Patterns

Production patterns for Nx monorepo management.

## When to Use This Skill

- Setting up new Nx workspaces
- Configuring project boundaries
- Optimizing CI with affected commands
- Implementing remote caching
- Managing dependencies between projects
- Migrating to Nx

## Core Concepts

### 1. Nx Architecture

```
workspace/
├── apps/              # Deployable applications
│   ├── web/
│   └── api/
├── libs/              # Shared libraries
│   ├── shared/
│   │   ├── ui/
│   │   └── utils/
│   └── feature/
│       ├── auth/
│       └── dashboard/
├── tools/             # Custom executors/generators
├── nx.json            # Nx configuration
└── workspace.json     # Project configuration
```

### 2. Library Types

| Type            | Purpose                          | Example             |
| --------------- | -------------------------------- | ------------------- |
| **feature**     | Smart components, business logic | `feature-auth`      |
| **ui**          | Presentational components        | `ui-buttons`        |
| **data-access** | API calls, state management      | `data-access-users` |
| **util**        | Pure functions, helpers          | `util-formatting`   |
| **shell**       | App bootstrapping                | `shell-web`         |

## Templates and detailed worked examples

Full template library and detailed worked examples live in `references/details.md`. Read that file when you need the concrete templates.

## Best Practices

### Do's

- **Use tags consistently** - Enforce with module boundaries
- **Enable caching early** - Significant CI savings
- **Keep libs focused** - Single responsibility
- **Use generators** - Ensure consistency
- **Document boundaries** - Help new developers

### Don'ts

- **Don't create circular deps** - Graph should be acyclic
- **Don't skip affected** - Test only what changed
- **Don't ignore boundaries** - Tech debt accumulates
- **Don't over-granularize** - Balance lib count
