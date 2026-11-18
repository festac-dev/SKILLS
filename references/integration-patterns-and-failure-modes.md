# Integration Patterns and Failure Modes

## Integration approaches
Synchronous APIs, asynchronous queues, webhooks, polling, file exchange, embedded SDKs, identity federation, and event streams.

## Failure modes
Timeout, rate limit, expired credential, schema drift, duplicate delivery, out-of-order event, partial response, provider outage, quota exhaustion, and silent data mismatch.

## Controls
Timeouts, bounded retries, idempotency, signature verification, replay protection, dead-letter queues, reconciliation, circuit breakers, alerting, and manual repair tools.

## Ownership
Every integration needs an owner, data classification, permissions, vendor contact, cost visibility, change monitoring, and exit/export strategy.

## Application evidence

For each timeout, distinguish no request sent, uncertain commit and known rejection. Retry only with a bounded reconciliation strategy; surface an unavailable provider honestly and identify fixture-backed demonstrations separately.

For ledger-backed workflows, HTTP liveness does not establish synchronizer readiness or transaction confirmation. Verify identity rights, visible active records and a completed command against the actual provider. Allow command confirmation a suitable timeout distinct from ordinary reads; an interrupted confirmation can still commit. Preserve the command identifier for reconciliation, keep pending feedback visible and do not label an uncertain commit as a rejected action or blindly submit it with a new identifier.
