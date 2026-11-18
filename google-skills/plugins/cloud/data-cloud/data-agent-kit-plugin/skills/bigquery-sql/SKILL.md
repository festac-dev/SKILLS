---
name: google-bigquery-sql
description: Provides BigQuery SQL query optimization techniques, execution best practices,
  and performance tuning rules for high-efficiency querying. Use when optimizing BigQuery
  SQL queries, reducing query costs, or designing performant SQL transformations.
metadata:
  version: v1
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../../../../../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# BigQuery SQL Optimization

Performance and efficiency guidelines for BigQuery SQL queries. Includes rules
for column pruning, predicate pushdown, join optimization, and materialization
strategies.

## SQL Optimization Rules

> [!TIP] Always include a **"Summary of Optimizations"** section listing only
> the optimizations applied.

### Always Apply (Automatic)

-   **Column Pruning**: Remove unnecessary columns from all query stages.
-   **Common Subexpression Reuse**: Factor out identical expressions to avoid
    redundant computation.
-   **Predicate Pushdown**: Apply `WHERE` filters as early as possible.
-   **Early Aggregation**: Perform `GROUP BY` before joins when possible.
-   **Intermediate Materialization**: Choose `VIEW` vs `TABLE` for intermediate
    nodes based on efficiency.

#### Intermediate Node Strategy

-   **`VIEW`**: Small datasets or simple transformations.
-   **`TABLE`**: Large datasets, expensive computations, or nodes reused
    multiple times.

### Always Rewrite (Mandatory)

-   **`WHERE <col> IN (SELECT ...)`**: Replace With `WHERE EXISTS (SELECT 1 FROM
    ...)`
-   **`WHERE (SELECT COUNT(*) ...) > 0`**: Replace With `WHERE EXISTS (SELECT 1
    FROM ...)`

### Propose with Confirmation (Conditional)

-   **`UNION` → `UNION ALL`**: Faster (skips deduplication), but permits
    duplicate rows.
-   **`COUNT(DISTINCT)` → `APPROX_COUNT_DISTINCT`**: Faster and lower memory,
    but approximate.
