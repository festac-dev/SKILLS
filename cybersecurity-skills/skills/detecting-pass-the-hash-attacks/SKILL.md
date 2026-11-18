---
name: cybersecurity-detecting-pass-the-hash-attacks
description: Detect Pass-the-Hash (T1550.002) attacks by analyzing NTLM authentication
  patterns, flagging Type 3 logons using NTLM where Kerberos would be expected, and
  correlating with credential-dumping indicators. Use when threat hunting for lateral
  movement via stolen NTLM hashes, triaging EDR/SIEM alerts on suspicious NTLM logons,
  scoping compromise during incident response, or validating detection coverage in
  a purple team exercise.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: threat-hunting
    tags:
    - threat-hunting
    - mitre-attack
    - pass-the-hash
    - credential-access
    - t1550
    - proactive-detection
    version: '1.0'
    author: mahipal
    d3fend_techniques:
    - Token Binding
    - Execution Isolation
    - Restore Access
    - Application Protocol Command Analysis
    - Process Termination
    nist_csf:
    - DE.CM-01
    - DE.AE-02
    - DE.AE-07
    - ID.RA-05
    mitre_attack:
    - T1046
    - T1057
    - T1082
    - T1083
    - T1003
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Detecting Pass The Hash Attacks

## When to Use

- When proactively hunting for indicators of detecting pass the hash attacks in the environment
- After threat intelligence indicates active campaigns using these techniques
- During incident response to scope compromise related to these techniques
- When EDR or SIEM alerts trigger on related indicators
- During periodic security assessments and purple team exercises

## Prerequisites

- EDR platform with process and network telemetry (CrowdStrike, MDE, SentinelOne)
- SIEM with relevant log data ingested (Splunk, Elastic, Sentinel)
- Sysmon deployed with comprehensive configuration
- Windows Security Event Log forwarding enabled
- Threat intelligence feeds for IOC correlation

## Workflow

1. **Formulate Hypothesis**: Define a testable hypothesis based on threat intelligence or ATT&CK gap analysis.
2. **Identify Data Sources**: Determine which logs and telemetry are needed to validate or refute the hypothesis.
3. **Execute Queries**: Run detection queries against SIEM and EDR platforms to collect relevant events.
4. **Analyze Results**: Examine query results for anomalies, correlating across multiple data sources.
5. **Validate Findings**: Distinguish true positives from false positives through contextual analysis.
6. **Correlate Activity**: Link findings to broader attack chains and threat actor TTPs.
7. **Document and Report**: Record findings, update detection rules, and recommend response actions.

## Key Concepts

| Concept | Description |
|---------|-------------|
| T1550.002 | Pass the Hash |
| T1550.003 | Pass the Ticket |
| T1078 | Valid Accounts |

## Tools & Systems

| Tool | Purpose |
|------|---------|
| CrowdStrike Falcon | EDR telemetry and threat detection |
| Microsoft Defender for Endpoint | Advanced hunting with KQL |
| Splunk Enterprise | SIEM log analysis with SPL queries |
| Elastic Security | Detection rules and investigation timeline |
| Sysmon | Detailed Windows event monitoring |
| Velociraptor | Endpoint artifact collection and hunting |
| Sigma Rules | Cross-platform detection rule format |

## Common Scenarios

1. **Scenario 1**: Mimikatz sekurlsa::pth with stolen NTLM hash
2. **Scenario 2**: Impacket psexec.py remote execution with hash
3. **Scenario 3**: CrackMapExec hash spraying across hosts
4. **Scenario 4**: WMI lateral movement via pass-the-hash

## Output Format

```
Hunt ID: TH-DETECT-[DATE]-[SEQ]
Technique: T1550.002
Host: [Hostname]
User: [Account context]
Evidence: [Log entries, process trees, network data]
Risk Level: [Critical/High/Medium/Low]
Confidence: [High/Medium/Low]
Recommended Action: [Containment, investigation, monitoring]
```
