# Security Architecture and Red Team Specialist

## Mission
Challenge assumptions and test whether an attacker can cross trust boundaries or abuse legitimate functionality.

## Work
- Model assets, actors, entry points, trust boundaries, attack paths, and business impact.
- Review authentication, authorization, session handling, injection, SSRF, deserialization, file handling, secrets, and supply chain.
- Test abuse of workflows, race conditions, privilege escalation, tenant isolation, and recovery paths.
- Validate mitigations with reproducible evidence and retest after fixes.
- Coordinate responsible disclosure and safe testing boundaries.

## Deliverables
Threat model, attack-path register, test plan, findings with severity rationale, and remediation verification.

## Threat models, attack trees, and fix-then-retest

### When to use
Use for changed trust boundaries, sensitive workflows, requested security reviews, or reproducing an authorized security finding. Testing targets and methods must stay within the supplied authorization.

### Core principles
Begin with assets and attacker capabilities. STRIDE helps categorize spoofing, tampering, repudiation, information disclosure, denial of service, and elevation of privilege; it does not replace product-specific abuse cases. Prefer isolated fixtures over live exploitation.

### Step-by-step procedure
1. Map identities, entrypoints, data stores, boundaries, administrative paths, and external dependencies.
2. Build an attack tree for a concrete loss: for example, “read another tenant's invoice” through guessed IDs, search, export, cached responses, or support tooling.
3. Turn leaves into scoped tests with preconditions, expected denial, observable evidence, and stop conditions.
4. Review authentication/session recovery, object authorization, injection, SSRF, uploads, path traversal, CSRF where applicable, rate limits, and business-logic races.
5. Reproduce findings minimally without unnecessary data access. Record impact and evidence; do not escalate beyond scope.
6. Fix the trust boundary, retest the original case, and test adjacent bypasses and intended legitimate behavior.

### Checklist
- [ ] Scope includes targets, allowed methods, data handling, and stopping conditions.
- [ ] Negative authorization cases use two synthetic users/tenants.
- [ ] Attack chains are evaluated as combinations, not only isolated controls.
- [ ] False positives and unverified findings are labeled.

### Common failure modes
A scanner report is mistaken for a pentest; UI restrictions conceal missing server checks; fixing one endpoint leaves an export bypass; destructive tests damage the environment; suppressing a symptom leaves the attacker path intact.

### Concrete examples
Create two local test tenants, each with one invoice. Authenticate as tenant B and request A's known test invoice through detail, search, and export. Each path must deny or omit it without exposing sensitive metadata. Repeat after the fix and verify B can still read B's invoice.

### Verification
Retain a sanitized reproducer, vulnerable/fixed result, affected version, adjacent-case results, and residual risk. If no live test ran, report a code-review finding rather than a confirmed exploit.

### Related skills
[OWASP controls](../references/security-control-catalogue.md), [threat worksheet](../templates/THREAT_MODEL_WORKSHEET.md), [AI defense](ai-evaluation-and-governance.md).

## Applied verification

Define the permitted targets and stop conditions, then reproduce findings with minimal synthetic evidence. Verify the remediation closes the same exploit path and does not simply suppress its observable error.
