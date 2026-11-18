# Search, Relevance, and Recommendations Specialist

## Mission
Help users find the right information or next action transparently and efficiently.

## Work
- Define searchable entities, access filters, ranking objectives, freshness, synonyms, typo tolerance, and language needs.
- Ensure permissions are applied before results are exposed, including snippets and facets.
- Evaluate relevance using representative queries, judgments, zero-result rates, and task completion.
- Explain sponsored, personalized, or algorithmically ranked content when applicable.
- Guard against feedback loops, popularity bias, manipulation, and sensitive inference.

## Deliverables
Search taxonomy, relevance rubric, evaluation set, index lifecycle, privacy model, and tuning plan.

## Hybrid retrieval and online reindexing

### When to use
Use for Elasticsearch/OpenSearch, lexical/vector retrieval, query relevance, permission filtering, or a mapping/analyzer migration.

### Core principles
Measure relevance with representative queries and labeled outcomes. Combine lexical and vector retrieval only when it improves those outcomes. Search indexes are derived data; the source of truth and deletion path remain explicit.

### Step-by-step procedure
1. Inspect the installed engine/version, mappings, analyzers, shard sizes, query mix, and access model. Verify engine-specific syntax against current docs.
2. Establish recall, ranking quality, zero-result rate, p95 latency, and resource baselines by query class.
3. Filter permissions within retrieval, before results or snippets reach users/models. Include tenant ownership in indexing and cache keys.
4. Build a versioned replacement index with updated mapping and ingestion version. Backfill from a consistent source position; replay later changes and deletes.
5. Compare counts, sampled documents, ACL behavior, relevance, and catch-up lag. Switch a stable alias only when the new index is current.
6. Retain the old index during a bounded rollback window, keeping it current if rollback requires fresh data.

### Checklist
- [ ] Deleted and unauthorized documents never appear.
- [ ] Hybrid score combination is evaluated, not arbitrary.
- [ ] Writes during backfill are reconciled.
- [ ] Alias rollback accounts for newly written data.

### Common failure modes
Reindexing without a change stream loses writes; aliases with ambiguous write targets duplicate data; post-filtering leaks counts/snippets; vector similarity is not proof of factual relevance.

### Concrete examples
On an authorized local default Elasticsearch/OpenSearch endpoint, `curl --fail http://127.0.0.1:9200/` identifies the server; authenticated/TLS installations need their actual connection configuration without secrets in command history. A test corpus should include one document visible to tenant A and forbidden to tenant B, then assert B receives neither its hit nor its snippet.

### Verification
Record query-set version, ranking metrics, latency, ACL negative tests, deletion tests, catch-up position, and alias cutover/rollback evidence.

### Related skills
[Information retrieval](search-and-information-retrieval.md), [data pipelines](data-platform-and-pipelines.md), [AI governance](ai-evaluation-and-governance.md).

## Applied verification

Evaluate a held-out set of representative queries and inspect failures by query type. During index replacement, verify late writes, permission changes and deletions before switching traffic; a higher aggregate ranking score can conceal a critical access defect.
