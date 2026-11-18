---
name: redhat-security-no-credential-forwarding
description: Prevent MCP servers from forwarding user credentials or tokens to downstream
  tools. Use when building, reviewing, or auditing MCP server integrations with external
  tools or APIs.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# No Credential Forwarding in MCP Servers

## Security Requirement

MCP servers MUST NOT forward any credentials or authentication tokens received from users to downstream tools or third-party APIs. This is explicitly forbidden by the MCP specification and has a high security impact.

## Risks of Credential Forwarding

- **Token leakage**: User tokens exposed to third-party services
- **Confused deputy attacks**: Third-party services may use the user's token to access resources beyond what the MCP server intended
- **Excessive privilege**: Downstream tools receive user-level access when they only need scoped tool-level access
- **Audit trail corruption**: Actions performed by tools are attributed to the user instead of the MCP server

## Required Approach

Instead of forwarding user tokens, MCP servers MUST obtain separate credentials for downstream services through one of:

1. **OAuth client flows**: MCP server acts as an OAuth client and initiates its own OAuth flow to obtain tokens for third-party APIs
2. **Pre-registered service accounts**: Use API keys or service accounts registered specifically for the MCP server
3. **Token Exchange** (preferred): See the `token-exchange-for-tools` skill for the recommended approach

## Implementation Checklist

- [ ] Audit all outbound requests from the MCP server to external services
- [ ] Verify no user tokens are included in any outbound request headers, query parameters, or bodies
- [ ] Implement separate credential management for each downstream API
- [ ] Add automated tests that verify user tokens are never forwarded
- [ ] Log outbound requests (excluding sensitive headers) for security audit

## Anti-Pattern

```
# FORBIDDEN - never do this
def call_external_tool(user_token, tool_url, params):
    headers = {"Authorization": f"Bearer {user_token}"}  # WRONG
    return requests.post(tool_url, headers=headers, json=params)
```

## Correct Pattern

```
# CORRECT - use MCP server's own credentials
def call_external_tool(tool_url, params):
    server_token = get_server_credential_for(tool_url)
    headers = {"Authorization": f"Bearer {server_token}"}
    return requests.post(tool_url, headers=headers, json=params)
```
