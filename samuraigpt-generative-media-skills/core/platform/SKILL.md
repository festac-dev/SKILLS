---
name: skills-muapi-platform
description: Setup and utility scripts for muapi.ai — configure API keys, test connectivity,
  and poll for async generation results
metadata:
  upstream_headers:
    version: 0.1.0
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Preserve the project stack, existing authorization, source prerequisites and required notices. Source workflows do not grant permission for external actions or delegation.

# ⚙️ MuAPI Platform Utilities

**Setup and polling utilities for the muapi.ai platform.**

Configure your API key, verify connectivity, and poll for async generation results.

## Available Scripts

| Script | Description |
| :--- | :--- |
| `setup.sh` | Configure API key, show config, test key validity |
| `check-result.sh` | Poll for async generation results by request ID |

## Quick Start

```bash
# Save your API key
bash setup.sh --add-key "YOUR_MUAPI_KEY"

# Show current configuration
bash setup.sh --show-config

# Test API key validity
bash setup.sh --test

# Poll for a result (waits for completion)
bash check-result.sh --id "your-request-id"

# Check once without polling
bash check-result.sh --id "your-request-id" --once
```

## Requirements

- `curl`
