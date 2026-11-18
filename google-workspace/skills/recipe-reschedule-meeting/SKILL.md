---
name: google-workspace-recipe-reschedule-meeting
description: Move a Google Calendar event to a new time and automatically notify all
  attendees.
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

# Reschedule a Google Calendar Meeting

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-calendar`

Move a Google Calendar event to a new time and automatically notify all attendees.

## Steps

1. Find the event: `gws calendar +agenda`
2. Get event details: `gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'`
3. Update the time: `gws calendar events patch --params '{"calendarId": "primary", "eventId": "EVENT_ID", "sendUpdates": "all"}' --json '{"start": {"dateTime": "2025-01-22T14:00:00", "timeZone": "America/New_York"}, "end": {"dateTime": "2025-01-22T15:00:00", "timeZone": "America/New_York"}}'`

