# Domain and Integration Gate

A product is ready for this gate when:

- [ ] The actual product domain and business rules are documented.
- [ ] Candidate capabilities were selected based on user evidence, not catalogue completeness.
- [ ] Core state transitions and invariants are explicit.
- [ ] External providers have owners, permissions, failure behavior, and exit plans.
- [ ] Retries, duplicates, timeouts, partial failures, and reconciliation are tested.
- [ ] Data ownership, retention, export, and deletion are defined.
- [ ] Security boundaries and tenant isolation are tested.
- [ ] Operational alerts and recovery procedures exist for critical workflows.
- [ ] User-facing language explains outcomes and next steps clearly.

Record exceptions with rationale, owner, and revisit trigger.

## Application evidence

Trace the core journey through domain validation, authorized side effect and reconciliation. Verify downloaded/exported content when it is the result of the journey, rather than only asserting that a button was clicked.
