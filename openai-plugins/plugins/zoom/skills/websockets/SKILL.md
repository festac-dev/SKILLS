---
name: openai-setup-zoom-websockets
description: Use when building Zoom WebSockets.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Setup Zoom WebSockets

Use this skill when the integration needs persistent Zoom event delivery instead of HTTP webhook callbacks. If normal webhook retries and delivery are enough, prefer `setup-zoom-webhooks`.

## Workflow

1. Confirm WebSockets are justified by latency, firewall, connection model, or deployment constraints.
2. Configure the app and event subscriptions for the required event stream.
3. Implement connection setup, authentication, heartbeat, reconnect, backoff, and shutdown handling.
4. Normalize events into the same internal contract used by webhook handlers when both are supported.
5. Add observability for connection state, reconnect count, event lag, and dropped messages.
6. Debug by isolating token/auth problems, app subscription settings, network proxies, TLS interception, and reconnect loops.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Connection: [references/connection.md](references/connection.md)
- Events: [references/events.md](references/events.md)
- Common issues: [troubleshooting/common-issues.md](troubleshooting/common-issues.md)
