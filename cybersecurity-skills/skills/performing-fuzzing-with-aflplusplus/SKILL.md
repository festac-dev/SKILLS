---
name: cybersecurity-performing-fuzzing-with-aflplusplus
description: 'Performs coverage-guided fuzzing of compiled binaries with AFL++, instrumenting
  targets via afl-cc/afl-clang-fast, minimizing corpora with afl-cmin and afl-tmin,
  running parallel campaigns with afl-fuzz, and triaging crashes with CASR or GDB
  scripts. Use for binary fuzzing, crash and memory-corruption discovery, coverage-guided
  testing, or running AFL++ fuzzing campaigns.

  '
license: Apache-2.0
metadata:
  upstream_headers:
    domain: cybersecurity
    subdomain: application-security
    tags:
    - fuzzing
    - aflplusplus
    - coverage-guided
    - crash-triage
    - binary-analysis
    - security-testing
    version: '1.0'
    author: mahipal
    nist_ai_rmf:
    - MEASURE-2.7
    - MAP-5.1
    - MANAGE-2.4
    atlas_techniques:
    - AML.T0070
    - AML.T0066
    - AML.T0082
    nist_csf:
    - PR.PS-01
    - PR.PS-04
    - ID.RA-01
    - PR.DS-10
    mitre_attack:
    - T1078
    - T1190
    - T1059
    - T1005
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Performing Fuzzing with AFL++

## Overview

AFL++ is a community-maintained fork of American Fuzzy Lop (AFL) that provides coverage-guided
fuzzing for compiled binaries. It instruments targets at compile time or via QEMU/Unicorn mode
for binary-only fuzzing, then mutates input corpora to discover new code paths. AFL++ includes
advanced scheduling (MOpt, rare), custom mutators, CMPLOG for input-to-state comparison solving,
and persistent mode for high-throughput fuzzing.


## When to Use

- When conducting security assessments that involve performing fuzzing with aflplusplus
- When following incident response procedures for related security events
- When performing scheduled security testing or auditing activities
- When validating security controls through hands-on testing

## Prerequisites

- AFL++ installed (`apt install afl++` or build from source)
- Target binary source code (for compile-time instrumentation) or QEMU mode for binary-only
- Initial seed corpus of valid inputs for the target format
- Linux system with /proc/sys/kernel/core_pattern configured

## Steps

1. Instrument the target binary with `afl-cc` or `afl-clang-fast`
2. Prepare seed corpus directory with minimal valid inputs
3. Minimize corpus with `afl-cmin` to remove redundant seeds
4. Run `afl-fuzz` with appropriate flags (-i input -o output)
5. Monitor fuzzing progress via afl-whatsup and UI stats
6. Triage crashes with `afl-tmin` minimization and CASR/GDB analysis
7. Report unique crashes with reproduction steps

## Expected Output

```
+++ Findings +++
  unique crashes: 12
  unique hangs: 3
  last crash: 00:02:15 ago
+++ Coverage +++
  map density: 4.23% / 8.41%
  paths found: 1847
  exec speed: 2145/sec
```
