# Infrastructure Config Snippets

Starting points for common deployments. **Adapt, review and test before production.** Pin versions, replace placeholders (`example.com`, `appuser`, paths), and validate with each tool's own check command. Configs that cannot be verified in your environment are labeled in the playbook evidence.

## 1. Caddy (automatic HTTPS reverse proxy)
```caddyfile
example.com {
    encode zstd gzip
    header {
        Strict-Transport-Security "max-age=31536000; includeSubDomains"
        X-Content-Type-Options nosniff
        Referrer-Policy strict-origin-when-cross-origin
        -Server
    }
    reverse_proxy 127.0.0.1:8080 {
        health_uri /readyz
        health_interval 10s
    }
    log { output file /var/log/caddy/access.log }
}
```
Validate: `caddy validate --config /etc/caddy/Caddyfile`.

## 2. Nginx reverse proxy (TLS via certbot or provider)
```nginx
server {
    listen 443 ssl http2;
    server_name example.com;
    # ssl_certificate / ssl_certificate_key managed by certbot or your CA
    client_max_body_size 2m;
    add_header X-Content-Type-Options nosniff always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 30s;
    }
    location /ws/ {                                  # WebSockets
        proxy_pass http://127.0.0.1:8080;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 3600s;
    }
}
server { listen 80; server_name example.com; return 301 https://$host$request_uri; }
```
Validate: `nginx -t`.

## 3. systemd service with sandboxing
```ini
[Unit]
Description=Example API
After=network-online.target
Wants=network-online.target

[Service]
User=appuser
Group=appuser
WorkingDirectory=/opt/app
EnvironmentFile=/etc/app/app.env          # chmod 640 root:appuser; no secrets in the unit file
ExecStart=/opt/app/bin/server
Restart=on-failure
RestartSec=3
TimeoutStopSec=30
# Hardening
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/lib/app
CapabilityBoundingSet=
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX
SystemCallFilter=@system-service
MemoryMax=512M

[Install]
WantedBy=multi-user.target
```
Check: `systemd-analyze verify app.service`, `systemd-analyze security app.service`.

## 4. Dockerfile (multi-stage, non-root, healthcheck)
```dockerfile
# syntax=docker/dockerfile:1
FROM node:22-slim AS build            # pin by digest in production
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build && npm prune --omit=dev

FROM node:22-slim AS runtime
ENV NODE_ENV=production
WORKDIR /app
RUN useradd --system --uid 10001 app
COPY --from=build --chown=app:app /app /app
USER app
EXPOSE 8080
HEALTHCHECK --interval=15s --timeout=3s --retries=3 CMD node -e "fetch('http://127.0.0.1:8080/healthz').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))"
CMD ["node", "src/server.js"]
```
Add `.dockerignore` (`.git`, `node_modules`, `.env*`, tests, docs). Scan images (Trivy/Grype), generate an SBOM, sign (cosign), run read-only root filesystem where possible.

## 5. Docker Compose (app + Postgres + proxy; adapt)
```yaml
services:
  app:
    build: .
    restart: unless-stopped
    env_file: .env.production            # not committed
    depends_on:
      db: { condition: service_healthy }
    read_only: true
    tmpfs: [/tmp]
    cap_drop: [ALL]
    security_opt: ["no-new-privileges:true"]
    networks: [internal, web]
  db:
    image: postgres:16                   # choose a supported major; pin digest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets: [db_password]
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks: [internal]                 # not published to the host
volumes: { pgdata: {} }
networks:
  internal: { internal: true }
  web: {}
secrets:
  db_password: { file: ./secrets/db_password.txt }
```
Never publish database ports publicly; note Docker's published ports bypass some host firewall rules (bind to `127.0.0.1:` or use the `DOCKER-USER` chain).

## 6. Fresh VPS baseline (Debian/Ubuntu)
```bash
# as root on first login; keep a second SSH session open while changing sshd
adduser --disabled-password --gecos "" deploy && usermod -aG sudo deploy
install -d -m 700 -o deploy -g deploy /home/deploy/.ssh   # then add your public key
cat >/etc/ssh/sshd_config.d/10-hardening.conf <<'EOT'
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AllowUsers deploy
MaxAuthTries 3
EOT
sshd -t && systemctl reload ssh
ufw default deny incoming && ufw default allow outgoing
ufw allow OpenSSH && ufw allow 80/tcp && ufw allow 443/tcp && ufw enable
apt-get update && apt-get install -y unattended-upgrades fail2ban chrony
dpkg-reconfigure -plow unattended-upgrades
timedatectl set-timezone UTC
```
Also: provider snapshots plus off-box backups, monitoring agent, log rotation, swap sized for the workload, SSH on key-only (optionally behind a VPN/Tailscale/WireGuard), separate non-root service users, and a documented rebuild procedure.

## 7. Backups (restic + Postgres dump; schedule with systemd timer or cron)
```bash
#!/usr/bin/env bash
set -euo pipefail
export RESTIC_REPOSITORY="s3:s3.example.com/backups/app"   # or sftp:, b2:, etc.
export RESTIC_PASSWORD_FILE=/etc/restic/password           # chmod 600
pg_dump --format=custom --file=/var/backups/app.dump "$DATABASE_URL"
restic backup /var/backups/app.dump /var/lib/app/uploads --tag nightly
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune
restic check --read-data-subset=5%
```
For point-in-time recovery use pgBackRest or WAL-G. A backup that has not been restored in a drill is a hope, not a backup.

## 8. CI pipeline (GitHub Actions shape; pin actions to commit SHAs)
```yaml
name: ci
on: { pull_request: {}, push: { branches: [main] } }
permissions: { contents: read }
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@<sha>
      - uses: actions/setup-node@<sha>
        with: { node-version: 22, cache: npm }
      - run: npm ci
      - run: npm run lint && npm test && npm run build
  security:
    runs-on: ubuntu-latest
    permissions: { contents: read, security-events: write }
    steps:
      - uses: actions/checkout@<sha>
      - run: npm audit --omit=dev --audit-level=high
```
Add secret scanning, dependency review, SAST (CodeQL/Semgrep), container scan, SBOM, provenance (SLSA), environment protections, manual approval for production, and automated rollback or a documented one.

## 9. Kubernetes deployment essentials
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: api }
spec:
  replicas: 3
  strategy: { type: RollingUpdate, rollingUpdate: { maxUnavailable: 0, maxSurge: 1 } }
  selector: { matchLabels: { app: api } }
  template:
    metadata: { labels: { app: api } }
    spec:
      securityContext: { runAsNonRoot: true, seccompProfile: { type: RuntimeDefault } }
      terminationGracePeriodSeconds: 30
      containers:
        - name: api
          image: registry.example.com/api@sha256:<digest>
          ports: [{ containerPort: 8080 }]
          readinessProbe: { httpGet: { path: /readyz, port: 8080 }, periodSeconds: 5 }
          livenessProbe:  { httpGet: { path: /healthz, port: 8080 }, periodSeconds: 10, failureThreshold: 3 }
          resources: { requests: { cpu: 100m, memory: 128Mi }, limits: { memory: 256Mi } }
          securityContext: { allowPrivilegeEscalation: false, readOnlyRootFilesystem: true, capabilities: { drop: [ALL] } }
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata: { name: api }
spec: { minAvailable: 2, selector: { matchLabels: { app: api } } }
```
Add NetworkPolicies, HPA with sane bounds, topology spread, secrets via external secret operators, namespace quotas. Use Kubernetes only when you need what it provides.

## 10. Prometheus alert examples (symptom-based)
```yaml
groups:
- name: api
  rules:
  - alert: HighErrorRate
    expr: sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) > 0.02
    for: 10m
    labels: { severity: page }
    annotations: { summary: ">2% 5xx for 10m", runbook: "runbooks/high-error-rate.md" }
  - alert: SlowRequests
    expr: histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m]))) > 1
    for: 15m
    labels: { severity: ticket }
  - alert: QueueAgeHigh
    expr: max(queue_oldest_message_age_seconds) > 300
    for: 10m
    labels: { severity: page }
```
Alert on user-visible symptoms and error-budget burn; every page links a runbook; delete alerts nobody acts on.

## 11. Terraform/IaC skeleton conventions
Remote encrypted state with locking; one module per concern; variables with validation; pinned provider versions; plan in CI, apply with approval; tag everything (owner, env, cost-center); least-privilege deploy role; drift detection; no secrets in state where avoidable (use references to a secrets manager).

## 12. DNS and email deliverability checklist
A/AAAA/CNAME for hosts, low TTL before migrations; CAA records; SPF, DKIM, DMARC (start `p=none`, move to `quarantine`/`reject` after monitoring); MTA-STS/TLS-RPT where relevant; separate transactional and marketing sending domains; reverse DNS for mail servers; monitor bounces and complaints.

## Verification
Record which snippets were syntax-checked (`nginx -t`, `caddy validate`, `docker compose config`, `systemd-analyze verify`, `kubectl apply --dry-run=server`, `terraform validate`, `shellcheck`, `yamllint`) versus only reviewed.

**Checked when this edition was assembled:** the YAML blocks (Compose, CI, Kubernetes, Prometheus) parse as valid YAML; the shell blocks pass `bash -n`; the systemd unit passes `systemd-analyze verify` apart from the placeholder binary path. **Not executed:** nginx, Caddy, Docker builds, Kubernetes dry-runs, Terraform, restic/pg_dump runs. Run the tools listed above in your environment before relying on them.
