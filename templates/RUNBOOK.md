# Runbook: <service or scenario>

- Owner/on-call:
- Last reviewed:
- Severity guidance:

## Symptoms
What users and alerts show:

## Quick checks (≤5 minutes)
1.
2.
3.

## Diagnosis
| Hypothesis | How to check | Result means |
|---|---|---|
| | | |

## Mitigation
Safe actions in order, with expected effect and risk:

## Rollback / recovery
Exact steps and verification:

## Escalation
Who, when, how:

## After
Communication, postmortem trigger, follow-up tasks:

## Deep guidance (v4)
**Example symptom-to-action entry:** *Symptom:* API p95 > 1 s and queue age rising. *Quick checks:* dashboard "API overview", recent deploys, database connections, error rate by route. *Hypotheses:* slow query after deploy (check slow-query log), pool exhaustion (connections vs max), downstream timeout (traces). *Mitigation:* roll back last deploy; raise pool or shed load with the feature flag; pause non-critical jobs. *Verify:* p95 under target for 15 minutes. *Escalate:* database owner if lock waits persist.
Keep runbooks short, command-level, tested during game days, and linked from the alert.
