---
name: cybersecurity-implementing-log-forwarding-with-fluentd
description: Configures Fluent Bit as an endpoint log forwarder and Fluentd as the
  central aggregator for centralized log collection, routing, filtering, and enrichment,
  covering input plugins for syslog/file-tailing/application logs and output routing
  to Elasticsearch, S3, and Splunk. Use when setting up centralized log aggregation
  across distributed infrastructure or generating Fluent Bit/Fluentd configuration
  files for a new log pipeline.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: security-operations
    tags:
    - fluentd
    - fluent-bit
    - log-aggregation
    - log-forwarding
    - siem
    - centralized-logging
    - observability
    version: '1.0'
    author: mahipal
    nist_csf:
    - DE.CM-01
    - RS.MA-01
    - GV.OV-01
    - DE.AE-02
    mitre_attack:
    - T1078
    - T1190
    - T1059
    - T1685.002
    - T1685.005
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Implementing Log Forwarding with Fluentd

## Overview

This skill covers configuring Fluentd and Fluent Bit for centralized log collection, routing, and enrichment. Fluent Bit acts as a lightweight log forwarder on endpoints, while Fluentd serves as the central aggregator and processor. The configuration covers input plugins for syslog, file tailing, and application logs, with output routing to Elasticsearch, S3, and Splunk.


## When to Use

- When deploying or configuring implementing log forwarding with fluentd capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Fluentd (td-agent) v1.16+ or Fluent Bit v3.0+
- Python 3.8+ with fluent-logger library
- Elasticsearch or Splunk for log destination
- Network access on port 24224 (Fluentd forward protocol)
- Ruby 2.7+ (for Fluentd plugin development)

## Steps

1. **Generate Fluent Bit Configuration** — Create input, filter, and output configuration for endpoint log collection
2. **Generate Fluentd Aggregator Configuration** — Configure the central Fluentd instance with forward input, parsing, and multi-output routing
3. **Configure Log Filtering and Enrichment** — Add record_transformer and grep filters for log enrichment and noise reduction
4. **Validate Configuration Syntax** — Parse and validate Fluentd/Fluent Bit configuration files for syntax errors
5. **Test Log Forwarding** — Send test events via fluent-logger Python library and verify delivery
6. **Generate Deployment Report** — Produce configuration summary with routing topology and health metrics

## Expected Output

- Fluent Bit and Fluentd configuration files (INI/YAML format)
- Configuration validation report
- Log routing topology diagram (text-based)
- Test event delivery confirmation
