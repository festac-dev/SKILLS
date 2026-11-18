# Backend Reference Patterns (zero dependencies)

Runnable, tested reference for patterns that production backends need. It is a teaching and starting reference, **not a framework to adopt**: translate each pattern into the project's real stack.

Run: `node --test` (12 tests; Node 20+). Start: `PORT=8080 node src/server.js`.

| Pattern | Where | Production note |
|---|---|---|
| Structured JSON logs, request IDs | `lib.js`, `app.js` | Ship to a log backend; never log secrets or full bodies |
| Problem+JSON errors, no internals on 5xx | `lib.js` | Keep a stable machine-readable `type` per error class |
| Body size limit, JSON parse errors | `lib.js` | Also limit at the reverse proxy |
| Allow-list validation | `lib.js` | Use the project's schema validator when larger contracts need one |
| Token-bucket rate limit | `lib.js` | In-memory is per-process; use Redis/edge for fleets; key by user/key, not only IP |
| Idempotency keys | `lib.js` | Persist in the database with a unique constraint and TTL |
| Cursor (keyset) pagination | `lib.js` | Cursor must encode the sort key, not an offset |
| Webhook HMAC with replay window | `lib.js` | Verify the raw bytes; rotate secrets with overlap |
| Retry with full jitter | `lib.js` | Retry only idempotent or keyed operations; add a budget and circuit breaker |
| Liveness vs readiness, graceful drain | `app.js` | Readiness flips before shutdown so load balancers stop routing |
| Constant-time API key compare | `app.js` | Prefer hashed, scoped, revocable keys stored server-side |

Deliberately absent: persistence, real authN (sessions/OIDC), TLS, metrics endpoint, queue. See `references/backend-code-patterns.md`, `references/sql-and-data-patterns.md` and `references/infrastructure-config-snippets.md`.
