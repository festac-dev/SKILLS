---
name: trailofbits-prepare-regression
description: Use when pinning before/after sources and collecting PR or commit context
  for a regression investigation.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Prepare a change

## When to Use

Input: PR URL or repository plus commit/range, and registry assignment.
Follow [project guidance](../../references/evidence.md#project-guidance) after resolving the target commit.

## When NOT to Use

The same inputs have a verified preparation record; reuse it.

## Prepare

1. Read the [standard](../../docs/regression-definition.md) and
   [file contract](../../references/evidence.md). Pin the complete change as S0/S1:
   commit parent or explicit range baseline; merge base to frozen head for unmerged
   PRs; merge first parent to merge commit, squash parent to squash, or the complete
   rebased series for merged PRs. Ambiguous ranges and missing root baselines block
   preparation.
2. Freeze commit titles/messages or PR title, body, discussion, reviews and inline
   comments with URLs and collection time. Paginate APIs; record limits and
   lifecycle. Locate security/threat-model documents in both states; record paths
   or search limitations.
3. Run [snapshot.py](../../scripts/snapshot.py) via `uv run --no-project` with
   repository, S0, S1 and a new directory, or equivalent Git commands for special
   source needs. Preserve dependency/submodule/LFS revisions. Exclude later history;
   keep exports pristine and build in separate copies.
4. Write and seal `prepare.json` with boundary explanations, frozen context and
   source artifacts. If blocked, preserve collected evidence and name the prerequisite.

## Report Back

Keep detailed evidence in the sealed package. Return only:

- Status: `complete` or `blocked`, matching the record.
- Record: sealed `prepare.json` path, or why none was produced.
- Result: selected S0/S1 and material collection limitations.
- Blocker: missing prerequisite or required caller action, if blocked.

## Rationalizations to Reject

- “The PR is merged”: that does not identify the complete change boundary.
