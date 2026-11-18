---
name: agentic-awesome-ffuf-claude-skill-8526e196
description: Web fuzzing with ffuf
metadata:
  upstream_headers:
    risk: offensive
    source: https://github.com/jthack/ffuf_claude_skill
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Ffuf Claude Skill

> **⚠️ AUTHORIZED USE ONLY**
> This skill is for educational purposes or authorized security assessments only.
> You must have explicit, written permission from the system owner before using this tool.
> Misuse of this tool is illegal and strictly prohibited.

## Overview

Web fuzzing with ffuf

## When to Use This Skill

Use this skill when you need to work with web fuzzing with ffuf.

## Instructions

Use only a specifically authorized fuzzing target and allowed paths. Record host,
protocol, scope, time window, request-rate limits and prohibited side effects before
sending traffic. This AAS entrypoint does not bundle ffuf, a wordlist or an upstream
runner. Inspect the installed version's help and review the selected wordlist.

Plan a bounded run against a local or explicitly authorized test environment;
avoid writes, authenticated-state changes and rate-limit bypass. Compare candidate
responses with a known missing-path baseline; response size/status alone does not
prove a vulnerability. Preserve request/response evidence after redacting secrets,
stop on target instability or scope changes, and report untested paths as unknown.
## Mandatory confirmation gate

Before each probing command, collect the exact target URL, IP, account, or resource, written authorization and permitted scope. Show the exact command and expected effect. Wait for explicit confirmation in the current conversation. Without confirmation, remain read-only and provide defensive guidance only. No traffic is authorized simply by invoking this guide.

## Example

**User request:**

> Use @ffuf-claude-skill for this task: Web fuzzing with ffuf.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
