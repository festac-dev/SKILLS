---
name: agentic-awesome-vector-index-tuning-f8dc6bed
description: Optimize vector index performance for latency, recall, and memory. Use
  when tuning HNSW parameters, selecting quantization strategies, or scaling vector
  search infrastructure.
metadata:
  upstream_headers:
    risk: safe
    source: community
    date_added: '2026-02-27'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Vector Index Tuning

Guide to optimizing vector indexes for production performance.

## Use this skill when

- Tuning HNSW parameters
- Implementing quantization
- Optimizing memory usage
- Reducing search latency
- Balancing recall vs speed
- Scaling to billions of vectors

## Do not use this skill when

- You only need exact search on small datasets (use a flat index)
- You lack workload metrics or ground truth to validate recall
- You need end-to-end retrieval system design beyond index tuning

## Instructions

1. Gather workload targets (latency, recall, QPS), data size, and memory budget.
2. Choose an index type and establish a baseline with default parameters.
3. Benchmark parameter sweeps using real queries and track recall, latency, and memory.
4. Validate changes on a staging dataset before rolling out to production.

Refer to `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Safety

- Avoid reindexing in production without a rollback plan.
- Validate changes under realistic load before applying globally.
- Track recall regressions and revert if quality drops.

## Resources

- `resources/implementation-playbook.md` for detailed patterns, checklists, and templates.

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
