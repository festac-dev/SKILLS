// Step 1: choose the apps. For each shared category and platform, take the US
// top-free chart and draw apps from three rank bands with a fixed seed.
// Output: data/apps.json

import gplay from "google-play-scraper";
import { CATEGORIES, APPS_PER_CATEGORY, RANK_BANDS, CHART_COUNTRY, SEED } from "./config.mjs";
import { dataPath, getJson, rng, shuffle, hash, writeJson, readJson, log, sleep, args } from "./lib/util.mjs";

// chart: "free" or "paid".
async function appleChart(genre, chart = "free", country = CHART_COUNTRY) {
  const list = chart === "paid" ? "toppaidapplications" : "topfreeapplications";
  const url = `https://itunes.apple.com/${country}/rss/${list}/limit=200/genre=${genre}/json`;
  const feed = await getJson(url);
  return (feed?.feed?.entry || []).map((e, i) => ({
    id: e.id.attributes["im:id"],
    name: e["im:name"].label,
    developer: e["im:artist"]?.label ?? null,
    rank: i + 1,
  }));
}

async function playChart(category) {
  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const list = await gplay.list({ collection: gplay.collection.TOP_FREE, category, num: 200, country: CHART_COUNTRY, lang: "en" });
      return list.map((a, i) => ({ id: a.appId, name: a.title, developer: a.developer ?? null, rank: i + 1 }));
    } catch (err) {
      log(`play chart ${category} failed (${err.message}), retrying`);
      await sleep(2000 * 2 ** attempt);
    }
  }
  throw new Error(`play chart ${category} failed`);
}

// Split a quota across rank bands, then draw at random inside each band,
// skipping apps another category already took.
export function drawFromChart(chart, quota, random, taken = () => false) {
  const counts = RANK_BANDS.map((b) => Math.round(quota * b.share));
  counts[0] += quota - counts.reduce((a, b) => a + b, 0);
  const picked = [];
  RANK_BANDS.forEach((band, i) => {
    const pool = chart.filter((a) => a.rank >= band.from && a.rank <= band.to && !taken(a));
    for (const app of shuffle(pool, random).slice(0, counts[i])) picked.push({ ...app, band: band.name });
  });
  return picked;
}

// Add apps to one store without touching the ones already chosen: a second
// draw from the same charts and rank bands, skipping every app already in.
export function bandOf(rank) {
  return rank <= 10 ? "head" : rank <= 50 ? "middle" : rank <= 100 ? "tail" : "deep";
}

// Usage:
//   node 1-apps.mjs --add apple --per-category 18 [--chart paid]
//   node 1-apps.mjs --add play --all                    every chart app not yet in
//   node 1-apps.mjs --add apple --all --chart-country gb  the same, from another storefront's chart
async function extend(platform, perCategory, chart = "free", { all = false, chartCountry = CHART_COUNTRY } = {}) {
  const file = dataPath("apps.json");
  const current = readJson(file);
  const seen = new Set(current.apps.map((a) => `${a.platform}:${a.id}`));
  // Rounds are numbered per store, past any round drawn and later dropped.
  const used = [
    ...current.apps.filter((a) => a.platform === platform).map((a) => a.round || 1),
    ...(current.rounds || []).filter((r) => r.platform === platform).map((r) => r.round),
  ];
  const round = Math.max(1, ...used) + 1;
  let added = 0;
  for (const [category, stores] of Object.entries(CATEGORIES)) {
    const storeCats = stores[platform];
    const quota = Math.round(perCategory / storeCats.length);
    for (const storeCat of storeCats) {
      const list = platform === "apple" ? await appleChart(storeCat, chart, chartCountry) : await playChart(storeCat);
      const random = rng(SEED ^ hash(`${platform}:${storeCat}:round${round}`));
      const picked = all
        ? shuffle(list.filter((a) => !seen.has(`${platform}:${a.id}`)), random).map((a) => ({ ...a, band: bandOf(a.rank) }))
        : drawFromChart(list, quota, random, (a) => seen.has(`${platform}:${a.id}`));
      for (const app of picked) {
        seen.add(`${platform}:${app.id}`);
        current.apps.push({ platform, category, storeCategory: String(storeCat), chartSize: list.length, round, chart, chartCountry, ...app });
      }
      added += picked.length;
      log(`${platform} ${category}/${storeCat}: took ${picked.length} more`);
    }
  }
  current.rounds = [...(current.rounds || []), { round, platform, perCategory: all ? "all" : perCategory, chart, chartCountry, at: new Date().toISOString() }];
  writeJson(file, current);
  log(`added ${added} ${platform} apps in round ${round}`);
}

async function main() {
  const opts = args();
  if (opts.add) return extend(opts.add, Number(opts["per-category"]), opts.chart || "free", { all: !!opts.all, chartCountry: opts["chart-country"] || CHART_COUNTRY });
  const apps = [];
  const seen = new Set();
  for (const [category, stores] of Object.entries(CATEGORIES)) {
    for (const platform of ["apple", "play"]) {
      const storeCats = stores[platform];
      const quota = Math.round(APPS_PER_CATEGORY / storeCats.length);
      for (const storeCat of storeCats) {
        const chart = platform === "apple" ? await appleChart(storeCat) : await playChart(storeCat);
        const random = rng(SEED ^ hash(`${platform}:${storeCat}`));
        const picked = drawFromChart(chart, quota, random, (a) => seen.has(`${platform}:${a.id}`));
        for (const app of picked) {
          seen.add(`${platform}:${app.id}`);
          apps.push({ platform, category, storeCategory: String(storeCat), chartSize: chart.length, ...app });
        }
        const added = picked.length;
        log(`${platform} ${category}/${storeCat}: chart ${chart.length}, took ${added}`);
      }
    }
  }
  writeJson(dataPath("apps.json"), { collectedAt: new Date().toISOString(), chartCountry: CHART_COUNTRY, seed: SEED, apps });
  const by = (p) => apps.filter((a) => a.platform === p).length;
  log(`apps: ${apps.length} (apple ${by("apple")}, play ${by("play")})`);
}

if (import.meta.url === `file://${process.argv[1]}`) await main();
