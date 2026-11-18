# Anti-Bloat and Anti-Generic-AI Gate

Reject or revise work when it contains:
- features with no identified user problem;
- redundant navigation, cards, dashboards or settings;
- decorative 3D, animation or effects without purpose;
- random gradients, blobs, orbs, particles or glowing objects used as filler;
- a forced logo, palette, font, theme, brand voice or design trend;
- generic template layouts that ignore the product's information architecture;
- robotic copy, empty marketing claims or repetitive headings;
- fake metrics, testimonials, customer logos or invented research;
- nonfunctional buttons, misleading disabled states or dead links;
- unnecessary dependencies, abstractions or architecture rewrites.

Aesthetic experimentation is allowed when requested or justified. The gate is against automatic, unconsidered use—not against any particular visual style.

## Agent failure modes and countermeasures

### When to use
Use during self-review when apparent progress may conceal scope growth, false evidence, or incomplete behavior.

### Core principles
Measure delivered user outcomes. Preserve intentional project instructions and attribution while removing irrelevant assistant narration.

### Step-by-step procedure
1. Compare the diff with the requested acceptance criteria.
2. Trace every fallback and error path to visible behavior and telemetry.
3. Challenge tests with a deliberately wrong result in an isolated fixture.
4. Inspect added abstractions/dependencies for actual callers and ownership.
5. Remove only clearly unnecessary additions introduced by the task; preserve user work.

### Checklist
- [ ] No silent fallback converts a failure into fake success.
- [ ] No test replaces the important implementation with its expected answer.
- [ ] No invented metrics, files, APIs, or verification claims remain.
- [ ] No unrelated feature is justified solely by catalogue coverage.

### Common failure modes
| Failure | Countermeasure |
|---|---|
| Overengineering | Deliver one real slice before generalizing |
| Scope creep | Link each addition to an acceptance criterion |
| Silent fallback | Surface degraded behavior and preserve the cause |
| Fake tests | Verify a meaningful negative case fails |
| Symptom patch | Reproduce and fix the causal boundary |
| Tool hallucination | Inspect installed help/types or versioned docs |
| Retry amplification | Bound attempts and reconcile side effects |
| Context drift | Reconcile checkpoint facts against current files |

### Concrete examples
A failed provider call must not return sample production data as though it were live. If a demo fallback is authorized, label it visibly and keep the failure available to operators. Read-only hygiene checks: `git diff --check` and `git diff --cached --stat`.

### Verification
Record the failure scenarios attempted, real outcomes, and unresolved gaps. A style cleanup does not establish behavioral correctness.

### Related skills
[Repository audit](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md), [engineering judgment](../orchestrator/ENGINEERING_JUDGMENT_AND_EVIDENCE.md).

## Application evidence

Requested brand work or moving graphics is part of the brief. Evaluate whether the delivered identity and motion meet that request; do not reject them through a blanket preference for static or neutral UI. Remove redundant scaffolding labels and verify real destinations.

## Code and content review

Remove added comments that narrate obvious syntax, abandoned plans, artificial section banners, duplicate documentation and claims about the assistant's effort. Keep comments that explain a non-obvious invariant, compatibility constraint, algorithmic trade-off, license or operational hazard. Do not delete existing project guidance or attribution under the label “AI slop.”

Replace empty adjectives and repetitive marketing sections with concrete user actions, evidence and necessary explanation. A request for broad capability expands this library's useful coverage; it does not make every feature, dependency, dashboard or document mandatory in each project.
