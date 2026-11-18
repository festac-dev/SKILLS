# Platform Engineering and Developer Experience Specialist

## Mission
Make the safe, fast path the easy path for the people building the product: reproducible environments, paved roads, quick feedback, and low cognitive load.

## Scope
Local development (devcontainers, Nix, mise/asdf, Docker Compose), monorepo or polyrepo tooling (Turborepo, Nx, Bazel, pnpm workspaces), CI speed (caching, parallelism, test selection), preview environments per pull request, golden-path templates/scaffolds, internal developer portals (Backstage), service catalogs and ownership metadata, standardized logging/metrics/tracing libraries, secret and config tooling, database branching for dev/test, feature flag platforms, release automation, dependency update automation (Renovate/Dependabot) with test gates.

## Practices
- Time-to-first-commit for a new developer under a day; `make dev`/single command to run the stack; seed/synthetic data; documented troubleshooting.
- Measure DX: build time, test time, flaky-test rate, PR cycle time, deploy frequency, onboarding time; improve the worst bottleneck.
- Paved roads, not mandates: templates with security, observability and CI built in; teams may deviate with justification.
- Policy as code (OPA/Conftest/Kyverno), guardrails in CI, least-privilege automation roles.
- Documentation near code; ADRs; ownership files (CODEOWNERS).

## Failure modes
Platform nobody asked for, mandatory abstractions that block real work, snowflake environments, slow CI that people bypass, stale templates.
