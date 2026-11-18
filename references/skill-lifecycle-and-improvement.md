# Skill Authoring, Versioning, and Evidence-Based Improvement

## When to use
Load when adding/changing a skill, resolving overlap, deprecating guidance, or proposing a post-task improvement.

## Core principles
A skill should change a useful decision or behavior. Preserve useful existing guidance, required notices and explicit user scope. Authorized revisions may replace stale instructions. Fix demonstrated failures narrowly; do not turn every incident into a universal rule.

## Step-by-step procedure
1. Inventory existing resources and mark coverage before writing. Extend partial coverage in its owner; add a file only for a distinct missing capability.
2. Match naming, headings, tone, and frontmatter. In this toolkit, ordinary resources have no frontmatter; discoverable SKILL.md entrypoints use name and description.
3. Give each capability a trigger, load/skip rule, overlap owner, procedure, failure cases, concrete example, and verification.
4. Add 3–5 behavioral evaluation prompts and run static/routing checks. Run live cases when available; disclose when they are unverified.
5. After a task, record what worked/failed, evidence, proposed minimal change, expected effect, and regression risk. Propose edits before expanding scope beyond the authorized toolkit maintenance.
6. Version material behavior/contract changes in the project's chosen release system. Deprecate with replacement route, reason, compatibility window, and removal criteria.
7. Resolve conflicts through instruction hierarchy and current user requirements; within equal authority, keep one owner and explicit overlap rule instead of competing duplicates.

## Checklist
- [ ] The change addresses a demonstrated gap.
- [ ] Existing resources remain reachable.
- [ ] Rules do not invent permissions or blanket approval steps.
- [ ] Evaluation includes exclusions and failure cases.
- [ ] Retirement does not silently break consumers.

## Common failure modes
An ever-growing rulebook harms routing; duplicated skills disagree; wording-only tests reward repetition; anecdotes become global bans; self-improvement silently changes unrelated user configuration.

## Concrete examples
Post-task evidence: “The agent retried a timed-out mutation and created a duplicate. Add reconciliation-before-retry to the owning tool contract; add a timeout-after-commit case.” Do not respond by banning all retries.

Toolkit checks: `python scripts/toolkit.py validate` and `python scripts/toolkit.py dry-run`.

## Verification
Compare baseline and changed behavior on the triggering case and a counterexample where the old behavior was correct. Record static checks separately from live behavioral results.

## Related skills
[Skill evaluations](../playbooks/SKILL_EVALUATION_PLAYBOOK.md), [routing](../orchestrator/PROJECT_ROUTING.md), [context](agent-context-and-handoffs.md).

## Application evidence

Treat the merge baseline as historical provenance, not a permanent ban on authorized edits. Review all resources during a library upgrade, preserve required notices, replace stale guidance in its owner, and validate links, routing and meaningful behavior. Use audit for fingerprints and search for uncovered domains; do not claim fresh behavioral passes from static validation.

For an archive import, inspect members before writing: reject traversal, absolute paths, duplicate entries and links that escape the destination. Compare existing files before overwriting; identical files already satisfy extraction and do not need another nested skill folder. Merge differing guidance into its existing owner, preserve requested entrypoints, refresh discovery and validate. Importing a skill into the toolkit does not require copying it or its source ZIP into every application repository.
