---
name: google-workspace-recipe-create-task-list
description: Set up a new Google Tasks list with initial tasks.
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

# Create a Task List and Add Tasks

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-tasks`

Set up a new Google Tasks list with initial tasks.

## Steps

1. Create task list: `gws tasks tasklists insert --json '{"title": "Q2 Goals"}'`
2. Add a task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Review Q1 metrics", "notes": "Pull data from analytics dashboard", "due": "2024-04-01T00:00:00Z"}'`
3. Add another task: `gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "Draft Q2 OKRs"}'`
4. List tasks: `gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}' --format table`

