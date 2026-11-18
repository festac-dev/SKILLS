# Specialist: Security and Privacy

Threat-model the actual product, assets, users, integrations and data flows.

Review authentication, authorization, session handling, secrets, input validation, output encoding, injection, SSRF, CSRF, CORS, file uploads, dependency risks, logging, encryption, tenant isolation and abuse controls as relevant.

Apply least privilege and data minimization. Never log secrets. Do not claim compliance or security certification without evidence. Record severity, exploitability, impact, mitigation and residual risk. Obtain authorization before intrusive testing.

## Applied verification

Trace the changed operation across input, authorization, storage and output boundaries. Attempt one realistic forbidden action with synthetic data and inspect logs for leakage; report the exact tested scope instead of broad security claims.

## Focused security resources

For an authorized review, use [application security](application-security-engineering.md), [key management](secrets-and-key-management.md) and the [backend threat checklist](../references/owasp-and-backend-threat-checklist.md) according to the actual attack surface. STRIDE and LINDDUN can structure security and privacy questions; no checklist or framework label proves compliance.
