---
name: agentic-awesome-github-actions-templates-116f572f
description: Production-ready GitHub Actions workflow patterns for testing, building,
  and deploying applications.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# GitHub Actions Workflow Patterns

## When to Use

Implement testing, matrix builds, artifact preparation or an explicitly authorized deployment workflow for an existing repository.

## Inputs

Inspect the repository's actual scripts, lockfile, supported runtimes, required check names and release policy. Read `resources/implementation-playbook.md` and `references/common-workflows.md` before choosing job boundaries.

## Test Workflow

This Node example assumes the target repository declares `npm test` and supports Node 22. Adapt the runtime and command to the actual project. The pinned action revisions are explicit review inputs; verify them before adopting or updating the template.

```yaml
name: Test
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@93cb6efe18208431cddfb8368fd83d5badbf9bfd
        with:
          persist-credentials: false
      - uses: actions/setup-node@a0853c24544627f65ddf259abe73b1d18a591444
        with:
          node-version: '22'
          cache: npm
      - run: npm ci
      - run: npm test
```

## Matrix Builds

Add a matrix only for versions and operating systems the project supports. Keep dependencies reproducible, identify failing combinations, and avoid hiding failures with blanket continue-on-error. Test required-check behavior when jobs are conditionally skipped.

## Build and Publication

Build an artifact from the tested commit and record its identity. Publication needs a separate trusted job with the minimum registry permission. Do not publish artifacts produced by arbitrary untrusted code in a privileged context; bind accepted artifacts to their exact source and producing workflow.

## Deployment

Use the project's protected release path. Identify the immutable artifact, destination, workload identity, rollout and rollback checks before adding deployment commands. A named GitHub environment does not configure reviewers automatically. Verify its actual protections. Do not label a placeholder echo command as a successful deployment.

## Verification

Exercise one passing change and one deliberate test failure on a topic branch. Confirm the failing check prevents downstream publication. Inspect tokens, runner isolation, caches and artifact boundaries. Keep production credentials absent from untrusted validation jobs.

## Example

A project needs Linux and Windows tests. Select its supported runtime, add the two runner combinations and confirm that either failure blocks the required result. Prepare publication separately; do not add registry credentials to the matrix.

## Limitations

This skill supplies patterns, not an installed deployment program. Repository policy, runner trust and environment settings must be inspected. Review every third-party action at its full commit SHA and treat logs and uploaded artifacts as possible data-exposure paths.

## Sources

- [GitHub secure workflow guidance](https://docs.github.com/en/actions/reference/security/secure-use)
