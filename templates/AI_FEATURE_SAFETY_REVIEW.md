# AI Feature Safety and Quality Review

- Feature and user goal:
- Trigger and expected output:
- Model/provider:
- Data sent to provider:
- User disclosure and retention:

## Trust boundaries
- Is model output treated as untrusted?
- Is structured output validated?
- Can output trigger external actions?
- Is human confirmation required?
- Are permissions enforced independently of model output?
- Can users inspect, edit, reject or undo suggestions?

## Reliability
- Timeout/rate-limit handling:
- Retry and duplicate-request behavior:
- Malformed output handling:
- Provider outage fallback:
- Evaluation and regression tests:

## Privacy and cost
- Data minimization:
- Credential handling:
- Usage limits and cost visibility:
- Abuse prevention:
- Deletion and retention:

## Acceptance
- [ ] Generated content is identified.
- [ ] Consequential changes receive appropriate review.
- [ ] Output is validated before use.
- [ ] Failure states are safe and understandable.
- [ ] Credentials remain server-side.
- [ ] Disclosures match actual data flows.
- [ ] Quality is evaluated on representative cases.

## Execution record

Keep only fields relevant to this artifact.

- Untrusted input source and trusted enforcement boundary:
- Timeout-after-commit behavior and reconciliation evidence:
- Observed denial or escalation result:
