---
name: agentic-awesome-akf-trust-metadata
description: The AI native file format. EXIF for AI — stamps every file with trust
  scores, source provenance, and compliance metadata. Embeds into 20+ formats (DOCX,
  PDF, images, code). EU AI Act, SOX, HIPAA auditing.
metadata:
  upstream_headers:
    risk: critical
    source: community
    date_added: '2026-03-27'
    author: HMAKT99
    tags:
    - trust
    - metadata
    - provenance
    - compliance
    - file-format
    - ai-native
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# AKF — The AI Native File Format

Every photo has EXIF. Every song has ID3. AKF is the native metadata format for AI-generated content.

## When to Use
Use this skill when you need to stamp, inspect, or audit provenance and trust metadata on AI-generated or AI-modified files for compliance, review, or handoff workflows.

## Scope and Evidence

Use a reviewed, project-pinned installation; inspect the installed CLI help before using version-dependent flags. Stamping modifies files: confirm the target scope, preserve originals and verify metadata plus content integrity afterward. Trust scores and labels are declarations, not independent proof of accuracy or legal compliance. Never stamp “tests pass” unless the actual named checks passed for the exact artifact. Keep confidential data out of metadata that may travel with shared files.

## After creating or modifying files

```bash
akf stamp <file> --agent <agent-name> --evidence "<what you did>"
```

Evidence examples:
- "generated from user prompt"
- "refactored existing code"
- "tests pass"
- "docs reviewed"

## Before modifying existing files

```bash
akf read <file>          # Check existing trust metadata
akf inspect <file>       # See detailed trust scores
```

## Advisory Metadata Checks

The following upstream-style command examples inspect metadata fields. Their output cannot certify regulatory compliance; verify applicability and requirements separately.

```bash
akf audit <file> --regulation eu_ai_act    # EU AI Act Article 50
akf audit <file> --regulation hipaa         # HIPAA
akf audit <file> --regulation sox           # SOX
akf audit <file> --regulation nist_ai       # NIST AI RMF
```

## Classification

- `--label confidential` for finance/secret/internal paths
- `--label public` for README, docs, examples
- Default: `internal`

## Install

```bash
pip install akf
```

## Links

- https://akf.dev
- https://github.com/HMAKT99/AKF
- npm: `npm install akf-format`

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
