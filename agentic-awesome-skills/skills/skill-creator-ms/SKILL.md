---
name: agentic-awesome-skill-creator-ms-2e0bbea7
description: Guide for creating effective skills for AI coding agents working with
  Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating
  existing skills.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Skill Creator

Guide for creating skills that extend AI agent capabilities, with emphasis on Azure SDKs and Microsoft Foundry.

> **Required Context:** When creating SDK or API skills, establish the SDK package, target language, installed version and primary documentation from the project/user; ask only for missing essentials for the skill to be based on.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Example

For an Azure Blob SDK skill, identify the installed package version, document
read-only list/download plus a least-privilege credential, and show paging/errors.
Use a synthetic container fixture first; do not create or delete a live storage
account to satisfy a pattern-matching acceptance test.
