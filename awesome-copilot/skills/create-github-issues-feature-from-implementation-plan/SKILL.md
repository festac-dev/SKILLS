---
name: copilot-create-github-issues-feature-from-implementation-plan
description: 'Create GitHub Issues from implementation plan phases using feature_request.yml or chore_request.yml templates.'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Create GitHub Issue from Implementation Plan

Create GitHub Issues for the implementation plan at `${file}`.

## Process

1. Analyze plan file to identify phases
2. Check existing issues using `search_issues`
3. Create new issue per phase using `create_issue` or update existing with `update_issue`
4. Use `feature_request.yml` or `chore_request.yml` templates (fallback to default)

## Requirements

- One issue per implementation phase
- Clear, structured titles and descriptions
- Include only changes required by the plan
- Verify against existing issues before creation

## Issue Content

- Title: Phase name from implementation plan
- Description: Phase details, requirements, and context
- Labels: Appropriate for issue type (feature/chore)
