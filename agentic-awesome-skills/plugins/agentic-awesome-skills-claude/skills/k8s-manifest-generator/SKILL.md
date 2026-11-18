---
name: agentic-awesome-k8s-manifest-generator-aaec56a0
description: Step-by-step guidance for creating production-ready Kubernetes manifests
  including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Kubernetes Manifest Generator

Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and PersistentVolumeClaims.

## Use this skill when

Use this skill when you need to:
- Create new Kubernetes Deployment manifests
- Define Service resources for network connectivity
- Generate ConfigMap and Secret resources for configuration management
- Create PersistentVolumeClaim manifests for stateful workloads
- Follow Kubernetes best practices and naming conventions
- Implement resource limits, health checks, and security contexts
- Design manifests for multi-environment deployments

## Do not use this skill when

- The task is unrelated to kubernetes manifest generator
- You need a different domain or tool outside this scope

## Deployment boundaries

These are illustrative fragments, not validated production manifests. Resolve placeholders, pin images, select supported APIs/controllers for the target cluster, and verify ServiceAccount, storage, secrets, ports and probes. Generating files does not authorize kubectl apply, debug Pods, load balancers, migrations or credential reads. Confirm target context and namespace before authorized operations; server dry-run still contacts admission webhooks. Keep secrets out of Git and logs. ConfigMap/Secret environment updates do not refresh existing processes automatically. Replicas and maxUnavailable alone do not guarantee availability. Never apply all template variants together.

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
