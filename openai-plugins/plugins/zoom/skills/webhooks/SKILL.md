---
name: openai-setup-zoom-webhooks
description: Use when building Zoom webhooks.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Setup Zoom Webhooks

Use this skill when the integration receives Zoom events over HTTP. If the user needs persistent low-latency event streams, compare against `setup-zoom-websockets`.

## Workflow

1. Identify the event types and resource scope before creating subscriptions.
2. Implement endpoint verification and signature verification before processing business logic.
3. Store raw event IDs, timestamps, and delivery metadata for replay protection and debugging.
4. Make handlers idempotent because Zoom can retry delivery.
5. Separate webhook ingestion from downstream API calls with a queue when reliability matters.
6. Debug by checking endpoint reachability, TLS, validation token handling, signature base string, app event subscription, and account-level settings.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Signature verification: [references/signature-verification.md](references/signature-verification.md)
- Subscriptions: [references/subscriptions.md](references/subscriptions.md)
- Events: [references/events.md](references/events.md)
- Common issues: [troubleshooting/common-issues.md](troubleshooting/common-issues.md)
