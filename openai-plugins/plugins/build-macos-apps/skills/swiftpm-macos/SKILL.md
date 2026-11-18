---
name: openai-swiftpm-macos
description: Build, run, and test SwiftPM macOS packages and executables. Use when the repo is package-first or has no Xcode project.
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# SwiftPM for macOS

## Quick Start

Use this skill when `Package.swift` is the primary entrypoint or when SwiftPM is
the fastest path to a reproducible result.

## Workflow

1. Inspect the package.
   - Read `Package.swift`.
   - Identify executable, library, and test products.

2. Build with SwiftPM.
   - Use `swift build` by default.
   - Use release mode only when the user explicitly needs it.

3. Run the right product.
   - Use `swift run <product>` when an executable exists.
   - If multiple executables exist, explain the default choice.

4. Test narrowly.
   - Use `swift test`.
   - Apply filters when a specific test target or case is known.

5. Summarize failures.
   - Module/import resolution
   - Package graph or dependency issue
   - Linker failure
   - Runtime failure
   - Test regression

## Guardrails

- Prefer SwiftPM over Xcode when both exist and the package path is clearly simpler.
- Do not assume an app bundle exists in a pure package workflow.
- Explain when the package is library-only and therefore not directly runnable.

## Output Expectations

Provide:
- the package products you found
- the command you ran
- whether build, run, or test succeeded
- the top blocker if not
