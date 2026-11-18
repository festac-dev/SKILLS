---
name: redhat-security-oauth-scopes-handling
description: Handle OAuth scopes in MCP clients according to the WWW-Authenticate
  header and Protected Resource Metadata discovery flow. Use when building or reviewing
  MCP client authorization flows, scope negotiation, or permission handling.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-client
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# OAuth Scopes Handling in MCP Clients

## Security Requirement

MCP clients MUST discover and use OAuth scopes from the WWW-Authenticate header or Protected Resource Metadata when authenticating to MCP servers. Scopes define the permissions the client is requesting and MUST be handled as follows:

## Scope Discovery Priority

1. **WWW-Authenticate header**: If the MCP client receives a `scope` parameter in the `WWW-Authenticate` header of a 401 response, it MUST use those scopes.
2. **Protected Resource Metadata**: If no scope is provided in the 401 response, check `scopes_supported` in the Protected Resource Metadata (PRM) document.

## Flow

```
1. MCP client attempts to access MCP server resource
2. MCP server returns 401 Unauthorized with:
   WWW-Authenticate: Bearer realm="mcp", scope="tools:read tools:execute"
3. MCP client extracts scope from WWW-Authenticate header
   → If scope present: use those scopes for authorization request
   → If scope absent: fetch PRM and use scopes_supported
4. MCP client requests authorization with the discovered scopes
```

## Example: WWW-Authenticate with Scope

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer realm="mcp-server",
  scope="tools:read tools:execute resources:read"
```

The client should request exactly these scopes (or a subset) from the authorization server.

## Implementation Checklist

- [ ] Parse `scope` parameter from `WWW-Authenticate` header on 401 responses
- [ ] Fall back to `scopes_supported` from Protected Resource Metadata if no scope in 401
- [ ] Request only the scopes needed for the intended operation (principle of least privilege)
- [ ] Handle scope downgrading by checking granted scopes against requested scopes and disabling features that lack authorization (authorization server may grant fewer scopes)
- [ ] Re-request scopes if the server indicates insufficient permissions on subsequent requests
