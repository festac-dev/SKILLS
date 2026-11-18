---
name: cybersecurity-implementing-log-integrity-with-blockchain
description: Builds an append-only log integrity chain using SHA-256 hash chaining,
  where each entry incorporates the previous entry's hash so tampering invalidates
  all subsequent hashes; covers log ingestion (syslog/JSON/plain text), chain verification,
  pinpoint tamper detection, and checkpoint anchoring to external timestamping services.
  Use for tamper-evident log storage for compliance or forensics, or to verify whether
  log entries were altered.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: security-operations
    tags:
    - log-integrity
    - tamper-detection
    - hash-chaining
    - sha-256
    - audit-logging
    - security-operations
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
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Implementing Log Integrity with Blockchain


## When to Use

- When deploying or configuring implementing log integrity with blockchain capabilities in your environment
- When establishing security controls aligned to compliance requirements
- When building or improving security architecture for this domain
- When conducting security assessments that require this implementation

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install requests`
2. Ingest log entries from syslog, JSON, or plain text files.
3. For each entry, compute SHA-256 hash of: previous_hash + timestamp + log_content.
4. Store the chain as a JSON ledger with entry index, timestamp, content hash, previous hash, and chain hash.
5. Verify chain integrity by recomputing all hashes and detecting breaks.
6. Optionally anchor checkpoint hashes to an external timestamping service.

```bash
python scripts/agent.py --log-file /var/log/syslog --chain-file log_chain.json --verify --output integrity_report.json
```

## Examples

### Chain Entry Structure
```json
{"index": 42, "timestamp": "2024-01-15T10:30:00Z", "content_hash": "a1b2c3...",
 "prev_hash": "d4e5f6...", "chain_hash": "SHA256(prev_hash + timestamp + content_hash)"}
```

### Tamper Detection
If entry 42 is modified, chain_hash[42] will not match SHA256(chain_hash[41] + ...), and all entries from 42 onward will be flagged as invalid.
