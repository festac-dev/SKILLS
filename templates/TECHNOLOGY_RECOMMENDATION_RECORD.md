# Technology Recommendation Record

- Context and requirement driving the choice:
- Current state (what exists and works):
- Options considered (including "keep current"):
- Recommendation:
- Why (evidence, constraints, team skill):
- Costs and risks (licensing, ops, lock-in, security):
- Exit/rollback path:
- How to validate (prototype, benchmark, spike) and results:
- Decision and approver:

## Deep guidance (v4)
**Worked example (shape, not a verdict):**
- Context: 5-person team, B2B scheduling app, 8-week MVP, spiky evening traffic.
- Current: none (greenfield). Constraint: team knows TypeScript and PostgreSQL.
- Options: (A) modular monolith in TypeScript + PostgreSQL + Postgres-backed jobs; (B) microservices on Kubernetes; (C) serverless functions + managed NoSQL.
- Recommendation: A. Why: fits team skill, transactional integrity needed for bookings, lowest operational load, easy to evolve. Costs: single deploy unit, must keep module boundaries disciplined. Revisit if: independent scaling or team split demands extraction, or job throughput exceeds what Postgres handles comfortably.
- Exit path: modules communicate via explicit interfaces and an outbox, so extraction is incremental.
- Validate: load-test booking path at 3× expected peak; restore drill before launch.
