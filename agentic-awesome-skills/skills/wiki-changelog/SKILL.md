---
name: agentic-awesome-wiki-changelog-eb8f3c49
description: Generate structured changelogs from git history. Use when user asks "what
  changed recently", "generate a changelog", "summarize commits" or user wants to
  understand recent development activity.
metadata:
  upstream_headers:
    risk: safe
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Wiki Changelog

Generate structured changelogs from git history.

## When to Use
- User asks "what changed recently", "generate a changelog", "summarize commits"
- User wants to understand recent development activity

## Procedure

1. Examine git log (commits, dates, authors, messages)
2. Group by time period: daily (last 7 days), weekly (older)
3. Classify each commit: Features (🆕), Fixes (🐛), Refactoring (🔄), Docs (📝), Config (🔧), Dependencies (📦), Breaking (⚠️)
4. Generate concise user-facing descriptions using project terminology

## Example

**User request:**

> Generate a changelog from the recent git history, grouping user-visible changes and linking each claim to its commit.

## Constraints

- Focus on user-facing changes
- Merge related commits into coherent descriptions
- Use project terminology from README
- Highlight breaking changes prominently with migration notes

### When to Use
This skill is applicable to execute the workflow or actions described in the overview.
