---
name: openai-debug-zoom-integration
description: Use when isolating failures.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Debug Zoom Integration

Use this skill when the user already built something and it is failing.

## Triage Order

1. Auth and app configuration
2. Request construction or event verification
3. SDK initialization or platform mismatch
4. Media/session behavior
5. Client platform and capability assumptions

## Evidence To Request

- Exact error text
- Platform and SDK/runtime
- Relevant request or payload sample
- What worked versus what failed
- Whether the issue is reproducible or intermittent

## Reference Routing

- [oauth](../oauth/SKILL.md)
- [rest-api](../rest-api/SKILL.md)
- [webhooks](../webhooks/SKILL.md)
- [meeting-sdk](../meeting-sdk/SKILL.md)
- [video-sdk](../video-sdk/SKILL.md)
- [rtms](../rtms/SKILL.md)

## Output

- Most likely failing layer
- Ranked hypotheses
- Short fix plan
- Verification steps
