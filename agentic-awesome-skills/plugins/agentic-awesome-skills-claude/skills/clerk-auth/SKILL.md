---
name: agentic-awesome-clerk-auth-e72663c2
description: Expert patterns for Clerk auth implementation, middleware, organizations,
  webhooks, and user sync
metadata:
  upstream_headers:
    risk: safe
    source: vibeship-spawner-skills (Apache 2.0)
    date_added: 2026-02-27
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Clerk Authentication

Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
- User mentions or implies: adding authentication
- User mentions or implies: clerk auth
- User mentions or implies: user authentication
- User mentions or implies: sign in
- User mentions or implies: sign up
- User mentions or implies: user management
- User mentions or implies: multi-tenancy
- User mentions or implies: organizations
- User mentions or implies: sso
- User mentions or implies: single sign-on

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.

Guide snippets are independent alternatives/files, not one deployable module; duplicate default exports and omitted Prisma models/imports must be resolved in the actual project. Pin compatible Next.js/Clerk versions and check current middleware/proxy filenames. Authenticate each server route/action, validate inputs and authorize organization permissions/individual resources; client UI and `org:admin` do not grant global-user access. Verify webhook raw bytes first, then use a durable transactional event inbox keyed by Svix ID plus a domain ordering/tombstone policy; upsert alone does not prevent stale events resurrecting deleted users or overwriting newer state. Hard deletion must follow the application’s retention/foreign-key policy. Choose actual primary email rather than array order and allow phone-only identities. Use synthetic test instances and never log signing secrets/raw private payloads. See [Clerk sync guidance](https://clerk.com/docs/guides/development/webhooks/syncing) and [Svix raw payload verification](https://www.svix.com/guides/receiving/receive-webhooks-with-svix-cli/).
