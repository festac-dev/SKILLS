# Skill Evaluation Playbook

## When to use
Use after adding a skill, changing routing, correcting an observed failure, or changing a rule that affects autonomy, permissions, or delivery.

## Core principles
Evaluate decisions and outcomes, not keyword repetition. Separate static validation, routing simulation, and actual behavioral execution. Static checks cannot prove an agent follows a skill.

## Step-by-step procedure
1. Define 3–5 prompts per new skill: a normal task, a boundary/failure task, and an exclusion or permission case. Use [the evaluation cases](../evals/SKILL_EVALS.json).
2. Record expected loaded resources, observable actions, prohibited effects, evidence, and failure signs before running a candidate.
3. Run cases in disposable fixtures. Keep tools and external actions scoped; use real local behavior for correctness, and mock only unsafe external boundaries.
4. Compare baseline and candidate using the same fixtures and budget. Give an independent reviewer the task and artifacts without the preferred conclusion when authorized.
5. Require no observed destructive unauthorized action or fabricated verification. Record other failures by severity and affected task class.
6. Retain held-out cases and version the evaluation set. Proposed skill edits need an observed failure and a targeted counterexample.

## Checklist
- [ ] Prompts test activation and non-activation.
- [ ] The unit under test is the agent's behavior, not a prewritten answer.
- [ ] Routing dry-runs are labeled simulations.
- [ ] Permission cases assert absence of side effects.
- [ ] Cost, latency, and environment limitations are disclosed.

## Common failure modes
Testing only happy paths rewards verbosity; supplying the correct answer biases review; editing eval cases until they pass hides regressions; a lint pass says nothing about live tool use.

## Concrete examples
Static validation in this toolkit: `python scripts/toolkit.py validate`. Routing examples: `python scripts/toolkit.py dry-run`. These execute no product deployment, model call, or security scan. For a behavioral case, ask an agent to fix a failing parser in a disposable repository and check that the real regression fails before and passes after the fix.

## Verification
Report static results, routing results, and live behavioral results separately. A case is unverified until it actually ran with an observable trace and checked artifacts.

## Related skills
[AI evaluation](../specialists/ai-evaluation-and-governance.md), [skill lifecycle](../references/skill-lifecycle-and-improvement.md), [gate protocol](../quality-gates/GATE_PROTOCOL.md).

## Application evidence

Run toolkit validation, routing cases and scenario execution as distinct layers. Keep held-out behavior cases unchanged while fixing a routing defect. A recorded pass needs an execution artifact; the local validator cannot establish live model behavior.
