---
name: redhat-security-input-output-sanitization
description: Enforce input and output sanitization in MCP servers. Use when building
  or reviewing MCP server request handling, tool invocation, or response processing.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: mcp-server
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Input/Output Sanitization for MCP Servers

## Security Requirement

MCP servers MUST treat all inputs as untrusted, including:

- User-provided parameters
- Prompt-driven parameters (values determined by the LLM)
- Descriptions and outputs from other tools
- Any data that flows through the MCP protocol

## Input Sanitization

| Input Source | Risk | Sanitization |
|---|---|---|
| **User parameters** | Injection, path traversal, XSS | Validate type, length, format; reject unexpected values |
| **LLM-generated parameters** | Prompt injection artifacts, malformed data | Same validation as user input; never trust LLM output implicitly |
| **Tool outputs used as inputs** | Poisoned tool chains, injection propagation | Validate before passing to next tool; treat as untrusted |
| **File paths** | Path traversal, symlink attacks | Canonicalize and validate against allowed directories |

## Output Sanitization

Tool outputs returned to clients or passed to other tools must also be sanitized:

- Strip or escape content that could be interpreted as code or commands
- Validate output format matches the expected schema
- Truncate excessively large outputs to prevent resource exhaustion
- Scrub sensitive data from outputs before returning to clients

## Key Principle

Never assume any input is safe because it came from "inside" the system. LLM-generated content and inter-tool communication are just as untrusted as external user input.

## Implementation Checklist

- [ ] Validate all input parameters (type, length, format, allowed values)
- [ ] Treat LLM-generated parameters as untrusted input
- [ ] Treat outputs from other tools as untrusted input
- [ ] Implement path traversal prevention for any file path parameters
- [ ] Sanitize outputs before returning to clients
- [ ] Validate output format against expected schemas
- [ ] Truncate excessively large outputs
- [ ] Log sanitization actions (blocked or modified inputs) for security monitoring
