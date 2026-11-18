---
name: agentic-awesome-codex-review
description: Professional code review with auto CHANGELOG generation, integrated with
  Codex AI. Use when you want professional code review before commits, you need automatic
  CHANGELOG generation, or reviewing large-scale refactoring.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# codex-review

## Overview
Professional code review with auto CHANGELOG generation, integrated with Codex AI

## When to Use
- When you want professional code review before commits
- When you need automatic CHANGELOG generation
- When reviewing large-scale refactoring

## Installation
```bash
npx skills add -g BenedictKing/codex-review
```

## Step-by-Step Guide
1. This entrypoint does not bundle the upstream integration. Inspect a selected upstream revision and authorize installation scope before using the installation option above.
2. Ensure Codex CLI is installed
3. Use `/codex-review` only when the installed host exposes it. Pin repository/base/head and inspect the net diff directly; return findings with exact trigger, location and evidence. A generated CHANGELOG must match the actual diff and must not rewrite unrelated release history.

## Examples
See [GitHub Repository](https://github.com/BenedictKing/codex-review) for examples.

## Best Practices
- Keep CHANGELOG.md in your project root
- Use conventional commit messages

## Troubleshooting
See the GitHub repository for troubleshooting guides.

## Related Skills
- context7-auto-research, tavily-web, exa-search, firecrawl-scraper

## Limitations
- An automated reviewer is advisory, not merge approval. Confirm provider/data/cost scope before sending private source externally; no implicit commit, push or publication.
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
