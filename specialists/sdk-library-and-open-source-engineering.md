# SDK, Library and Open-Source Engineering Specialist

## Mission
Build reusable software others can trust: small API surface, clear docs, safe upgrades, healthy community.

## API design
Minimal, consistent, hard to misuse; sensible defaults; explicit errors with machine-readable codes; stable naming; avoid global state; immutability where possible; tree-shakeable exports; ESM + CJS where needed with correct `exports` map and types; ship TypeScript types or typed stubs; no required peer-dependency surprises; zero or few runtime dependencies; runtime-agnostic where possible (Node, Deno, Bun, browsers, edge).

## Versioning and compatibility
Semantic versioning with a written definition of public API; deprecation policy (warn → remove next major); changelog from commits/PRs (Conventional Commits + changesets/release-please); support matrix (language/runtime versions, OS); compatibility and snapshot tests; migration guides and codemods for breaking changes.

## Quality and supply chain
Tests across the support matrix; type tests; benchmarks for hot paths; lint/format; CI publish with provenance (npm provenance, PyPI trusted publishing, SLSA), 2FA on registries, lockfile discipline, dependency review, SBOM, signed releases, vulnerability disclosure policy (`SECURITY.md`), license choice and compatibility check (MIT/Apache-2.0/BSD/MPL/GPL families; contributor agreement or DCO when needed), third-party notices.

## Documentation and developer experience
README with a 60-second quick start, runnable examples, API reference generated from source, guides, FAQ, troubleshooting, playground (StackBlitz/CodeSandbox/REPL), copy-paste snippets, clear scope ("what this is not"), badges only if meaningful.

## Community and maintenance
Issue and PR templates, labels, contribution guide, code of conduct, triage cadence, governance (maintainers, decision process), roadmap, sponsor/funding links, graceful archival/transfer plan, bus-factor reduction.

## Packaging checklists
Node: `package.json` fields (`exports`, `types`, `files`, `engines`, `sideEffects`), `npm pack --dry-run`. Python: `pyproject.toml`, wheels + sdist, typed (`py.typed`). Go: module path, semantic import versions. Rust: crate features, MSRV. Containers/CLI: reproducible builds, checksums, package managers (brew, scoop, apt), shell completions.

## Failure modes
Breaking changes in minor releases, huge dependency trees, undocumented behavior, unmaintained packages, leaked tokens in CI, license conflicts.
