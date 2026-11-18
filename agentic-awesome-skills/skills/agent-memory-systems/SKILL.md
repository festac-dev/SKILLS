---
name: agentic-awesome-agent-memory-systems-06089068
description: Design tenant-scoped memory, retrieval and retention for agents. Use
  when planning RAG, conversation history, vector stores or remembering across sessions.
metadata:
  upstream_headers:
    risk: safe
    source: vibeship-spawner-skills (Apache 2.0)
    date_added: 2026-02-27
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Agent Memory Systems

Choose semantic records for facts/preferences, episodic records for events, and procedural records for reusable methods. Keep retrieval quality separate from storage volume and bind persistent access to verified identity.

## Procedure

1. Establish the actual task, authenticated tenant/user, permission to retain content, retention limits and existing store/model versions.
2. Read the guide's tenant-scoped contract and relevant storage/chunking sections. Select an adapter supported by the installed SDK; the guide's historical sketches are not deployable integrations.
3. Specify record IDs, source evidence, timestamps, namespace, retrieval limits and conflict/version policy. Preserve originals and propose consolidation without deletion.
4. Test cross-identity rejection, stale/conflicting records, bounded retrieval and failed writes with isolated fixtures. Benchmark retrieval against held-out questions before expanding storage.
5. Deliver the architecture and evidence-backed change plan, listing unresolved adapters and hosted cost/data destinations. Apply only the persistence or provider operations actually authorized.

## Detailed Guide

Read [the detailed guide](references/detailed-guide.md) before executing this skill. It retains the complete procedure and reference material. Treat its safety, prerequisites, and validation requirements as mandatory. For focused work, load the relevant sections; for end-to-end work, read the guide completely.

## When to Use
- Design memory namespaces and retention for an agent serving distinct tenants or users.
- Diagnose retrieval of stale, conflicting or unauthorized conversation records.
- Plan an embedding/store migration while preserving source records and verifying isolation.

## Example

**Request:** “Our support agent forgets preferences between sessions. Design memory for two customer tenants without sharing their history.”

**Output:** Load the tenant-scoped contract and background-extraction sections. Propose a semantic namespace per verified tenant/user, records with source IDs and revisions, and bounded retrieval. Retain conflicting preferences until the owner resolves them; include tests that tenant B cannot retrieve or consolidate tenant A records. Identify the existing persistent adapter and consent/retention evidence before any write.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
