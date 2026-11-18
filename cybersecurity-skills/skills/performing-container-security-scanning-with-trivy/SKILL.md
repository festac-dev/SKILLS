---
name: cybersecurity-performing-container-security-scanning-with-trivy
description: 'Runs Trivy across every target type it supports - container images,
  filesystems, Git repositories, and Kubernetes clusters - for OS and dependency vulnerabilities,
  IaC misconfiguration, exposed secrets, and licences, generating CycloneDX or SPDX
  SBOMs. Use when integrating Trivy into CI/CD, deploying the Trivy Kubernetes operator,
  scanning non-image targets, or triaging results at scale. Keywords: Trivy, trivy
  k8s, operator, SBOM, CycloneDX, SPDX, misconfig, secret scanning. Do not use for
  a single Docker image scan - use scanning-docker-images-with-trivy.'
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: container-security
    tags:
    - trivy
    - container-security
    - vulnerability-scanning
    - sbom
    - docker
    - kubernetes
    - devsecops
    - supply-chain
    version: '1.0'
    author: mahipal
    nist_csf:
    - PR.PS-01
    - PR.IR-01
    - ID.AM-08
    - DE.CM-01
    mitre_attack:
    - T1610
    - T1611
    - T1609
    - T1525
    - T1195
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Performing Container Security Scanning with Trivy

## Overview

Trivy is an open-source security scanner by Aqua Security that detects vulnerabilities in OS packages and language-specific dependencies, infrastructure-as-code misconfigurations, exposed secrets, and software license issues across container images, filesystems, Git repositories, and Kubernetes clusters. Trivy generates Software Bill of Materials (SBOM) in CycloneDX and SPDX formats for supply chain transparency. This skill covers comprehensive container image scanning, CI/CD pipeline integration, Kubernetes operator deployment, and scan result triage for security operations.


## When to Use

- When conducting security assessments that involve performing container security scanning with trivy
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Trivy v0.50+ installed (binary, Docker, or Homebrew)
- Docker daemon access for local image scanning
- Container registry credentials for remote image scanning
- CI/CD platform (GitHub Actions, GitLab CI, Jenkins) for pipeline integration
- Kubernetes cluster for Trivy Operator deployment (optional)

## Steps

### Step 1: Scan Container Images

Run vulnerability and secret scanning against container images from local builds or remote registries. Configure severity thresholds and ignore unfixed vulnerabilities.

### Step 2: Generate SBOM

Produce CycloneDX or SPDX SBOM documents from scanned images for supply chain compliance and vulnerability tracking across the software lifecycle.

### Step 3: Scan IaC and Kubernetes Manifests

Detect misconfigurations in Dockerfiles, Kubernetes YAML, Terraform, and Helm charts using built-in policy checks aligned with CIS benchmarks.

### Step 4: Integrate into CI/CD

Add Trivy scanning as a pipeline gate that blocks builds with critical/high vulnerabilities, generates SARIF reports for GitHub Advanced Security, and produces JUnit XML for test dashboards.

## Expected Output

JSON/table report listing CVEs with severity, CVSS scores, fixed versions, affected packages, misconfiguration findings, and exposed secrets with file locations.
