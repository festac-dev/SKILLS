---
name: openai-zoom-rtms
description: Use when using RTMS.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom Realtime Media Streams

Use this skill when the integration needs real-time meeting or contact-center media as a backend stream. If the workflow needs a visible participant bot, compare against `build-zoom-bot` and `zoom-meeting-sdk-linux` before choosing RTMS.

## Workflow

1. Confirm the source surface: Meetings RTMS, Contact Center voice media, or another documented RTMS stream.
2. Decide whether RTMS is sufficient or whether a Meeting SDK bot is required for participant identity, meeting controls, or UI-visible behavior.
3. Implement the WebSocket lifecycle first: event subscription, connection validation, media start, heartbeat, reconnect, and shutdown.
4. Process media types intentionally: audio, video, screen share, chat, live transcript, and metadata have different payload and timing constraints.
5. Design downstream pipelines for buffering, transcription, AI analysis, recording, or tool invocation.
6. Debug by isolating app setup, webhook/event delivery, stream authorization, network connectivity, and media payload decoding.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Connection architecture: [concepts/connection-architecture.md](concepts/connection-architecture.md)
- Lifecycle flow: [concepts/lifecycle-flow.md](concepts/lifecycle-flow.md)
- Media types: [references/media-types.md](references/media-types.md)
- Data types: [references/data-types.md](references/data-types.md)
- RTMS bot example: [examples/rtms-bot.md](examples/rtms-bot.md)
- Common issues: [troubleshooting/common-issues.md](troubleshooting/common-issues.md)
