---
name: openai-build-zoom-virtual-agent
description: Use when using Virtual Agent.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Build Zoom Virtual Agent

Use this skill when the workflow embeds or wraps Zoom Virtual Agent, including web campaigns and mobile WebView integrations.

## Workflow

1. Identify the client: web, Android WebView, iOS WKWebView, campaign entry, support handoff, or knowledge-base sync pipeline.
2. Route to the platform skill before coding because event handling and native bridge behavior differ by client.
3. Confirm campaign, entry ID, allowed origins, lifecycle events, and support handoff behavior.
4. Keep user context updates, native URL handling, and handoff payloads explicit.
5. Debug by checking SDK readiness, campaign configuration, bridge injection, CSP, WebView lifecycle, and version drift.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Web: [web/SKILL.md](web/SKILL.md)
- Android: [android/SKILL.md](android/SKILL.md)
- iOS: [ios/SKILL.md](ios/SKILL.md)
- Architecture and lifecycle: [concepts/architecture-and-lifecycle.md](concepts/architecture-and-lifecycle.md)
- Common drift and breaks: [troubleshooting/common-drift-and-breaks.md](troubleshooting/common-drift-and-breaks.md)
