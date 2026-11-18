---
name: google-workspace-recipe-review-overdue-tasks
description: Find Google Tasks that are past due and need attention.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: productivity
    requires:
      bins:
      - gws
      skills:
      - gws-tasks
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Review Overdue Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Find Google Tasks that are past due and need attention.

## Steps

1. List task lists: `gws tasks tasklists list --format table`
2. List tasks with status: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID", "showCompleted": false}' --format table`
3. Review due dates and prioritize overdue items

