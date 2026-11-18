---
name: agentic-awesome-claude-ally-health
description: A health assistant skill for medical information analysis, symptom tracking,
  and wellness guidance.
metadata:
  upstream_headers:
    risk: critical
    source: https://github.com/huifer/Claude-Ally-Health
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Claude Ally Health

## Overview

A health assistant skill for medical information analysis, symptom tracking, and wellness guidance.

## When to Use

Organize user-supplied symptom notes or medical records into a clear timeline and
questions for a qualified clinician; explain supplied terminology with sources.

## Evidence and Privacy Workflow

1. Establish the requested informational task, supplied records, dates and intended
   recipient. Do not infer missing diagnosis, medication, dosage or test results.
2. Separate patient-reported symptoms, documented findings and unresolved questions.
3. Produce a source-linked timeline or appointment summary; mark missing/conflicting
   records explicitly. Keep sensitive records local unless sharing is authorized.
4. For medical explanations, consult current authoritative clinical sources and
   distinguish general information from individualized professional advice.

This entrypoint does not bundle a clinical decision system. It cannot diagnose,
recommend treatment changes, certify wellness or replace urgent medical care.
Do not wait on this workflow when the user reports an apparent medical emergency.
Preserve the original source attribution; the upstream project now redirects to
WellAlly-health and its implementation must be separately reviewed before use.

## Example

**User request:**

> Use @claude-ally-health for this task: A health assistant skill for medical information analysis, symptom tracking, and wellness guidance.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
