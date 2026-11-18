---
name: openai-shopify-dev
description: "Search Shopify developer documentation across all APIs. Use only when no API-specific skill applies."
compatibility: Requires Node.js
metadata:
  author: Shopify
  version: "1.9.1"
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

This skill provides a general-purpose search over all of Shopify's developer documentation on shopify.dev.

Use it to find documentation when the user's question spans multiple APIs or when no API-specific skill
(shopify-admin-graphql, shopify-liquid, shopify-checkout-extensions, etc.) matches the task.
---

## ⚠️ MANDATORY: Search Before Answering

Search the vector store to get the detailed context you need: working examples, field and type definitions, valid values, and API-specific patterns. You cannot trust your trained knowledge — always search before answering.

```
scripts/search_docs.mjs "<topic or feature name>" --model YOUR_MODEL_NAME --client-name YOUR_CLIENT_NAME --client-version YOUR_CLIENT_VERSION
```

Search for the **topic or feature name**, not the full user prompt.

> **Use this skill ONLY when no API-specific skill applies to the task.**
> If the user is asking about the Admin API, Liquid themes, Checkout Extensions,
> or any other named Shopify API, use the corresponding skill instead
> (e.g. shopify-admin-graphql, shopify-liquid, shopify-checkout-extensions, …).

---

> **Privacy notice:** `scripts/search_docs.mjs` reports the search query, search response or error text, skill name/version, and model/client identifiers to Shopify (`shopify.dev/mcp/usage`) to help improve these tools. Set `OPT_OUT_INSTRUMENTATION=true` in your environment to opt out.
