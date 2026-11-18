---
name: redhat-security-secure-pipeline
description: Enforce SAST and SCA in CI/CD pipelines for AI software. Use when building,
  configuring, or reviewing CI/CD pipelines for MCP servers, inference engines, or
  any AI system components.
metadata:
  upstream_headers:
    category: secure_development
    subcategory: supply-chain
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Secure CI/CD Pipeline

## Security Requirement

CI/CD pipelines for AI software MUST implement security scanning to catch vulnerabilities before they reach production.

## Required Scanning Types

### SAST (Static Application Security Testing)

Analyze source code for security vulnerabilities without executing it:

| What SAST Catches | Examples |
|---|---|
| Injection vulnerabilities | SQL injection, command injection, XSS |
| Hardcoded secrets | API keys, passwords in source code |
| Insecure configurations | Weak crypto, disabled TLS verification |
| Code quality issues | Buffer overflows, null dereferences |

### SCA (Software Composition Analysis)

Analyze third-party dependencies for known vulnerabilities:

| What SCA Catches | Examples |
|---|---|
| Known CVEs | Vulnerabilities in libraries and frameworks |
| License compliance | Incompatible or problematic licenses |
| Outdated dependencies | Libraries with available security patches |
| Transitive vulnerabilities | Vulnerabilities in dependencies of dependencies |

## Pipeline Integration

```
Source code commit
  → SAST scan (analyze source code)
  → SCA scan (analyze dependencies)
  → Unit tests
  → Build artifacts
  → Container image scan
  → Sign artifacts
  → Generate SBOM
  → Deploy (if all checks pass)
```

## Implementation Checklist

- [ ] Integrate SAST scanning into the CI/CD pipeline (run on every PR/commit)
- [ ] Integrate SCA scanning into the CI/CD pipeline
- [ ] Fail the build on high/critical severity findings
- [ ] Scan container images for vulnerabilities before pushing to registry
- [ ] Configure alerts for newly discovered CVEs in dependencies
- [ ] Review and triage SAST/SCA findings regularly
- [ ] Maintain suppression/allowlists for accepted risks (documented and time-limited)
