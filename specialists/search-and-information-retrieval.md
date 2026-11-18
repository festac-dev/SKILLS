# Specialist: Search and Information Retrieval

Design search around the user's task and the data's structure.

Consider full-text search, filters, facets, sorting, saved searches, autocomplete, typo tolerance, synonyms, semantic retrieval and permission-aware results only as needed. Define indexing freshness, deletion propagation, pagination, ranking, query limits and failure behavior.

Search must never reveal records the current user is not authorized to access. Avoid sending private content to external search or embedding providers without a clear basis and appropriate disclosure. Provide useful no-results, partial-results and unavailable states.

## Applied verification

Search for a known authorized record and a forbidden record using titles, snippets and facets, then delete the authorized record. Verify access filtering and deletion freshness across cached results and pagination.

## Index operations

Treat search as a derived, rebuildable representation. Specify update propagation through the project’s outbox, CDC or queue, index lag, full reindex and an atomic alias/version switch. Enforce current permissions before returning results, including after index lag or deletion. Evaluate language analyzers, synonyms and hybrid/vector retrieval with judged queries, not anecdotal examples; monitor zero-result rate alongside latency and relevance.
