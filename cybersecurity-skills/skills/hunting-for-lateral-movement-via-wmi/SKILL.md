---
name: cybersecurity-hunting-for-lateral-movement-via-wmi
description: Detects WMI-based lateral movement (e.g. wmic process call create, Win32_Process.Create())
  by analyzing Windows Event ID 4688 and Sysmon Event ID 1 for WmiPrvSE.exe spawning
  suspicious child processes like cmd.exe or powershell.exe, plus WMI-Activity/Operational
  events 5857/5860/5861 for subscription-based persistence. Use when hunting for remote
  code execution via WMI or investigating lateral movement across Windows hosts.
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: threat-hunting
    tags:
    - threat-hunting
    - lateral-movement
    - wmi
    - sysmon
    - mitre-attack
    - process-creation
    version: '1.0'
    author: mahipal
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
    - T1021
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Hunting for Lateral Movement via WMI

## Overview

Windows Management Instrumentation (WMI) is commonly abused for lateral movement via `wmic process call create` or Win32_Process.Create() to execute commands on remote hosts. Detection focuses on identifying WmiPrvSE.exe spawning child processes (cmd.exe, powershell.exe) in Windows Security Event ID 4688 and Sysmon Event ID 1 logs, along with WMI-Activity/Operational events (5857, 5860, 5861) for event subscription persistence.


## When to Use

- When investigating security incidents that require hunting for lateral movement via wmi
- When building detection rules or threat hunting queries for this domain
- When SOC analysts need structured procedures for this analysis type
- When validating security monitoring coverage for related attack techniques

## Prerequisites

- Windows Security Event Logs with Process Creation auditing enabled (Event 4688 with command line)
- Sysmon installed with Event ID 1 (Process Creation) configured
- Python 3.9+ with `python-evtx`, `lxml` libraries
- Understanding of WMI architecture and WmiPrvSE.exe behavior

## Steps

### Step 1: Parse Process Creation Events
Extract Event ID 4688 and Sysmon Event 1 entries from EVTX files.

### Step 2: Detect WmiPrvSE Child Processes
Flag processes where ParentImage/ParentProcessName is WmiPrvSE.exe, indicating remote WMI execution.

### Step 3: Analyze Command Line Patterns
Identify suspicious command lines matching WMI lateral movement patterns (cmd.exe /q /c, output redirection to admin$ share).

### Step 4: Check WMI Event Subscriptions
Parse WMI-Activity/Operational log for event consumer creation indicating persistence.

## Expected Output

JSON report with WMI-spawned processes, suspicious command lines, WMI event subscription alerts, and timeline of lateral movement activity.
