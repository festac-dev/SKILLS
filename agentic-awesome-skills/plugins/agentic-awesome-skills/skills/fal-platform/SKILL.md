---
name: agentic-awesome-fal-platform
description: Platform APIs for model management, pricing, and usage tracking
metadata:
  upstream_headers:
    risk: critical
    source: https://github.com/fal-ai-community/skills/blob/main/skills/claude.ai/fal-platform/SKILL.md
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Fal Platform

## Overview

Platform APIs for model management, pricing, and usage tracking

## When to Use This Skill

Use this skill when you need to work with platform apis for model management, pricing, and usage tracking.

## Procedure

Use a configured integration to inspect the requested account/model information.
Confirm account identity, region, model endpoint and time window; select only the
fields needed. Read pricing and usage from actual returned records with timestamps,
currency, unit and period. A model's advertised unit price is not the total job cost.
Do not invent management endpoints: no API client is bundled and the historical
upstream path is absent from the current source tree.

Keep read-only inspection separate from model changes, key rotation or billing
operations, which need explicit authorization. Protect account identifiers and keys.
If the tool or permissions are absent, report the missing evidence rather than zero
usage or an available balance. Return source-linked observations and remaining gaps.

## Example

**User request:**

> Use @fal-platform for this task: Platform APIs for model management, pricing, and usage tracking.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
