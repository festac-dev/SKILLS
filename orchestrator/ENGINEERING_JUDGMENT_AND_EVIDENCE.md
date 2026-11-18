# Engineering Judgment and Evidence

Professional work closes the distance between promised outcomes and actual behavior. Increase depth where failure matters; keep ceremony proportional to scope.

| Scope | Useful minimum evidence | Increase depth when |
|---|---|---|
| Copy/style correction | Inspect output and relevant accessibility/links | Meaning, navigation, or critical controls change |
| Existing product feature | Acceptance behavior and relevant regressions | Permissions, side effects, concurrency, or compatibility change |
| New application/service | End-to-end journey, boundary tests, deployment instructions | Public exposure, sensitive data, or operating commitments apply |
| Migration/production change | Representative rehearsal, invariants, stop conditions, recovery | Irreversible transformations or broad blast radius apply |
| Prototype | Demonstrated hypothesis, explicit mocks and limits | Users could mistake it for production |

## Improve decisions

Find the hardest uncertainty early: permission model, hardware capability, transaction boundary, integration limit, or performance constraint. Build the smallest experiment that resolves it. Do not add layers to compensate for an untested premise.

Complete the real path: useful input → validated action → durable result → understandable feedback → recovery. Optimize for coherent behavior, readable ownership, predictable failure, and maintainable changes. Polish matters when it improves the experience; complexity has to earn its place.

## Evidence ledger

For each material claim record requirement, build/artifact, environment, command/procedure, expected outcome, actual result, and limitation. Link evidence rather than copying logs into several documents. Redact sensitive output and follow project retention/access rules.

- **Passed:** the named check ran and met its criteria.
- **Failed:** a check ran and contradicted the criteria.
- **Unverified:** adequate execution evidence is missing, including unavailable devices/environments.
- **Not applicable:** an explicit reason ties exclusion to scope.

An accepted risk is a decision about a gap, not a passing test. Record owner, impact, mitigation, expiry, and authority when an exception is permitted. Claims must not exceed evidence.

## Configuration and external account state

Answer an enabled/disabled or readiness question from the layer that owns the state:

| Evidence inspected | Establishes | Does not establish |
|---|---|---|
| Source code and tests | A capability is implemented or its local contract is tested | The running deployment uses it |
| Effective process/deployment configuration | Which mode and endpoint that environment selected | Provider-side consent, entitlement or activation |
| Read-only provider setting for the correct account/project | The observed setting in that account at that time | A successful end-to-end operation |
| Actual provider response and resulting record | The particular live operation observed | Other environments, accounts or future reliability |

Source defaults may be overridden. A missing key in one shell does not prove it is missing from a deployed secret store. Provider documentation can explain a default or where to look, but cannot prove the current account setting. Local receipt/audit logging does not establish a provider's data-sharing opt-in. A mock receipt is not evidence that a payment settled.

Distinguish **enabled**, **disabled**, **not configured by this work**, and **unverified**. Absence of evidence is not evidence that a switch is off. State what was configured, what remains unobserved and the smallest useful read-only check in one concise answer. Do not repeatedly answer only “unknown” when the user needs the reason or the next action. For a mandatory Yes/No field, do not guess to finish the form; identify the owning setting and check it when access is available.

Inspect configuration without printing secrets, whole environment dumps, raw authentication headers or unrestricted account exports. A request to describe or verify data collection is not an instruction to enable it. Apply existing authorization to any requested setting change and verify the resulting state separately.

## Finish criteria

Required behavior works; applicable blockers are resolved; instructions match the implementation; verification is recorded honestly; limitations have a clear effect on use. This toolkit makes no claim that a model becomes equivalent or superior to another. Any comparison needs representative tasks and a disclosed evaluation method.

## Repository and docs-only reviews

Use when evaluating a README, submission or pasted critique without a verified runtime result. State what was inspected and what was inaccessible. Treat the supplied review as feedback to check against current artifacts, not as an authority on functionality or eligibility.

Separate implemented capability, documented procedure, observed test output and independent validation. Missing live evidence leaves the live path unverified; it does not prove it fails. Test files and CI configuration show available checks, not that those checks passed. A self-authored report is useful when tied to inspectable results, but is not independent corroboration by itself.

Stars, a short Git history, an empty About field and AI-assisted authorship do not establish correctness or failure. Check current repository facts before quoting them. Never manufacture stars, user reports, issue activity or incremental history to look validated.

Check the official criteria and publication/submission timestamps before concluding a project is late or ineligible. Reviewing it after the deadline does not establish a late submission. Local-only software can be valid when the rules allow it; an inaccessible or misspelled event URL does not establish the rules. Do not invent a grade, eligibility decision or promised future score from missing evidence.

## Adversarial self-review procedure

### When to use
Use after implementing a material change and before a readiness claim. Scale depth to user impact, data sensitivity, and reversibility.

### Core principles
Attempt to falsify the claim that the task is complete. Separate verified facts, inference with supporting evidence, and unknowns. Confidence does not substitute for tests.

### Step-by-step procedure
1. Restate acceptance criteria and identify the highest-impact failure.
2. Trace empty, malformed, unauthorized, concurrent, duplicate, interrupted, and overloaded inputs where relevant.
3. Inspect old clients, partial rollout, stale caches, real data volumes, dependency failure, and rollback.
4. Try to break your own assumptions with a negative case or independent oracle.
5. Fix causal defects and rerun affected checks. State residual uncertainty and its practical effect.

### Checklist
- [ ] No check mocks the behavior being claimed.
- [ ] No exception is swallowed to obtain success.
- [ ] Reversal or recovery is concrete.
- [ ] Evidence identifies build and environment.

### Common failure modes
Reviewing only the happy path; checking the source instead of runtime; treating “no exception” as success; trusting an SDK method remembered from another version; adding architecture instead of resolving a requirement.

### Concrete examples
For a “saved” indicator, interrupt the network after the server commit but before the response. The client must reconcile without duplicate writes or falsely declaring failure irreversible. Inspect `git diff --check` when Git is available, then run the actual journey; the diff check alone proves neither behavior nor readiness.

### Verification
Record attempted counterexamples, observed outcomes, fixes, and remaining gaps. Never turn an unexecuted scenario into a passing check.

### Related skills
[Test strategy](../specialists/quality-engineering-and-test-strategy.md), [global rules](GLOBAL_RULES.md), [gate protocol](../quality-gates/GATE_PROTOCOL.md).

## Current-task application

Reusing evidence requires an unchanged relevant artifact, environment and assumption. Probe time-sensitive claims such as running preview links again. A workflow tested with fixtures establishes that UI behavior, while real-provider access remains a separate claim.
