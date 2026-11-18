---
name: redhat-security-request-validation
description: Enforce request validation and filtering at the API gateway for AI systems.
  Use when designing, building, or reviewing API gateways that protect inference engines,
  guardrails, or prompt orchestrators.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: api-gateway
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Request Validation at the API Gateway

## Security Requirement

API gateways SHOULD validate incoming requests and filter malformed ones before dispatching them to downstream components. This prevents specially crafted requests from exploiting vulnerabilities in the systems behind the gateway.

## Components Protected

By filtering at the gateway, the following downstream components are shielded from malformed input:

- Guardrails component
- Prompt orchestrator
- Inference engine
- Models themselves

## Validation Controls

| Control | Description |
|---|---|
| **Schema validation** | Validate request body against the expected API schema (e.g., OpenAPI spec) |
| **Content-Type enforcement** | Reject requests with unexpected or missing Content-Type headers |
| **Payload size limits** | Enforce maximum request body size to prevent resource exhaustion |
| **Character encoding validation** | Ensure proper encoding, reject unexpected encodings |
| **Header validation** | Validate required headers are present and well-formed |
| **Path traversal prevention** | Block requests with path traversal patterns |
| **Input length limits** | Enforce maximum prompt length / token count at the gateway |

## Implementation Checklist

- [ ] Define and enforce API schema validation (OpenAPI or equivalent)
- [ ] Set maximum payload size limits appropriate for the model input
- [ ] Validate Content-Type headers on all requests
- [ ] Enforce character encoding standards (UTF-8)
- [ ] Block requests with path traversal patterns or injection attempts
- [ ] Set maximum prompt/input length limits
- [ ] Log rejected requests with reason for security monitoring
- [ ] Return appropriate HTTP error codes (400, 413, 415) for validation failures
