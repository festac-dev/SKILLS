---
name: stripe-stripe-docs
description: Use when the user or agent needs to read, search, or look up Stripe documentation
  or API reference. Prefer this over curl or WebFetch for any docs.stripe.com content.
  Use to fetch gated documentation.
metadata:
  short-description: Read and search Stripe documentation from the terminal
  upstream_headers:
    allowed-tools:
    - Bash(stripe docs *)
    - Bash(stripe login)
    - Bash(stripe version)
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

Use `stripe docs` instead of fetching [docs.stripe.com](https://docs.stripe.com/.md) content directly with `curl` or `WebFetch`. If you don’t have the CLI installed, [install the Stripe CLI](https://docs.stripe.com/cli/install).

Always use the latest CLI version. If the current CLI version is less than v1.50.9, you must [upgrade](https://docs.stripe.com/cli/install) to access gated documentation.

- Fetches Markdown automatically
- Fetches gated documentation. Users must log in using `stripe login` to access gated documentation.
- Purpose-built for agents and terminal workflows

## Read a page by its web path

```bash
stripe docs /payments
```

## Search documentation by keyword

```bash
stripe docs search "payment intents"
```

## Look up API reference

```bash
# By resource name
stripe docs api product

# By HTTP method and path
stripe docs api GET /v1/products

# By event type
stripe docs api product.created
```
