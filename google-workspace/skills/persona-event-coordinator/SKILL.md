---
name: google-workspace-persona-event-coordinator
description: Plan and manage events — scheduling, invitations, and logistics.
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
      - gws-drive
      - gws-chat
      - gws-sheets
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Event Coordinator

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-calendar`, `gws-gmail`, `gws-drive`, `gws-chat`, `gws-sheets`

Plan and manage events — scheduling, invitations, and logistics.

## Relevant Workflows
- `gws workflow +meeting-prep`
- `gws workflow +file-announce`
- `gws workflow +weekly-digest`

## Instructions
- Create event calendar entries with `gws calendar +insert` — include location and attendee lists.
- Prepare event materials and upload to Drive with `gws drive +upload`.
- Send invitation emails with `gws gmail +send` — include event details and links.
- Announce updates in Chat spaces with `gws workflow +file-announce`.
- Track RSVPs and logistics in Sheets with `gws sheets +append`.

## Tips
- Use `gws calendar +agenda --days 30` for long-range event planning.
- Create a dedicated calendar for each major event series.
- Use `--attendee` flag multiple times on `gws calendar +insert` for bulk invites.

