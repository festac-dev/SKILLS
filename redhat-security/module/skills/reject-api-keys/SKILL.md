---
name: redhat-security-reject-api-keys
description: Reject raw API key authentication in inference engines. Use when designing,
  reviewing, or auditing authentication mechanisms for inference engines or LLM API
  endpoints in production environments.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: inference-engine
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Reject Raw API Keys in Inference Engines

## Security Requirement

Inference engines MUST reject raw API keys as an authentication mechanism. If legacy interoperability requires API key support, the inference engine (or an API gateway in front of it) MUST proxy and convert API keys into short-lived IdP-issued tokens before processing the request.

## Rationale

API keys present significant security risks in production:
- Typically long-lived, increasing exposure window if compromised
- Difficult to rotate across distributed systems
- Lack fine-grained scoping and sender binding
- Cannot be revoked instantly without infrastructure support
- Do not carry identity claims needed for audit trails

## Acceptable Approach for Legacy Interop

When legacy systems require API key authentication:

```
Client sends API key
  → API Gateway intercepts
  → Gateway exchanges API key for short-lived IdP token
    (via client_credentials or token exchange)
  → Gateway forwards IdP token to inference engine
  → Inference engine validates IdP token (never sees API key)
```

## Implementation Checklist

- [ ] Configure inference engine to reject requests authenticated only with API keys
- [ ] If legacy API key support needed, deploy an API gateway as a proxy
- [ ] Gateway exchanges API keys for short-lived IdP tokens (TTL ≤15min)
- [ ] Map API keys to specific service accounts in the IdP
- [ ] Log API key usage for migration tracking
- [ ] Set a deprecation timeline for API key consumers to migrate to OIDC
