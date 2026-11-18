# Release and Change Management

## Release dimensions
- Product scope and user-visible changes.
- Data/schema compatibility and migration.
- API, SDK, webhook, and integration compatibility.
- Security, privacy, accessibility, and performance impact.
- Support readiness, documentation, and incident ownership.
- Rollback or forward-fix strategy.

## Safe delivery patterns
Use feature flags for controlled exposure when appropriate. Separate deployment from activation. Prefer progressive rollout for high-impact changes. Monitor guardrail metrics and define stop conditions before release.

## Change record
Capture the change, rationale, affected users, dependencies, migration, validation evidence, owner, release window, rollback, and follow-up actions.

## Avoid
Unreviewed production migrations, silent breaking changes, unbounded rollout, and claims of successful release without deployment evidence.

## Git, PRs, versioning, and reversible delivery

### When to use
Use for committing an implementation, reviewing a PR, versioning a public contract, or releasing a deployable artifact. A local edit does not imply permission to publish.

### Core principles
Keep commits reviewable and preserve user changes. Semver describes a declared public API: incompatible changes are major, compatible functionality minor, compatible fixes patch. Clarify pre-1.0 policy rather than assuming stable compatibility. A code rollback cannot reverse every data change.

### Step-by-step procedure
1. Inspect branch, status, diff, tracked artifacts, and repository contribution rules.
2. Separate unrelated work. Stage explicit reviewed paths; inspect the staged diff before committing.
3. Describe the actual problem, changed behavior, compatibility impact, and checks run in the PR.
4. Maintain a user-facing changelog when the project uses one. Include migration guidance for changed contracts.
5. Build once and promote the same artifact. Use staged exposure with explicit success signals and stop thresholds.
6. Keep database changes additive during the rollback window. Test a rollback or forward-fix rehearsal before destructive contraction.

### Checklist
- [ ] Staged changes match the requested scope.
- [ ] Release version follows the project's public-contract policy.
- [ ] Flags have owners and removal dates.
- [ ] Canary thresholds use a baseline and a minimum observation window.
- [ ] Backups and rollback instructions match the actual data transformation.

### Common failure modes
Blind `git add .` includes secrets; force-push rewrites others' work; changelogs merely list commits; a canary without traffic proves little; rolling back binaries against incompatible data can worsen an outage.

### Concrete examples
Read-only review sequence: `git status --short`, `git diff --check`, `git diff --cached --stat`, `git diff --cached`. For a public API change from an optional to a required field, treat compatibility as broken even if internal tests pass. A feature flag should disable the new read path while old and new schema readers remain compatible.

### Verification
Record artifact digest, revision, release decision, migration rehearsal, rollback result, and observed post-release signals. Publication and deployment are separate actions requiring applicable authorization.

### Related skills
[Release plan](../templates/RELEASE_PLAN_AND_ROLLBACK.md), [repository audit](../playbooks/EXISTING_REPOSITORY_AUDIT_PLAYBOOK.md), [migration](../specialists/migration-and-compatibility.md).

## Application evidence

Bind checks to the exact artifact being released and rerun affected checks after a material change. Preview links must be probed immediately before handoff; publishing, deployment and production mutations stay within the user’s existing authorization.
