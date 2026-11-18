// Shared helpers for the research pipeline: paths, seeded randomness,
// gzip JSONL files, polite fetching, and progress state.

import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";

export const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
export const DATA = process.env.UNSLOP_DATA || path.join(ROOT, "data");
export const RESULTS = path.join(ROOT, "results");

export function dataPath(...parts) {
  const p = path.join(DATA, ...parts);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  return p;
}

export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// mulberry32: small, fast, seeded PRNG so every sample is reproducible.
export function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

export function shuffle(items, random) {
  const a = items.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// Stable string hash, used to derive per-app seeds.
export function hash(s) {
  let h = 2166136261;
  for (let i = 0; i < s.length; i++) h = Math.imul(h ^ s.charCodeAt(i), 16777619);
  return h >>> 0;
}

export function writeJson(file, value) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const tmp = `${file}.tmp`;
  fs.writeFileSync(tmp, JSON.stringify(value, null, 2) + "\n");
  fs.renameSync(tmp, file);
}

export function readJson(file, fallback) {
  try {
    return JSON.parse(fs.readFileSync(file, "utf8"));
  } catch (err) {
    if (fallback !== undefined && err.code === "ENOENT") return fallback;
    throw err;
  }
}

// Gzipped JSONL, written whole: a file exists only once it is complete,
// which makes every step resumable by checking for the file.
export function writeJsonlGz(file, rows) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const body = rows.map((r) => JSON.stringify(r)).join("\n") + (rows.length ? "\n" : "");
  const tmp = `${file}.tmp`;
  fs.writeFileSync(tmp, zlib.gzipSync(body));
  fs.renameSync(tmp, file);
}

export function readJsonlGz(file) {
  const text = zlib.gunzipSync(fs.readFileSync(file)).toString("utf8");
  return text ? text.trimEnd().split("\n").map((l) => JSON.parse(l)) : [];
}

export function* listFiles(dir, suffix) {
  if (!fs.existsSync(dir)) return;
  for (const name of fs.readdirSync(dir).sort()) if (name.endsWith(suffix)) yield path.join(dir, name);
}

const UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36";

// GET JSON with retries and exponential backoff on throttling and server errors.
// Returns null for 4xx responses that mean "nothing here" (400, 404).
export async function getJson(url, { tries = 5, minDelay = 0 } = {}) {
  for (let attempt = 0; ; attempt++) {
    if (minDelay) await sleep(minDelay);
    let res;
    try {
      res = await fetch(url, { headers: { "user-agent": UA, accept: "application/json" } });
    } catch (err) {
      if (attempt + 1 >= tries) throw err;
      await sleep(1000 * 2 ** attempt);
      continue;
    }
    if (res.ok) {
      const text = await res.text();
      try {
        return JSON.parse(text);
      } catch {
        return null;
      }
    }
    if (res.status === 400 || res.status === 404) return null;
    if (attempt + 1 >= tries) throw new Error(`${res.status} for ${url}`);
    const retryAfter = Number(res.headers.get("retry-after"));
    await sleep(retryAfter > 0 ? retryAfter * 1000 : 1500 * 2 ** attempt);
  }
}

// Run fn over items with at most `limit` in flight.
export async function pool(items, limit, fn) {
  let next = 0;
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (next < items.length) {
      const i = next++;
      await fn(items[i], i);
    }
  });
  await Promise.all(workers);
}

export function log(...args) {
  console.log(new Date().toISOString().slice(11, 19), ...args);
}

export function args() {
  const out = {};
  const argv = process.argv.slice(2);
  for (let i = 0; i < argv.length; i++) {
    if (!argv[i].startsWith("--")) continue;
    const key = argv[i].slice(2);
    const val = argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[++i] : true;
    out[key] = val;
  }
  return out;
}
