# Tool and MCP Engineering Specialist

## When to use
Load for tool schemas, MCP servers/clients, resources, prompts, transport, error contracts, or execution sandboxes. Skip when a task only consumes a stable existing tool.

## Core principles
MCP is an integration protocol, not a permission grant. Advertise only supported capabilities. Separate discovery, validation, authorization, execution, and result rendering. Use narrow tools for consequential actions; the caller must know whether an error happened before or after a side effect.

## Step-by-step procedure
1. Inspect the installed SDK and protocol version, transport, authentication, and client capabilities. Verify against current docs before using version-specific methods.
2. Define typed input/output schemas, required fields, limits, units, and explicit error/retry semantics. Reject extra or ambiguous action fields when they could broaden scope.
3. Scope resources and credentials per user/tenant. Canonicalize paths and destinations before authorization; prevent traversal and unintended redirects.
4. Bound execution time, output bytes, concurrency, and network/filesystem access. Handle cancellation and partial completion.
5. For stdio, send protocol messages on stdout and diagnostics on stderr. Do not mix logs into framing.
6. Contract-test discovery, success, validation failure, denied permission, timeout, cancellation, duplicate mutation, and unavailable dependencies.

## Checklist
- [ ] Discovery describes actual capabilities and schema versions.
- [ ] Errors distinguish invalid input, denial, transient failure, and uncertain side effect.
- [ ] Tools never trust caller-supplied tenant or user identity without authenticated context.
- [ ] Sandbox policy is enforced outside generated code.

## Common failure modes
A generic shell wrapper exceeds task scope; a timeout after commit causes duplicate retries; huge outputs exhaust context; malicious server metadata is treated as authority; network-enabled sandboxes allow unintended exfiltration.

## Concrete examples
Inspect JS dependencies with `npm ls @modelcontextprotocol/sdk` or Python packages with `python -m pip show mcp`; then check the documentation for that installed version. A narrow schema for read-only lookup:
```json
{"type":"object","properties":{"issue_id":{"type":"string","pattern":"^issue-[0-9]+$"}},"required":["issue_id"],"additionalProperties":false}
```
The issue lookup still needs server-side access checks; the pattern does not authorize access.

## Verification
Replay contract cases against an isolated server with synthetic credentials. Assert both returned results and absent unauthorized side effects. Record protocol/SDK versions and transport.

## Related skills
[Agent runtime](../playbooks/AI_AGENT_IMPLEMENTATION_PLAYBOOK.md), [API contracts](api-and-developer-experience.md), [security review](security-architecture-and-red-teaming.md).

## Applied verification

Validate malformed inputs, partial responses, cancellation and a timeout after a mutation commits. Confirm schema errors stay distinguishable from tool failures and that retries reconcile operation identity before repeating side effects.
