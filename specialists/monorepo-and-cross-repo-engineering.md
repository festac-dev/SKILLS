# Monorepo and Cross-Repository Engineering Specialist

## When to use
Load for shared contracts, package-wide migrations, cross-repository releases, or codemods affecting many consumers.

## Core principles
Compute blast radius from dependency and runtime contracts, not directory proximity. Distinguish source dependencies, generated clients, deployments, data consumers, and externally versioned APIs.

## Step-by-step procedure
1. Inventory workspaces, manifests, package exports, schemas, generators, ownership, and release topology.
2. Trace changed symbols/contracts to direct and transitive consumers. Include repositories not available locally as explicit unknowns.
3. Choose additive compatibility and staged release order before editing.
4. Run codemods in a bounded dry-run or disposable copy. Prefer AST-aware edits for syntax changes; inspect generated diffs and exceptions.
5. Test changed packages plus dependent integration boundaries. Rebuild generated clients through their real generator.
6. Publish only within existing authorization; track consumer adoption before removing compatibility.

## Checklist
- [ ] Dependency graph includes runtime and schema relationships.
- [ ] Codemods are idempotent and preserve formatting/comments where intended.
- [ ] Generated files follow repository policy.
- [ ] Cross-repo access and publication are not assumed.

## Common failure modes
Text replacement changes string literals; hidden consumers break; a package version is bumped before compatible clients exist; local green tests omit deployed consumers; running a codemod twice corrupts code.

## Concrete examples
Start with `rg --files -g 'package.json' -g 'go.mod' -g 'Cargo.toml' -g 'pyproject.toml'`. In a disposable Git copy, inspect codemod output with `git diff --stat` and `git diff --check`. Run the codemod twice and confirm the second run produces no additional diff.

## Verification
Record dependency graph scope, changed packages, affected consumers, dry-run diff, idempotency check, integration tests, and inaccessible repositories left unverified.

## Related skills
[Refactoring](technical-debt-and-modernization.md), [migration](migration-and-compatibility.md), [release workflow](../references/release-and-change-management.md).

## Applied verification

Run the affected consumer against the changed package, not only the package’s own tests. Record unavailable consumers explicitly and confirm a second codemod run makes no additional changes.
