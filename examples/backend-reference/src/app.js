'use strict';
const http = require('node:http');
const crypto = require('node:crypto');
const L = require('./lib');

/** Builds an HTTP server wired with the production-minded patterns in lib.js.
 *  The "items" store is in-memory so the example runs anywhere; swap for a real database. */
function createApp(opts = {}) {
  const config = {
    webhookSecret: opts.webhookSecret || process.env.WEBHOOK_SECRET || '',
    apiKeys: opts.apiKeys || (process.env.API_KEYS ? process.env.API_KEYS.split(',') : []),
    bodyLimit: opts.bodyLimit || 100_000,
    trustProxy: opts.trustProxy ?? false,
    rate: opts.rate || { capacity: 20, refillPerSec: 10 },
  };
  const logger = opts.logger || L.createLogger({ service: 'backend-reference' });
  const limiter = L.createRateLimiter(config.rate);
  const idem = L.createIdempotencyStore();
  const items = []; // append-only; ids are monotonically increasing
  let ready = true, inflight = 0;

  const clientIp = (req) =>
    (config.trustProxy && req.headers['x-forwarded-for']?.split(',')[0].trim()) || req.socket.remoteAddress || 'unknown';

  function authenticate(req) {
    if (!config.apiKeys.length) return 'anonymous';
    const given = Buffer.from(String(req.headers['x-api-key'] || ''));
    for (const k of config.apiKeys) {
      const want = Buffer.from(k);
      if (given.length === want.length && crypto.timingSafeEqual(given, want)) return 'key:' + crypto.createHash('sha256').update(k).digest('hex').slice(0, 8);
    }
    throw new L.HttpError(401, 'Unauthorized');
  }

  async function route(req, res, ctx) {
    const url = new URL(req.url, 'http://x');
    const { method } = req;

    if (url.pathname === '/healthz') return L.sendJson(res, 200, { status: 'ok' });            // liveness: process is up
    if (url.pathname === '/readyz') return L.sendJson(res, ready ? 200 : 503, { ready });        // readiness: accept traffic?

    if (url.pathname === '/webhooks/example' && method === 'POST') {
      const raw = await L.readBody(req, config.bodyLimit);                                       // verify on RAW bytes, then parse
      const ok = L.verifyWebhook({ secret: config.webhookSecret, timestamp: req.headers['x-timestamp'], signature: req.headers['x-signature'], rawBody: raw.toString('utf8') });
      if (!config.webhookSecret || !ok) throw new L.HttpError(401, 'Invalid signature');
      return L.sendJson(res, 202, { accepted: true });                                           // ack fast; process async via a queue
    }

    if (url.pathname === '/v1/items') {
      const principal = authenticate(req);                                                       // authN
      ctx.principal = principal;                                                                 // authZ would check ownership here
      if (method === 'POST') {
        const raw = await L.readBody(req, config.bodyLimit);
        const input = L.validate(L.parseJson(raw), { name: { type: 'string', required: true, min: 1, max: 100 }, quantity: { type: 'integer', min: 0, max: 1_000_000 } });
        const key = req.headers['idempotency-key'];
        if (key) {
          const r = idem.begin(key, principal, raw.toString('utf8'));
          if (r.kind === 'conflict') throw new L.HttpError(422, 'Idempotency-Key reused with a different request');
          if (r.kind === 'in_progress') throw new L.HttpError(409, 'A request with this Idempotency-Key is in progress');
          if (r.kind === 'replay') return L.sendJson(res, r.response.status, r.response.body, { 'idempotent-replayed': 'true' });
        }
        try {
          const item = { id: items.length + 1, name: input.name, quantity: input.quantity ?? 0, owner: principal };
          items.push(item);
          const response = { status: 201, body: item };
          if (key) idem.complete(key, principal, response);
          return L.sendJson(res, 201, item, { location: `/v1/items/${item.id}` });
        } catch (e) { if (key) idem.abandon(key, principal); throw e; }
      }
      if (method === 'GET') {
        const limit = Math.min(Math.max(parseInt(url.searchParams.get('limit') || '10', 10) || 10, 1), 100);
        const after = url.searchParams.get('cursor') ? L.decodeCursor(url.searchParams.get('cursor')).after : 0;
        const page = items.filter((i) => i.id > after).slice(0, limit + 1);                     // fetch one extra to know if more exist
        const hasMore = page.length > limit;
        const data = page.slice(0, limit);
        return L.sendJson(res, 200, { data, next_cursor: hasMore ? L.encodeCursor({ after: data[data.length - 1].id }) : null });
      }
      throw new L.HttpError(405, 'Method Not Allowed');
    }
    throw new L.HttpError(404, 'Not Found');
  }

  const server = http.createServer(async (req, res) => {
    const start = process.hrtime.bigint();
    const requestId = req.headers['x-request-id'] && /^[\w-]{8,64}$/.test(req.headers['x-request-id']) ? req.headers['x-request-id'] : crypto.randomUUID();
    res.setHeader('x-request-id', requestId);
    for (const [k, v] of Object.entries(L.SECURITY_HEADERS)) res.setHeader(k, v);
    const ctx = {}; inflight++;
    res.on('close', () => {
      inflight--;
      logger.info('request', { request_id: requestId, method: req.method, path: req.url.split('?')[0], status: res.statusCode, ms: Number(process.hrtime.bigint() - start) / 1e6, principal: ctx.principal });
    });
    try {
      const path = req.url.split('?')[0];
      if (path !== '/healthz' && path !== '/readyz') {
        const rl = limiter(clientIp(req));
        res.setHeader('ratelimit-remaining', String(rl.remaining));
        if (!rl.allowed) { res.setHeader('retry-after', String(rl.retryAfter)); throw new L.HttpError(429, 'Too Many Requests'); }
      }
      await route(req, res, ctx);
    } catch (err) {
      if (!(err instanceof L.HttpError)) logger.error('unhandled', { request_id: requestId, err: String(err && err.stack || err) });
      if (!res.headersSent) L.sendProblem(res, err, requestId); else res.end();
    }
  });
  // Slowloris and idle-connection protection
  server.headersTimeout = 10_000; server.requestTimeout = 30_000; server.keepAliveTimeout = 5_000;

  /** Graceful shutdown: flip readiness, stop accepting, drain in-flight, then exit. */
  async function shutdown(graceMs = 10_000) {
    ready = false;
    await new Promise((r) => setTimeout(r, Math.min(graceMs, opts.drainDelayMs ?? 0))); // let the load balancer notice
    await new Promise((resolve) => { server.close(() => resolve()); server.closeIdleConnections?.(); setTimeout(() => { server.closeAllConnections?.(); resolve(); }, graceMs).unref(); });
  }
  return { server, shutdown, config, state: () => ({ ready, inflight, items: items.length }) };
}
module.exports = { createApp };
