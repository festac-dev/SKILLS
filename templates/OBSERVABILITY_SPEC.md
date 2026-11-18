# Observability Specification

## Critical journeys and signals
| Journey/service | Signal | Definition | Alert condition | Owner |
|---|---|---|---|---|
| | | | | |

## Telemetry rules
- Use structured logs with correlation/request IDs.
- Do not log passwords, tokens, payment credentials, or unnecessary personal data.
- Use metrics for aggregate behavior and traces for cross-service diagnosis.
- Define sampling, retention, access, and redaction.
- Ensure alerts are actionable and have an owner/runbook.

## Operational readiness
Document dashboards, alert routes, dependency health, known failure modes, and how to verify recovery.

## Execution record

Keep only fields relevant to this artifact.

- Injected or observed failure and matching trace/alert:
- Sensitive fields inspected in actual telemetry:
- Signal proving recovery of the user operation:
