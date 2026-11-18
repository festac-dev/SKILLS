# Quality Engineering and Test Strategy Specialist

## Mission
Build confidence that the product behaves correctly under expected and adverse conditions.

## Work
- Derive tests from user journeys, domain invariants, risks, and acceptance criteria.
- Balance unit, component, contract, integration, end-to-end, accessibility, security, performance, and exploratory testing.
- Identify test data, environment parity, deterministic setup, cleanup, and isolation needs.
- Prioritize high-risk paths and meaningful regression coverage over arbitrary coverage percentages.
- Test failure, retry, concurrency, permissions, migrations, and recovery—not just happy paths.

## Deliverables
Test pyramid/portfolio, risk-based coverage map, test data strategy, CI quality gates, flake policy, and evidence report.

## Test implementation and failure diagnosis

### When to use
Use for changed behavior, a missing regression, contract drift, nondeterminism, or a flaky CI check. For a low-impact copy change, inspect the output instead of creating tests that repeat the implementation.

### Core principles
Test observable contracts and invariants. Keep the unit under test real; replace only external boundaries. Prefer integration tests for database constraints and authorization. One critical end-to-end journey is more useful than many brittle screenshots. Do not require a universal coverage percentage.

### Step-by-step procedure
1. Map each changed requirement to a failing observation and the lowest layer that can prove it.
2. Add unit tests for pure rules, integration tests for persistence/permissions, contract tests for consumers, and end-to-end tests for critical journeys.
3. Control time, randomness, network, data ownership, and cleanup. Reproduce flakes with a recorded seed and order before changing waits.
4. For concurrent work, run competing operations against a real disposable datastore. Assert durable results, not only response codes.
5. For properties, generate boundary inputs and shrink failing cases. Record the minimal reproducer.
6. Quarantine a flaky test only with an owner, expiry, retained failure signal, and separate repair task. Never turn automatic retries into evidence that the test is stable.

### Checklist
- [ ] The regression fails before the fix and passes after it.
- [ ] Error, permission, duplicate, and cancellation paths are represented when affected.
- [ ] Fixtures cannot contact production.
- [ ] Tests fail when the important invariant is deliberately violated in an isolated copy.

### Common failure modes
Mocking the business rule proves the mock; sleeping hides a race; snapshots can bless broken output; randomized failures without seeds cannot be replayed; swallowed exceptions manufacture green runs.

### Concrete examples
For a Python project using pytest, first check `python -m pytest --help`, then run `python -m pytest -q`. A concurrency regression for stock of one must assert exactly one successful reservation and final stock zero after two simultaneous attempts. For a JS repository inspect `npm run` before choosing its existing test script.

### Verification
Record the tested revision, environment, case IDs, observed failures before/after, and any excluded environment. Use [differential testing](../references/differential-and-metamorphic-testing.md) when an independent implementation or relation provides a stronger oracle.

### Related skills
[QA](qa-and-verification.md), [testing gate](../quality-gates/TESTING_AND_EVIDENCE_GATE.md), [formal invariants](formal-methods-and-invariants.md).

## Applied verification

Demonstrate that a regression test fails with the relevant defect present and passes with its fix. Keep at least one check across the real persistence or integration boundary when that boundary owns the failure.

When a generated browser assertion fails, compare its evaluated predicate with the requested condition, the screenshot and the request sequence before changing the application. Compound assertions can misinterpret negation or combine different page states. Preserve the requirement and rerun with independently checkable conditions—for example, a visible locked heading and a count of zero visible dialogs. Establish that the intended client stayed open through an independently observed lock; navigating to a fresh locked page does not prove cross-client propagation. A runner error or unavailable preview is distinct from a reproduced product defect.

For an explicitly accepted browser-only phone target, reuse an installed browser with touch/mobile settings and separate persistent profiles before adding an OS emulator. Honor local-data constraints when choosing the runner. Record the emulated browser settings separately from the native backend and physical-device claims. A tap completing does not establish that an asynchronous mutation committed; wait for the resulting state. For forced interruption, identify the owned process tree, distinguish browser/controller death from backend death, and verify the restarted durable records rather than only a relaunched page.

On reuse, verify that the browser/controller still targets the intended fixture; reject a conflicting URL instead of silently driving the previously opened page. Add a newly required acceptance check to the maintained verification entrypoint so a one-off pass does not leave future runs without that coverage. For large native fixtures, use explicitly owned private test storage and preserve the same storage selection when restoring a checkpoint; do not fill the source disk or discard recovery evidence to make space.

Contract fixtures should reproduce the owning API’s observed or pinned response format. Do not echo a request field into the response when the real provider adds network, currency or version semantics. Verify one complete operation through the actual adapter and native provider, keep test networks explicitly separated from production, and retain pre-fix failures as regression evidence.
