---
name: openai-packaging-notarization
description: Prepare macOS packaging and notarization workflows. Use when archiving apps, validating bundles, or explaining distribution-only failures.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Packaging & Notarization

## Quick Start

Use this skill when the work is about shipping the app rather than merely
running it locally: archives, exported app bundles, notarization readiness,
hardened runtime, or distribution validation.

## Workflow

1. Confirm the distribution goal.
   - Local archive validation
   - Signed distributable app
   - Notarization troubleshooting

2. Inspect the artifact.
   - Validate app bundle structure.
   - Check nested frameworks, helper tools, and entitlements.

3. Inspect signing and runtime prerequisites.
   - Hardened runtime
   - Signing identity
   - Nested code signatures
   - Required entitlements

4. Explain notarization readiness or failure.
   - Separate packaging issues from trust-policy symptoms.
   - Point to the minimum follow-up validation commands.

## Guardrails

- Do not present notarization as required for ordinary local debug runs.
- Call out when you lack the actual exported artifact and are inferring from project settings.
- Keep advice concrete and verifiable.

## Output Expectations

Provide:
- what artifact or settings were inspected
- whether the app looks distribution-ready
- the top missing prerequisite or failure mode
- the next validation or repair step
