---
name: google-workspace-recipe-plan-weekly-schedule
description: Review your Google Calendar week, identify gaps, and add events to fill
  them.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: scheduling
    requires:
      bins:
      - gws
      skills:
      - gws-calendar
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Plan Your Weekly Google Calendar Schedule

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Review your Google Calendar week, identify gaps, and add events to fill them.

## Steps

1. Check this week's agenda: `gws calendar +agenda`
2. Check free/busy for the week: `gws calendar freebusy query --json '{"timeMin": "2025-01-20T00:00:00Z", "timeMax": "2025-01-25T00:00:00Z", "items": [{"id": "primary"}]}'`
3. Add a new event: `gws calendar +insert --summary 'Deep Work Block' --start '2026-01-21T14:00:00' --end '2026-01-21T16:00:00'`
4. Review updated schedule: `gws calendar +agenda`

