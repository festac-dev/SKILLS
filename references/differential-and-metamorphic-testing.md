# Differential and Metamorphic Testing

## When to use
Load when a strong test oracle is hard to write, replacing an implementation, or testing parsers, codecs, transformations, search, numerical code, and stateful algorithms.

## Core principles
Differential tests compare independent implementations or a trusted baseline. Metamorphic tests check justified relations between transformed inputs/outputs. Shared bugs and invalid properties can make both approaches falsely reassuring.

## Step-by-step procedure
1. Define equivalence: exact bytes, normalized structure, numerical tolerance, or a domain invariant.
2. Choose an independent reference or a relation with a written justification.
3. Generate boundary and adversarial inputs; record seeds and shrink counterexamples.
4. Compare errors and invalid-input behavior as well as successful results.
5. Investigate differences before selecting a winner. Preserve counterexamples as regressions.

## Checklist
- [ ] Reference implementations do not share the same critical logic.
- [ ] Tolerances are domain-based, not chosen to hide failures.
- [ ] Metamorphic transformations preserve stated preconditions.
- [ ] Nondeterministic fields are normalized deliberately.

## Common failure modes
Two wrappers call the same buggy library; sorting hides meaningful order differences; round-trip tests miss paired encoder/decoder bugs; overly broad numerical tolerances conceal instability.

## Concrete examples
```python
import json
value = {"count": 3, "items": ["a", "b"]}
encoded = json.dumps(value, sort_keys=True)
assert json.loads(encoded) == value
assert json.dumps(json.loads(encoded), sort_keys=True) == encoded
```
These test round-trip/idempotent normalization for this JSON domain, not independent implementation correctness. For a money refactor compare an independently computed decimal reference across boundary amounts and rounding rules.

## Verification
Demonstrate detection of at least one deliberately seeded defect in an isolated fixture, retain minimized failures, and state the reference's limitations.

## Related skills
[Test strategy](../specialists/quality-engineering-and-test-strategy.md), [formal methods](../specialists/formal-methods-and-invariants.md), [migration](../specialists/migration-and-compatibility.md).

## Application evidence

Include a deliberately broken implementation to test whether the oracle or relation can detect the relevant defect. If baseline and candidate share the same parser, data source or algorithm, record that correlated failure risk instead of claiming independence.
