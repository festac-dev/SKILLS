# Incident Response Playbook

## Prepare
Define severity, incident commander, technical lead, communications owner, escalation, access, and runbooks.

## Detect and assess
Confirm signal, establish scope, identify affected users/data, preserve evidence, and distinguish facts from hypotheses.

## Contain
Use the least harmful effective action. Protect data, stop ongoing abuse, and avoid destructive changes without understanding consequences.

## Recover
Restore service, validate data integrity, monitor for recurrence, and communicate status honestly.

## Learn
Publish a blameless timeline, identify contributing system conditions, assign corrective actions, and verify completion.

## Root-cause debugging and bounded recovery

### When to use
Use for production incidents or reproducible defects whose cause is unknown. Urgent containment may precede diagnosis; label a mitigation honestly and retain the root-cause work.

### Core principles
Preserve evidence and build competing hypotheses. Change one causal factor at a time. Do not silence errors, broadly disable checks, or add retries to an unknown failure. Confirm destructive recovery scope and honor authorization already given.

### Step-by-step procedure
1. Capture expected/actual behavior, first bad time or revision, affected users, request IDs, and recent changes without collecting secrets.
2. Reproduce with the smallest realistic input. Separate client, network, service, database, and dependency failure.
3. Write hypotheses with an observation that would falsify each. Inspect the earliest causal error, not only the last stack frame.
4. Select reversible containment with an owner, stop condition, and verification. Preserve original data before repair.
5. Fix the causal boundary; add a regression that exercises real behavior. Retest related failure paths.
6. Validate recovery through user outcomes and data invariants, then record contributing conditions and follow-up ownership.

### Checklist
- [ ] Scope, timeline, hypothesis, evidence, mitigation, and fix are distinct.
- [ ] Logs are redacted; clocks/time zones are recorded.
- [ ] No catch-and-ignore or silent fallback hides the defect.
- [ ] Recovery checks include persisted state and queue backlog.

### Common failure modes
Restarting destroys evidence; checking only a health endpoint misses corrupt data; retrying non-idempotent work duplicates effects; a successful response can conceal an unsuccessful commit.

### Concrete examples
Read-only Git triage: `git status --short`, `git log -10 --oneline`, `git diff --stat`. For a confirmed local regression, run `git bisect --help` before using bisect in an isolated clean checkout; do not switch revisions over user changes. A timeout hypothesis is falsified if tracing shows the request never entered the dependency.

### Verification
The original reproducer passes, the regression would detect recurrence, customer impact has stopped, and data reconciliation agrees with source-of-truth records. An emergency mitigation alone does not close the root-cause finding.

### Related skills
[Performance investigation](PERFORMANCE_INVESTIGATION_PLAYBOOK.md), [incident report](../templates/INCIDENT_POSTMORTEM.md), [security review](../specialists/security-architecture-and-red-teaming.md).

## Application evidence

Verify the affected user journey after mitigation and confirm its failure signal has recovered. Record the first causal divergence and unresolved data reconciliation; process uptime alone does not close the incident.
