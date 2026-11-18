---
name: openai-remotion-docs
description: Search Remotion documentation
metadata:
  upstream_headers:
    version: 4.0.506
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

This skill teaches you how to discover and read current Remotion documentation.
If this is not relevant, load [Remotion Best Practices](../remotion-best-practices/SKILL.md) instead.

## Searching the docs

Use the Algolia search API to find relevant documentation pages:

```
POST https://plsduol1ca-dsn.algolia.net/1/indexes/*/queries?x-algolia-api-key=3e42dbd4f895fe93ff5cf40d860c4a85&x-algolia-application-id=PLSDUOL1CA
Content-Type: application/x-www-form-urlencoded

{
  "requests": [
    {
      "query": "<your search query>",
      "indexName": "remotion",
      "params": "attributesToRetrieve=[\"hierarchy.lvl0\",\"hierarchy.lvl1\",\"hierarchy.lvl2\",\"url\"]&hitsPerPage=10"
    }
  ]
}
```

Each hit contains a `url` field pointing to the documentation page.

## Fetching a page as Markdown

Append `.md` to any Remotion docs URL to retrieve its Markdown source (saves tokens):

```
https://www.remotion.dev/docs/use-video-config.md
https://www.remotion.dev/docs/sequence.md
https://www.remotion.dev/docs/lambda/rendermediaonlambda.md
```

## Workflow

1. Search Algolia for the concept or API you need.
2. Pick the most relevant URL(s) from the results.
3. Fetch each URL with the `.md` suffix.
4. Implement using the current documentation rather than memorized API knowledge.
