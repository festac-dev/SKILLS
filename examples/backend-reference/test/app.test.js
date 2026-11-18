'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const L = require('../src/lib');
const { createApp } = require('../src/app');

const silent = { info() {}, warn() {}, error() {} };
async function boot(opts = {}) {
  const app = createApp({ logger: silent, ...opts });
  await new Promise((r) => app.server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${app.server.address().port}`;
  return { app, base, close: () => app.shutdown(1000) };
}
const post = (base, path, body, headers = {}) => fetch(base + path, { method: 'POST', headers: { 'content-type': 'application/json', ...headers }, body: typeof body === 'string' ? body : JSON.stringify(body) });

test('health and readiness', async () => {
  const s = await boot(); 
  assert.equal((await fetch(s.base + '/healthz')).status, 200);
  assert.equal((await fetch(s.base + '/readyz')).status, 200);
  await s.close();
});

test('security headers and request id are set', async () => {
  const s = await boot(); const r = await fetch(s.base + '/healthz');
  assert.equal(r.headers.get('x-content-type-options'), 'nosniff');
  assert.match(r.headers.get('x-request-id'), /^[\w-]{8,64}$/);
  await s.close();
});

test('validation returns 422 problem+json with field errors; unknown keys dropped', async () => {
  const s = await boot();
  let r = await post(s.base, '/v1/items', { quantity: 'x' });
  assert.equal(r.status, 422); assert.match(r.headers.get('content-type'), /problem\+json/);
  const b = await r.json(); assert.ok(b.errors.length >= 1); assert.ok(b.request_id);
  r = await post(s.base, '/v1/items', { name: 'a', admin: true });
  assert.equal(r.status, 201); assert.equal((await r.json()).admin, undefined);
  await s.close();
});

test('bad JSON is 400 and oversized body is 413', async () => {
  const s = await boot({ bodyLimit: 50 });
  assert.equal((await post(s.base, '/v1/items', '{oops')).status, 400);
  const big = await post(s.base, '/v1/items', JSON.stringify({ name: 'x'.repeat(500) })).catch(() => ({ status: 413 }));
  assert.equal(big.status, 413);
  await s.close();
});

test('API key auth rejects missing/wrong keys and accepts the right one', async () => {
  const s = await boot({ apiKeys: ['secret-key-123'] });
  assert.equal((await post(s.base, '/v1/items', { name: 'a' })).status, 401);
  assert.equal((await post(s.base, '/v1/items', { name: 'a' }, { 'x-api-key': 'nope' })).status, 401);
  assert.equal((await post(s.base, '/v1/items', { name: 'a' }, { 'x-api-key': 'secret-key-123' })).status, 201);
  await s.close();
});

test('idempotency: replay returns same item; different body with same key conflicts', async () => {
  const s = await boot(); const h = { 'idempotency-key': 'key-abcdefgh' };
  const a = await post(s.base, '/v1/items', { name: 'one' }, h);
  const b = await post(s.base, '/v1/items', { name: 'one' }, h);
  assert.equal(a.status, 201); assert.equal(b.status, 201);
  assert.equal(b.headers.get('idempotent-replayed'), 'true');
  assert.equal((await a.json()).id, (await b.json()).id);
  assert.equal(s.app.state().items, 1);
  assert.equal((await post(s.base, '/v1/items', { name: 'two' }, h)).status, 422);
  await s.close();
});

test('cursor pagination walks all items without duplicates', async () => {
  const s = await boot({ rate: { capacity: 1000, refillPerSec: 1000 } });
  for (let i = 0; i < 25; i++) await post(s.base, '/v1/items', { name: 'n' + i });
  const seen = []; let cursor = null;
  do {
    const r = await (await fetch(`${s.base}/v1/items?limit=10${cursor ? '&cursor=' + cursor : ''}`)).json();
    seen.push(...r.data.map((d) => d.id)); cursor = r.next_cursor;
  } while (cursor);
  assert.equal(seen.length, 25); assert.equal(new Set(seen).size, 25);
  assert.equal((await fetch(s.base + '/v1/items?cursor=@@@')).status, 400);
  await s.close();
});

test('rate limiter returns 429 with Retry-After once the bucket is empty', async () => {
  const s = await boot({ rate: { capacity: 3, refillPerSec: 0.001 } });
  const codes = []; for (let i = 0; i < 5; i++) codes.push((await fetch(s.base + '/v1/items')).status);
  assert.deepEqual(codes.slice(0, 3), [200, 200, 200]); assert.equal(codes[3], 429);
  const r = await fetch(s.base + '/v1/items'); assert.ok(Number(r.headers.get('retry-after')) >= 1);
  assert.equal((await fetch(s.base + '/healthz')).status, 200); // health checks are not rate limited
  await s.close();
});

test('webhook signature: valid accepted; tampered, stale and unsigned rejected', async () => {
  const secret = 'whsec_test'; const s = await boot({ webhookSecret: secret });
  const body = JSON.stringify({ event: 'ping' }); const ts = String(Math.floor(Date.now() / 1000));
  const good = L.signWebhook(secret, ts, body);
  assert.equal((await post(s.base, '/webhooks/example', body, { 'x-timestamp': ts, 'x-signature': good })).status, 202);
  assert.equal((await post(s.base, '/webhooks/example', body + ' ', { 'x-timestamp': ts, 'x-signature': good })).status, 401);
  const old = String(Math.floor(Date.now() / 1000) - 3600);
  assert.equal((await post(s.base, '/webhooks/example', body, { 'x-timestamp': old, 'x-signature': L.signWebhook(secret, old, body) })).status, 401);
  assert.equal((await post(s.base, '/webhooks/example', body)).status, 401);
  await s.close();
});

test('retry uses backoff with jitter and stops on non-retryable errors', async () => {
  const sleeps = []; let calls = 0;
  const out = await L.retry(async () => { if (++calls < 3) throw new Error('boom'); return 'ok'; }, { sleep: async (ms) => sleeps.push(ms), rand: () => 1 });
  assert.equal(out, 'ok'); assert.deepEqual(sleeps, [100, 200]);
  calls = 0;
  await assert.rejects(L.retry(async () => { calls++; throw new Error('fatal'); }, { retryable: () => false }));
  assert.equal(calls, 1);
});

test('graceful shutdown flips readiness before closing', async () => {
  const s = await boot({ drainDelayMs: 50 });
  const p = s.app.shutdown(1000);
  assert.equal(s.app.state().ready, false);
  await p;
});

test('unknown route is 404 problem+json and never leaks internals', async () => {
  const s = await boot(); const r = await fetch(s.base + '/nope');
  assert.equal(r.status, 404); const b = await r.json(); assert.equal(b.title, 'Not Found'); assert.equal(b.stack, undefined);
  await s.close();
});
