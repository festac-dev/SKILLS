# SQL and Data Patterns (PostgreSQL-flavored, portable ideas)

Snippets are patterns to adapt. Check syntax against the project's database and version. Test on a copy of production-like data before migrating.

## Schema fundamentals
```sql
CREATE TABLE accounts (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  public_id   uuid   NOT NULL DEFAULT gen_random_uuid() UNIQUE,  -- or UUIDv7/ULID generated in app
  email       text   NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now(),
  deleted_at  timestamptz,
  CONSTRAINT email_lower CHECK (email = lower(email))
);
-- Uniqueness that ignores soft-deleted rows:
CREATE UNIQUE INDEX accounts_email_active ON accounts (email) WHERE deleted_at IS NULL;

CREATE TABLE orders (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  account_id  bigint NOT NULL REFERENCES accounts(id),
  status      text   NOT NULL CHECK (status IN ('draft','placed','paid','shipped','cancelled')),
  total_minor bigint NOT NULL CHECK (total_minor >= 0),   -- money as integer minor units
  currency    char(3) NOT NULL,
  version     int    NOT NULL DEFAULT 1                     -- optimistic concurrency
);
CREATE INDEX orders_account_id_idx ON orders (account_id);  -- index foreign keys you join or delete on
```

## Keyset pagination
```sql
SELECT id, created_at, title FROM posts
WHERE (created_at, id) < ($1, $2)          -- cursor from the last row
ORDER BY created_at DESC, id DESC
LIMIT 51;                                  -- one extra row tells you if there is another page
-- supporting index:
CREATE INDEX posts_created_id_idx ON posts (created_at DESC, id DESC);
```

## Upsert and idempotency
```sql
INSERT INTO idempotency_keys (scope, key, request_hash, status)
VALUES ($1, $2, $3, 'in_progress')
ON CONFLICT (scope, key) DO NOTHING
RETURNING 1;            -- no row returned => key already exists; read it and decide replay/conflict/in-progress
-- table: PRIMARY KEY (scope, key); store response_code, response_body, created_at; purge by TTL
```

## Optimistic locking
```sql
UPDATE orders SET status = 'paid', version = version + 1
WHERE id = $1 AND version = $2;   -- 0 rows updated => conflict (HTTP 409)
```

## Job queue in Postgres
```sql
WITH next AS (
  SELECT id FROM jobs
  WHERE state = 'queued' AND run_at <= now()
  ORDER BY priority DESC, run_at
  FOR UPDATE SKIP LOCKED
  LIMIT 10
)
UPDATE jobs j SET state = 'running', locked_at = now(), attempts = attempts + 1
FROM next WHERE j.id = next.id
RETURNING j.*;
```
Good for moderate throughput with transactional enqueue. Move to a dedicated broker when volume, fan-out or latency requirements justify it.

## Transactional outbox
```sql
BEGIN;
  INSERT INTO orders (...) VALUES (...);
  INSERT INTO outbox (aggregate, aggregate_id, type, payload) VALUES ('order', $1, 'order.placed', $2);
COMMIT;
-- relay: SELECT ... FROM outbox WHERE published_at IS NULL ORDER BY id FOR UPDATE SKIP LOCKED LIMIT 100; publish; UPDATE ... SET published_at = now();
```
Consumers must be idempotent (at-least-once delivery).

## Multi-tenancy with row-level security
```sql
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON documents
  USING (tenant_id = current_setting('app.tenant_id')::bigint)
  WITH CHECK (tenant_id = current_setting('app.tenant_id')::bigint);
-- per request, inside the transaction:  SET LOCAL app.tenant_id = '42';
```
Use a non-superuser, non-owner application role (superusers and table owners bypass RLS unless forced). Test cross-tenant reads and writes explicitly. Pooled connections: always `SET LOCAL` inside a transaction.

## Audit trail and history
Append-only `audit_log(actor, action, object_type, object_id, before, after, at, request_id)`; or temporal/history tables; protect from updates with permissions and triggers; retain per policy.

## Ledger (double-entry) essentials
Immutable entries; every transaction balances (sum of debits = credits) enforced by constraint or transactional check; currency per entry; idempotency key per external event; balances derived or materialized with reconciliation jobs; corrections are new entries, never edits.

## Search and similarity
```sql
-- Full-text
ALTER TABLE articles ADD COLUMN tsv tsvector GENERATED ALWAYS AS (to_tsvector('english', title || ' ' || body)) STORED;
CREATE INDEX articles_tsv_idx ON articles USING gin (tsv);
SELECT id FROM articles WHERE tsv @@ websearch_to_tsquery('english', $1) ORDER BY ts_rank(tsv, websearch_to_tsquery('english', $1)) DESC LIMIT 20;
-- Fuzzy: pg_trgm + GIN/GiST;  Vectors: pgvector with HNSW/IVFFlat indexes; evaluate recall and filter behavior
```

## Partitioning and retention
Range-partition time-series/event tables by month/day; drop old partitions instead of mass `DELETE`; index per partition; automate partition creation; consider TimescaleDB/ClickHouse for heavy analytics.

## Safe migrations (expand → migrate → contract)
1. Add nullable column or new table (fast, no rewrite). 2. Deploy code writing both. 3. Backfill in batches (resumable, throttled). 4. Switch reads. 5. Add constraints `NOT VALID` then `VALIDATE`. 6. Drop old column later.
```sql
CREATE INDEX CONCURRENTLY orders_status_idx ON orders (status);          -- avoid blocking writes
ALTER TABLE orders ADD CONSTRAINT total_nonneg CHECK (total_minor >= 0) NOT VALID;
ALTER TABLE orders VALIDATE CONSTRAINT total_nonneg;
SET lock_timeout = '3s';  -- fail fast instead of queueing behind long transactions and blocking everyone
```

## Performance triage
`EXPLAIN (ANALYZE, BUFFERS)`; look for sequential scans on large tables, row estimate errors, sorts spilling to disk, nested loops with large outer sets; `pg_stat_statements` for top queries; check missing FK indexes, bloat, long-running transactions, connection pool saturation (PgBouncer in transaction mode), autovacuum health, replication lag.

## Backups for databases
Base backup + WAL archiving (PITR) via pgBackRest, WAL-G or Barman; logical dumps (`pg_dump`) for portability, not as the only plan; encrypt, store off-site and immutably; **test restores on a schedule** and record the measured RTO/RPO (`templates/BACKUP_RESTORE_TEST_LOG.md`).

## Anti-patterns
Float money; storing JSON blobs for relational data; EAV for everything; `SELECT *` in APIs; offset pagination at depth; no FK indexes; business rules only in app code; soft delete without partial unique indexes; migrations that rewrite huge tables under lock; shared "settings" rows updated by many writers.
