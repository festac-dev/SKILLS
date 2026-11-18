# Data Modeling and Integrity Guide

## Model around domain meaning
Use stable identifiers, explicit ownership, lifecycle states, and clear relationships. Avoid overloading fields with multiple meanings.

## Integrity
Define uniqueness, referential integrity, invariants, transactional boundaries, concurrency behavior, and deletion semantics.

## Evolution
Plan schema versioning, migrations, backfills, compatibility windows, and rollback/forward-fix options.

## Time and money
Store timestamps with clear timezone semantics. Represent currency and precision explicitly. Never rely on floating-point arithmetic for authoritative monetary values.

## Privacy and portability
Classify fields, minimize collection, document provenance, retention, export, correction, and deletion behavior.

## Review questions
What is authoritative? Who may change it? Can changes race? Can records be reconstructed? What must remain auditable?

## Application evidence

For each invariant, identify the enforcing constraint or transactional boundary and a competing-write test. Validate historical and derived records after a change; matching row counts alone cannot establish monetary or relational integrity.
