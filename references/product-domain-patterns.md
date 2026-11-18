# Product Domain Patterns

This is a discovery catalogue, not a mandatory feature checklist. Select patterns only when supported by the product's users, business model, risks, and constraints.

## Common product domains
- SaaS: organizations, seats, roles, plans, usage limits, audit history, integrations.
- Commerce: catalogues, pricing, carts, checkout, orders, refunds, fulfilment.
- Marketplace: participants, listings, matching, trust, disputes, settlement.
- Developer tools: projects, environments, APIs, keys, logs, webhooks, SDKs.
- Content platforms: editorial roles, drafts, revisions, approvals, publishing.
- Education: courses, lessons, practice, assessments, progress, instructor tools.
- Financial workflows: accounts, journal entries, reconciliation, approvals, statements.
- Health workflows: consent, provenance, access audit, clinical oversight, safety boundaries.
- IoT: device identity, provisioning, telemetry, commands, firmware, fleet management.
- Collaboration: workspaces, presence, comments, mentions, conflict resolution.

## Cross-domain capabilities to evaluate
Identity, authorization, search, notifications, import/export, billing, analytics, audit logs, integrations, localization, accessibility, offline behavior, recovery, support, observability, and governance.

## Selection test
For each candidate, document the user problem, evidence, operational cost, data implications, failure modes, and reason to defer or reject.

## Application evidence

Use domain examples to discover invariants rather than copy feature lists. For a ledger, reconcile exact amounts and reversals; for a marketplace, verify participant authority and dispute state. Route unfamiliar legal or clinical assumptions to their accountable reviewer.
