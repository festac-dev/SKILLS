---
name: google-workspace-recipe-post-mortem-setup
description: Create a Google Docs post-mortem, schedule a Google Calendar review,
  and notify via Chat.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: engineering
    requires:
      bins:
      - gws
      skills:
      - gws-docs
      - gws-calendar
      - gws-chat
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Set Up Post-Mortem

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-docs`, `gws-calendar`, `gws-chat`

Create a Google Docs post-mortem, schedule a Google Calendar review, and notify via Chat.

## Steps

1. Create post-mortem doc: `gws docs +write --title 'Post-Mortem: [Incident]' --body '## Summary\n\n## Timeline\n\n## Root Cause\n\n## Action Items'`
2. Schedule review meeting: `gws calendar +insert --summary 'Post-Mortem Review: [Incident]' --attendee team@company.com --start '2026-03-16T14:00:00' --end '2026-03-16T15:00:00'`
3. Notify in Chat: `gws chat +send --space spaces/ENG_SPACE --text '🔍 Post-mortem scheduled for [Incident].'`

