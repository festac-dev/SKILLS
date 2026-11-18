---
name: copilot-qdrant-scaling-data-volume
description: Guides Qdrant data volume scaling decisions. Use when someone asks 'data
  doesn't fit on one node', 'too much data', 'need more storage', 'vertical or horizontal
  scaling', 'tenant scaling', 'time window rotation', or 'data growth exceeds capacity'.
metadata:
  upstream_headers:
    allowed-tools:
    - Read
    - Grep
    - Glob
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Scaling Data Volume

This document covers data volume scaling scenarios,
where the total size of the dataset exceeds the capacity of a single node.

## Tenant Scaling

If the use case is multi-tenant, meaning that each user only has access to a subset of the data,
and we never need to query across all the data, then we can use multi-tenancy patterns to scale.

The recommended way is to use multi-tenant workloads with payload partitioning, per-tenant indexes, and tiered multitenancy.

Learn more [Tenant Scaling](tenant-scaling/SKILL.md)

## Sliding Time Window

Some use-cases are based on a sliding time window, where only the most recent data is relevant.
For example an index for social media posts, where only the last 6 months of data require fast search.

Learn more [Sliding Time Window](sliding-time-window/SKILL.md)

## Global Search

Most general use-cases require global search across all data.
In these situations, we might need to fall back to vertical scaling,
and then horizontal scaling when we reach the limits of vertical scaling.


### Vertical Scaling

When data doesn't fit in a single node, the first approach is to scale the node itself — more RAM, better disk, quantization, mmap.
Exhaust vertical options before going horizontal, as horizontal scaling adds permanent operational complexity.

Learn more [Vertical Scaling](vertical-scaling/SKILL.md)

### Horizontal Scaling

When a single node can't hold the data even with quantization and mmap, distribute data across multiple nodes via sharding.

Learn more [Horizontal Scaling](horizontal-scaling/SKILL.md)
