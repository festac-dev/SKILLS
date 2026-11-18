---
name: openai-vercel-agent
description: Vercel Agent guidance — AI-powered code review, incident investigation, and SDK installation. Automates PR analysis and anomaly debugging. Use when configuring or understanding Vercel's AI development tools.
metadata:
  priority: 4
  docs:
    - "https://vercel.com/docs"
    - "https://sdk.vercel.ai/docs"
  sitemap: "https://vercel.com/sitemap/docs.xml"
  pathPatterns: 
    - '.github/workflows/vercel*.yml'
    - '.github/workflows/vercel*.yaml'
    - '.github/workflows/deploy*.yml'
    - '.github/workflows/deploy*.yaml'
    - '.github/workflows/preview*.yml'
    - '.github/workflows/preview*.yaml'
  bashPatterns: 
    - '\bvercel\s+agent\b'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Vercel Agent

You are an expert in Vercel Agent — AI-powered development tools built into the Vercel platform.

## What It Is

Vercel Agent is a suite of **AI-powered development tools** that leverage deep context about your codebase, deployment history, and runtime behavior. It provides automated code review, incident investigation, and SDK installation assistance.

## Capabilities

### Code Review
- Automatic PR analysis triggered on push or via `@vercel` mention in PR comments
- Multi-step reasoning: identifies security vulnerabilities, logic errors, performance issues
- Generates and validates patches in **Vercel Sandbox** (secure execution)
- Supports inline suggestions and full patch proposals

### Investigation
- Analyzes anomaly alerts by querying logs and metrics
- Finds patterns and correlations across deployment data
- Provides root cause insights
- **Requires Observability Plus** subscription

### Installation
- Auto-installs Web Analytics and Speed Insights SDKs
- Analyzes repo structure, installs dependencies, writes integration code
- Creates PRs with the changes
- **Free** (no credit cost)

## Pricing

- $0.30 per Code Review or Investigation + token costs
- $100 promotional credit for Pro teams
- Installation is free

## Configuration

Vercel Agent is configured at `https://vercel.com/{team}/{project}/settings` → **AI** section. No npm package required — it is a platform-level service.

## When to Use

- Automated security and quality checks on every PR
- Root-cause analysis when anomaly alerts fire
- Quick SDK installation for analytics/monitoring

## References

- 📖 docs: https://vercel.com/docs/agent
