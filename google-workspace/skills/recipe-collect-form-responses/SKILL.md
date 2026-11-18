---
name: google-workspace-recipe-collect-form-responses
description: Retrieve and review responses from a Google Form.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: productivity
    requires:
      bins:
      - gws
      skills:
      - gws-forms
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Check Form Responses

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-forms`

Retrieve and review responses from a Google Form.

## Steps

1. List forms: `gws forms forms list` (if you don't have the form ID)
2. Get form details: `gws forms forms get --params '{"formId": "FORM_ID"}'`
3. Get responses: `gws forms forms responses list --params '{"formId": "FORM_ID"}' --format table`

