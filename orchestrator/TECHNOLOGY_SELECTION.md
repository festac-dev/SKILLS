# Technology Selection and Evolution

Use when a stack decision changes maintenance, architecture, cost, or deployment. Do not reopen settled choices for a routine feature.

## Hard constraints

Record supported runtimes/devices, hosting restrictions, data residency, offline requirements, license policy, team expertise, integrations, operational ownership, budget, and delivery horizon. Separate measured demand from forecasts. Verify version-specific claims against official documentation and record version/date.

## Compare a credible shortlist

Include the existing stack or simplest viable option. Compare only alternatives satisfying hard constraints.

| Dimension | Questions that change the choice |
|---|---|
| Correctness | Can it express required transactions, concurrency, permissions, and invariants? |
| Workload | Does execution fit CPU work, I/O, job duration, fan-out, and latency? |
| Delivery | Can this team debug, test, ship, and maintain it? Which unknown merits a spike? |
| Operations | Who patches/restores it, handles incidents, and funds peak/recovery capacity? |
| Ecosystem | Supported releases, security updates, dependencies, tooling, accessibility, licensing? |
| Evolution | What is locked in? Can contracts/data be exported? What triggers migration? |

Choose qualitatively with evidence; do not hide subjective weights behind precise scores. If performance is decisive, benchmark representative workloads including cold starts, tail latency, memory, and cost. Hello-world benchmarks do not establish suitability.

## Architecture and hosting

Use in-process modules when independent deployment does not solve a concrete constraint. Services require ownership, versioned contracts, failure isolation, observability, and operations. Queues need replay handling; caches need invalidation; clusters need operators. Treat each as a responsibility.

Managed platforms trade control for service boundaries and constraints. VPS hosting trades direct control for patching, backups, and incident responsibility. Containers provide packaging; persistence, secrets, high availability, and recovery remain separate decisions.

## Record consequential decisions

Use [the decision template](../references/technical-decision-records.md): context, options, evidence, decision, consequences, rollout/exit, and revisit trigger. Keep a decision provisional while its decisive assumption is untested. Plan compatibility and ownership before migration.

## Version verification and build-versus-buy procedure

### When to use
Use for an uncertain API/flag, new dependency, provider choice, or a material build-versus-buy decision.

### Core principles
Verify installed reality before relying on memory. Prefer the existing supported stack when it meets requirements. Include integration, operations, security, support, exit, and opportunity cost in a choice.

### Step-by-step procedure
1. Inspect manifests, lockfiles, installed versions, project scripts, and local docs.
2. Confirm the exact API or flag in installed help/types/source or authoritative docs for that version.
3. If uncertain, say “verify against current docs,” give the exact inspection command, and avoid presenting untested syntax as working.
4. Compare build and buy over the same horizon: delivery effort + maintenance + infrastructure + operations + migration/exit + expected risk cost.
5. Identify the decisive uncertain assumption and test it with a bounded spike.
6. Record decision, evidence, tradeoffs, and revisit trigger in the existing decision template.

### Checklist
- [ ] API, flag, file, and dependency names were observed or explicitly left unverified.
- [ ] The selected tool exists in the actual environment.
- [ ] Provider prices/limits are dated sources, not invented constants.
- [ ] A cheaper license does not conceal higher operating cost.

### Common failure modes
Using obsolete examples; choosing a framework by popularity; mistaking benchmark throughput for product latency; assuming a managed service removes operational responsibility.

### Concrete examples
Use `python --version`, `git --version`, `npm run`, and `python -m pip show pytest` only where those tools apply. For a new provider, compare a measured monthly operating estimate and an exit plan; do not invent price data to fill a table.

### Verification
Run the smallest relevant example in the installed environment and retain result/version. If docs or dependencies are unavailable offline, state the limitation and continue independent work.

### Related skills
[Decision record](../references/technical-decision-records.md), [economics](../specialists/financial-planning-and-unit-economics.md), [Termux](../references/termux-and-constrained-environments.md).

## Current-task application

For documentation-library upgrades, improve instructions and executable maintenance tools before considering package installation. Preserve the supplied directory and avoid unrelated global configuration changes; justify any new dependency with a specific missing capability.
