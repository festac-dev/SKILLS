---
name: google-workspace-recipe-create-gmail-filter
description: Create a Gmail filter to automatically label, star, or categorize incoming
  messages.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: productivity
    requires:
      bins:
      - gws
      skills:
      - gws-gmail
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Create a Gmail Filter

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-gmail`

Create a Gmail filter to automatically label, star, or categorize incoming messages.

## Steps

1. List existing labels: `gws gmail users labels list --params '{"userId": "me"}' --format table`
2. Create a new label: `gws gmail users labels create --params '{"userId": "me"}' --json '{"name": "Receipts"}'`
3. Create a filter: `gws gmail users settings filters create --params '{"userId": "me"}' --json '{"criteria": {"from": "receipts@example.com"}, "action": {"addLabelIds": ["LABEL_ID"], "removeLabelIds": ["INBOX"]}}'`
4. Verify filter: `gws gmail users settings filters list --params '{"userId": "me"}' --format table`

