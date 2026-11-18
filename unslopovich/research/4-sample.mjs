// Step 4: define the population and draw the classification sample.
// Population: collected reviews with MAX_STARS stars or fewer and at least
// MIN_WORDS words, after removing duplicate texts within an app.
// Sample: up to SAMPLE_PER_APP reviews per app, drawn at random. Each sampled
// review carries a weight (the app's population over its sample size) so
// estimates can be made per review as well as per app.
// Reference sample: GOLD_PER_PLATFORM reviews per store, drawn uniformly from
// the store's low-rated population (LOW_STARS or fewer), and
// GOLD_FOUR_STAR_PER_PLATFORM drawn uniformly from its 4-star population, for
// labelling one by one. It measures the rule
// classifier's accuracy and gives a direct estimate of each theme's share.
// Output: data/sample.jsonl.gz, data/population.json, data/gold/sample.jsonl.gz,
//         data/gold/batch-NN.json (what a labeller reads)

import { MAX_STARS, LOW_STARS, MIN_WORDS, SAMPLE_PER_APP, SEED, GOLD_PER_PLATFORM, GOLD_FOUR_STAR_PER_PLATFORM, GOLD_BATCH } from "./config.mjs";
import { dataPath, writeJsonlGz, writeJson, rng, shuffle, hash, log } from "./lib/util.mjs";
import { corpusApps, corpusRows } from "./lib/corpus.mjs";

export const words = (s) => (s.match(/[\p{L}\p{N}']+/gu) || []).length;
export const normalize = (s) => s.toLowerCase().replace(/[^\p{L}\p{N}]+/gu, " ").trim();

export function population(rows) {
  const seen = new Set();
  const out = [];
  for (const r of rows) {
    if (!(r.rating >= 1 && r.rating <= MAX_STARS)) continue;
    if (words(r.text) < MIN_WORDS) continue;
    const key = normalize(`${r.title} ${r.text}`);
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(r);
  }
  return out;
}

async function main() {
  const sample = [];
  const perApp = [];
  const totals = { corpus: 0, lowRated: 0, fourStar: 0, population: 0 };
  const everyone = { apple: { low: [], four: [] }, play: { low: [], four: [] } };
  for (const info of corpusApps()) {
    const platform = info.platform;
    const appId = info.id;
    const rows = corpusRows(info);
    if (!rows.length) continue;
    const pop = population(rows);
    for (const r of pop) everyone[platform][r.rating <= LOW_STARS ? "low" : "four"].push({ r, appId, info });
    const take = shuffle(pop.filter((r) => r.rating <= LOW_STARS), rng(SEED ^ hash(`sample:${platform}:${appId}`))).slice(0, SAMPLE_PER_APP);
    const weight = take.length ? pop.filter((r) => r.rating <= LOW_STARS).length / take.length : 0;
    for (const r of take) {
      sample.push({
        key: `s${sample.length}`,
        review: { id: r.id, platform, rating: r.rating, title: r.title, text: r.text, date: r.date, country: r.country, sort: r.sort },
        app: appId,
        platform,
        category: info.category,
        band: info.band,
        weight,
      });
    }
    const low = rows.filter((r) => r.rating <= LOW_STARS).length;
    const four = rows.filter((r) => r.rating === 4).length;
    const lowPop = pop.filter((r) => r.rating <= LOW_STARS).length;
    totals.corpus += rows.length;
    totals.lowRated += low;
    totals.fourStar += four;
    totals.population += lowPop;
    perApp.push({ platform, app: appId, category: info.category, band: info.band, corpus: rows.length, lowRated: low, fourStar: four, population: lowPop, fourStarPopulation: pop.length - lowPop, sampled: take.length });
  }
  writeJsonlGz(dataPath("sample.jsonl.gz"), sample);

  const gold = [];
  const draws = [
    ["low", "g", "gold", GOLD_PER_PLATFORM],
    ["four", "f", "gold4", GOLD_FOUR_STAR_PER_PLATFORM],
  ];
  for (const [group, prefix, seedName, size] of draws) for (const platform of ["apple", "play"]) {
    const drawn = shuffle(everyone[platform][group], rng(SEED ^ hash(`${seedName}:${platform}`))).slice(0, size);
    for (const { r, appId, info } of drawn) {
      gold.push({
        key: `${prefix}${platform[0]}${gold.length}`,
        set: group,
        review: { id: r.id, platform, rating: r.rating, title: r.title, text: r.text, date: r.date, country: r.country, sort: r.sort },
        app: appId,
        platform,
        category: info.category,
        band: info.band,
      });
    }
  }
  // Interleave stores and star groups so every labelling batch holds both.
  const order = shuffle(gold, rng(SEED ^ hash("gold:order")));
  writeJsonlGz(dataPath("gold", "sample.jsonl.gz"), order);
  for (let i = 0; i < order.length; i += GOLD_BATCH) {
    const batch = order.slice(i, i + GOLD_BATCH).map((g) => ({ key: g.key, store: g.platform === "apple" ? "App Store" : "Google Play", stars: g.review.rating, title: g.review.title, text: g.review.text }));
    writeJson(dataPath("gold", `batch-${String(i / GOLD_BATCH).padStart(2, "0")}.json`), batch);
  }
  writeJson(dataPath("population.json"), { totals, sampled: sample.length, perApp });
  log(`corpus ${totals.corpus}, low-rated ${totals.lowRated}, 4-star ${totals.fourStar}, low-rated population ${totals.population}, sample ${sample.length}, reference ${gold.length}`);
}

if (import.meta.url === `file://${process.argv[1]}`) await main();
