---
name: cybersecurity-analyzing-network-packets-with-scapy
description: Use Scapy to craft, send, sniff, and dissect TCP/UDP/ICMP/DNS packets,
  analyze pcap files, implement SYN scans, and detect anomalous traffic such as fragmented
  or malformed packets. Use when performing authorized network reconnaissance, protocol-level
  forensic analysis, or building traffic anomaly detection during security testing.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: network-security
    tags:
    - scapy
    - packet-analysis
    - network-forensics
    - protocol-dissection
    - pcap
    - traffic-analysis
    version: '1.0'
    author: mahipal
    nist_csf:
    - PR.IR-01
    - DE.CM-01
    - ID.AM-03
    - PR.DS-02
    mitre_attack:
    - T1040
    - T1071
    - T1046
    - T1557
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Analyzing Network Packets with Scapy

## Overview

Scapy is a Python packet manipulation library that enables crafting, sending, sniffing, and dissecting network packets at granular protocol layers. This skill covers using Scapy for security-relevant tasks including TCP/UDP/ICMP packet crafting, pcap file analysis, protocol field extraction, SYN scan implementation, DNS query analysis, and detecting anomalous traffic patterns such as unusually fragmented packets or malformed headers.


## When to Use

- When investigating security incidents that require analyzing network packets with scapy
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Python 3.8+ with `scapy` library installed (`pip install scapy`)
- Root/administrator privileges for raw socket operations (sniffing, sending)
- Npcap (Windows) or libpcap (Linux) for packet capture
- Authorization to perform packet operations on target network

## Steps

1. Read and parse pcap/pcapng files with `rdpcap()` for offline analysis
2. Extract protocol layers (IP, TCP, UDP, DNS, HTTP) and field values
3. Compute traffic statistics: top talkers, protocol distribution, port frequency
4. Detect SYN flood patterns by analyzing TCP flag ratios
5. Identify DNS exfiltration indicators via query length and entropy analysis
6. Craft custom probe packets for authorized network testing
7. Export findings as structured JSON report

## Expected Output

JSON report containing packet statistics, protocol distribution, top source/destination IPs, detected anomalies (SYN floods, DNS tunneling indicators, fragmentation attacks), and per-flow summaries.
