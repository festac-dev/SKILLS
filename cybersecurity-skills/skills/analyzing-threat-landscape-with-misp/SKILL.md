---
name: cybersecurity-analyzing-threat-landscape-with-misp
description: Query a MISP (Malware Information Sharing Platform) instance via PyMISP
  to compute event statistics, IOC type breakdowns, threat actor galaxy clusters,
  and tag trends, and generate threat landscape reports with temporal trends. Use
  when asked to analyze threat intelligence data, summarize top threat actors or malware
  families, or produce a CTI landscape report from MISP events.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: threat-intelligence
    tags:
    - threat-intelligence
    - misp
    - threat-landscape
    - ioc-analysis
    - cti
    - threat-sharing
    version: '1.0'
    author: mahipal
    d3fend_techniques:
    - File Metadata Consistency Validation
    - Application Protocol Command Analysis
    - Identifier Analysis
    - Content Format Conversion
    - Message Analysis
    nist_csf:
    - ID.RA-01
    - ID.RA-05
    - DE.CM-01
    - DE.AE-02
    mitre_attack:
    - T1566
    - T1071.001
    - T1568
    - T1583.001
    - T1102
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Analyzing Threat Landscape with MISP


## When to Use

- When investigating security incidents that require analyzing threat landscape with misp
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Familiarity with threat intelligence concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install pymisp`
2. Configure MISP URL and API key.
3. Run the agent to generate threat landscape analysis:
   - Pull event statistics by threat level and date range
   - Analyze attribute type distributions (IP, domain, hash, URL)
   - Identify top MITRE ATT&CK techniques from event tags
   - Track threat actor activity via galaxy clusters
   - Generate temporal trend analysis of IOC submissions

```bash
python scripts/agent.py --misp-url https://misp.local --api-key YOUR_KEY --days 90 --output landscape_report.json
```

## Examples

### Threat Landscape Summary
```
Period: Last 90 days
Events analyzed: 1,247
Top threat level: High (43%)
Top attribute type: ip-dst (31%), domain (22%), sha256 (18%)
Top MITRE technique: T1566 Phishing (89 events)
Top threat actor: APT28 (34 events)
```
