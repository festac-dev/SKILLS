# Authentication and Authorization Pattern Catalogue

## Browser apps
- Server session cookie (Secure, HttpOnly, SameSite=Lax or Strict) plus CSRF token for state-changing requests.
- Backend-for-frontend holding tokens server-side when integrating OAuth providers.
- Avoid storing long-lived tokens in localStorage.

## Single-page and mobile apps
- Authorization code + PKCE; short-lived access tokens; rotating refresh tokens; secure OS storage on devices.

## APIs and services
- Scoped API keys (hashed, prefixed, revocable); OAuth client credentials for machine clients; mTLS or workload identity internally.
- Signed webhooks: HMAC with timestamp, replay window, constant-time comparison.

## Authorization models
- RBAC: simple, role-to-permission. Good when roles are few and stable.
- ABAC/policy engines: conditions on user, resource, context. Good for complex rules.
- ReBAC: relationships (owner, member, viewer, shared-with). Good for sharing and hierarchies.
- Multi-tenant: every query scoped by tenant; tests that attempt cross-tenant access.

## Common flaws to test
IDOR via sequential IDs, missing checks on secondary endpoints, mass assignment, JWT alg confusion, long-lived tokens not revoked, password reset token reuse, user enumeration, privilege escalation through role-edit endpoints, trusting client-provided tenant or role fields.

## Recovery and support
Account recovery that does not bypass MFA silently, audit trails for support actions, session list with remote logout.
