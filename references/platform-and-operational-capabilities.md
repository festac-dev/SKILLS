# Platform and Operational Capability Catalogue

This is a discovery index, not a roadmap. Select only capabilities supported by user needs and operating constraints.

## Platform foundations
- Authentication, session management, account recovery and identity federation.
- Organizations, workspaces, membership, roles and resource-level permissions.
- Configuration, feature flags, preferences and environment separation.
- Search, filtering, sorting, pagination and saved views.
- Import, export, backup, restore and data portability.

## Collaboration and communication
- Presence, comments, mentions, shared editing, notifications and activity history.
- Conflict handling, version history, approval workflows and assignment.
- Email, push, in-app and webhook delivery with preferences and deduplication.

## Workflow and integration
- Trigger-condition-action automation, schedules, queues and background jobs.
- Webhooks, external connectors, scoped credentials, retries and execution history.
- Human approvals, dry runs, cancellation and audit evidence.

## Enterprise operations
- Tenant isolation, SSO, SCIM, delegated administration and policy controls.
- Audit logs, retention, legal holds, support access and data export.
- Billing, entitlements, quotas, metering and reconciliation where commercially needed.

## Resilience
- Offline queues, sync status, conflict resolution and stale-data warnings.
- Rate limiting, circuit breakers, graceful degradation and retry/backoff.
- Health checks, observability, incident response, backup and disaster recovery.

## Trust and governance
- Privacy notices, data minimization, consent where applicable, deletion and retention.
- Threat modeling, security testing, dependency governance and vulnerability response.
- Accessibility, localization, RTL, inclusive content and user-controlled preferences.

## Advanced capabilities
- Realtime updates, semantic search, AI agents, recommendation systems, multimodal input, 3D, AR/VR and device integrations.
- Treat each as optional and assess performance, privacy, safety, maintenance and user benefit first.

## Application evidence

Add operating capabilities only when needed by supported journeys and service commitments. For each selected capability, identify a concrete failure signal, responsible component and recovery operation before adding infrastructure.
