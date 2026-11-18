---
name: openai-zoom-general
description: Use when comparing products.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom General

Use this skill for cross-product platform context after the user’s goal is understood. For first-step routing, prefer `start`, `plan-zoom-product`, or `plan-zoom-integration`.

## Workflow

1. Classify the job by outcome: embed meetings, custom video, automate resources, consume events, process media, use meeting intelligence, or publish a Marketplace app.
2. Choose the Zoom surface that owns the behavior: REST API, webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Phone, Contact Center, Virtual Agent, Scribe, Rivet, or Cobrowse.
3. Confirm auth and scope model before implementation; Zoom surfaces differ on user-level OAuth, account-level OAuth, and SDK signatures.
4. Route to the narrow skill once the surface is chosen rather than keeping broad guidance in context.
5. Use the preserved guide only when a task crosses product boundaries or needs detailed comparison tables.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- App types: [references/app-types.md](references/app-types.md)
- Authentication: [references/authentication.md](references/authentication.md)
- Scopes: [references/scopes.md](references/scopes.md)
- Marketplace: [references/marketplace.md](references/marketplace.md)
- Query routing playbook: [references/query-routing-playbook.md](references/query-routing-playbook.md)
