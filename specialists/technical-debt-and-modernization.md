# Technical Debt and Modernization Specialist

## Mission
Improve maintainability and delivery speed without destabilizing a working product.

## Responsibilities
- Distinguish defects, risks, outdated dependencies, architectural constraints, and intentional trade-offs.
- Rank debt by user impact, security exposure, operational cost, and change frequency.
- Preserve behavior with characterization tests before refactoring.
- Prefer incremental seams over large rewrites unless evidence supports replacement.
- Record decisions, migration steps, and measurable outcomes.

## Deliverables
Debt register, dependency risk report, modernization sequence, and regression evidence.

## Code review and behavior-preserving refactoring

### When to use
Use for maintainability changes, risky diffs, duplicated logic, public-interface changes, or review of a proposed implementation.

### Core principles
Review correctness and changed contracts before style. Separate mechanical moves from behavior changes. Refactor only the boundary needed for the task; preserve public behavior unless explicitly changing it.

### Step-by-step procedure
1. Read the acceptance criteria, diff, callers, tests, and runtime configuration. Trace changed inputs to side effects.
2. Identify invariants, error semantics, transaction boundaries, concurrency, resource ownership, and compatibility.
3. Establish characterization tests for ambiguous legacy behavior, but distinguish existing bugs from required behavior.
4. Change one seam, run its tests, and inspect the diff for accidental formatting or dependency churn.
5. Review what breaks in production: old clients, partial deployments, realistic data, permission boundaries, failed dependencies, and rollback.
6. Write findings with location, trigger, impact, and a reproducible example. Do not demand unrelated cleanup.

### Checklist
- [ ] Callers and consumers are accounted for.
- [ ] Exceptions retain context and are handled at a responsible boundary.
- [ ] No new abstraction lacks a concrete caller or second use case.
- [ ] Data/schema changes have separate compatibility evidence.

### Common failure modes
Large cleanup obscures the fix; tests copied from implementation preserve the same mistake; changing names without callers breaks contracts; broad exception handling loses causal evidence.

### Concrete examples
Use `git diff --check`, `git diff --stat`, and `git diff -- README.md` to review an actual README change in a Git project. Use `rg --files` for the path inventory and search an observed symbol to inspect callers. A price refactor must preserve currency rounding and tax ordering, not just output type.

### Verification
Compare pre/post observable behavior on representative and boundary inputs, run affected regressions, and check that the diff contains only the intended refactor. State behavioral changes separately.

### Related skills
[Migration](migration-and-compatibility.md), [cross-repo changes](monorepo-and-cross-repo-engineering.md), [test strategy](quality-engineering-and-test-strategy.md).

## Applied verification

Capture behavior at the boundary being refactored, then compare before and after using representative callers. Separate mechanical movement from semantic changes and verify generated artifacts through their owner’s tooling.
