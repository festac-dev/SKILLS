---
name: redhat-security-roots-support
description: Enforce roots directive support in MCP servers. Use when building or
  reviewing MCP server filesystem access, directory scoping, or path boundary enforcement.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Roots Support for MCP Servers

## Security Requirement

MCP servers MUST support the roots directive and respect root boundaries during all operations. The roots directive defines the allowed filesystem boundaries within which the MCP server can operate.

## What Roots Provide

The roots mechanism allows MCP clients to declare which directories or resources the server is authorized to access. The server must:

- Accept the roots declaration from the client
- Constrain all operations to within the declared roots
- Reject any operation that would access resources outside the declared roots
- Never traverse above or outside root boundaries (no path traversal)

## Boundary Enforcement

```
Declared root: /home/user/project

Allowed:
  /home/user/project/src/main.py       ✓ (within root)
  /home/user/project/docs/readme.md    ✓ (within root)

Blocked:
  /home/user/.ssh/id_rsa               ✗ (outside root)
  /home/user/project/../.ssh/id_rsa    ✗ (traversal outside root)
  /etc/passwd                           ✗ (outside root)
```

## Implementation Checklist

- [ ] Implement support for the MCP roots directive
- [ ] Accept and store root declarations from clients
- [ ] Canonicalize all file paths before checking root boundaries (resolve symlinks, `..`, etc.)
- [ ] Reject operations targeting resources outside declared roots
- [ ] Prevent symlink-based escapes from root boundaries
- [ ] Default to no filesystem access if no roots are declared
- [ ] Log root boundary violations as security events
