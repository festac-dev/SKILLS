---
name: openai-build-zoom-bot
description: Use when building bots.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /build-zoom-bot

Use this skill for automation that joins meetings, captures media, or reacts to live session data.

## Covers

- Bot architecture
- Meeting join strategy
- Real-time media and transcript handling
- Backend orchestration
- Storage, post-processing, and event flow design

## Workflow

1. Clarify whether the bot needs to join, observe, transcribe, summarize, or act.
2. Route to Meeting SDK and RTMS as the core implementation path.
3. Add REST API for meeting/resource management and Webhooks for asynchronous events when needed.
4. Call out environment and lifecycle constraints early.

## Primary References

- [meeting-sdk](../meeting-sdk/SKILL.md)
- [rtms](../rtms/SKILL.md)
- [scribe](../scribe/SKILL.md)
- [rest-api](../rest-api/SKILL.md)
- [webhooks](../webhooks/SKILL.md)

## Common Mistakes

- Treating batch transcription and live media as the same workflow
- Designing the bot before defining join authority and auth model
- Forgetting post-meeting storage and retry behavior
