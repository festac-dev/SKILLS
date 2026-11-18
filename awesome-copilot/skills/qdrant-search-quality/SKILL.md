---
name: copilot-qdrant-search-quality
description: Diagnoses and improves Qdrant search relevance. Use when someone reports
  'search results are bad', 'wrong results', 'low precision', 'low recall', 'irrelevant
  matches', 'missing expected results', or asks 'how to improve search quality?',
  'which embedding model?', 'should I use hybrid search?', 'should I use reranking?'.
  Also use when search quality degrades after quantization, model change, or data
  growth.
metadata:
  upstream_headers:
    allowed-tools:
    - Read
    - Grep
    - Glob
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Qdrant Search Quality

First determine whether the problem is the embedding model, Qdrant configuration, or the query strategy. Most quality issues come from the model or data, not from Qdrant itself. If search quality is low, inspect how chunks are being passed to Qdrant before tuning any parameters. Splitting mid-sentence can drop quality 30-40%.

- Start by testing with exact search to isolate the problem [Search API](https://search.qdrant.tech/md/documentation/search/search/?s=search-api)


## Diagnosis and Tuning

Isolate the source of quality issues, tune HNSW parameters, and choose the right embedding model. [Diagnosis and Tuning](diagnosis/SKILL.md)


## Search Strategies

Hybrid search, reranking, relevance feedback, and exploration APIs for improving result quality. [Search Strategies](search-strategies/SKILL.md)
