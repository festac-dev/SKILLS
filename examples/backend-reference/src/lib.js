'use strict';
const crypto = require('node:crypto');

/* ---------- structured logging ---------- */
function createLogger(base = {}, out = process.stdout) {
  const log = (level, msg, fields) =>
    out.write(JSON.stringify({ ts: new Date().toISOString(), level, msg, ...base, ...fields }) + '\n');
  return {
    info: (m, f) => log('info', m, f),
    warn: (m, f) => log('warn', m, f),
    error: (m, f) => log('error', m, f),
  };
}

/* ---------- problem+json errors (RFC 9457 shape) ---------- */
class HttpError extends Error {
  constructor(status, title, detail, extra = {}) {
    super(title);
    this.status = status; this.title = title; this.detail = detail; this.extra = extra;
  }
}
function sendJson(res, status, body, headers = {}) {
  const data = JSON.stringify(body);
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8', 'content-length': Buffer.byteLength(data), ...headers });
  res.end(data);
}
function sendProblem(res, err, requestId) {
  const status = err.status || 500;
  const body = { type: 'about:blank', title: status >= 500 ? 'Internal Server Error' : err.title, status, request_id: requestId };
  if (status < 500 && err.detail) body.detail = err.detail; // never leak internals on 5xx
  Object.assign(body, status < 500 ? err.extra : {});
  sendJson(res, status, body, { 'content-type': 'application/problem+json; charset=utf-8' });
}

/* ---------- body parsing with a hard size limit ---------- */
function readBody(req, limit = 1_000_000) {
  return new Promise((resolve, reject) => {
    const chunks = []; let size = 0;
    req.on('data', (c) => {
      size += c.length;
      if (size > limit) { reject(new HttpError(413, 'Payload Too Large')); req.destroy(); return; }
      chunks.push(c);
    });
    req.on('end', () => resolve(Buffer.concat(chunks)));
    req.on('error', reject);
  });
}
function parseJson(buf) {
  if (!buf.length) return {};
  try { return JSON.parse(buf.toString('utf8')); }
  catch { throw new HttpError(400, 'Invalid JSON'); }
}

/* ---------- tiny schema validation (use zod/valibot/ajv/pydantic in real projects) ---------- */
function validate(input, schema) {
  const errors = [], out = {};
  for (const [key, rule] of Object.entries(schema)) {
    const v = input[key];
    if (v === undefined || v === null) { if (rule.required) errors.push({ field: key, message: 'required' }); continue; }
    if (rule.type === 'string' && typeof v !== 'string') errors.push({ field: key, message: 'must be a string' });
    else if (rule.type === 'integer' && !Number.isInteger(v)) errors.push({ field: key, message: 'must be an integer' });
    else if (rule.type === 'string' && (v.length < (rule.min ?? 0) || v.length > (rule.max ?? 10_000))) errors.push({ field: key, message: `length must be ${rule.min ?? 0}-${rule.max ?? 10000}` });
    else if (rule.type === 'integer' && ((rule.min !== undefined && v < rule.min) || (rule.max !== undefined && v > rule.max))) errors.push({ field: key, message: 'out of range' });
    else out[key] = v;
  }
  if (errors.length) throw new HttpError(422, 'Validation failed', 'One or more fields are invalid', { errors });
  return out; // unknown keys are dropped (allow-list)
}

/* ---------- token-bucket rate limiter (single node; use Redis/edge for many nodes) ---------- */
function createRateLimiter({ capacity = 20, refillPerSec = 10, maxKeys = 10_000, now = () => Date.now() } = {}) {
  const buckets = new Map();
  return function take(key) {
    const t = now();
    let b = buckets.get(key);
    if (!b) {
      if (buckets.size >= maxKeys) buckets.delete(buckets.keys().next().value); // bound memory
      b = { tokens: capacity, last: t }; buckets.set(key, b);
    }
    b.tokens = Math.min(capacity, b.tokens + ((t - b.last) / 1000) * refillPerSec);
    b.last = t;
    if (b.tokens >= 1) { b.tokens -= 1; return { allowed: true, remaining: Math.floor(b.tokens), retryAfter: 0 }; }
    return { allowed: false, remaining: 0, retryAfter: Math.ceil((1 - b.tokens) / refillPerSec) };
  };
}

/* ---------- idempotency keys: same key + same payload => same stored response ---------- */
function createIdempotencyStore({ ttlMs = 24 * 3600 * 1000, now = () => Date.now() } = {}) {
  const entries = new Map();
  const hash = (s) => crypto.createHash('sha256').update(s).digest('hex');
  return {
    begin(key, scope, payload) {
      const id = `${scope}:${key}`, h = hash(payload), e = entries.get(id);
      if (e && now() - e.at > ttlMs) entries.delete(id);
      const cur = entries.get(id);
      if (!cur) { entries.set(id, { h, at: now(), state: 'in_progress' }); return { kind: 'new' }; }
      if (cur.h !== h) return { kind: 'conflict' };            // same key, different body: client bug
      if (cur.state === 'in_progress') return { kind: 'in_progress' };
      return { kind: 'replay', response: cur.response };
    },
    complete(key, scope, response) { const e = entries.get(`${scope}:${key}`); if (e) { e.state = 'done'; e.response = response; } },
    abandon(key, scope) { entries.delete(`${scope}:${key}`); },
  };
}

/* ---------- opaque keyset (cursor) pagination ---------- */
const encodeCursor = (obj) => Buffer.from(JSON.stringify(obj)).toString('base64url');
function decodeCursor(c) {
  try { return JSON.parse(Buffer.from(c, 'base64url').toString('utf8')); }
  catch { throw new HttpError(400, 'Invalid cursor'); }
}

/* ---------- webhook signature verification (HMAC-SHA256, timestamp window, constant-time compare) ---------- */
function signWebhook(secret, timestamp, rawBody) {
  return crypto.createHmac('sha256', secret).update(`${timestamp}.${rawBody}`).digest('hex');
}
function verifyWebhook({ secret, timestamp, signature, rawBody, toleranceSec = 300, now = () => Date.now() }) {
  const ts = Number(timestamp);
  if (!Number.isFinite(ts) || Math.abs(now() / 1000 - ts) > toleranceSec) return false; // replay protection
  const expected = Buffer.from(signWebhook(secret, timestamp, rawBody), 'hex');
  let given; try { given = Buffer.from(String(signature), 'hex'); } catch { return false; }
  return given.length === expected.length && crypto.timingSafeEqual(given, expected);
}

/* ---------- retry with exponential backoff and full jitter (for outbound calls) ---------- */
async function retry(fn, { attempts = 4, baseMs = 100, capMs = 5000, retryable = () => true, sleep = (ms) => new Promise((r) => setTimeout(r, ms)), rand = Math.random } = {}) {
  let lastErr;
  for (let i = 0; i < attempts; i++) {
    try { return await fn(i); }
    catch (e) {
      lastErr = e;
      if (i === attempts - 1 || !retryable(e)) break;
      await sleep(rand() * Math.min(capMs, baseMs * 2 ** i)); // full jitter avoids retry storms
    }
  }
  throw lastErr;
}

/* ---------- security headers for API responses ---------- */
const SECURITY_HEADERS = {
  'x-content-type-options': 'nosniff',
  'referrer-policy': 'no-referrer',
  'cross-origin-resource-policy': 'same-origin',
  'cache-control': 'no-store',
  'content-security-policy': "default-src 'none'; frame-ancestors 'none'",
};

module.exports = { createLogger, HttpError, sendJson, sendProblem, readBody, parseJson, validate, createRateLimiter, createIdempotencyStore, encodeCursor, decodeCursor, signWebhook, verifyWebhook, retry, SECURITY_HEADERS };
