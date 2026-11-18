# Specialist: Billing and Entitlements

Add billing only when the business model requires paid access or metered usage.

Model plans, entitlements, trials, seats, quotas, usage events, invoices, payment status, refunds, cancellations and grace periods according to the actual provider and legal context. Treat payment webhooks as untrusted until signature and replay checks pass. Make event processing idempotent and reconcile provider state.

Do not store raw payment credentials. Do not invent prices, plans, tax treatment or financial promises. Clearly distinguish billing state from access entitlement and provide a recovery path for failed payments.

## Applied verification

Replay an authenticated provider event, deliver an older event after a newer one, and lose a webhook response after commit. Assert one financial effect and the correct entitlement state, including the provider’s documented grace and cancellation semantics.

## Billing state and reconciliation

Keep pricing, provider billing state and application entitlements distinct. Specify trials, grace periods, pause/cancellation, proration, metered-event deduplication and the effective time of plan changes. Provider webhooks need signature verification and duplicate/out-of-order handling; reconcile with authoritative provider records when delivery is missed. Hosted payment fields may reduce exposure, but do not by themselves prove PCI scope or compliance. Test provider clocks, failed renewals, tax/currency rounding and entitlement transitions.
