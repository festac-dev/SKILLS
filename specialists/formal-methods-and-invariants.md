# Formal Methods and Invariants Specialist

## When to use
Load for critical state machines, concurrency, accounting, authorization, or protocols where ordinary examples miss dangerous interleavings. Skip heavy modeling when a simple unit test adequately resolves a low-risk change.

## Core principles
State assumptions and invariants before selecting notation. A bounded model check is not an unbounded proof. The implementation must be related to the model; proving the wrong model proves little about the product.

## Step-by-step procedure
1. Define state, allowed transitions, initial conditions, environment assumptions, and forbidden outcomes.
2. Separate safety (“nothing bad happens”) from liveness (“progress eventually happens”), including fairness assumptions.
3. Sketch the smallest useful TLA+, Alloy, or equivalent model. Bound actors/data intentionally and record the explored scope.
4. Model failure, retry, concurrent actions, and recovery. Inspect counterexamples rather than weakening the invariant to obtain a pass.
5. Translate invariants and counterexamples into implementation tests.
6. Record proof/model-check limits and the refinement argument connecting model and code.

## Checklist
- [ ] Invariants capture the business loss being prevented.
- [ ] Model assumptions match deployment reality.
- [ ] Fairness and boundedness are explicit.
- [ ] Counterexamples become regression cases.

## Common failure modes
A sequential model omits races; a tiny scope is presented as universal proof; invalid states are removed by assumptions; the deployed implementation no longer matches the checked model.

## Concrete examples
A bounded Alloy transfer model:
```alloy
sig Item {}
sig Owner {}
sig State { owns: Owner -> set Item }
pred valid[s: State] { all i: Item | lone (s.owns).i }
pred transfer[b, a: State, i: Item, from, to: Owner] {
  i in from.(b.owns)
  a.owns = b.owns - (from -> i) + (to -> i)
}
assert TransferPreservesUnique {
  all b, a: State, i: Item, from, to: Owner |
    valid[b] and transfer[b, a, i, from, to] implies valid[a]
}
check TransferPreservesUnique for 4
```
This checks whether the specified transfer preserves unique ownership within the explored scope. It does not model network failure, authorization, or liveness. Removing the old-owner subtraction is a useful seeded defect: the checker should find a double-owner counterexample.

A separate TLA+ reservation sketch:
```tla
---------------- MODULE Reservation ----------------
EXTENDS Naturals
VARIABLES stock, reserved
Init == /\ stock = 1 /\ reserved = 0
Reserve == /\ stock > 0
           /\ stock' = stock - 1
           /\ reserved' = reserved + 1
Release == /\ reserved > 0
           /\ stock' = stock + 1
           /\ reserved' = reserved - 1
Next == Reserve \/ Release
Invariant == /\ stock + reserved = 1
             /\ stock >= 0 /\ reserved >= 0
Spec == Init /\ [][Next]_<<stock, reserved>>
====================================================
```
For TLC, configure `INIT Init`, `NEXT Next`, and `INVARIANT Invariant`. This finite sketch checks conservation and nonnegative state; no fairness or eventual-completion property is claimed. Verify against current Alloy/TLA+ docs and the installed tools. Check Java with `java -version`; if the official `tla2tools.jar` is locally present, inspect `java -jar tla2tools.jar -help` before invoking the checker. These model examples remain unexecuted until those tools actually run.

## Verification
Retain model version, tool version, bounds, assumptions, counterexamples, and results. Mark the example unexecuted unless the actual model checker ran. Link each critical invariant to real implementation evidence.

## Related skills
[Distributed systems](edge-and-distributed-systems.md), [ledger systems](fintech-and-ledger-systems.md), [test strategy](quality-engineering-and-test-strategy.md).

## Applied verification

Seed a known invariant violation and confirm the chosen checker produces a counterexample within the stated bounds. If it does not, investigate the model and configuration before trusting a clean result; retain implementation tests separately.
