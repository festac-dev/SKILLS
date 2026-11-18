---
name: google-workspace-recipe-share-doc-and-notify
description: Share a Google Docs document with edit access and email collaborators
  the link.
metadata:
  version: 0.22.5
  openclaw:
    category: recipe
    domain: productivity
    requires:
      bins:
      - gws
      skills:
      - gws-drive
      - gws-docs
      - gws-gmail
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Share a Google Doc and Notify Collaborators

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`, `gws-docs`, `gws-gmail`

Share a Google Docs document with edit access and email collaborators the link.

## Steps

1. Find the doc: `gws drive files list --params '{"q": "name contains '\''Project Brief'\'' and mimeType = '\''application/vnd.google-apps.document'\''"}'`
2. Share with editor access: `gws drive permissions create --params '{"fileId": "DOC_ID"}' --json '{"role": "writer", "type": "user", "emailAddress": "reviewer@company.com"}'`
3. Email the link: `gws gmail +send --to reviewer@company.com --subject 'Please review: Project Brief' --body 'I have shared the project brief with you: https://docs.google.com/document/d/DOC_ID'`

