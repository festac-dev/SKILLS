# Solidity and Foundry Contract Engineering Specialist

## When to use
Load for Solidity contracts, Foundry tests, upgrades/proxies, contract reviews, or financial invariants. Deployment authorization is separate from implementation.

## Core principles
Use established, version-compatible libraries for standard primitives. Specify assets, roles, accounting invariants, and upgrade trust before code. Fuzzing and a green test suite do not replace independent review for high-value contracts.

## Step-by-step procedure
1. Inspect compiler, EVM target, library versions, storage layout, deployed compatibility, and privileged roles.
2. Define invariants: conservation of accounted assets, bounded withdrawals, authorized upgrades, and valid state transitions.
3. Review external calls, reentrancy, checks-effects-interactions, token return behavior, rounding, oracle freshness, slippage/deadlines, and MEV exposure.
4. For proxies, verify initializer access, implementation locking, storage layout compatibility, and upgrade authority. Preserve a tested upgrade/rollback plan where feasible.
5. Add unit, fuzz, invariant, and fork tests with pinned fork state. Separate external-mainnet dependencies from deterministic local tests.
6. Review the diff against an attack checklist, fix findings, and retest original and adjacent exploits in authorized fixtures.

## Checklist
- [ ] Reentrancy is considered across functions and contracts.
- [ ] Accounting handles fees, decimals, rounding, and unusual tokens.
- [ ] Admin keys and upgrade powers are explicit.
- [ ] Test assumptions do not exclude adversarial valid inputs.

## Common failure modes
Testing only standard tokens; proxy initialization takeover; storage collisions; oracle manipulation; excessive fuzz assumptions; deployment scripts silently choosing mainnet.

## Concrete examples
Inspect `forge --version`, `forge test --help`, and `forge inspect --help`. In an existing Foundry project run `forge test`; use installed-version help before selecting fuzz/invariant options. A withdrawal invariant should assert total successful withdrawals never exceed credited assets even under repeated callbacks and multiple callers.

## Verification
Record compiler/library versions, seeds, counterexamples, invariant coverage, fork block if used, storage-layout comparison, and fix/retest evidence. Mainnet deployment remains a separately reviewed action.

## Related skills
[EVM transactions](evm-transaction-engineering.md), [formal methods](formal-methods-and-invariants.md), [security review](security-architecture-and-red-teaming.md).

## Applied verification

Test the invariant under an adversarial call sequence and the actual upgrade/storage layout when relevant. Record compiler, dependencies, network and deployed bytecode separately; a local unit pass does not establish deployment equivalence.
