---
name: google-workspace-gws-events-renew
description: 'Google Workspace Events: Renew/reactivate Workspace Events subscriptions.'
metadata:
  version: 0.22.5
  openclaw:
    category: productivity
    requires:
      bins:
      - gws
    cliHelp: gws events +renew --help
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# events +renew

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Renew/reactivate Workspace Events subscriptions

## Usage

```bash
gws events +renew
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--name` | — | — | Subscription name to reactivate (e.g., subscriptions/SUB_ID) |
| `--all` | — | — | Renew all subscriptions expiring within --within window |
| `--within` | — | 1h | Time window for --all (e.g., 1h, 30m, 2d) |

## Examples

```bash
gws events +renew --name subscriptions/SUB_ID
gws events +renew --all --within 2d
```

## Tips

- Subscriptions expire if not renewed periodically.
- Use --all with a cron job to keep subscriptions alive.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-events](../gws-events/SKILL.md) — All subscribe to google workspace events commands
