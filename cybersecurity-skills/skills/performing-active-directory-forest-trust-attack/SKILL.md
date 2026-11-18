---
name: cybersecurity-performing-active-directory-forest-trust-attack
description: Enumerate and audit Active Directory forest trust relationships using
  Impacket for SID filtering analysis, trust key extraction, cross-forest SID history
  abuse detection, and inter-realm Kerberos ticket assessment. Use when red-teaming
  multi-forest AD environments or auditing forest trusts for cross-forest privilege
  escalation and trust ticket forgery exposure.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: red-team
    tags:
    - active-directory
    - forest-trust
    - impacket
    - SID-filtering
    - kerberos
    - red-team
    - trust-enumeration
    version: '1.0'
    author: mahipal
    nist_csf:
    - ID.RA-01
    - GV.OV-02
    - DE.AE-07
    mitre_attack:
    - T1595
    - T1190
    - T1059
    - T1078
    - T1558.003
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Performing Active Directory Forest Trust Attack

## Overview

Active Directory forest trusts enable authentication across organizational boundaries but introduce attack surface if misconfigured. This skill uses impacket to enumerate trust relationships, analyze SID filtering configuration, detect SID history abuse vectors, perform cross-forest SID lookups via LSA/LSAT RPC calls, and assess inter-realm Kerberos ticket configurations for trust ticket forgery risks.


## When to Use

- When conducting security assessments that involve performing active directory forest trust attack
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- Python 3.9+ with `impacket`, `ldap3`
- Domain credentials with read access to AD trust objects
- Network access to Domain Controllers (ports 389, 445, 88)
- Authorized penetration testing engagement or lab environment


> **Legal Notice:** This skill is for authorized security testing and educational purposes only. Unauthorized use against systems you do not own or have written permission to test is illegal and may violate computer fraud laws.

## Steps

1. Enumerate forest trust relationships via LDAP trusted domain objects
2. Query trust attributes and SID filtering status for each trust
3. Perform SID lookups across trust boundaries using LsarLookupNames3
4. Enumerate foreign security principals in trusted domains
5. Check for SID history on cross-forest accounts
6. Assess trust direction and transitivity for lateral movement paths
7. Generate trust security audit report with risk findings

## Expected Output

- JSON report listing all trust relationships, SID filtering status, foreign principals, trust direction/transitivity, and risk assessment
- Cross-forest attack path analysis with remediation recommendations
