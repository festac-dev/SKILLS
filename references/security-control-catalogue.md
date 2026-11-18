# Security Control Catalogue

## Identity and access
MFA where appropriate, secure recovery, session rotation/revocation, least privilege, scoped service identities, authorization checks on every object, and tenant isolation.

## Application security
Input validation, output encoding, parameterized queries, CSRF defenses where relevant, safe file processing, SSRF controls, secure redirects, rate limits, and abuse-resistant workflows.

## Data protection
Classification, minimization, encryption in transit/at rest, key management, secret rotation, retention, deletion, backup protection, and access audit.

## Infrastructure and delivery
Hardened images, patching, network boundaries, CI isolation, signed artifacts, dependency review, vulnerability management, and protected deployment credentials.

## Detection and response
Structured security events, alert ownership, incident playbooks, evidence preservation, customer communication, and recovery exercises.

Controls must be selected for the threat model and verified. A checklist alone does not establish security.

## OWASP control selection and verification

### When to use
Use for application security requirements or a release review. Treat OWASP Top 10 as awareness categories and ASVS as a source of versioned, testable requirements.

### Core principles
Select controls from assets, threats, exposure, and assurance needs. Record the ASVS version and requirement IDs from the current source; do not invent IDs or claim compliance from broad coverage.

### Step-by-step procedure
1. Inventory entrypoints, trust boundaries, authentication, sensitive records, and external calls.
2. Map threats to concrete controls: parameterized queries, context-appropriate encoding, object authorization, CSRF protection for relevant cookie flows, upload isolation, SSRF egress controls, and bounded consumption.
3. Choose applicable ASVS requirements with an owner, implementation location, and test.
4. Review browser security headers and session controls in context; CORS is not authorization and SameSite is not a universal CSRF solution.
5. Verify fail-closed behavior at permission boundaries and explicit recovery for ordinary failures.

### Checklist
- [ ] Server-side checks protect every entrypoint.
- [ ] Redirects, uploads, and outbound requests have explicit constraints.
- [ ] Tokens, session identifiers, and PII are redacted.
- [ ] Security requirements map to evidence and exceptions.

### Common failure modes
A Top 10 checklist substitutes for threat modeling; input validation is mistaken for output encoding; security headers hide broken access control; denied operations still leak through counts or caches.

### Concrete examples
Read-only header inspection of an authorized local service: `curl --head --fail http://127.0.0.1:8000/`. This checks response headers only; it does not prove XSS, CSRF, or authorization protection. Consult [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) for current versioned controls.

### Verification
Record requirement version/ID, exact behavior tested, build, result, and limitation. Include negative tests and cross-entrypoint cases.

### Related skills
[Threat review](../specialists/security-architecture-and-red-teaming.md), [identity](../specialists/identity-and-access-management.md), [supply chain](../specialists/supply-chain-and-build-security.md).

## Application evidence

Choose controls from the actual changed trust boundary and record the standard/version only when assessed. Pair each material control claim with a negative test or configuration observation; a completed generic checklist is not an attestation.
