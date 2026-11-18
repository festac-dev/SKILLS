---
name: redhat-security-mcp-client-protected-resource-metadata
description: Enforce use of OAuth 2.0 Protected Resource Metadata in MCP clients for
  discovering authorization servers. Use when building or reviewing MCP client authentication
  flows and authorization server discovery.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-client
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Protected Resource Metadata Usage in MCP Clients

## Security Requirement

MCP clients MUST use OAuth 2.0 Protected Resource Metadata (RFC 9728) to discover the authorized authorization servers for any MCP server they connect to. Clients MUST NOT hardcode or manually configure authorization server URLs when the MCP server provides Protected Resource Metadata.

## Discovery Flow

```
1. MCP client attempts to access MCP server resource
2. MCP server returns 401 with WWW-Authenticate header
3. MCP client fetches /.well-known/oauth-protected-resource from MCP server
4. Extract authorization_servers list from the metadata
5. Use the authorization server(s) listed for token acquisition
6. Authenticate with the authorization server and obtain token
7. Retry the original request with the obtained token
```

## Metadata Fields to Consume

| Field | Usage |
|---|---|
| `authorization_servers` | List of trusted authorization server URLs to use |
| `scopes_supported` | Available scopes to request during authorization |
| `bearer_methods_supported` | How to present the bearer token (e.g., `header`) |

## Implementation Checklist

- [ ] On 401 response, fetch `/.well-known/oauth-protected-resource` from the MCP server
- [ ] Parse the `authorization_servers` field and select appropriate server
- [ ] Use `scopes_supported` to inform scope requests
- [ ] Respect `bearer_methods_supported` when presenting tokens
- [ ] Cache the metadata with appropriate TTL to avoid repeated lookups
- [ ] Re-fetch metadata when authorization fails after token refresh
