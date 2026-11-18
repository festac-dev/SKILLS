---
name: google-workspace-recipe-organize-drive-folder
description: Create a Google Drive folder structure and move files into the right
  locations.
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
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Organize Files into Google Drive Folders

> **PREREQUISITE:** Load the following skills to execute this recipe: `gws-drive`

Create a Google Drive folder structure and move files into the right locations.

## Steps

1. Create a project folder: `gws drive files create --json '{"name": "Q2 Project", "mimeType": "application/vnd.google-apps.folder"}'`
2. Create sub-folders: `gws drive files create --json '{"name": "Documents", "mimeType": "application/vnd.google-apps.folder", "parents": ["PARENT_FOLDER_ID"]}'`
3. Move existing files into folder: `gws drive files update --params '{"fileId": "FILE_ID", "addParents": "FOLDER_ID", "removeParents": "OLD_PARENT_ID"}'`
4. Verify structure: `gws drive files list --params '{"q": "FOLDER_ID in parents"}' --format table`

