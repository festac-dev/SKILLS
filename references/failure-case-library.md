# Failure Case Library (gotchas that keep recurring)

Scan this before design reviews and launches. Each item names the trap and the usual defense.

## Distributed systems and backend
- **Dual write** (DB + message broker in two steps) → inconsistent state. *Outbox pattern.*
- **At-least-once delivery** treated as exactly-once → duplicate side effects. *Idempotent consumers, dedupe keys.*
- **Retry storms / thundering herd** after an outage. *Backoff with jitter, retry budgets, circuit breakers, load shedding.*
- **Cache stampede** when a hot key expires. *Single-flight, jittered TTL, stale-while-revalidate.*
- **Unbounded queues/maps/caches** → memory exhaustion. *Bounds, eviction, backpressure.*
- **No timeouts** on outbound calls → thread/connection exhaustion. *Timeouts at every hop; deadlines propagated.*
- **Health checks that depend on the database** restart-loop everything during a DB blip. *Liveness = process only; readiness = can serve.*
- **Clock skew and wall-clock durations.** *Monotonic clocks for durations; NTP; never trust client time for security.*
- **Hot partitions/keys.** *Better key design, sharding by high-cardinality attributes, request coalescing.*
- **Long transactions and lock queues** blocking migrations. *`lock_timeout`, small batches, online schema change tools.*
- **N+1 queries.** *Batch loading, joins, query counts in tests.*
- **Offset pagination at depth.** *Keyset pagination.*
- **Float money, naive rounding.** *Integer minor units, explicit rounding mode, currency per amount.*
- **Time zones and DST** (missing/duplicated hours), leap seconds, month-end math. *Store UTC + zone ID; use a vetted date library; test DST transitions.*
- **Unicode**: case-insensitive comparison, normalization (NFC/NFD), emoji length, homoglyph spoofing. *Normalize and case-fold identifiers; length by grapheme where UX matters.*
- **Integer overflow, ID exhaustion** (32-bit IDs). *64-bit IDs from day one.*
- **Secrets in logs/URLs/error messages.** *Redaction, structured logging allow-lists.*
- **Mass assignment / over-posting.** *Allow-list fields per endpoint.*
- **Broken object-level authorization.** *Ownership checks on every read/write, negative tests.*
- **SSRF via URL fetchers/webhooks/importers.** *Egress allow-lists, resolve-then-validate, block metadata IPs.*
- **Open redirects and CORS wildcard with credentials.** *Exact allow-lists.*
- **Race conditions in check-then-act** (inventory, coupons, usernames). *Database constraints, atomic updates, locks.*
- **Zip/XML/JSON bombs, regex DoS.** *Size/time limits, safe parsers, linear-time regex engines.*
- **Deserializing untrusted data.** *Data-only formats, schema validation.*
- **Webhook replay and spoofing.** *Signatures, timestamps, event ID dedupe.*
- **Deploy-time breaking changes** (rename column while old code runs). *Expand/contract migrations, compatibility windows.*
- **Backups never restored.** *Scheduled restore drills with measured RTO/RPO.*
- **Single point of failure in "HA" setups** (shared disk, DNS, certificate, one engineer). *Dependency maps and game days.*
- **Alert fatigue.** *Page on symptoms; delete noisy alerts; runbooks.*
- **Cost surprises** (egress, NAT gateways, log volume, unbounded autoscale, LLM tokens). *Budgets, alerts, tagging, per-tenant metering.*
- **Vendor lock-in surprises.** *Exit plan and data export tested.*

## Frontend and experience
- Layout shift from images/fonts/ads without reserved space.
- Hydration mismatches and flash of unstyled/incorrect content.
- Hover-only functionality; tiny touch targets; fixed headers covering focused elements.
- Focus lost after route change or dialog close; focus traps without escape.
- Infinite scroll with no footer/keyboard access or lost position.
- Forms that clear input on error, validate only on submit, or block paste in password fields.
- Autoplay media and uncontrolled carousels.
- Parallax/scroll effects that cause motion sickness or ignore reduced motion.
- Client-only validation and authorization.
- Memory leaks from unremoved listeners, intervals, observers and WebGL resources.
- `100vh` on mobile; keyboard covering inputs; safe-area insets ignored.
- Text baked into images; no RTL or long-translation testing.
- Cookie banners that block content or dark-pattern consent flows.
- Over-reliance on third-party scripts that block rendering or leak data.
- Unreachable states: empty, offline, expired session, partial permissions, huge datasets.

## Product, process and AI
- Shipping features nobody asked for; measuring vanity metrics.
- Prototype data or sample media mistaken for real data (see `references/sample-and-placeholder-asset-policy.md`).
- Rewrites without migration paths; big-bang releases.
- "Done" without verification evidence; reporting untested checks as passed.
- AI features: hallucinated citations, prompt injection via retrieved content, tool over-permissioning, no eval set, silent model changes, unbounded spend, no human fallback.
- Regulated domains treated casually; legal/compliance claims without assessment.
- Documentation drift; no owner for runbooks; undocumented environment variables.
