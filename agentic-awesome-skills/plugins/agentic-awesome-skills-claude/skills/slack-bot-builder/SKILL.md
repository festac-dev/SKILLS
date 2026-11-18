---
name: agentic-awesome-slack-bot-builder-315f43a1
description: Build Slack apps using the Bolt framework across Python, JavaScript,
  and Java. Covers Block Kit for rich UIs, interactive components, slash commands,
  event handling, OAuth installation flows, and Workflow Builder integration.
metadata:
  upstream_headers:
    risk: critical
    source: vibeship-spawner-skills (Apache 2.0)
    date_added: 2026-02-27
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Slack Bot Builder

Build Slack apps using the Bolt framework across Python, JavaScript, and Java.
Covers Block Kit for rich UIs, interactive components, slash commands,
event handling, OAuth installation flows, and Workflow Builder integration.
Focus on best practices for production-ready Slack apps.

## Application boundary

The bundled guide is a set of partial Python sketches, not a runnable app across all three advertised languages. Supply missing business functions/stores/imports and verify the pinned Bolt SDK APIs. Authenticate and authorize the acting workspace/user/object before approvals, ticket creation or incident changes; removing a button does not prevent duplicate/concurrent processing. Use durable idempotency and tenant-scoped installation storage. Escape untrusted mrkdwn/mentions and redact tokens, response URLs and private channel data. Sending real messages and enabling OAuth/production integrations require explicit authorization. Socket Mode can support production and multiple connections; choose transport from verified platform/distribution requirements, not the guide's development-only claim. Legacy WorkflowStep examples are historical and need migration to supported custom steps.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
- User mentions or implies: slack bot
- User mentions or implies: slack app
- User mentions or implies: bolt framework
- User mentions or implies: block kit
- User mentions or implies: slash command
- User mentions or implies: slack webhook
- User mentions or implies: slack workflow
- User mentions or implies: slack interactive
- User mentions or implies: slack oauth

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
