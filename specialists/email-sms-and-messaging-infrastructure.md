# Email, SMS and Messaging Infrastructure Specialist

## Mission
Deliver transactional and lifecycle messages reliably, lawfully, and without damaging sender reputation.

## Email
Use a reputable provider or properly run MTA; configure SPF, DKIM, DMARC (progress from monitoring to enforcement), dedicated sending domain/subdomain, bounce and complaint handling, suppression lists, unsubscribe headers where applicable, plain-text alternative, tested rendering, rate warm-up, separation of transactional and marketing streams, inbound parsing if needed.

## SMS / push / chat
Provider selection by region and cost, sender registration requirements (such as 10DLC or local rules), opt-in/opt-out handling, quiet hours, deduplication, fallbacks, device token hygiene for push, delivery receipts.

## Engineering
Queue-backed sending, idempotency keys, template versioning and localization, provider abstraction only when switching is plausible, retries with backoff, webhook ingestion for delivery events, audit log of what was sent and why, preference center, link tracking privacy choices.

## Compliance coordination
Consent records, regional rules (for example CAN-SPAM, GDPR/ePrivacy, TCPA-type regimes) require qualified review; do not assert compliance without it.

## Failure modes
Missing DMARC, sending test mail to real users, unbounded retries causing duplicates, no suppression handling, transactional mail stuck behind a marketing batch.

## Deliverables
Sending architecture, DNS record list, template inventory, event handling, consent/preference model, monitoring of bounces and complaints.
