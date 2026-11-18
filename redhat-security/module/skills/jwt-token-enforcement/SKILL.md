---
name: redhat-security-jwt-token-enforcement
description: Enforce short-lived JWT access token validation for inference engines.
  Use when implementing or reviewing token validation, access control, or request
  authentication in inference engine endpoints.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: inference-engine
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Short-Lived JWT Token Enforcement for Inference Engines

## Security Requirement

Inference engines MUST enforce short-lived JWT access tokens with a maximum TTL of 15 minutes. Tokens MUST be validated against the IdP's JWKS endpoint on every request.

## Required JWT Claims Validation

Every request to the inference engine must include a JWT with the following validated claims:

```json
{
  "iss": "https://your-idp.com",
  "aud": "https://your-engine.com/inference.api",
  "scope": "chat:read inference:write",
  "sub": "user|service-id",
  "exp": "now+15min (maximum)",
  "jti": "unique_id_for_revocation",
  "cnf": "x509-thumbprint"
}
```

## Claim Validation Rules

| Claim | Validation Rule |
|---|---|
| `iss` | MUST match the configured external IdP issuer URL exactly |
| `aud` | MUST match the inference engine's audience identifier |
| `scope` | MUST contain the required scopes for the requested operation |
| `sub` | MUST identify the user or service account making the request |
| `exp` | MUST be present and no more than 15 minutes from `iat` |
| `jti` | MUST be unique; check against revocation blacklist |
| `cnf` | If mTLS is used, MUST match the client certificate thumbprint (sender-constrained token) |

## Implementation Checklist

- [ ] Validate JWT signature against IdP JWKS on every request
- [ ] Reject tokens with `exp` exceeding 15 minutes from issuance
- [ ] Verify `iss` matches the trusted IdP
- [ ] Verify `aud` matches the engine's identifier
- [ ] Check `jti` against revocation blacklist (Redis or local cache)
- [ ] Validate `scope` contains permissions required for the operation
- [ ] If mTLS enabled, verify `cnf` claim matches client certificate
- [ ] Reject tokens missing any required claims
