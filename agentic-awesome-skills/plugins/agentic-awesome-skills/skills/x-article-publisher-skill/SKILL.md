---
name: agentic-awesome-x-article-publisher-skill
description: Publish articles to X/Twitter
metadata:
  upstream_headers:
    risk: critical
    source: https://github.com/wshuyi/x-article-publisher-skill
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# X Article Publisher Skill

## Overview

Publish articles to X/Twitter

## When to Use This Skill

Use this skill when you need to work with publish articles to x/twitter.

## Procedure

This entrypoint does not bundle an X publishing client. Resolve the target account, article text, media rights, visibility and timing. Prepare a draft and inspect it before publication. Use only a configured integration whose current schema supports articles; do not substitute a post or invent an endpoint. Publish only the exact content and destination authorized by the user. Record the returned article identity and verify its state before reporting success; reconcile an ambiguous timeout before retrying. Keep credentials out of text and logs.

The [source repository](https://github.com/wshuyi/x-article-publisher-skill) is an external prerequisite; inspect its complete content and license before installation.

## Example

**User request:**

> Publish articles to X/Twitter.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
