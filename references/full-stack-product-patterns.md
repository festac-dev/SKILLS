# Full-Stack Product Patterns

The TaskForge AI brief is an example, not a template to copy blindly. Reuse patterns only when they solve a real problem.

## Application shell
Possible patterns: persistent/collapsible navigation, contextual header, search, global create action, profile controls, breadcrumbs and workspace switcher. Choose based on information architecture; none is mandatory.

## Workflow boards
Potential capabilities: configurable workflow columns, task cards, priority, assignment, labels, subtasks, progress, notes, activity and task detail views. Persist moves on the server, validate transitions, handle concurrency and provide keyboard alternatives to drag-and-drop. Do not communicate status by colour alone.

## Embedded AI assistance
Potential capabilities: suggest subtasks, draft plans, summarize, clarify writing, identify dependencies and estimate effort. Treat model output as untrusted suggestions. Require review for consequential changes, preserve originals, validate structured output, handle timeouts/rate limits/provider outages, keep credentials server-side, use replaceable provider adapters, disclose uncertainty and minimize data shared with providers.

## Analytics
Possible charts: completion over time, work distribution, cycle time, throughput, workload and AI usage. Define formulas, sources, time zones, aggregation, reopened/deleted record handling, freshness and caveats before charting. Provide accessible text/table alternatives. Do not imply causation from descriptive counts.

## Data model candidates
User, organization/workspace, project, task, subtask/dependency, note/comment, membership, assignment, label, attachment, activity/audit event and AI usage record. Create only entities justified by real workflows. Define ownership, tenant boundaries, indexes, constraints, deletion and retention.

## Database and delivery
Choose local and production databases based on concurrency, hosting, migrations, backup and operations. Switching engines is not necessarily configuration-only; verify types, constraints, SQL and transaction behavior. Document runtime versions, install commands, safe environment examples, database setup, migrations, seed data, test/build commands, deployment, backup and rollback. Verify instructions against the actual repository.

## Application evidence

Choose a pattern by the journey it completes and implement its real persistence and error path. A polished shell with fixture data remains a UI demonstration until the actual server contract and authorization boundary have been exercised.
