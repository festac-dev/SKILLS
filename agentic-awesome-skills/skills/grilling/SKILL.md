---
name: agentic-awesome-grilling-a821a9aa
description: Interview the user relentlessly about a plan or design. Use when the
  user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.
license: MIT
metadata:
  upstream_headers:
    category: productivity
    risk: safe
    source: community
    source_repo: mattpocock/skills
    source_type: community
    date_added: '2026-06-19'
    author: Matt Pocock
    license_source: https://github.com/mattpocock/skills/blob/main/LICENSE
    tags:
    - productivity
    - workflow
    - coding-agents
    tools:
    - claude-code
    - codex-cli
    - cursor
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

## When to Use

Use when this workflow matches the user request: Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill' trigger phrases.


_Source: [mattpocock/skills](https://github.com/mattpocock/skills) (MIT)._Interview the user about relevant uncertainties in the supplied plan until the stated decision criteria are resolved or the user ends the interview. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing. Asking multiple questions at once is bewildering.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Example

**User request:**

> Use @grilling for this task: Interview the user relentlessly about a plan or design.

## Limitations

- Requires the upstream tool, account, API key, or local setup when the workflow names one.
- Does not authorize destructive, production, paid, or external-message actions without explicit user approval.
- Validate generated artifacts or recommendations against the user's real sources before treating them as final.
