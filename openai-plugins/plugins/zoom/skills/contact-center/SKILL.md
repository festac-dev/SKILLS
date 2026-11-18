---
name: openai-build-zoom-contact-center-app
description: Use when using Contact Center.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Build Zoom Contact Center App

Use this skill when the integration targets Zoom Contact Center rather than general meetings, chat, or phone. Route to the platform-specific skill once the client surface is clear.

## Workflow

1. Identify the channel and client: web, Android, iOS, campaign embed, video engagement, chat engagement, Virtual Agent handoff, or scheduled callback.
2. Confirm the lifecycle: initialization, engagement start, context retrieval, state changes, transfer or handoff, and cleanup.
3. Choose the platform reference before coding; Contact Center SDKs differ by event names, lifecycle hooks, and wrapper requirements.
4. Treat engagement context as shared state and validate how it flows into CRM, ticketing, analytics, or AI workflows.
5. Debug version drift by checking SDK version, documented event names, app settings, campaign configuration, and browser or mobile lifecycle behavior.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Web SDK: [web/SKILL.md](web/SKILL.md)
- Android SDK: [android/SKILL.md](android/SKILL.md)
- iOS SDK: [ios/SKILL.md](ios/SKILL.md)
- High-level scenarios: [scenarios/high-level-scenarios.md](scenarios/high-level-scenarios.md)
- Common drift and breaks: [troubleshooting/common-drift-and-breaks.md](troubleshooting/common-drift-and-breaks.md)
