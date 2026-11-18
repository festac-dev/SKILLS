---
name: agentic-awesome-amazon-alexa-2e0ac5ac
description: Integracao completa com Amazon Alexa para criar skills de voz inteligentes,
  transformar Alexa em assistente com Claude como cerebro (projeto Auri) e integrar
  com AWS ecosystem (Lambda, DynamoDB, Polly, Transcribe, Lex, Smart Home).
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-03-06'
    author: renat
    tags:
    - voice
    - alexa
    - aws
    - smart-home
    - iot
    tools:
    - claude-code
    - antigravity
    - cursor
    - gemini-cli
    - codex-cli
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# AMAZON ALEXA — Voz Inteligente com Claude

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use This Skill

- When you need specialized assistance with this domain

## Do Not Use This Skill When

- The task is unrelated to amazon alexa
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Example

Prototype a read-only `ChatIntent` for one authorized test account. Verify the
interaction model and timeout in the ASK simulator before deploying; keep smart
home control disabled until account linking and device ownership checks pass.
