---
name: claude-code-toolkit-claude-memory-kit
description: Persistent memory system for Claude Code. Two-layer architecture (hot
  cache + knowledge wiki), safety hooks, /close-day end-of-day synthesis. Zero external
  dependencies.
license: MIT
metadata:
  upstream_headers:
    author: awrshift
    version: 3.2.0
    tags:
    - memory
    - context-management
    - productivity
    - agent-memory
    repository: https://github.com/awrshift/claude-memory-kit
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Claude Memory Kit

Your Claude agent remembers everything across sessions and projects.

## What it does

- **Persistent memory** — MEMORY.md hot cache + knowledge wiki with [[wikilinks]]
- **Multi-project support** — per-project backlogs and context isolation
- **Safety hooks** — prevent context loss during compression and long sessions
- **`/close-day`** — one command captures your entire day
- **`/tour`** — interactive guided walkthrough

## Quick Start

```bash
git clone https://github.com/awrshift/claude-memory-kit.git my-project
cd my-project
claude
```

## Built from production

700+ sessions across 7 projects. Adapted from Karpathy/Cole Medin's knowledge base pattern, simplified for daily CLI use.
