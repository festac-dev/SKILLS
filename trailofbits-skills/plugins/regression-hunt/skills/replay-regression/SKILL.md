---
name: trailofbits-replay-regression
description: Use when independently verifying a supplied PoC against fresh live before/after
  deployments.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Independently replay a PoC

## When to Use

Input: candidate, frozen source records, complete sealed reproduction package
and registry assignment. Use a fresh context distinct from the reproducer.
Follow [project guidance](../../references/evidence.md#project-guidance) before target work.

## When NOT to Use

Authoring or repairing the PoC. Return changes to the caller for reproduction;
changed PoCs require new reproduction and replay.

## Replay

1. Read the [standard](../../docs/regression-definition.md) and
   [file contract](../../references/evidence.md). Verify the package; read setup
   and security guidance. Stop execution if prerequisites fail.
2. Independently build and run actual S0/S1 only inside your attempt directory; never reuse another attempt's build output. List every build directory in `build_dirs`. Execute the
   unchanged PoC with the same input against both. Record whether S0 behaves
   correctly and S1 exhibits the claimed failure.
3. Check real interface reachability using only the claimed user's/attacker's access.
   Save setup, versions, commands, observations and separate logs.
4. Write and seal `replay.json`, referencing the reproduction record and original
   PoC/input. Record divergence or blockers; uncertainty stays unresolved.
   Release temporary resources without deleting evidence.

## Report Back

Keep detailed evidence in the sealed package. Return only:

- Status: `complete` or `blocked`, matching the record.
- Record: sealed `replay.json` path, or why none was produced.
- Result: one sentence describing observed agreement or divergence.
- Blocker: missing prerequisite or required caller action, if blocked.

Completion means the replay attempt finished, not that the regression is confirmed.

## Rationalizations to Reject

- “The previous logs look right”: replay requires your own execution.
