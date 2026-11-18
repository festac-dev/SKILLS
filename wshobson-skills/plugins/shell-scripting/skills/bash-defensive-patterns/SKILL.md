---
name: wshobson-bash-defensive-patterns
description: Master defensive Bash programming techniques for production-grade scripts.
  Use when writing robust shell scripts, CI/CD pipelines, or system utilities requiring
  fault tolerance and safety.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Bash Defensive Patterns

Comprehensive guidance for writing production-ready Bash scripts using defensive programming techniques, error handling, and safety best practices to prevent common pitfalls and ensure reliability.

## When to Use This Skill

- Writing production automation scripts
- Building CI/CD pipeline scripts
- Creating system administration utilities
- Developing error-resilient deployment automation
- Writing scripts that must handle edge cases safely
- Building maintainable shell script libraries
- Implementing comprehensive logging and monitoring
- Creating scripts that must work across different platforms

## Detailed patterns and worked examples

Detailed pattern documentation lives in `references/details.md`. Read that file when the navigation tier above is insufficient.

## Best Practices Summary

1. **Always use strict mode** - `set -Eeuo pipefail`
2. **Quote all variables** - `"$variable"` prevents word splitting
3. **Use [[]] conditionals** - More robust than [ ]
4. **Implement error trapping** - Catch and handle errors gracefully
5. **Validate all inputs** - Check file existence, permissions, formats
6. **Use functions for reusability** - Prefix with meaningful names
7. **Implement structured logging** - Include timestamps and levels
8. **Support dry-run mode** - Allow users to preview changes
9. **Handle temporary files safely** - Use mktemp, cleanup with trap
10. **Design for idempotency** - Scripts should be safe to rerun
11. **Document requirements** - List dependencies and minimum versions
12. **Test error paths** - Ensure error handling works correctly
13. **Use `command -v`** - Safer than `which` for checking executables
14. **Prefer printf over echo** - More predictable across systems
