---
name: trailofbits-reproduce-regression
description: Use when deploying before/after systems and building a live-system PoC
  for a regression candidate.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Reproduce a candidate

## When to Use

Input: sealed preparation/discovery packages, candidate and registry assignment.
Follow [project guidance](../../references/evidence.md#project-guidance) before target work.

## When NOT to Use

Independent verification of an existing PoC; use replay.

## Reproduce

1. Read the [standard](../../docs/regression-definition.md) and
   [file contract](../../references/evidence.md). Verify inputs; read security
   guidance. Stop execution if prerequisites fail.
2. Build and run actual S0/S1 with required services. Trace the candidate to a real
   user/attacker entry point. Build/install CLIs and libraries; exercise supported
   interfaces. For build findings, execute the supported build workflow.
3. Create and execute a portable PoC against both live deployments with identical
   input and comparable configuration. Record whether S0 behaves correctly and S1
   exhibits the claimed failure. No mocks, extracted functions or simulated systems.
4. Save setup, tool/dependency versions, sanitized configuration, input, PoC,
   revisions, commands and separate logs. Record observations and false-positive
   checks in `reproduce.json`. If blocked, retain attempted setup and exact prerequisites.
   Build and deploy only inside your attempt directory, and list every build directory in `build_dirs`.
5. Release temporary resources without deleting evidence. Record their disposition,
   then seal the package.

## Report Back

Keep detailed evidence in the sealed package. Return only:

- Status: `complete` or `blocked`, matching the record.
- Record: sealed `reproduce.json` path, or why none was produced.
- Result: one sentence describing observed S0/S1 behavior.
- Blocker: missing prerequisite or required caller action, if blocked.

Completion means the experiment finished, not that the regression is confirmed.

## Rationalizations to Reject

- “The unit test proves it”: synthetic tests cannot establish a regression.
