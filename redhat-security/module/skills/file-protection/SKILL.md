---
name: redhat-security-file-protection
description: Protect LLM model files against unauthorized access and modification.
  Use when designing, deploying, or reviewing storage and access controls for AI model
  files and weights.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: large-language-model
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# LLM File Protection

## Security Requirement

Large Language Models are composed of files (weights, configuration, tokenizer, etc.) loaded by the inference engine. These files MUST be protected against unauthorized access and modification.

## Risks of Unprotected Model Files

| Risk | Impact |
|---|---|
| **Unauthorized access** | Model theft, intellectual property loss |
| **Unauthorized modification** | Backdoored or poisoned model served to users |
| **Tampering** | Modified weights producing biased, harmful, or incorrect outputs |
| **Data extraction** | Extracting sensitive training data embedded in model weights |

## Required Controls

| Control | Description |
|---|---|
| **Access control** | Only authorized users and services can read model files |
| **Write protection** | Only authorized pipelines can modify model files |
| **Integrity verification** | Detect unauthorized modifications via checksums or signatures |
| **Encryption at rest** | Encrypt model files on disk to protect against storage-level access |
| **Audit logging** | Log all access to model files |

## Implementation Checklist

- [ ] Store model files in access-controlled storage (not world-readable)
- [ ] Grant read access only to the inference engine service account
- [ ] Grant write access only to authorized model deployment pipelines
- [ ] Mount model files as read-only in the inference engine container
- [ ] Enable encryption at rest for model storage volumes
- [ ] Implement integrity checks (checksums or signatures) verified at load time
- [ ] Log all access to model files for audit
- [ ] Regularly audit file permissions and access patterns
