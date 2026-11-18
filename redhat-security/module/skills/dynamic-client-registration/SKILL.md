---
name: redhat-security-dynamic-client-registration
description: Support OAuth 2.0 Dynamic Client Registration in authorization servers.
  Use when building or reviewing authorization server client management for MCP ecosystems.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: authorization-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Dynamic Client Registration for Authorization Servers

## Security Recommendation

Authorization servers MAY support the OAuth 2.0 Dynamic Client Registration Protocol (RFC 7591). This allows MCP clients to register automatically without manual intervention.

## Registration Endpoint

If supported, the authorization server MUST expose a `registration_endpoint` in its discovery metadata and handle registration requests per RFC 7591.

## Example Registration Request

```http
POST /register HTTP/1.1
Host: auth.example.com
Content-Type: application/json

{
  "client_name": "MCP Client App",
  "redirect_uris": ["https://client.example.com/callback"],
  "grant_types": ["authorization_code"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "none",
  "scope": "tools:read tools:execute"
}
```

## Example Registration Response

```json
{
  "client_id": "generated-client-id",
  "client_id_issued_at": 1700000000,
  "redirect_uris": ["https://client.example.com/callback"],
  "grant_types": ["authorization_code"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "none"
}
```

## Security Considerations

| Concern | Mitigation |
|---|---|
| Abuse/spam registrations | Rate limit registration endpoint, require initial access tokens |
| Malicious redirect URIs | Validate redirect URIs strictly (HTTPS, no open redirectors) |
| Resource exhaustion | Limit number of registrations per IP/token, expire unused registrations |
| Privilege escalation | Only grant requested scopes that are within the server's allowed set |

## Implementation Checklist

- [ ] Expose `registration_endpoint` in discovery metadata
- [ ] Implement RFC 7591 registration request processing
- [ ] Validate all client metadata fields per OAuth 2.1 requirements
- [ ] Enforce HTTPS-only redirect URIs
- [ ] Rate limit registration requests
- [ ] Optionally require initial access tokens for registration
- [ ] Auto-expire inactive client registrations
- [ ] Log all registration events for audit
