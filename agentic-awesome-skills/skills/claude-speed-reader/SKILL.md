---
name: agentic-awesome-claude-speed-reader-d558dd0a
description: -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style
  ORP highlighting
metadata:
  upstream_headers:
    risk: safe
    source: https://github.com/SeanZoR/claude-speed-reader
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Claude Speed Reader

## Overview

-Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting

## When to Use This Skill

Use when the user wants an RSVP reader for an existing response or supplied text and a compatible upstream reader is available.

## Instructions

This AAS entrypoint is a guide to the upstream reader, not the bundled reader itself.
Verify an installed, reviewed upstream copy before invoking its command. In Claude
Code, upstream documents `/speed` for the last response and `/speed "text"` for
custom text. Other hosts may not implement that slash command.

1. Confirm the text the user wants displayed; exclude sensitive response history
   from external tools unless sharing is authorized.
2. Use the reader's adjustable speed and pause controls; start at a comfortable rate.
3. Check that the actual reader opens and displays the intended text. Do not claim
   it ran merely because the command was printed.

RSVP presentation rate is not proof of comprehension. This skill does not guarantee
600 WPM reading ability and does not install browser assets automatically.

## Example

**User request:**

> Use @claude-speed-reader for this task: -Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
