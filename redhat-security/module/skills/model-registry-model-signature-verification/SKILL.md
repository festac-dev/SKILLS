---
name: redhat-security-model-registry-model-signature-verification
description: Verify model signatures in model registries to validate provenance. Use
  when building, configuring, or reviewing model registries, model upload pipelines,
  or model distribution workflows.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: model-registry
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Model Signature Verification in Model Registries

## Security Requirement

Model registries SHOULD be capable of verifying the cryptographic signature of models to validate their provenance. This ensures that only models from trusted sources are stored and distributed.

## When to Verify

| Event | Action |
|---|---|
| **Model upload** | Verify signature before accepting the model into the registry |
| **Model download** | Provide signature for consumers to verify (or re-verify on their behalf) |
| **Periodic audit** | Re-verify signatures of stored models to detect storage-level tampering |

## Verification Requirements

- Accept models signed with trusted keys only
- Reject or flag models with invalid, expired, or missing signatures
- Log all verification results as security events
- Alert security teams on verification failures
- Support standard signing mechanisms (Sigstore/cosign, GPG, or equivalent)

## Implementation Checklist

- [ ] Implement signature verification on model upload/ingestion
- [ ] Maintain and manage a list of trusted signing keys or certificates
- [ ] Reject models with invalid or missing signatures (or quarantine for review)
- [ ] Store and expose signatures for downstream consumers to verify
- [ ] Log signature verification results (success and failure)
- [ ] Alert on signature verification failures
- [ ] Support periodic re-verification of stored models
