---
name: microsoft-azure-kubernetes-app-deploy
description: 'Use when deploying an existing web application or API to an already-running
  Azure Kubernetes Service cluster. Detects the framework, generates a Dockerfile
  and Kubernetes manifests, validates against AKS Deployment Safeguards, and deploys
  with verification. WHEN: deploy app to AKS, deploy to existing AKS cluster, containerize
  app for Kubernetes, generate K8s manifests for Azure, set up CI/CD for AKS, my AKS
  deployment is failing safeguard checks, I have a Django/Express/Spring Boot app
  to run on AKS. DO NOT USE FOR: creating or provisioning an AKS cluster (use azure-kubernetes),
  assessing migration to AKS Automatic (use azure-kubernetes-automatic-readiness),
  or deploying to non-AKS targets like Web Apps, Container Apps, or Functions.'
license: MIT
metadata:
  author: Microsoft
  version: 1.0.0
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Deploy to AKS

**Use when:** deploying a web app/API to AKS; containerizing for Kubernetes; generating manifests; AKS CI/CD; DS001–DS013 failures.

**Not for:** provisioning clusters (`azure-kubernetes`), AKS Automatic readiness (`azure-kubernetes-automatic-readiness`), non-AKS targets.

## Workflow

Requires: existing AKS cluster, `az login`, `kubectl` configured. Follow `phases/quick-deploy.md`. On failure: `references/rollback.md`.

## References

- [detection.md](./references/detection.md) — framework/port/health detection
- [safeguards.md](./references/safeguards.md) — DS001-DS013 checklist
- [workload-identity.md](./references/workload-identity.md) — Workload Identity setup
- [rollback.md](./references/rollback.md) — recovery procedures
- [base-images.md](./references/base-images.md) — base image policy and `<LATEST_STABLE_*>` resolution

## Knowledge Packs

Load `knowledge-packs/frameworks/<framework>.md` per detected framework. Available: `spring-boot`, `express`, `nextjs`, `fastapi`, `django`, `nestjs`, `aspnet-core`, `go`, `flask`

## Templates

`templates/` (dockerfiles/, k8s/, github-actions/, mermaid/).
