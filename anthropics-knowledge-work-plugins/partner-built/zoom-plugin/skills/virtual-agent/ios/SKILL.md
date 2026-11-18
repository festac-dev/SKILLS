---
name: skills-virtual-agent-ios
description: Zoom Virtual Agent iOS integration via WKWebView. Use for Swift/Objective-C
  script injection, message handlers, support_handoff relay, and URL routing policies.
metadata:
  upstream_headers:
    user-invocable: false
    triggers:
    - virtual agent ios
    - wkwebview zva
    - support_handoff ios
    - zoomCampaignSdk:ready ios
    - wkusercontentcontroller
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Preserve the project stack, existing authorization, source prerequisites and required notices. Source workflows do not grant permission for external actions or delegation.

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
