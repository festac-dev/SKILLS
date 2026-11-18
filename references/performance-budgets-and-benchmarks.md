# Performance Budgets and Reference Numbers

Starting targets, not laws. Replace with measured user and business data. Measure at realistic percentiles (p75 for web vitals, p95/p99 for APIs) on representative devices and networks.

## Web (field data, p75)
| Metric | Good | Needs improvement | Poor |
|---|---|---|---|
| Largest Contentful Paint (LCP) | ≤ 2.5 s | ≤ 4 s | > 4 s |
| Interaction to Next Paint (INP) | ≤ 200 ms | ≤ 500 ms | > 500 ms |
| Cumulative Layout Shift (CLS) | ≤ 0.1 | ≤ 0.25 | > 0.25 |
| Time to First Byte (TTFB) guidance | ≤ 800 ms | | |

Typical page budgets (tune per audience): JS ≤ 150–200 KB compressed for content sites, ≤ 300–400 KB for apps' initial route; critical CSS inline or ≤ 50 KB; hero image ≤ 150 KB (AVIF/WebP); fonts ≤ 2 families, subset, `font-display: swap`/`optional`; third-party scripts audited and deferred.

## Animation and graphics
- 60 fps target = 16.7 ms per frame including browser work; aim for < 8 ms of your own script per frame on mid-range phones.
- Animate `transform` and `opacity`; avoid animating layout properties (`width`, `top`, `margin`) and large blurs/shadows.
- Canvas/WebGL: cap devicePixelRatio (1.5–2), cap particle counts (hundreds on mobile, low thousands on desktop for 2D), instance draws, pause when hidden or off-screen, test on a throttled CPU profile.
- Shaders: cost scales with pixels × per-pixel work; prefer half-resolution render targets for heavy effects.
- Respect `prefers-reduced-motion`, data-saver and low-power hints; provide a static equivalent.

## Response-time perception
~100 ms feels instant; ~1 s keeps flow; > 10 s loses attention (show progress). Give feedback within 100 ms for every action; use optimistic UI where rollback is safe.

## API and backend (illustrative starting SLOs)
| Surface | p95 latency | Availability |
|---|---|---|
| Read endpoints served from cache/index | 50–150 ms | 99.9% |
| Typical CRUD write | 100–300 ms | 99.9% |
| Search/aggregations | 200–800 ms | 99.5–99.9% |
| Background job queue age (normal) | < 1–5 min | alert on age, not depth |
Error budget for 99.9% ≈ 43 min/month; 99.99% ≈ 4.3 min/month. Pick SLOs users would actually notice; every extra nine multiplies cost.

## Database and capacity rules of thumb
- Connection pools sized to cores and workload, not "as many as possible"; use a pooler for many app instances.
- Keep hot working set in memory; watch cache-hit ratio, index bloat, replication lag, lock waits, slow queries (> 100 ms for OLTP).
- Back-of-envelope: requests/s = daily active users × actions per user ÷ 86,400 × peak factor (2–10). Test at 2–3× expected peak.
- Storage growth = rows/day × bytes/row × retention × index overhead (often 1.5–3×) × replicas/backups.

## Mobile and device
Cold start to interactive: ≤ 2–3 s on mid-range devices; keep main thread work < 50 ms chunks; reduce wake-ups for battery; test on low-memory devices and poor networks.

## Process
Set budgets early (`templates/PERFORMANCE_BUDGET.md`), enforce in CI (Lighthouse CI, bundle-size checks, k6/Locust load tests), watch real-user monitoring, review regressions per release. Investigation steps: `playbooks/PERFORMANCE_INVESTIGATION_PLAYBOOK.md`.
