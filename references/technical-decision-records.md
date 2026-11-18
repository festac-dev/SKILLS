# Technical Decision Records

Use one record for a consequential decision. Keep it short enough to stay current.

## Template
- **Title:**
- **Status:** proposed / accepted / superseded / rejected
- **Date and owner:**
- **Context:** constraints and problem.
- **Decision:** what is being chosen.
- **Alternatives:** credible options considered.
- **Consequences:** benefits, costs, risks, and operational implications.
- **Revisit trigger:** evidence or condition that would justify changing it.
- **Related work:** links to implementation, tests, and other decisions.

Record decisions, not every minor implementation detail.

## Technology comparison and evidence

### When to use
Use this existing decision-record resource for consequential stack, provider, architecture, or build-versus-buy choices.

### Core principles
Compare options against the same constraints and time horizon. Preserve the current supported choice unless evidence justifies migration. Keep uncertain decisions provisional.

### Step-by-step procedure
1. Record owner, date, status, requirement, and hard constraints.
2. Include the existing/simple baseline and credible alternatives.
3. Compare constraint fit, installed/versioned evidence, delivery/operating cost, failure modes, and exit implications.
4. State the decisive evidence, consequences, remaining assumptions, compatibility plan, and revisit trigger.

### Checklist
- [ ] Alternatives satisfy hard constraints.
- [ ] Claims about limits/prices/versions have sources.
- [ ] Migration and recovery costs are included.
- [ ] Uncertainty has a bounded validation experiment.

### Common failure modes
Subjective scores hide weak evidence; the baseline is omitted; a migration cost is ignored; a decision never records when to reconsider it.

### Concrete examples
For a local single-user utility, compare its existing SQLite database with a managed service against concurrency, offline use, backup, and operations. Do not choose the service solely for hypothetical scale. Inspect the local SQLite runtime with `python -c "import sqlite3; print(sqlite3.sqlite_version)"`.

### Verification
Run the experiment that addresses the decisive uncertainty and attach its environment/result. A completed table alone does not validate a choice.

### Related skills
[Technology selection](../orchestrator/TECHNOLOGY_SELECTION.md), [architecture decisions](architecture-decision-records.md), [economics](../specialists/financial-planning-and-unit-economics.md).

## Application evidence

Keep one current decision record with a replacement link when superseded. Record the smallest experiment that supported the choice and the condition that would reverse it; use the architectural form only when the decision concerns long-lived system boundaries.
