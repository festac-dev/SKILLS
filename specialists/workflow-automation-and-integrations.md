# Specialist: Workflow Automation and Integrations

Model triggers, conditions, actions, approvals, retries, timeouts, secrets, rate limits and execution history explicitly.

Use least-privilege credentials and scoped permissions. Validate webhook signatures where supported, prevent replay, deduplicate deliveries and protect against SSRF and untrusted callback URLs. Make side effects idempotent where possible. Include cancellation, pause, dry-run and manual approval when consequences warrant them.

Treat third-party systems as unreliable dependencies. Provide clear status, retry controls and reconciliation rather than claiming success from a queued request.

## Applied verification

Interrupt a workflow after an external effect but before acknowledgement, then resume it. Reconcile the external operation before retrying, retain a durable state transition and expose partial completion truthfully.
