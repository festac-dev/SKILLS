---
name: openai-zoom-cobrowse-sdk
description: Use when using Cobrowse.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom Cobrowse SDK

Use this skill after the support workflow is clearly a browser co-browsing experience. If the user is still choosing between Zoom Contact Center, Virtual Agent, Video SDK, or Cobrowse, route through `start` or `plan-zoom-product` first.

## Workflow

1. Confirm the role model: customer page, agent console, session initiation, and how the PIN or link is handed off.
2. Check auth and session setup before UI work: tokens, allowed origins, environment variables, and SDK loading.
3. Design privacy controls early: masking rules, blocked elements, remote-assist permission boundaries, and audit requirements.
4. Implement the minimal lifecycle first: initialize, start or join, subscribe to events, reconnect, and end.
5. Add advanced capabilities only after the base session is stable: annotations, multi-tab persistence, custom PINs, and remote assist.
6. When debugging, isolate browser support, CORS/CSP, token generation, third-party cookie behavior, and SDK event errors.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- API reference: [references/api-reference.md](references/api-reference.md)
- Session lifecycle: [concepts/session-lifecycle.md](concepts/session-lifecycle.md)
- Privacy masking: [examples/privacy-masking.md](examples/privacy-masking.md)
- Remote assist: [examples/remote-assist.md](examples/remote-assist.md)
- Common issues: [troubleshooting/common-issues.md](troubleshooting/common-issues.md)
