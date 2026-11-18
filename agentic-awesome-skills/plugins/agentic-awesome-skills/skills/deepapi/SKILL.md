---
name: agentic-awesome-deepapi
description: Use DeepAPI for supported scraping, research, and email workflows with
  explicit credentials and approval.
license: MIT
metadata:
  upstream_headers:
    category: research
    risk: critical
    source: community
    source_repo: davidondrej/skills
    source_type: community
    date_added: '2026-07-07'
    author: davidondrej
    tags:
    - deepapi
    - scraping
    - email
    - api
    tools:
    - claude
    - codex
    license_source: https://github.com/davidondrej/skills/blob/main/LICENSE
    version: b17ad5148ab7
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# DeepAPI

## Detailed Guide

The bundled endpoint guide describes a versioned external service, not a local runtime. Validate the authorized service origin and current schema before attaching credentials or spending credits; setup must never request secrets in chat.

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use

- Use when the task needs supported DeepAPI scraping, research, or email endpoints.
- Use when the user has provided or confirmed the required DeepAPI credentials and scope.

Use this skill when the user asks you to scrape public web data or draft/read/send email through DeepAPI.

## Limitations

- Adapted from `davidondrej/skills`; verify local paths, tools, credentials, and agent features before acting.
- For commands, remote access, scheduling, browser automation, or file-changing workflows, get explicit user approval and confirm the target environment first.
