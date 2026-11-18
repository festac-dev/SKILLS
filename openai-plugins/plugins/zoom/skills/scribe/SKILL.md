---
name: openai-scribe
description: Use when using Scribe.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Zoom AI Services Scribe

Use this skill for Zoom Scribe transcription pipelines over uploaded or stored media. If the user needs live meeting media, compare against RTMS or Meeting SDK bot workflows first.

## Workflow

1. Confirm the media source, size, language, expected latency, and whether fast mode or batch mode fits.
2. Set up Build-platform credentials and JWT handling separately from application transcription logic.
3. Design ingestion, chunking, retries, webhook callbacks, and persistence before connecting downstream AI workflows.
4. Implement a minimal transcription request and response parser, then add batching and operational monitoring.
5. Debug by checking credential audience, processing mode, media format, file size, backend timeout, and webhook delivery.

## References

- Full preserved guide: [references/full-guide.md](references/full-guide.md)
- Auth and processing modes: [concepts/auth-and-processing-modes.md](concepts/auth-and-processing-modes.md)
- High-level scenarios: [scenarios/high-level-scenarios.md](scenarios/high-level-scenarios.md)
- Fast mode Node example: [examples/fast-mode-node.md](examples/fast-mode-node.md)
- Batch webhook pipeline: [examples/batch-webhook-pipeline.md](examples/batch-webhook-pipeline.md)
- API reference: [references/api-reference.md](references/api-reference.md)
- Common drift and breaks: [troubleshooting/common-drift-and-breaks.md](troubleshooting/common-drift-and-breaks.md)
