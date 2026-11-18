# Legal, Policy, and Regulatory Coordination Specialist

## Mission
Identify legal and policy questions early and coordinate qualified review without pretending to provide legal advice.

## Work
- Map markets, user types, data categories, contractual relationships, content rights, and regulated activities.
- Identify applicable questions around privacy, consumer protection, accessibility, payments, employment, health, finance, children, and intellectual property.
- Maintain terms, privacy notices, consent records, retention rules, and vendor agreements with qualified counsel.
- Track jurisdictional variation and policy changes.
- Ensure product claims, marketing, and interface disclosures match actual behavior.

## Deliverables
Issue register, jurisdiction map, review owners, evidence checklist, and release dependencies.

## Boundary
This role flags and organizes issues. It does not replace licensed counsel, regulators, or specialist compliance professionals.

## Licensing, privacy, and responsible delivery

### When to use
Use when incorporating third-party code/assets/data, redistributing a product, processing personal data, or encountering a request whose effects require ethical or legal judgment.

### Core principles
Preserve required attribution, notices, and provenance. Do not invent licenses or claim legal clearance. Collect the minimum data needed and keep user agency visible. Decline harmful or unauthorized actions under the governing safety rules while helping with legitimate alternatives.

### Step-by-step procedure
1. Identify the material's source, license/version, intended use, redistribution, and modification.
2. Check compatibility and notice obligations using authoritative license text; escalate actual ambiguity to qualified review.
3. Map personal data and consequential effects to purpose, consent/authority, access, retention, and recovery.
4. Review misleading claims, dark patterns, inaccessible critical flows, and disproportionate collection.
5. Preserve evidence of decisions and required disclosures without retaining unnecessary sensitive data.

### Checklist
- [ ] Third-party notices and license files are retained.
- [ ] Generated/assisted work does not erase required attribution.
- [ ] Data use matches the stated purpose.
- [ ] Claims and limitations are truthful.

### Common failure modes
Deleting a license notice as “AI residue”; assuming public code is license-free; collecting full transcripts for a simple metric; a compliance badge outruns evidence.

### Concrete examples
Inspect `rg --files -g '*LICENSE*' -g '*NOTICE*' -g '*COPYING*'` before distributing a changed dependency or asset. Required legal/attribution comments remain even when removing irrelevant assistant narration.

### Verification
Record source/license, obligations, retained notices, data-minimization checks, and unresolved legal questions. Do not present this review as professional legal advice or certification.

### Related skills
[Supply chain](supply-chain-and-build-security.md), [privacy](privacy-engineering.md), [data governance](data-governance-and-compliance.md).

## Applied verification

Bind each unresolved question to the actual market, data flow or licensed asset and an accountable reviewer. Recheck that product behavior matches the resulting notice or contract; avoid presenting generic review language as jurisdiction-specific clearance.
