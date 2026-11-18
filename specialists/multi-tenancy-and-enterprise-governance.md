# Specialist: Multi-Tenancy and Enterprise Governance

Use multi-tenancy only when the product has distinct organizations or customer environments.

Define tenant boundaries, ownership, membership lifecycle, role hierarchy, delegated administration, cross-tenant access prevention, support access, audit trails, retention, export and deletion. Enforce isolation in trusted server/data layers, not only in the interface.

For enterprise identity, evaluate SSO, SCIM, domain verification, session policy and account recovery when required. Document break-glass access and support procedures. Test isolation with adversarial cross-tenant cases.

## Applied verification

Move or revoke a member while a session, export and background task remain active. Verify isolation and revocation for each operation using server-owned tenant identity, including support access and cached results.

## Tenant operations

Include tenant context in cache keys, queued work, exports and restore/deletion operations, not only request queries. Check noisy-neighbor limits, per-tenant quotas and the cost of moving to stronger isolation. Enterprise SSO/SCIM, residency, scoped support access and audit exports are requirements to discover, not features every app must implement.
