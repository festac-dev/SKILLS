---
name: openai-build-zoom-phone-integration
description: Use when building Phone.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Build Zoom Phone Integration

Use this skill when the target workflow is Zoom Phone, CTI, CRM calling, call events, or Smart Embed behavior.

## Workflow

1. Classify the integration: REST API automation, webhook event processing, Smart Embed, URI launch, CRM dialer, or call-handling workflow.
2. Confirm the actor, account settings, phone entitlements, and OAuth scopes before implementation.
3. Keep call control, call records, number management, and webhook processing as separate modules.
4. For Smart Embed, validate postMessage event contracts, embedding constraints, and CRM state mapping.
5. Debug by checking scopes, phone license, role permissions, number ownership, webhook subscriptions, and event payload shape.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Architecture and lifecycle: [concepts/architecture-and-lifecycle.md](concepts/architecture-and-lifecycle.md)
- Phone API service pattern: [examples/phone-api-service-pattern.md](examples/phone-api-service-pattern.md)
- Smart Embed bridge: [examples/smart-embed-postmessage-bridge.md](examples/smart-embed-postmessage-bridge.md)
- Event contract: [references/smart-embed-event-contract.md](references/smart-embed-event-contract.md)
- Common issues: [troubleshooting/common-issues.md](troubleshooting/common-issues.md)
