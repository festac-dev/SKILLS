---
name: trailofbits-gh-cli
description: Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch,
  and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests,
  or issues.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# gh-cli

## When to Use

- Working with GitHub repositories, pull requests, issues, releases, or raw file URLs.
- You need authenticated access to private repositories or higher API rate limits.
- You are about to use `curl`, `wget`, `WebFetch`, or an MCP fetch tool against GitHub.

## When NOT to Use

- The target is not GitHub.
- Plain local git operations already solve the task.

## Guidance

Prefer the authenticated `gh` CLI over raw HTTP fetches for GitHub content. In particular:

- Prefer `gh repo view`, `gh pr view`, `gh pr list`, `gh issue view`, and `gh api` over unauthenticated `curl` or `wget`.
- Prefer cloning a repository and reading files locally over fetching `raw.githubusercontent.com` blobs directly.
- Avoid using GitHub API `/contents/` endpoints as a substitute for cloning and reading repository files.

Examples:

```sh
gh repo view owner/repo
gh pr view 123 --repo owner/repo
gh api repos/owner/repo/pulls
```

For the hook implementation, see:
- `plugins/gh-cli/README.md`
- `plugins/gh-cli/hooks/`
