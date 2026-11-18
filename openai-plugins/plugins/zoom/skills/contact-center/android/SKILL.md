---
name: openai-zoom-contact-center-android
description: "Zoom Contact Center SDK for Android. Use for native Android chat/video/ZVA/scheduled callback integrations, campaign mode, service lifecycle, and rejoin handling."
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom Contact Center SDK - Android

Official docs:
- https://developers.zoom.us/docs/contact-center/android/
- https://marketplacefront.zoom.us/sdk/contact/android/index.html

## Quick Links

1. [concepts/sdk-lifecycle.md](concepts/sdk-lifecycle.md)
2. [examples/service-patterns.md](examples/service-patterns.md)
3. [references/android-reference-map.md](references/android-reference-map.md)
4. [troubleshooting/common-issues.md](troubleshooting/common-issues.md)

## SDK Surface Summary

- SDK manager: `ZoomCCInterface`
- Channel services:
- `getZoomCCChatService()`
- `getZoomCCVideoService()`
- `getZoomCCZVAService()`
- `getZoomCCScheduledCallbackService()`
- Campaign support via web campaign service and campaign metadata.

## Hard Guardrails

- Initialize SDK in `Application.onCreate`.
- Use `ZoomCCItem` to define channel + identifiers.
- Use `entryId` for chat/video/ZVA.
- Use `apiKey` for scheduled callback and campaign mode.
- Release services on teardown.

## Common Chains

- Contact Center app and engagement context: [../../zoom-apps-sdk/SKILL.md](../../zoom-apps-sdk/SKILL.md)
- Contact Center API automation: [../../rest-api/SKILL.md](../../rest-api/SKILL.md)

## Operations

- [RUNBOOK.md](RUNBOOK.md) - 5-minute preflight and debugging checklist.
