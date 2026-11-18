---
name: agentic-awesome-remotion-render
description: Export a Remotion video
metadata:
  upstream_headers:
    version: 4.0.526
    source_repo: remotion-dev/skills
    source_type: official
    source: remotion-dev
    date_added: '2026-09-21'
    risk: unknown
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

## General rendering strategy

Render a video using:

```
npx remotion render
```

Full list of options: https://www.remotion.dev/docs/cli/render.md

Render a still using:

```
npx remotion still
```

Full list of options: https://www.remotion.dev/docs/cli/still.md

## Transparent videos

See [Transparent videos](transparent-videos.md) for alpha-compatible codec/pixel-format settings. Confirm composition ID, frame range, output path and installed CLI version before rendering. Use a new output and inspect actual frames, duration, audio and alpha on a contrasting background; the command exiting successfully alone does not establish visual correctness.


## Examples

```text
User: Apply this skill to my current task.
Assistant: Follow the workflow in this skill, cite limitations, and ask before risky steps.
```

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
