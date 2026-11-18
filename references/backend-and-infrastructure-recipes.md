# Backend and Infrastructure Recipes

Reference patterns to adapt, not to paste blindly. Verify versions, flags, and distro paths against the project and current documentation. Never run server changes without authorization and a rollback path.

## 1. Error response (problem-details style)
```json
{
  "type": "https://api.example.com/problems/validation-error",
  "title": "Validation failed",
  "status": 422,
  "detail": "One or more fields are invalid.",
  "instance": "/v1/orders",
  "request_id": "req_01HZX...",
  "errors": [{ "field": "quantity", "code": "min", "message": "Must be at least 1." }]
}
```

## 2. Keyset (cursor) pagination
```sql
-- stable order on (created_at, id); index on (created_at DESC, id DESC)
SELECT id, created_at, title
FROM posts
WHERE (created_at, id) < ($1, $2)       -- cursor from previous page
ORDER BY created_at DESC, id DESC
LIMIT 51;                               -- fetch limit+1 to know if there is a next page
```

## 3. Idempotency keys
```sql
CREATE TABLE idempotency_keys (
  key         text NOT NULL,
  scope       text NOT NULL,            -- e.g. user or tenant id
  request_hash text NOT NULL,
  response_code int,
  response_body jsonb,
  created_at  timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (scope, key)
);
```
Flow: insert key (unique) → if conflict, compare request hash (mismatch = 422) → return stored response if finished, or 409/wait if in progress → perform work and store the result in the same transaction as the side effect when possible. Expire keys after a documented window.

## 4. Transactional outbox
```sql
CREATE TABLE outbox (
  id bigserial PRIMARY KEY,
  aggregate text NOT NULL, aggregate_id text NOT NULL,
  event_type text NOT NULL, payload jsonb NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz
);
-- In the business transaction: write domain rows + INSERT INTO outbox(...).
-- A relay selects unpublished rows (FOR UPDATE SKIP LOCKED), publishes, marks published. Consumers dedupe by event id.
```

## 5. Job claiming with a database queue
```sql
UPDATE jobs SET status='running', locked_at=now(), attempts=attempts+1
WHERE id = (
  SELECT id FROM jobs
  WHERE status='queued' AND run_at <= now()
  ORDER BY priority DESC, run_at
  FOR UPDATE SKIP LOCKED LIMIT 1)
RETURNING *;
```
Add visibility timeout recovery, max attempts, dead-letter status, and per-job idempotency.

## 6. Token-bucket rate limiter (concept)
Per key: `tokens = min(capacity, tokens + (now - last) * refill_rate)`; if `tokens >= cost` then allow and subtract, else reject with `Retry-After`. Implement atomically (Redis Lua script, database row lock, or gateway feature). Return `RateLimit-*`/`Retry-After` headers.

## 7. Health and readiness
- `/healthz` (liveness): process is up; no dependency checks.
- `/readyz` (readiness): can serve traffic (database reachable, migrations applied, warmed caches); fail during shutdown so the load balancer drains.
- Never expose sensitive diagnostics publicly.

## 8. Graceful shutdown (sequence)
Receive SIGTERM → mark not-ready → stop accepting new connections/jobs → finish in-flight work within a deadline → close pools → exit. Set the orchestrator's termination grace period longer than the deadline.

## 9. Multi-stage container build (pattern)
```dockerfile
# build stage: tools, compilers, dev dependencies
FROM <build-image> AS build
WORKDIR /src
COPY <lockfiles> ./
RUN <install deps from lockfile>
COPY . .
RUN <build / compile>

# runtime stage: minimal image, non-root, no build tools
FROM <slim-runtime-image>
WORKDIR /app
RUN adduser --system --no-create-home app
COPY --from=build --chown=app /src/<artifact> ./
USER app
EXPOSE 8080
HEALTHCHECK CMD ["<probe command>"]
ENTRYPOINT ["<app>"]
```

## 10. Compose service skeleton
```yaml
services:
  app:
    image: registry.example.com/app:${APP_VERSION}
    restart: unless-stopped
    env_file: .env.production        # file mode 600, not committed
    depends_on: { db: { condition: service_healthy } }
    healthcheck: { test: ["CMD", "<probe>"], interval: 15s, timeout: 3s, retries: 5 }
    deploy: { resources: { limits: { memory: 512M } } }
    networks: [internal, web]
  db:
    image: postgres:<pinned-major>
    restart: unless-stopped
    volumes: [dbdata:/var/lib/postgresql/data]
    healthcheck: { test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER"], interval: 10s, retries: 5 }
    networks: [internal]             # not published to the host
volumes: { dbdata: {} }
networks: { internal: { internal: true }, web: {} }
```

## 11. systemd unit with sandboxing
```ini
[Unit]
Description=Example app
After=network-online.target
Wants=network-online.target

[Service]
User=app
Group=app
WorkingDirectory=/srv/app/current
EnvironmentFile=/etc/app/app.env
ExecStart=/srv/app/current/bin/server
Restart=on-failure
RestartSec=3
TimeoutStopSec=30
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
ReadWritePaths=/var/lib/app /var/log/app
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

## 12. Reverse proxy essentials (Nginx-style)
```nginx
server {
  listen 443 ssl http2;
  server_name example.com;
  # ssl_certificate / key managed by ACME client; use a maintained TLS preset
  client_max_body_size 10m;
  add_header Strict-Transport-Security "max-age=31536000" always;   # only after HTTPS is verified
  location / {
    proxy_pass http://127.0.0.1:8080;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $remote_addr;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_read_timeout 60s;
  }
  location /ws/ {                    # WebSocket upgrade
    proxy_pass http://127.0.0.1:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 3600s;
  }
}
```
Caddy and Traefik provide automatic TLS with shorter configs; choose by team familiarity.

## 13. SSH and firewall baseline (concept)
`/etc/ssh/sshd_config.d/hardening.conf`: `PermitRootLogin no`, `PasswordAuthentication no`, `PubkeyAuthentication yes`, `MaxAuthTries 3`, `AllowUsers <admin>`. Test in a second session before closing the first. Firewall: default deny incoming, allow 22 (restricted if possible), 80, 443; verify from outside; keep provider console access as the escape hatch.

## 14. Database backup and verified restore (PostgreSQL example)
```bash
pg_dump --format=custom --file=/backups/app-$(date -u +%F).dump "$DATABASE_URL"
# ship off-host with encryption; then, regularly:
createdb restore_test && pg_restore --dbname=restore_test --no-owner /backups/app-YYYY-MM-DD.dump
psql restore_test -c "SELECT count(*) FROM <critical table>;"   # compare against expectations
```
Logical dumps complement, not replace, continuous archiving/PITR for larger systems. Alert on backup age and failure.

## 15. CI skeleton with short-lived cloud credentials (GitHub Actions style)
```yaml
permissions: { contents: read, id-token: write }
jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<pinned-sha>
      - run: <install from lockfile>
      - run: <lint> && <typecheck> && <test>
      - run: <build artifact + scan>
  deploy:
    needs: build-test
    environment: production            # protected, with required reviewers
    steps:
      - uses: <cloud-login-action>@<pinned-sha>   # OIDC; no static cloud keys
      - run: <deploy artifact by version>
      - run: <smoke test + verify>
```

## 16. Expand/contract example
Rename `users.name` → `users.full_name`: (1) add `full_name`; (2) dual-write; (3) backfill in batches; (4) switch reads; (5) stop writing `name`; (6) drop `name` in a later release.

## 17. Useful diagnostics
```bash
ss -tulpn                 # listening ports and owners
journalctl -u app -n 200 --no-pager
df -h && du -xh / --max-depth=1 | sort -h | tail
free -m && vmstat 1 5
curl -sv https://example.com/healthz -o /dev/null
dig +short example.com && openssl s_client -connect example.com:443 -servername example.com </dev/null | openssl x509 -noout -dates
```

## 18. Caddy-style reverse proxy (automatic TLS)
```
example.com {
  encode zstd gzip
  reverse_proxy 127.0.0.1:8080
}
```
Confirm DNS and ports 80/443 reachability. Validate configuration before reload; keep the previous config for rollback. For DNS migrations, lower TTL ahead of time, switch, verify, then raise TTL.
