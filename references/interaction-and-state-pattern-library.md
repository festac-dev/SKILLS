# Interaction and State Pattern Library

## Global patterns
Navigation, command/search palette, breadcrumbs, contextual help, account/workspace switching, responsive shell, keyboard shortcuts, and persistent preferences.

## Data patterns
Lists, tables, filters, sorting, pagination, bulk actions, detail views, comparison, import, export, history, versioning, and audit trails.

## Workflow patterns
Wizards, approvals, queues, assignment, status transitions, scheduling, recurring work, dependencies, undo, drafts, autosave, conflict resolution, and long-running jobs.

## Feedback patterns
Inline validation, actionable errors, progress, optimistic updates, success confirmation, warnings, destructive-action confirmation, retry, and recovery.

## Content patterns
Rich text, markdown, structured editors, attachments, media, previews, comments, annotations, and collaborative editing.

## Trust patterns
Permission explanations, consent, provenance, source citations, activity history, data freshness, human review, and action receipts.

## States every meaningful component should consider
Initial, loading, empty, populated, partial, stale, refreshing, disabled, read-only, validation error, server error, permission denied, offline, retrying, success, and destructive/irreversible.

Document which states are applicable; do not force irrelevant states onto simple components.

## Application evidence

Test state continuity when filtering, navigating back, refreshing and resizing with a dialog open. Distinguish no records, no matching records, denied access and unavailable data; each needs a different explanation and recovery action.
