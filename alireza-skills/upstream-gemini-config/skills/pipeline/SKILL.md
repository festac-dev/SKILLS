---
name: alireza-pipeline
description: 'Detect stack and generate CI/CD pipeline configs. Usage: /pipeline <detect|generate>
  [options]'
metadata:
  upstream_headers:
    argument-hint: <detect|generate> [options]
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# /pipeline

Detect project stack and generate CI/CD pipeline configurations for GitHub Actions or GitLab CI.

## Usage

```
/pipeline detect [--repo <project-dir>]               Detect stack, tools, and services
/pipeline generate --platform github|gitlab [--repo <project-dir>]  Generate pipeline YAML
```

## Examples

```
/pipeline detect --repo ./my-project
/pipeline generate --platform github --repo .
/pipeline generate --platform gitlab --repo .
```

## Scripts
- `engineering/skills/ci-cd-pipeline-builder/scripts/stack_detector.py` — Detect stack and tooling (`--repo <path>`, `--format text|json`)
- `engineering/skills/ci-cd-pipeline-builder/scripts/pipeline_generator.py` — Generate pipeline YAML (`--platform github|gitlab`, `--repo <path>`, `--input <stack.json>`, `--output <file>`)

## Skill Reference
→ `engineering/skills/ci-cd-pipeline-builder/SKILL.md`
