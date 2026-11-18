# Multi-Agent Coordination Specialist

## When to use
Load only when delegation is available and authorized and the work has independent subtasks or benefits from an independent review. Reading this resource does not authorize spawning agents.

## Core principles
Default to one agent for tightly coupled work. Delegate bounded outcomes with acceptance criteria, an owner, a write boundary, and a deadline. The lead remains accountable for integration and verification.

## Step-by-step procedure
1. Identify independent work and the dependency graph. Keep sequential decisions with the responsible owner.
2. Give each contributor a minimal brief: task, permitted files/tools, relevant facts, expected output, verification, budget, and stop conditions.
3. Assign disjoint edit ownership or isolated checkouts. Shared filesystem access does not imply safe concurrent edits.
4. Require reports distinguishing observed evidence, assumptions, changes, and unverified items.
5. Integrate in dependency order, inspect diffs, resolve contract conflicts, and run tests against the combined result.
6. Stop or rescope stalled work when its budget or dependency boundary is reached; do not spawn recursive agents to hide a blocker.

## Checklist
- [ ] Task authorization permits delegation.
- [ ] No two writers own the same file at the same time.
- [ ] Shared contracts have one decision owner.
- [ ] Independent review is not told the desired conclusion.

## Common failure modes
Duplicated work wastes tokens; stale briefs cause incompatible changes; parallel database migrations race; one passing branch test does not prove the merged result; agents can reinforce the same mistaken premise.

## Concrete examples
For an API plus documentation change, assign the API implementation to one writer and a read-only contract review to another. The reviewer reports “PUT /orders can update another tenant's order with a guessed ID,” including reproducer and expected denial. The lead fixes and retests the combined code before reporting success.

Read-only integration checks in a Git project: `git diff --stat`, `git diff --check`, `git status --short`.

## Verification
Compare actual output to each assignment, inspect the merged diff, and run the shared acceptance checks. Record delegated cost and unresolved ownership rather than claiming parallelism itself improved quality.

## Related skills
[Context and handoffs](../references/agent-context-and-handoffs.md), [code review](technical-debt-and-modernization.md), [skill evaluations](../playbooks/SKILL_EVALUATION_PLAYBOOK.md).

## Applied verification

Before integration, compare each contributor’s claimed files and evidence with the actual combined tree. Cancel duplicate writers and keep one owner for shared contracts; contributor summaries cannot substitute for running the integrated acceptance checks.
