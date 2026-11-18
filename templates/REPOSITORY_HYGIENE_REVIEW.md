# Repository Hygiene Review

- Repository:
- Branch/commit:
- Reviewer/date:

## AI-generated residue
- [ ] No irrelevant AI self-attribution or assistant disclaimers.
- [ ] No assistant-to-user narration or progress updates.
- [ ] No prompt scratchpads or unintended chat/tool transcripts.
- [ ] Comments explain intent, constraints, invariants, or hazards.
- [ ] Required attribution, licenses, and provenance are preserved.

## Git hygiene
- [ ] `.gitignore` reviewed and narrowly scoped.
- [ ] Local agent state and caches are excluded where appropriate.
- [ ] Secrets and real environment files are excluded.
- [ ] Safe environment templates remain tracked.
- [ ] Intentional agent instructions and skills remain tracked.
- [ ] Tests, docs, workflows, lockfiles, migrations, and source remain trackable.
- [ ] Already-tracked artifacts handled deliberately.
- [ ] Personal-only exclusions use `.git/info/exclude` where appropriate.

## Evidence
- `git status --short`:
- `git status --ignored --short`:
- `git diff -- .gitignore`:
- `git diff --cached --stat`:
- `git check-ignore -v` checks:
- Tests/lint/build:
- Remaining exceptions and rationale:
