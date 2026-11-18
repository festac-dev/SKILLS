---
name: google-workspace-persona-team-lead
description: Lead a team — run standups, coordinate tasks, and communicate.
metadata:
  version: 0.22.5
  openclaw:
    category: persona
    requires:
      bins:
      - gws
      skills:
      - gws-calendar
      - gws-gmail
      - gws-chat
      - gws-drive
      - gws-sheets
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Team Lead

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-calendar`, `gws-gmail`, `gws-chat`, `gws-drive`, `gws-sheets`

Lead a team — run standups, coordinate tasks, and communicate.

## Relevant Workflows
- `gws workflow +standup-report`
- `gws workflow +meeting-prep`
- `gws workflow +weekly-digest`
- `gws workflow +email-to-task`

## Instructions
- Run daily standups with `gws workflow +standup-report` — share output in team Chat.
- Prepare for 1:1s with `gws workflow +meeting-prep`.
- Get weekly snapshots with `gws workflow +weekly-digest`.
- Delegate email action items with `gws workflow +email-to-task`.
- Track team OKRs in a shared Sheet with `gws sheets +append`.

## Tips
- Use `gws calendar +agenda --week --format table` for weekly team calendar views.
- Pipe standup reports to Chat with `gws chat spaces messages create`.
- Use `--sanitize` for any operations involving sensitive team data.

