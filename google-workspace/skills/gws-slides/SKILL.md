---
name: google-workspace-gws-slides
description: 'Google Slides: Read and write presentations.'
metadata:
  version: 0.22.5
  openclaw:
    category: productivity
    requires:
      bins:
      - gws
    cliHelp: gws slides --help
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# slides (v1)

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

```bash
gws slides <resource> <method> [flags]
```

## API Resources

### presentations

  - `batchUpdate` — Applies one or more updates to the presentation. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests.
  - `create` — Creates a blank presentation using the title given in the request. If a `presentationId` is provided, it is used as the ID of the new presentation. Otherwise, a new ID is generated. Other fields in the request, including any provided content, are ignored. Returns the created presentation.
  - `get` — Gets the latest version of the specified presentation.
  - `pages` — Operations on the 'pages' resource

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws slides --help

# Inspect a method's required params, types, and defaults
gws schema slides.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

