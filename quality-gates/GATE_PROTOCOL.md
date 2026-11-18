# Evidence-Based Gate Protocol

Select gates by changed behavior and release risk. Give each requirement a passed, failed, unverified, or not-applicable result. Use [engineering judgment](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md) for the evidence standard.

| Criterion | Applicable? | Evidence/build/environment | Result | Impact | Owner/action |
|---|---|---|---|---|---|
| Project-specific requirement | | | | | |

## Decision rules

- A document's existence does not prove its behavioral criteria.
- Block release when a critical journey breaks, protected data crosses a trust boundary, authoritative data can be corrupted, or required recovery cannot be performed.
- Unverified critical requirements block readiness claims. Name the missing check and environment.
- A lower-risk exception requires the appropriate owner's explicit acceptance, mitigation, review date, and bounded scope. Preserve the failed/unverified result.
- “Not applicable” needs a scope-based reason; lack of time is not a reason.
- Do not apply every gate to every patch. Test affected behavior and realistic regression boundaries.

Gate decisions and execution permission are distinct: passing checks does not authorize deployment, and deployment authorization does not make failed checks pass.

## Gate application procedure

### When to use
Use to decide readiness for the changed behavior, not to impose every gate on every patch.

### Core principles
Evidence and execution authorization are distinct. Accepted risk does not become a passing test.

### Step-by-step procedure
1. Select relevant criteria and record applicability.
2. Run the actual checks and link build/environment evidence.
3. Record failed or unverified requirements and their impact.
4. Resolve blockers or record a permitted, explicit exception with owner and expiry.

### Checklist
- [ ] Results distinguish passed, failed, unverified, and not applicable.
- [ ] Critical gaps block broad readiness claims.
- [ ] Exceptions preserve their original result and evidence.

### Common failure modes
Copying a previous release's pass; treating a missing environment as not applicable; confusing approval to deploy with a passing check.

### Concrete examples
“Restore procedure documented; restore drill unverified because no isolated database was available” is an accurate result. “Backups verified” is not. Run `python scripts/toolkit.py validate` only to validate this toolkit's static structure.

### Verification
A reviewer can trace each material claim to a real check and understand the remaining release limitations.

### Related skills
[Definition of done](DEFINITION_OF_DONE.md), [evidence report](../templates/RELEASE_AND_EVIDENCE_REPORT.md), [skill evaluations](../playbooks/SKILL_EVALUATION_PLAYBOOK.md).

## Application evidence

Invalidate a previous pass when the relevant code, artifact, configuration or dataset changes. Reuse evidence only where its applicability remains defensible; record a current probe for claims that a service is running.
