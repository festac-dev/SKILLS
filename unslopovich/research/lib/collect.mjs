// The collection loop both platforms share: walk an app's storefront-and-sort
// passes in a seeded order, take at most CAP_PER_PASS from each, stop at the
// store's CAP_PER_APP, dedupe by review id, and write one file per app.
//
// Collection is incremental. An app already collected is skipped when it has
// reached the cap or has no pass left to run; otherwise it continues with the
// passes it has not run yet (new storefronts, or the rest of its order after a
// cap increase), keeping what it has. An app with a failed pass is collected
// again from scratch, so a temporary error leaves no hole.

import fs from "node:fs";
import { CAP_PER_APP, CAP_PER_PASS, CONCURRENCY, SEED, WINDOW_MONTHS } from "../config.mjs";
import { dataPath, readJson, readJsonlGz, writeJsonlGz, writeJson, rng, shuffle, hash, pool, log } from "./util.mjs";

// Countries in a per-app random order, each with every sort order, so a big
// app that hits its cap early still gets a random mix of storefronts and
// alternates between newest and most-helpful reviews.
export function passesFor(appId, countries, sorts) {
  const order = shuffle(countries, rng(SEED ^ hash(appId)));
  return order.flatMap((country) => sorts.map((sort) => ({ country, sort })));
}

// Rounds in order, and inside each round the categories in rotation, so that
// a collection stopped at any point has covered every category evenly.
export function collectionOrder(apps) {
  const rounds = [...new Set(apps.map((a) => a.round || 1))].sort((a, b) => a - b);
  const out = [];
  for (const round of rounds) {
    const byCategory = new Map();
    for (const a of apps.filter((x) => (x.round || 1) === round)) {
      if (!byCategory.has(a.category)) byCategory.set(a.category, []);
      byCategory.get(a.category).push(a);
    }
    const queues = [...byCategory.values()];
    for (let i = 0; queues.some((q) => i < q.length); i++) for (const q of queues) if (i < q.length) out.push(q[i]);
  }
  return out;
}

export function windowStart(now = new Date()) {
  const d = new Date(now);
  d.setUTCMonth(d.getUTCMonth() - WINDOW_MONTHS);
  return d.toISOString();
}

// Sort orders that return newest first: once a page is older than the window,
// later pages are too.
const NEWEST_FIRST = new Set(["mostrecent", "NEWEST"]);

export async function collectPlatform(platform, { countries, sorts, fetchPass, limit, concurrency, stopAt }) {
  const since = windowStart();
  const { apps } = readJson(dataPath("apps.json"));
  const mine = collectionOrder(apps.filter((a) => a.platform === platform)).slice(0, limit ? Number(limit) : undefined);
  let done = 0;
  let total = 0;
  // Count what is already collected, so --stop-at can stop starting new apps
  // once the store reaches its target. Apps are in rotation order, so stopping
  // early leaves every category covered evenly.
  let collected = 0;
  for (const a of mine) {
    const f = dataPath("raw", platform, `${a.id}.meta.json`);
    if (fs.existsSync(f)) collected += readJson(f).kept;
  }
  const target = Number(stopAt) || Infinity;
  await pool(mine, Number(concurrency) || CONCURRENCY, async (app) => {
    if (collected >= target && !fs.existsSync(dataPath("raw", platform, `${app.id}.meta.json`))) return;
    const out = dataPath("raw", platform, `${app.id}.jsonl.gz`);
    const metaFile = dataPath("raw", platform, `${app.id}.meta.json`);
    const cap = CAP_PER_APP[platform];
    const plan = passesFor(app.id, countries, sorts);
    const byId = new Map();
    let prior = [];
    let requests = 0;
    let todo = plan;
    let byIdStart = 0;
    if (fs.existsSync(out) && fs.existsSync(metaFile)) {
      const meta = readJson(metaFile);
      if (!meta.passes.some((p) => p.error)) {
        const ran = new Set(meta.passes.map((p) => `${p.country}|${p.sort}`));
        todo = plan.filter((p) => !ran.has(`${p.country}|${p.sort}`));
        if (meta.kept >= cap || !todo.length) {
          total += meta.kept;
          done++;
          return;
        }
        for (const r of readJsonlGz(out)) byId.set(r.id, r);
        byIdStart = byId.size;
        prior = meta.passes;
        requests = meta.requests;
      }
    }
    const passes = [];
    // A storefront whose newest-first list has nothing inside the window has
    // nothing inside it in any order, so its other passes are skipped.
    const empty = new Set(prior.filter((p) => p.inWindow === 0 && NEWEST_FIRST.has(p.sort)).map((p) => p.country));
    for (const pass of todo) {
      if (byId.size >= cap) break;
      if (empty.has(pass.country)) {
        passes.push({ ...pass, skipped: "no reviews in the window" });
        continue;
      }
      let inWindow = 0;
      let added = 0;
      let seenInPass = 0;
      let outside = 0;
      const room = () => Math.min(CAP_PER_PASS - added, cap - byId.size);
      try {
        for await (const page of fetchPass(app, pass)) {
          requests++;
          let pageInWindow = 0;
          for (const review of page) {
            seenInPass++;
            if (room() <= 0) break;
            if (!review.date || review.date < since) {
              outside++;
              continue;
            }
            pageInWindow++;
            inWindow++;
            if (byId.has(review.id)) continue;
            byId.set(review.id, { ...review, app: app.id, platform, country: pass.country, sort: pass.sort });
            added++;
          }
          if (room() <= 0) break;
          if (NEWEST_FIRST.has(pass.sort) && pageInWindow === 0) break;
        }
      } catch (err) {
        passes.push({ ...pass, error: String(err.message || err) });
        continue;
      }
      passes.push({ ...pass, seen: seenInPass, outsideWindow: outside, inWindow, added });
      if (NEWEST_FIRST.has(pass.sort) && inWindow === 0) empty.add(pass.country);
    }
    const rows = [...byId.values()];
    writeJsonlGz(out, rows);
    const dates = rows.map((r) => r.date).filter(Boolean).sort();
    writeJson(metaFile, {
      app: app.id,
      platform,
      requests,
      since,
      cap,
      collectedAt: new Date().toISOString(),
      kept: rows.length,
      oldest: dates[0] ?? null,
      newest: dates.at(-1) ?? null,
      passes: [...prior, ...passes],
    });
    total += rows.length;
    collected += rows.length - (prior.length ? byIdStart : 0);
    done++;
    log(`${platform} ${done}/${mine.length} ${app.name.slice(0, 40)}: ${rows.length} reviews, ${requests} requests (total ${total})`);
  });
  log(`${platform} finished: ${done} apps, ${total} reviews`);
}
