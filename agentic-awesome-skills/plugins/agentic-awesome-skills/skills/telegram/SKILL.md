---
name: agentic-awesome-telegram
description: Integracao completa com Telegram Bot API. Setup com BotFather, mensagens,
  webhooks, inline keyboards, grupos, canais. Boilerplates Node.js e Python.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-03-06'
    author: renat
    tags:
    - messaging
    - telegram
    - bots
    - webhooks
    tools:
    - claude-code
    - antigravity
    - cursor
    - gemini-cli
    - codex-cli
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Telegram Bot API - Integracao Profissional

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use This Skill

- When the user mentions "telegram" or related topics
- When the user mentions "bot telegram" or related topics
- When the user mentions "telegram bot" or related topics
- When the user mentions "api telegram" or related topics
- When the user mentions "chatbot telegram" or related topics
- When the user mentions "mensagem telegram" or related topics

## Do Not Use This Skill When

- The task is unrelated to telegram
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Execution boundaries

Examples are scoped integration fragments, not a production certification. Sending messages, registering webhooks, moderating chats and charging users require authorization for the actual account and recipients. Preserve pending updates; dropping them is a separate destructive decision. Use disposable fixtures for tests and never print bot tokens or private webhook URLs. The Python webhook boilerplate uses the library-managed lifecycle behind an HTTPS reverse proxy; no Flask health endpoint is provided.
