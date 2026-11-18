---
name: wshobson-track-management
description: Use this skill when creating, managing, or working with Conductor tracks
  - the logical work units for features, bugs, and refactors. Applies to spec.md,
  plan.md, and track lifecycle operations.
metadata:
  upstream_headers:
    version: 1.0.0
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Track Management

Guide for creating, managing, and completing Conductor tracks - the logical work units that organize features, bugs, and refactors through specification, planning, and implementation phases.

## When to Use This Skill

- Creating new feature, bug, or refactor tracks
- Writing or reviewing spec.md files
- Creating or updating plan.md files
- Managing track lifecycle from creation to completion
- Understanding track status markers and conventions
- Working with the tracks.md registry
- Interpreting or updating track metadata

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices

1. **One track, one concern**: Keep tracks focused on a single logical change
2. **Small phases**: Break work into phases of 3-5 tasks maximum
3. **Verification after phases**: Always include verification tasks
4. **Update markers immediately**: Mark task status as you work
5. **Record SHAs**: Always note commit SHAs for completed tasks
6. **Review specs before planning**: Ensure spec is complete before creating plan
7. **Link dependencies**: Explicitly note track dependencies
8. **Archive, don't delete**: Preserve completed tracks for reference
9. **Size appropriately**: Keep tracks between 1-5 days of work
10. **Clear acceptance criteria**: Every requirement must be testable
