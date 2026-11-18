# Architecture and Data Gate

- [ ] Architecture fits current constraints and team capability.
- [ ] Domain boundaries and authoritative data sources are clear.
- [ ] State transitions and invariants are documented.
- [ ] Security and privacy trust boundaries are explicit.
- [ ] Failure, concurrency, retry, and recovery behavior is defined.
- [ ] Data lifecycle, migration, export, and deletion are addressed.
- [ ] Observability and operational ownership are designed.
- [ ] Major decisions and alternatives are recorded.

## Application evidence

Verify the invariant under a competing write or retry in the actual persistence engine when concurrency is in scope. Mark substitute-engine checks separately, and verify historical records remain interpretable.
