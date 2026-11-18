---
name: redhat-security-discovery-mechanism
description: Enforce authorization server metadata discovery for MCP ecosystems. Use
  when configuring or reviewing authorization server endpoint publication and discovery
  metadata.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: authorization-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Discovery Mechanism for Authorization Servers

## Security Requirement

Authorization servers MUST provide at least one of the following discovery mechanisms:

1. **OAuth 2.0 Authorization Server Metadata** (RFC 8414)
2. **OpenID Connect Discovery 1.0**

MCP clients are required to support both, so the authorization server MUST implement at least one to ensure interoperability.

## Option 1: OAuth 2.0 Authorization Server Metadata (RFC 8414)

Expose metadata at `/.well-known/oauth-authorization-server`:

```json
{
  "issuer": "https://auth.example.com",
  "authorization_endpoint": "https://auth.example.com/authorize",
  "token_endpoint": "https://auth.example.com/token",
  "registration_endpoint": "https://auth.example.com/register",
  "revocation_endpoint": "https://auth.example.com/oauth/revoke",
  "scopes_supported": ["openid", "tools:read", "tools:execute"],
  "response_types_supported": ["code"],
  "grant_types_supported": ["authorization_code", "client_credentials", "urn:ietf:params:oauth:grant-type:device_code"],
  "code_challenge_methods_supported": ["S256"],
  "token_endpoint_auth_methods_supported": ["client_secret_basic", "none"]
}
```

## Option 2: OpenID Connect Discovery 1.0

Expose metadata at `/.well-known/openid-configuration`:

```json
{
  "issuer": "https://auth.example.com",
  "authorization_endpoint": "https://auth.example.com/authorize",
  "token_endpoint": "https://auth.example.com/token",
  "userinfo_endpoint": "https://auth.example.com/userinfo",
  "jwks_uri": "https://auth.example.com/.well-known/jwks.json",
  "registration_endpoint": "https://auth.example.com/register",
  "scopes_supported": ["openid", "profile", "tools:read", "tools:execute"],
  "response_types_supported": ["code"],
  "id_token_signing_alg_values_supported": ["RS256"]
}
```

## Implementation Checklist

- [ ] Implement at least one discovery endpoint (RFC 8414 or OIDC Discovery)
- [ ] Ensure `issuer` field matches the authorization server's canonical URL
- [ ] List all supported grant types, scopes, and response types
- [ ] Include `registration_endpoint` if Dynamic Client Registration is supported
- [ ] Include `revocation_endpoint` for token revocation
- [ ] Serve metadata over HTTPS
- [ ] Keep metadata up to date when server configuration changes
