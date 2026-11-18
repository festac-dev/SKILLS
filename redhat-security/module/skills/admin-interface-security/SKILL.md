---
name: redhat-security-admin-interface-security
description: Secure the administrative interface of model registries. Use when building,
  deploying, or reviewing model registry access controls and admin interfaces.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: model-registry
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Model Registry Administrative Interface Security

## Security Requirement

If the model registry has an administrative interface, only identified, authenticated, and authorized users MUST be able to connect to it.

## Required Controls

| Control | Description |
|---|---|
| **Identification** | Every admin user must have a unique identity (no shared accounts) |
| **Authentication** | Standard authentication mechanism (OIDC/OAuth 2.1 recommended) |
| **Authorization** | RBAC or ABAC to control which admin operations each user can perform |
| **Multi-factor authentication** | MFA recommended for administrative access |
| **Session management** | Short-lived sessions with automatic timeout |

## Admin Operations to Protect

| Operation | Risk |
|---|---|
| Model upload/publish | Introducing malicious or backdoored models |
| Model deletion | Removing approved models, causing service disruption |
| Access control changes | Granting unauthorized users access to models |
| Configuration changes | Weakening security settings |
| Registry metadata modification | Altering model provenance information |

## Implementation Checklist

- [ ] Require authentication for all administrative access (no anonymous admin)
- [ ] Integrate with OIDC Identity Provider for admin authentication
- [ ] Implement RBAC with least-privilege roles for admin operations
- [ ] Enforce MFA for admin accounts
- [ ] Use short-lived sessions with automatic timeout
- [ ] Log all administrative actions with the authenticated user's identity
- [ ] Restrict admin interface to internal networks or VPN unless external access is a documented requirement
- [ ] Disable default/shared admin accounts
