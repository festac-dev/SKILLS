# Specialist: Data Governance and Compliance

Map data categories, purposes, sources, destinations, access, retention, deletion and processors. Collect only what the product needs. Define consent and legal basis with qualified review where applicable.

Consider data subject requests, auditability, residency, encryption, key management, backups, retention exceptions and third-party processing. Do not claim legal compliance or certification based on a checklist. Record jurisdictional assumptions and refer specialized legal questions to qualified professionals.

## Privacy operations and assurance evidence

### When to use
Use for PII processing, retention/deletion, audit requirements, GDPR questions, or SOC 2 readiness work.

### Core principles
Map obligations to jurisdiction, contract, data purpose, and qualified review. GDPR is a legal framework; SOC 2 is an attestation process scoped to a system and controls. Neither is achieved by adding a badge or checklist.

### Step-by-step procedure
1. Inventory data purpose, legal-basis questions, processors, residency, access, and retention. Collect the minimum necessary.
2. Assign ownership for access, correction, export, deletion, incidents, and legal holds.
3. Propagate retention/deletion into derived data, caches, search, telemetry, and backup expiry. Explain backup restore suppression where deletion cannot immediately rewrite backups.
4. Define audit events for privileged access and material changes; protect integrity, restrict readers, minimize content, and bound retention.
5. Map required controls to evidence, operating period, reviewer, exceptions, and remediation. Obtain qualified review for legal interpretations and assurance claims.

### Checklist
- [ ] Each PII field has a documented purpose.
- [ ] Deletion covers derived copies and has tested limitations.
- [ ] Support access is scoped and auditable.
- [ ] Evidence itself follows privacy and retention rules.

### Common failure modes
Logs become an uncontrolled PII store; “encrypted” is mistaken for compliant; a deletion request leaves searchable vectors; a policy document is treated as evidence a control operated.

### Concrete examples
For a synthetic user's deletion test, inventory the primary record, export, search index, cache, analytics identifier, and backup policy. Verify each expected deletion or retained exception and record the reason. Use IDs and counts rather than copying the person's data into reports.

### Verification
Exercise a synthetic data-subject request and access review. Record scope, completion times, derived-store results, exceptions, and reviewer; reserve compliance/attestation claims for the appropriate process.

### Related skills
[Privacy engineering](privacy-engineering.md), [legal coordination](legal-policy-and-regulatory-coordination.md), [retention template](../templates/DATA_LIFECYCLE_AND_RETENTION.md).

## Applied verification

Follow one synthetic subject through source records, derived tables, logs, exports and backups. Verify the documented correction/deletion policy at each boundary, including retained legal exceptions; a policy document is not execution evidence.
