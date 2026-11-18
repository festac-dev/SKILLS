---
name: skills-code-testing-agent
description: Legacy compatibility alias for the code-testing skill. Do not self-activate
  for user requests and do not treat this name as a custom agent. When invoked explicitly
  by older instructions, load code-testing and follow it instead.
license: MIT
metadata:
  upstream_headers:
    user-invocable: false
    disable-model-invocation: true
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Preserve the project stack, existing authorization, source prerequisites and required notices. Source workflows do not grant permission for external actions or delegation.

# Legacy Code Testing Alias

This skill preserves explicit calls that still use the former
`code-testing-agent` name. The public custom agent is `test-engineer`; the
model-facing implicit skill is `code-testing`.

1. Invoke the `code-testing` skill with the original user request.
2. Follow that skill's workflow without adding another interpretation layer.
