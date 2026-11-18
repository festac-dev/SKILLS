# Existing Repository Audit Playbook

## Inspect before changing
Read project instructions, README, manifests, lockfiles, source tree, entry points, routes, schemas, migrations, tests, CI, deployment config, and recent history where available.

## Establish baseline
For a product audit, run applicable existing build, tests, lint, type checks and application smoke tests; record failures before edits. For cache cleanup or documentation-only hygiene, inspect the affected files and Git/runtime state instead of rebuilding unrelated application output.

## Audit dimensions
Correctness, architecture, security, privacy, accessibility, UX, performance, reliability, dependencies, configuration, documentation, operations, and maintainability.

## Prioritize
Fix security and data-loss risks first, then correctness and broken core journeys, then reliability and usability, then maintainability and polish.

## Change discipline
Preserve working behavior, avoid broad rewrites, add regression tests, and keep each phase runnable.

## Report
List findings, evidence, changes, tests, unresolved risks, and exact next steps. Never claim an unrun check passed.

## Repository hygiene and AI contamination prevention

### When to use
Use before committing/delivering changes or when local sessions, caches, transcripts, secrets, and assistant narration may have entered project files.

### Core principles
Remove irrelevant residue without erasing intentional project instructions or provenance. Preserve project guides, skills, documentation, tests, workflows, lockfiles, licenses, required notices and useful comments unless the current request explicitly removes a particular artifact. A mention of AI is not automatically contamination. [Repository hygiene](../references/repository-hygiene-and-ai-artifact-policy.md) owns prompt-file exclusion, cache classification and the scoped cleanup helper.

### Step-by-step procedure
1. Inspect tracked, untracked, ignored, and staged files. Classify artifacts by purpose and ownership before changing anything.
2. Review product code/docs for “As an AI,” unnecessary generation comments, copied chat, agent messages, progress narration, prompt scratchpads, and comments that merely repeat code.
3. Adapt [the ignore template](../templates/REPOSITORY_HYGIENE.gitignore) to actual local directories. Avoid broad patterns that hide required source or fixtures.
4. Inspect already tracked artifacts separately: .gitignore does not untrack them. Carry out authorized removal using explicit paths, preserve unrelated working/index changes, and check the resulting diff. If a file must remain local, distinguish removing it from the index from deleting it on disk.
5. If credentials are found, stop exposing them, rotate/revoke as appropriate, and assess history/copies. Deleting a line is not remediation.
6. Review staged content and resulting ignore behavior before committing or delivering.

### Checklist
- [ ] Intentional instructions, tests, docs, workflows, and notices remain.
- [ ] No local session, transcript, secret, cache, or build output entered the delivery unintentionally.
- [ ] Ignore rules were tested against real paths.
- [ ] Tracked artifacts were reviewed separately from ignored files.

### Common failure modes
Ignoring all Markdown hides documentation; banning “AI” deletes legitimate product text; deleting AGENTS.md removes project guidance; a broad cache pattern hides fixtures; .gitignore is mistaken for secret removal.

### Concrete examples
Read-only Git checks:
```sh
git status --short
git status --short --ignored
git ls-files -ci --exclude-standard
git diff --cached --stat
git diff --cached
```
Inspect `git check-ignore --help` before testing exact project paths. Without Git, keep an explicit before/after inventory and hashes; do not claim a staged review occurred.

### Verification
Confirm required files remain visible, unwanted local artifacts are excluded, and the delivered diff contains only intended changes. Manually review heuristic matches instead of deleting them automatically.

### Related skills
[Failure-mode gate](../quality-gates/ANTI-BLOAT-AND-ANTI-GENERIC-AI.md), [supply chain](../specialists/supply-chain-and-build-security.md), [legal notices](../specialists/legal-policy-and-regulatory-coordination.md).

## Application evidence

Preserve a baseline before edits using Git when available or a scoped file snapshot and fingerprints otherwise. Classify each finding by user impact and evidence; do not overwrite unknown work or treat historical test reports as current passes.
