# Specialist: Observability and Incident Response

Instrument only what is useful to operate the product and protect users.

Define structured logs, metrics, traces, correlation IDs, service-level indicators, alerts, dashboards, runbooks and incident ownership. Redact secrets and sensitive content. Set retention and access controls for telemetry. Avoid high-cardinality labels and excessive event collection.

For incidents, preserve evidence, communicate impact accurately, provide mitigation and recovery steps, and record follow-up actions. Do not claim an incident is resolved until the relevant service and user journeys are verified.

## Applied verification

Trigger a representative failure in an authorized environment and follow its correlation ID from the user action to the dependency. Confirm the alert identifies impact and recovery, and inspect captured fields for accidental sensitive data.

## Operable signals

Define availability and latency from user-visible operations, including failure and degradation semantics. Use percentiles and error budgets where they support decisions; averages can hide tail failures. Track saturation at the constrained resource: database pool wait, queue age, worker concurrency, disk, connection limits or provider quota.

Propagate correlation and causation IDs across synchronous calls and jobs. Set sampling, cardinality, redaction and retention deliberately. Keep identifiers that can explode metric cardinality in traces or logs where appropriate. Confirm that errors remain diagnosable without collecting secrets or full private payloads.

An alert needs a user impact, actionable condition, owner and a useful runbook. Exercise alert firing and recovery on a permitted representative fault; a dashboard screenshot is not evidence of detection. During incidents, distinguish mitigation from root-cause repair, preserve a timeline, and verify the affected operation before declaring recovery. Avoid speculative root causes and perform disruptive diagnostics only within the authorized incident scope.

## Signal selection and alert ownership

Use request rate/errors/duration for service behavior and utilization/saturation/errors for resources. Correlate traces through jobs and external calls; bound metric-cardinality and retention costs. Monitor critical journeys from outside the failure domain, and define symptom or error-budget alerts with an owner and useful runbook. Resource dashboards alone do not establish user recovery. Consult the [signal catalogue](../references/observability-signal-catalogue.md), [SLO specification](../templates/SLO_AND_ALERT_SPEC.md) and [runbook](../templates/RUNBOOK.md).
