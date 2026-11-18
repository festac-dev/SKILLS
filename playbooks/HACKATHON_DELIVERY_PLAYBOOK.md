# Hackathon Delivery Playbook

## When to use
Load for a time-boxed competition, demo, prototype pitch, or submission deadline. Do not apply prototype shortcuts to an existing production system without explicit scope.

## Core principles
Deliver one truthful end-to-end demonstration of the core value. Cut secondary features before correctness of the demonstrated path. Label seeded data, mocks, and unavailable integrations visibly.

## Step-by-step procedure
1. Read judging criteria, deadline/time zone, team rules, allowed assets, licensing, disclosure, deployment, video, and submission requirements.
2. Define a one-sentence user problem and a 90-second core journey. Choose one vertical slice with a measurable success condition.
3. Allocate a default first 20% of remaining time to risk discovery and skeleton, 50% to the working slice, 20% to testing/demo resilience, and 10% to submission. Adjust explicitly to the actual deadline.
4. Build the demo path in dependency order: data/behavior, usable interaction, error recovery, then visual polish. Establish a working demo before optional integrations.
5. Freeze risky additions before the final verification window. Keep a local fallback demo and recorded evidence without pretending it is live.
6. Rehearse the pitch: problem, intended user, demonstration, technical distinction, evidence, limitations, and next step.
7. Validate links, permissions, fresh-clone setup, video duration, repository access, attribution, and submission confirmation.

## Checklist
- [ ] The demo demonstrates a real user outcome.
- [ ] Sample data and mocks are labeled.
- [ ] Offline/provider-failure behavior is rehearsed.
- [ ] Submission assets meet the actual rules and deadline.
- [ ] Secrets and local transcripts are excluded.

## Common failure modes
Building many half-finished screens; adding an untested provider near deadline; using fabricated traction; demoing only on a developer's warm session; forgetting access permissions or time-zone conversion.

## Concrete examples
A useful scope cut for a scheduling demo is “one calendar, one conflict rule, one booking and cancellation,” deferring team administration and billing. A pitch line can state: “This demo prevents double booking for one shared room; the conflict is checked by the server. Multi-room scheduling is outside this prototype.”

Run the project's documented setup/test commands from a fresh disposable copy; inspect `git status --short` before submission.

## Verification
Rehearse from a clean session, time the demo, test the failure fallback, and open every submission link with the intended access level. Record submission confirmation only after it actually occurs.

## Submission answers and repository contents

Write the project description from implemented behavior: what it does, who needs it, the problem and the actual flow. Distinguish a supported integration from a live operation that was verified. Use [configuration evidence](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md#configuration-and-external-account-state) for form fields about enabled services, collection or account settings; a local log does not answer a provider-consent question.

Use [repository hygiene](../references/repository-hygiene-and-ai-artifact-policy.md) before Git handoff. Exclude development prompt dumps, transcripts, caches, render work and unrelated downloaded packages. Keep code, required assets, tests, lockfiles, configuration examples, licenses and useful project documentation. Check the actual submission's logo format, video duration/resolution/size and access requirements; a sample prompt's settings do not override the current form. A local preview URL is not a public submission URL.

Apply [public README guidance](../specialists/technical-documentation.md#documentation-audience-and-evidence) to the published product description. Keep personal submission reminders and speculative judging advice in private working notes. Retain required reused-code, dependency and team/project disclosures in the locations the rules specify. If a baseline and extension diff are required, verify that judges can open both; citing an unavailable hash or telling the owner to publish the diff does not supply it. Preserve real chronology rather than inventing or rewriting history to suggest timely development.

Internal delivery reports, verification summaries written for the owner, submission checklists and untested factual assertions stay outside the application repository and are never included in a hackathon push. Check tracked content and links before publication. Keep the README useful for trying the product, with concise supported behavior and actual evidence; required public disclosures remain public.

Use [docs-only review guidance](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md#repository-and-docs-only-reviews) before repeating a critique's eligibility or score claims. Verify actual publication/submission evidence against the applicable deadline. A past deadline, simulation demo or absent hosted URL alone does not determine eligibility.

## Related skills
[Product strategy](../specialists/product-strategy.md), [feature selection](../orchestrator/FEATURE_DECISION_FRAMEWORK.md), [release workflow](../references/release-and-change-management.md).

## Application evidence

Rehearse the complete demonstration from a fresh session with the available network and credentials. Keep a truthful fixture-backed recovery path where authorized, and state which operations are live, simulated or unavailable.
