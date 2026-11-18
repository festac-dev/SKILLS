---
name: google-workspace-persona-content-creator
description: Create, organize, and distribute content across Workspace.
metadata:
  version: 0.22.5
  openclaw:
    category: persona
    requires:
      bins:
      - gws
      skills:
      - gws-docs
      - gws-drive
      - gws-gmail
      - gws-chat
      - gws-slides
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Content Creator

> **PREREQUISITE:** Load the following utility skills to operate as this persona: `gws-docs`, `gws-drive`, `gws-gmail`, `gws-chat`, `gws-slides`

Create, organize, and distribute content across Workspace.

## Relevant Workflows
- `gws workflow +file-announce`

## Instructions
- Draft content in Google Docs with `gws docs +write`.
- Organize content assets in Drive folders — use `gws drive files list` to browse.
- Share finished content by announcing in Chat with `gws workflow +file-announce`.
- Send content review requests via email with `gws gmail +send`.
- Upload media assets to Drive with `gws drive +upload`.

## Tips
- Use `gws docs +write` for quick content updates — it handles the Docs API formatting.
- Keep a 'Content Calendar' in a shared Sheet for tracking publication schedules.
- Use `--format yaml` for human-readable output when debugging API responses.

