---
name: google-workspace-gws-sheets-read
description: 'Google Sheets: Read values from a spreadsheet.'
metadata:
  version: 0.22.5
  openclaw:
    category: productivity
    requires:
      bins:
      - gws
    cliHelp: gws sheets +read --help
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# sheets +read

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Read values from a spreadsheet

## Usage

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | ✓ | — | Spreadsheet ID |
| `--range` | ✓ | — | Range to read (e.g. 'Sheet1!A1:B2') |

## Examples

```bash
gws sheets +read --spreadsheet ID --range "Sheet1!A1:D10"
gws sheets +read --spreadsheet ID --range Sheet1
```

## Tips

- Read-only — never modifies the spreadsheet.
- For advanced options, use the raw values.get API.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-sheets](../gws-sheets/SKILL.md) — All read and write spreadsheets commands
