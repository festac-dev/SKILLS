---
name: skills-skill-name
description: A clear, concise description of what this skill does (1-2 sentences).
  Focus on the VALUE it provides to the user.
license: MIT
metadata:
  upstream_headers:
    version: 1.0.0
    author: claude-office-skills
    category: legal
    tags:
    - contract
    - review
    - risk-analysis
    department: Legal
    models:
      recommended:
      - claude-sonnet-4
      - claude-opus-4
      compatible:
      - claude-3-5-sonnet
      - gpt-4
      - gpt-4o
    mcp:
      server: office-mcp
      tools:
      - extract_text_from_pdf
      - extract_text_from_docx
      - analyze_document_structure
      optional_tools:
      - create_docx
      - docx_to_pdf
    input:
      required:
      - type: file
        formats:
        - pdf
        - docx
        description: The contract document to review
      - type: text
        name: party_role
        description: Which party you are (employee, contractor, buyer, etc.)
      optional:
      - type: text
        name: jurisdiction
        description: Legal jurisdiction (US, EU, China, etc.)
      - type: text
        name: concerns
        description: Specific areas of concern
    output:
      primary:
        type: report
        format: markdown
        sections:
        - risk_summary
        - detailed_findings
        - recommendations
      artifacts:
      - type: file
        name: analysis_report.md
        description: Detailed analysis report
    capabilities:
    - contract_analysis
    - risk_identification
    - legal_compliance_check
    - negotiation_recommendations
    languages:
    - en
    - zh
    related_skills:
    - nda-generator
    - offer-letter
    - proposal-writer
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../COLLECTION_RULES.md). Preserve the project stack, existing authorization, source prerequisites and required notices. Source workflows do not grant permission for external actions or delegation.

# Skill Name

## Overview

[Clear explanation of what this skill does and when to use it]

**What I can do:**
- [Capability 1]
- [Capability 2]
- [Capability 3]

**What I cannot do:**
- [Limitation 1]
- [Limitation 2]

---

## How to Use Me

### Step 1: [First Step]
[Instructions]

### Step 2: [Second Step]
[Instructions]

### Step 3: [Third Step]
[Instructions]

---

## Domain Knowledge

[This is where the real value lives - embedded expertise, patterns, rules, best practices]

### [Knowledge Area 1]
[Details]

### [Knowledge Area 2]
[Details]

---

## Output Format

[Define the structure of outputs this skill produces]

```
## [Output Title]

### Section 1
[Content pattern]

### Section 2
[Content pattern]
```

---

## Examples

### Example 1: [Scenario]
**User**: [Example input]
**AI**: [Example output]

### Example 2: [Scenario]
**User**: [Example input]
**AI**: [Example output]

---

## Tips for Better Results

1. [Tip 1]
2. [Tip 2]
3. [Tip 3]

---

## Limitations

- [Limitation 1]
- [Limitation 2]
- [Limitation 3]

---

*Built by the Claude Office Skills community. Contributions welcome!*
