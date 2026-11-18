---
name: redhat-security-model-registry-secure-storage
description: Enforce authenticated and authorized access to model registry storage.
  Use when deploying, configuring, or reviewing the storage backend for model registries.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: model-registry
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Secure Storage for Model Registries

## Security Requirement

Only authenticated and authorized users MUST be able to access the storage where models are stored. Unauthorized access to model storage can lead to model theft, tampering, or injection of malicious models.

## Required Controls

| Control | Description |
|---|---|
| **Authentication** | All access to storage requires authenticated identity |
| **Authorization** | RBAC controls over read, write, and delete operations |
| **Encryption at rest** | Model files encrypted on the storage backend |
| **Access logging** | All storage access operations logged |
| **Network isolation** | Storage accessible only from authorized networks/services |

## Access Control Matrix

| Role | Read Models | Write/Upload | Delete | Admin |
|---|---|---|---|---|
| Inference engine (service) | Yes | No | No | No |
| ML engineer | Yes | Yes (with approval) | No | No |
| Model pipeline (CI/CD) | Yes | Yes | No | No |
| Registry admin | Yes | Yes | Yes | Yes |
| Unauthorized | No | No | No | No |

## Implementation Checklist

- [ ] Require authentication for all access to model storage
- [ ] Implement RBAC with least-privilege roles for storage operations
- [ ] Enable encryption at rest on the storage backend
- [ ] Restrict network access to storage (internal only, use network policies)
- [ ] Log all storage access operations for audit
- [ ] Regularly audit storage access permissions
- [ ] Disable anonymous or public access to model storage
