---
name: google-workspace-gws-events-subscribe
description: 'Google Workspace Events: Subscribe to Workspace events and stream them
  as NDJSON.'
metadata:
  version: 0.22.5
  openclaw:
    category: productivity
    requires:
      bins:
      - gws
    cliHelp: gws events +subscribe --help
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# events +subscribe

> **PREREQUISITE:** Read `../gws-shared/SKILL.md` for auth, global flags, and security rules. If missing, run `gws generate-skills` to create it.

Subscribe to Workspace events and stream them as NDJSON

## Usage

```bash
gws events +subscribe
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--target` | — | — | Workspace resource URI (e.g., //chat.googleapis.com/spaces/SPACE_ID) |
| `--event-types` | — | — | Comma-separated CloudEvents types to subscribe to |
| `--project` | — | — | GCP project ID for Pub/Sub resources |
| `--subscription` | — | — | Existing Pub/Sub subscription name (skip setup) |
| `--max-messages` | — | 10 | Max messages per pull batch (default: 10) |
| `--poll-interval` | — | 5 | Seconds between pulls (default: 5) |
| `--once` | — | — | Pull once and exit |
| `--cleanup` | — | — | Delete created Pub/Sub resources on exit |
| `--no-ack` | — | — | Don't auto-acknowledge messages |
| `--output-dir` | — | — | Write each event to a separate JSON file in this directory |

## Examples

```bash
gws events +subscribe --target '//chat.googleapis.com/spaces/SPACE' --event-types 'google.workspace.chat.message.v1.created' --project my-project
gws events +subscribe --subscription projects/p/subscriptions/my-sub --once
gws events +subscribe ... --cleanup --output-dir ./events
```

## Tips

- Without --cleanup, Pub/Sub resources persist for reconnection.
- Press Ctrl-C to stop gracefully.

> [!CAUTION]
> This is a **write** command — confirm with the user before executing.

## See Also

- [gws-shared](../gws-shared/SKILL.md) — Global flags and auth
- [gws-events](../gws-events/SKILL.md) — All subscribe to google workspace events commands
