---
name: google-workspace-recipe-compare-sheet-tabs
description: Read data from two tabs in a Google Sheet to compare and identify differences.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: productivity
    requires:
      bins:
      - gws
      skills:
      - gws-sheets
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Compare Two Google Sheets Tabs

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-sheets`

Read data from two tabs in a Google Sheet to compare and identify differences.

## Steps

1. Read the first tab: `gws sheets +read --spreadsheet SHEET_ID --range "January!A1:D"`
2. Read the second tab: `gws sheets +read --spreadsheet SHEET_ID --range "February!A1:D"`
3. Compare the data and identify changes

