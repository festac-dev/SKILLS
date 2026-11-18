# Backend Code Patterns

Language-neutral patterns with the reasoning that makes them correct. A tested JavaScript implementation of many of these lives in `examples/backend-reference/`. Translate, do not copy blindly.

## Request lifecycle (order matters)
1. Assign or accept a **request ID** (validate format) and attach to logs and responses.
2. Apply **limits** early: body size, header size, timeouts, connection caps, rate limits.
3. **Authenticate** (who are you), then **authorize** (may you do this to *this* object).
4. **Validate** input with an allow-list schema; reject or drop unknown fields.
5. Execute in a **transaction** boundary appropriate to the use case.
6. Emit **side effects** (email, webhook, event) through an outbox or queue, not inline.
7. Return a consistent **error envelope**; log details server-side, not to the client.

## Authentication and sessions
- Passwords: argon2id (preferred), scrypt or bcrypt with current cost settings; per-user salt (built into these); optional pepper in a secrets manager; never roll your own; rate-limit and lock progressively; check against breached-password lists.
- Server sessions: opaque random ID (≥128 bits) in a cookie with `HttpOnly; Secure; SameSite=Lax` (or Strict), rotate on login and privilege change, absolute and idle timeouts, server-side revocation.
- Tokens (JWT/PASETO): short-lived access tokens, rotating refresh tokens with reuse detection, fixed algorithm allow-list, validate `iss`, `aud`, `exp`, `nbf`; avoid putting authorization state that must be revocable only in a token.
- OAuth2/OIDC: Authorization Code + PKCE for public and confidential clients; no implicit flow; exact redirect URI matching; validate `state` and `nonce`.
- MFA: TOTP or WebAuthn/passkeys; recovery codes hashed; step-up for sensitive actions.
- Service-to-service: mTLS or workload identity or signed short-lived tokens; never shared static admin keys.

## Authorization
- Default deny. Centralize policy (RBAC for roles, ABAC/ReBAC for relationships; engines like OPA, Cedar, Zanzibar-style systems when complexity justifies).
- Check **object-level** access on every read/write (the top API vulnerability class is broken object-level authorization): `WHERE id = ? AND owner_id = ?` or a policy check, never just "is logged in".
- Check **function-level** and **property-level** access (mass assignment, excessive data exposure).
- Test authorization with a matrix (`templates/AUTHORIZATION_MATRIX.md`), including cross-tenant negative tests.

## Idempotency and retries
- Make unsafe operations idempotent with a client-supplied key stored under a unique constraint; same key + same payload returns the stored result; same key + different payload is an error.
- Retry only when safe; exponential backoff with **full jitter**, a retry budget, and a circuit breaker; honor `Retry-After`; set timeouts on every outbound call (connect, read, total).
- Make consumers idempotent: processed-message table or natural unique keys; assume at-least-once delivery.

## Outbox and sagas
- Write business row and an `outbox` row in **one transaction**; a relay publishes and marks sent. Avoids the dual-write bug.
- Multi-step distributed workflows: orchestrated saga or a workflow engine (Temporal, Step Functions, Cadence, Camunda, durable functions) with compensations, timeouts and visibility.

## Concurrency control
- Optimistic: `version`/`updated_at` column; `UPDATE … WHERE id=? AND version=?`; 409 on conflict, ETag/`If-Match` at the API.
- Pessimistic: `SELECT … FOR UPDATE [SKIP LOCKED]` for queues and scarce resources; keep transactions short; consistent lock ordering.
- Uniqueness and inventory rules belong in the database (unique/exclusion/check constraints), not only in application code.

## Pagination, filtering, sorting
Keyset pagination for large or changing data; opaque cursors; stable total ordering (sort key + unique tiebreaker); cap `limit`; allow-list sortable fields; index to match the order.

## Caching
Decide what is cacheable, key design, TTL, invalidation, stampede protection (single-flight, jittered TTLs, stale-while-revalidate), and what happens when the cache is down. HTTP caching (`ETag`, `Cache-Control`, `Vary`) before bespoke caches. Never cache per-user data in a shared cache without a user-scoped key.

## File uploads
Validate size and type by content (magic bytes), not extension; generate server-side names; store outside the web root or in object storage; presigned URLs with short expiry and size/type conditions; virus scan if shared; serve user content from a separate origin with `Content-Disposition` as needed; strip metadata when privacy matters.

## Outbound HTTP safety (SSRF)
Allow-list destinations when possible; resolve DNS and block private, loopback, link-local and metadata ranges **after** resolution and on each redirect; disable redirects or cap them; restrict schemes; separate network egress policy for fetchers.

## Webhooks
Receive: verify signature over raw body, check timestamp window, dedupe by event ID, ack quickly then process asynchronously, return 2xx only after durable enqueue. Send: sign payloads, retry with backoff for days, expose delivery logs and replay, support secret rotation with overlap, per-endpoint rate limits and circuit breaking.

## Background jobs
Idempotent handlers; visibility timeout > max runtime; retries with backoff and a dead-letter queue; poison-message handling; priority lanes; concurrency limits per tenant; schedules with distributed locks or a single scheduler; alert on queue age, not only depth.

## Errors and observability
Typed errors; map to status codes; never leak stack traces or SQL; correlate logs/metrics/traces with request ID and trace ID; RED metrics (rate, errors, duration) per route; USE metrics (utilization, saturation, errors) per resource; log at boundaries; sample traces; redact PII.

## Config and secrets
12-factor style environment config validated at startup (fail fast); secrets from a manager or injected files, never committed; separate config per environment; feature flags with owners and expiry; no secrets in images or logs.

## Shutdown and deploy safety
Handle SIGTERM: flip readiness, stop accepting, finish in-flight work within a deadline, close pools, exit. Rolling or blue/green deploys; backwards-compatible schema (expand → migrate → contract); health checks that reflect real dependencies carefully (avoid cascading failures by not making liveness depend on the database).

## Time, money, text
UTC storage; explicit time zones for user-facing scheduling; monotonic clocks for durations; integer minor units or decimals for money; Unicode normalization and case-folding for identifiers; locale-aware formatting at the edge; never parse human-entered dates ambiguously.

## Testing the backend
Unit tests for domain rules; integration tests against a real database (containers); contract tests for APIs and consumers; property-based tests for parsers and invariants; authorization negative tests; migration tests on production-like data; load tests with realistic mixes; chaos/failure injection for dependencies; backup restore tests. See `specialists/backend-testing-and-verification.md`.
