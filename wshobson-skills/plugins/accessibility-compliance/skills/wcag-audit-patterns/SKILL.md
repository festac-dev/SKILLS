---
name: wshobson-wcag-audit-patterns
description: Conduct WCAG 2.2 accessibility audits with automated testing, manual
  verification, and remediation guidance. Use when auditing websites for accessibility,
  fixing WCAG violations, or implementing accessible design patterns.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# WCAG Audit Patterns

Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies.

## When to Use This Skill

- Conducting accessibility audits
- Fixing WCAG violations
- Implementing accessible components
- Preparing for accessibility lawsuits
- Meeting ADA/Section 508 requirements
- Achieving VPAT compliance

## Core Concepts

### 1. WCAG Conformance Levels

| Level   | Description            | Required For      |
| ------- | ---------------------- | ----------------- |
| **A**   | Minimum accessibility  | Legal baseline    |
| **AA**  | Standard conformance   | Most regulations  |
| **AAA** | Enhanced accessibility | Specialized needs |

### 2. POUR Principles

```
Perceivable:  Can users perceive the content?
Operable:     Can users operate the interface?
Understandable: Can users understand the content?
Robust:       Does it work with assistive tech?
```

### 3. Common Violations by Impact

```
Critical (Blockers):
├── Missing alt text for functional images
├── No keyboard access to interactive elements
├── Missing form labels
└── Auto-playing media without controls

Serious:
├── Insufficient color contrast
├── Missing skip links
├── Inaccessible custom widgets
└── Missing page titles

Moderate:
├── Missing language attribute
├── Unclear link text
├── Missing landmarks
└── Improper heading hierarchy
```

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices

### Do's

- **Start early** - Accessibility from design phase
- **Test with real users** - Disabled users provide best feedback
- **Automate what you can** - 30-50% issues detectable
- **Use semantic HTML** - Reduces ARIA needs
- **Document patterns** - Build accessible component library

### Don'ts

- **Don't rely only on automated testing** - Manual testing required
- **Don't use ARIA as first solution** - Native HTML first
- **Don't hide focus outlines** - Keyboard users need them
- **Don't disable zoom** - Users need to resize
- **Don't use color alone** - Multiple indicators needed
