---
name: redhat-security-protected-resource-metadata
description: Enforce OAuth 2.0 Protected Resource Metadata implementation in MCP servers.
  Use when building, configuring, or reviewing MCP server authentication and authorization
  discovery.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Protected Resource Metadata for MCP Servers

## Security Requirement

MCP servers MUST implement OAuth 2.0 Protected Resource Metadata (RFC 9728). MCP clients MUST use this metadata to discover the authorized authorization servers for a given MCP server.

## What It Provides

Protected Resource Metadata allows MCP clients to discover:
- Which authorization servers are trusted by the MCP server
- What scopes are available (`scopes_supported`)
- What token formats and mechanisms are required

## Implementation Checklist

- [ ] Expose a `/.well-known/oauth-protected-resource` endpoint
- [ ] Include `resource` identifier matching the MCP server's URL
- [ ] List all trusted authorization servers in `authorization_servers`
- [ ] Publish `scopes_supported` for available permissions
- [ ] Ensure metadata is served over HTTPS
- [ ] Keep metadata up to date when authorization configuration changes

## Example: Protected Resource Metadata Response

```json
{
  "resource": "https://mcp-server.example.com",
  "authorization_servers": [
    "https://auth.example.com"
  ],
  "scopes_supported": [
    "tools:read",
    "tools:execute",
    "resources:read"
  ],
  "bearer_methods_supported": ["header"],
  "resource_documentation": "https://docs.example.com/mcp-api"
}
```
