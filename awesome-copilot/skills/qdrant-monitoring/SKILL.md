---
name: copilot-qdrant-monitoring
description: Guides Qdrant monitoring and observability setup. Use when someone asks
  'how to monitor Qdrant', 'what metrics to track', 'is Qdrant healthy', 'optimizer
  stuck', 'why is memory growing', 'requests are slow', or needs to set up Prometheus,
  Grafana, or health checks. Also use when debugging production issues that require
  metric analysis.
metadata:
  upstream_headers:
    allowed-tools:
    - Read
    - Grep
    - Glob
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Qdrant Monitoring

Qdrant monitoring allows tracking performance and health of your deployment, and identifying issues before they become outages. First determine whether you need to set up monitoring or diagnose an active issue.

- Understand available metrics [Monitoring docs](https://search.qdrant.tech/md/documentation/operations/monitoring/)


## Monitoring Setup

Prometheus scraping, health probes, Hybrid Cloud specifics, alerting, and log centralization. [Monitoring Setup](setup/SKILL.md)


## Debugging with Metrics

Optimizer stuck, memory growth, slow requests. Using metrics to diagnose active production issues. [Debugging with Metrics](debugging/SKILL.md)
