---
name: agentic-awesome-matematico-tao-a7beaa51
description: Analyze code complexity, dependency graphs, concurrency and invariants
  using explicit mathematical assumptions. Use for algorithm or architecture reviews;
  bundled Kotlin scanners produce advisory estimates, not formal proofs.
metadata:
  upstream_headers:
    risk: safe
    source: community
    date_added: '2026-03-06'
    author: renat
    tags:
    - mathematics
    - code-analysis
    - algorithms
    - formal-methods
    tools:
    - claude-code
    - antigravity
    - cursor
    - gemini-cli
    - codex-cli
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Mathematical Code and Architecture Review

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use This Skill

- Analyze a concrete algorithm’s time/space complexity and boundary cases.
- Review dependency cycles, state transitions, concurrent access or stated invariants.
- Use mathematical models to test a specific code hypothesis with explicit assumptions.

## Do Not Use This Skill When

- The task is unrelated to matematico tao
- A simpler, more specific tool can handle the request
- The user needs general-purpose assistance without domain expertise

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

## Example

Review a local Kotlin pipeline for cancellation leaks. Map the actual states and resource owners, build a synthetic failing schedule, and distinguish measured evidence from assumptions before proposing a fix.

## Tool and evidence boundary

The scripts read authorized local Kotlin files and optionally write reports inside the workspace; they never prove complete code coverage or execute target source. Use an isolated output path and preserve existing files. Regex scores and Auri-specific package mappings are advisory. Do not infer authorization to access the original author’s filesystem, publish reports, modify source or run network operations. No claim of endorsement, credentials or equivalence to any named mathematician is made.
