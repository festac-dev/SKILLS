---
name: redhat-security-rbac
description: Implement role-based access control in MCP servers by mapping token claims
  to internal roles. Use when building or reviewing MCP server authorization, permission
  models, or access control enforcement.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Role-Based Access Control (RBAC) for MCP Servers

## Security Recommendation

MCP servers SHOULD implement RBAC as a defense-in-depth layer by mapping token claims to internal application roles. This adds authorization beyond what OAuth scopes alone provide.

## How It Works

1. The IdP issues a token with claims (e.g., `roles`, `groups`, or custom claims)
2. The MCP server maps those claims to internal roles
3. Internal roles determine which tools and operations are available

## Example Token-to-Role Mapping

Token claim:
```json
{
  "sub": "user-123",
  "realm_access": {
    "roles": ["mcp-admin", "data-reader"]
  }
}
```

MCP server role mapping:
```yaml
rbac:
  role_mappings:
    admin:
      token_claim: "realm_access.roles"
      claim_value: "mcp-admin"
      permissions: ["tools:*", "config:*"]
    reader:
      token_claim: "realm_access.roles"
      claim_value: "data-reader"
      permissions: ["tools:read", "resources:read"]
    default:
      permissions: ["tools:list"]
```

## Defense-in-Depth Value

| Layer | Control |
|---|---|
| **OAuth scopes** | What the token is authorized for (coarse-grained) |
| **RBAC roles** | What the user's role allows within the application (fine-grained) |
| **Tool-level checks** | What the specific tool permits for this role |

All three layers must agree for an operation to proceed.

## Implementation Checklist

- [ ] Define internal roles relevant to the MCP server (e.g., admin, operator, reader)
- [ ] Map IdP token claims (roles, groups, custom claims) to internal roles
- [ ] Enforce RBAC checks on every tool invocation alongside scope checks
- [ ] Default to the least-privileged role when no matching claim is found
- [ ] Log role-based authorization decisions (grants and denials)
- [ ] Document the role definitions and their permissions
- [ ] Regularly review and audit role assignments
