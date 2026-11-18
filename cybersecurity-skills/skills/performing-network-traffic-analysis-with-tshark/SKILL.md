---
name: cybersecurity-performing-network-traffic-analysis-with-tshark
description: Automate network traffic analysis using tshark (Wireshark CLI) and pyshark
  to compute protocol distribution statistics, detect suspicious flows such as port
  scans and beaconing, extract IOCs (IPs, domains, URLs), and identify DNS tunneling
  patterns from PCAP files. Use when scripted or repeatable analysis of packet captures
  is needed rather than interactive inspection.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: network-security
    tags:
    - tshark
    - pyshark
    - pcap
    - packet-analysis
    - network-forensics
    - wireshark
    - traffic-analysis
    version: '1.0'
    author: mahipal
    nist_csf:
    - PR.IR-01
    - DE.CM-01
    - ID.AM-03
    - PR.DS-02
    mitre_attack:
    - T1046
    - T1040
    - T1557
    - T1071
    - T1005
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Performing Network Traffic Analysis with TShark

## Overview

This skill automates packet capture analysis using tshark (Wireshark CLI) and pyshark (Python wrapper). It extracts protocol distribution statistics, identifies suspicious network flows (port scans, beaconing, data exfiltration), extracts IOCs (IPs, domains, URLs), and detects DNS tunneling patterns from PCAP files.


## When to Use

- When conducting security assessments that involve performing network traffic analysis with tshark
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- tshark (Wireshark CLI) installed and in PATH
- Python 3.8+ with pyshark library
- PCAP or PCAPNG capture file for analysis

## Steps

1. **Extract Protocol Statistics** — Generate protocol hierarchy and conversation statistics from the capture
2. **Identify Top Talkers** — Rank source/destination IPs by volume and connection count
3. **Detect Suspicious Flows** — Flag port scanning patterns, unusual port usage, and high-frequency connections
4. **Extract Network IOCs** — Pull unique IPs, domains from DNS queries, and URLs from HTTP traffic
5. **Analyze DNS Traffic** — Detect DNS tunneling via high-entropy subdomain queries and excessive TXT records
6. **Generate Analysis Report** — Produce structured report with flow summaries and threat indicators

## Expected Output

- JSON report with protocol statistics and top talkers
- Suspicious flow detections with severity ratings
- Extracted IOCs (IPs, domains, URLs)
- DNS anomaly analysis results
