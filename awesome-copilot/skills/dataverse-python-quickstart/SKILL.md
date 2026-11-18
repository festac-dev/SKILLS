---
name: copilot-dataverse-python-quickstart
description: 'Generate Python SDK setup + CRUD + bulk + paging snippets using official patterns.'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

You are assisting with Microsoft Dataverse SDK for Python (preview).
Generate concise Python snippets that:
- Install the SDK (pip install PowerPlatform-Dataverse-Client)
- Create a DataverseClient with InteractiveBrowserCredential
- Show CRUD single-record operations
- Show bulk create and bulk update (broadcast + 1:1)
- Show retrieve-multiple with paging (top, page_size)
- Optionally demonstrate file upload to a File column
Keep code aligned with official examples and avoid unannounced preview features.
