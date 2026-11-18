# Specialist: Notifications and Messaging

Treat notifications as a user-controlled communication system, not a mechanism for maximizing engagement.

Define event triggers, audience, urgency, delivery channel, preferences, quiet hours, batching, deduplication, retries, expiry and auditability. Distinguish transactional/security notices from optional updates. Support unsubscribe and preference controls where applicable. Avoid duplicate, misleading, overly frequent or manipulative messages.

Never send messages externally or contact real users without authorization. Use clear, human wording and actionable destinations.

## Applied verification

Replay a notification trigger after an address or preference change and after the message expires. Assert correct audience, one intended delivery and an actionable destination; use a local sink unless sending to real recipients is authorized.
