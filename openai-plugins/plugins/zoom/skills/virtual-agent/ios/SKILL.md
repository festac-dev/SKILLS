---
name: openai-zoom-virtual-agent-ios
description: "Zoom Virtual Agent iOS integration via WKWebView. Use for Swift/Objective-C script injection, message handlers, support_handoff relay, and URL routing policies."
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom Virtual Agent - iOS

Official docs:
- https://developers.zoom.us/docs/virtual-agent/ios/

## Quick Links

1. [concepts/webview-lifecycle.md](concepts/webview-lifecycle.md)
2. [examples/js-bridge-patterns.md](examples/js-bridge-patterns.md)
3. [references/ios-reference-map.md](references/ios-reference-map.md)
4. [troubleshooting/common-issues.md](troubleshooting/common-issues.md)

## Integration Model

- Load campaign URL in `WKWebView`.
- Inject `window.zoomCampaignSdkConfig` using `WKUserScript`.
- Register message handlers for exit/common/handoff flows.
- Handle URL behavior in navigation delegates (`in-app`, `SFSafariViewController`, or system browser).

## Hard Guardrails

- Register scripts and handlers before web interaction.
- Handle iOS 14.5+ download behavior where needed.
- Keep deprecated `openURL` command support as fallback only.

## Chaining

- Product-level patterns: [../SKILL.md](../SKILL.md)
- Contact Center mobile scope: [../../contact-center/ios/SKILL.md](../../contact-center/ios/SKILL.md)
