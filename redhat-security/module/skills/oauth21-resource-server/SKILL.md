---
name: redhat-security-oauth21-resource-server
description: Enforce MCP servers to act as OAuth 2.1 resource servers by default.
  Use when building, configuring, or reviewing MCP server authentication and authorization
  defaults.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# OAuth 2.1 Resource Server for MCP Servers

## Security Requirement

MCP servers MUST be capable of acting as an OAuth 2.1 resource server, and this MUST be their default behavior. The server should not operate without authentication unless explicitly opted out by the deployer.

## What "Resource Server" Means

As an OAuth 2.1 resource server, the MCP server:

- Accepts and validates OAuth 2.1 access tokens on every request
- Rejects requests without a valid token (401 Unauthorized)
- Enforces scopes from the token against the requested operation
- Publishes its Protected Resource Metadata for client discovery (see `mcp_server/protected-resource-metadata`)

## Default Behavior

| Configuration | Acceptable |
|---|---|
| OAuth 2.1 token validation enabled by default | **Yes (required)** |
| No authentication by default, opt-in OAuth | **No** |
| API key only by default | **No** |
| Open access by default | **No** |

The principle is: **secure by default, opt-out only with explicit configuration**.

## Implementation Checklist

- [ ] Implement OAuth 2.1 resource server capabilities (token validation, scope enforcement)
- [ ] Enable OAuth 2.1 as the default authentication mechanism (not opt-in)
- [ ] Validate access tokens on every incoming request
- [ ] Return 401 Unauthorized for requests without valid tokens
- [ ] Enforce token scopes against the requested operation
- [ ] Publish Protected Resource Metadata (see `mcp_server/protected-resource-metadata`)
- [ ] Allow deployers to configure the authorization server, but not to disable authentication without explicit action
