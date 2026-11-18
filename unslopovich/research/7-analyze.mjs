// Step 7: turn labels into estimates with uncertainty.
//
// Three sources, each reported for what it is:
//   1. Reference labels on a uniform random sample of each store's population
//      (data/gold). They give a direct estimate of each theme's share of
//      low-rated reviews, with a Wilson 95% interval.
//   2. Rule labels on the whole population (data/rules.jsonl.gz). They cover
//      every app, so they can show app shares and breakdowns, but they are
//      biased by the rules' errors.
//   3. The rule estimates corrected for those errors (Rogan-Gladen), using the
//      rules' sensitivity and specificity measured against the reference.
//      Intervals come from a bootstrap that resamples both the reference
//      sample and the apps.
// If Claude labels exist (optional path, data/labels.jsonl.gz), they are
// summarised too.
// Output: results/summary.json, results/summary.md

import path from "node:path";
import fs from "node:fs";
import { SEED, LOW_STARS, MIN_WORDS, WINDOW_MONTHS, GOLD_PER_PLATFORM, GOLD_FOUR_STAR_PER_PLATFORM } from "./config.mjs";
import { THEME_IDS, DESIGN_THEMES } from "./lib/taxonomy.mjs";
import { DATA, RESULTS, dataPath, readJson, readJsonlGz, listFiles, writeJson, rng, log } from "./lib/util.mjs";
import { corpusApps } from "./lib/corpus.mjs";

const B = 1000;
const MIN_APP_REVIEWS = 10;
const PLATFORMS = ["apple", "play"];
const STORE = { apple: "App Store", play: "Google Play" };

// Derived groups reported next to the single themes.
export const GROUPS = {
  stability: (themes) => themes.some((t) => ["crash", "performance", "bug"].includes(t)),
  design_addressable: (themes) => themes.some((t) => DESIGN_THEMES.includes(t)),
};
export const KEYS = [...THEME_IDS, ...Object.keys(GROUPS)];

export function has(themes, key) {
  return GROUPS[key] ? GROUPS[key](themes) : themes.includes(key);
}

export function wilson(k, n, z = 1.96) {
  if (!n) return [NaN, NaN];
  const p = k / n;
  const d = 1 + (z * z) / n;
  const c = p + (z * z) / (2 * n);
  const m = z * Math.sqrt((p * (1 - p)) / n + (z * z) / (4 * n * n));
  return [(c - m) / d, (c + m) / d];
}

// Rule accuracy against reference labels, for one key.
export function accuracy(pairs, key) {
  let tp = 0, fp = 0, fn = 0, tn = 0;
  for (const [rule, ref] of pairs) {
    const a = has(rule, key);
    const b = has(ref, key);
    if (a && b) tp++;
    else if (a) fp++;
    else if (b) fn++;
    else tn++;
  }
  const n = tp + fp + fn + tn;
  const po = (tp + tn) / n;
  const pe = ((tp + fp) / n) * ((tp + fn) / n) + ((fn + tn) / n) * ((fp + tn) / n);
  return {
    positives: tp + fn,
    sensitivity: tp + fn ? tp / (tp + fn) : NaN,
    specificity: fp + tn ? tn / (fp + tn) : NaN,
    precision: tp + fp ? tp / (tp + fp) : NaN,
    kappa: pe === 1 ? NaN : (po - pe) / (1 - pe),
  };
}

// Rogan-Gladen: the true share given an observed share and the classifier's
// sensitivity and specificity. Undefined when the classifier is near chance.
export function correct(observed, se, sp) {
  const j = se + sp - 1;
  if (!(j > 0.2)) return NaN;
  return Math.min(1, Math.max(0, (observed + sp - 1) / j));
}

// Per-app counts of rule positives: [{ n, k: {key: count} }]
function appCounts(rows) {
  const byApp = new Map();
  for (const r of rows) {
    const id = `${r.platform}:${r.app}`;
    if (!byApp.has(id)) byApp.set(id, { platform: r.platform, category: r.category, band: r.band, n: 0, k: Object.fromEntries(KEYS.map((x) => [x, 0])) });
    const a = byApp.get(id);
    a.n++;
    for (const key of KEYS) if (has(r.themes, key)) a.k[key]++;
  }
  return [...byApp.values()];
}

export function reviewShare(apps, key) {
  let k = 0, n = 0;
  for (const a of apps) {
    k += a.k[key];
    n += a.n;
  }
  return n ? k / n : NaN;
}

export function appShare(apps, key) {
  const eligible = apps.filter((a) => a.n >= MIN_APP_REVIEWS);
  return eligible.length ? eligible.reduce((s, a) => s + a.k[key] / a.n, 0) / eligible.length : NaN;
}

// A 95% interval from bootstrap values. NaN (a resample where the correction
// is undefined) breaks numeric sorting, so only finite values are sorted, and
// no interval is given when more than a tenth of the resamples are undefined.
export function interval(values) {
  const xs = values.filter(Number.isFinite).sort((a, b) => a - b);
  if (xs.length < 0.9 * values.length) return [NaN, NaN];
  const at = (q) => xs[Math.min(xs.length - 1, Math.max(0, Math.round(q * (xs.length - 1))))];
  return [at(0.025), at(0.975)];
}

function resample(items, random) {
  return Array.from({ length: items.length }, () => items[Math.floor(random() * items.length)]);
}

function corpusStats() {
  const pop = readJson(dataPath("population.json"));
  const apps = corpusApps();
  const out = { totals: pop.totals, platforms: {} };
  for (const platform of PLATFORMS) {
    const mine = apps.filter((a) => a.platform === platform);
    const metas = mine.map((a) => readJson(path.join(DATA, "raw", platform, `${a.id}.meta.json`)));
    const spans = metas.filter((m) => m.oldest && m.newest).map((m) => (new Date(m.newest) - new Date(m.oldest)) / 864e5).sort((a, b) => a - b);
    const per = pop.perApp.filter((a) => a.platform === platform);
    out.platforms[platform] = {
      apps: mine.length,
      appsWithReviews: per.filter((a) => a.corpus > 0).length,
      corpus: per.reduce((s, a) => s + a.corpus, 0),
      lowRated: per.reduce((s, a) => s + a.lowRated, 0),
      fourStar: per.reduce((s, a) => s + (a.fourStar || 0), 0),
      fourStarPopulation: per.reduce((s, a) => s + (a.fourStarPopulation || 0), 0),
      population: per.reduce((s, a) => s + a.population, 0),
      countries: [...new Set(metas.flatMap((m) => m.passes.filter((p) => p.added).map((p) => p.country)))].length,
      medianDaysCovered: spans.length ? Math.round(spans[Math.floor(spans.length / 2)]) : null,
    };
  }
  return out;
}

function readGold() {
  const sample = new Map(readJsonlGz(dataPath("gold", "sample.jsonl.gz")).map((g) => [g.key, g]));
  const labels = new Map();
  for (const file of listFiles(path.join(DATA, "gold"), ".jsonl")) {
    for (const line of fs.readFileSync(file, "utf8").split("\n")) {
      if (!line.trim()) continue;
      const l = JSON.parse(line);
      if (sample.has(l.key)) labels.set(l.key, { ...l, themes: (l.themes || []).filter((t) => THEME_IDS.includes(t)) });
    }
  }
  return { sample, labels };
}

async function main() {
  const random = rng(SEED ^ 0xb007);
  const allRules = readJsonlGz(dataPath("rules.jsonl.gz")).filter((r) => r.english);
  const rules = allRules.filter((r) => r.stars <= LOW_STARS);
  const ruleById = new Map(rules.map((r) => [r.id, r]));
  const { sample: goldSample, labels: allGoldLabels } = readGold();
  // The low-rated reference sample drives the headline estimates; the 4-star
  // one is reported on its own below.
  const isFour = (key) => goldSample.get(key).set === "four";
  const goldLabels = new Map([...allGoldLabels].filter(([k]) => !isFour(k)));
  const fourLabels = [...allGoldLabels].filter(([k]) => isFour(k)).map(([, l]) => l);

  const result = {
    generatedAt: new Date().toISOString(),
    method: { maxStars: LOW_STARS, fourStarReferencePerStore: GOLD_FOUR_STAR_PER_PLATFORM, minWords: MIN_WORDS, windowMonths: WINDOW_MONTHS, referencePerStore: GOLD_PER_PLATFORM, bootstrap: B, minAppReviews: MIN_APP_REVIEWS },
    corpus: corpusStats(),
    platforms: {},
    byCategory: {},
    byBand: {},
    byStars: {},
    fourStar: {},
  };

  const allApps = appCounts(rules);
  const accuracyBy = {};
  for (const platform of PLATFORMS) {
    // Reference reviews in English, with the rule label of the same review.
    const ref = [...goldLabels.values()].filter((l) => goldSample.get(l.key).platform === platform);
    const refEnglish = ref.filter((l) => l.english);
    const pairs = refEnglish.map((l) => [ruleById.get(goldSample.get(l.key).review.id)?.themes, l.themes]).filter(([a]) => a);
    const apps = allApps.filter((a) => a.platform === platform);
    const p = { reference: { labelled: ref.length, english: refEnglish.length, complaintShare: refEnglish.filter((l) => l.complaint).length / refEnglish.length }, rules: { apps: apps.length, reviews: apps.reduce((s, a) => s + a.n, 0) }, estimates: {} };
    accuracyBy[platform] = {};

    // Bootstrap draws shared by every key: reference resamples and app resamples.
    const refDraws = Array.from({ length: B }, () => resample(pairs, random));
    const appDraws = Array.from({ length: B }, () => resample(apps, random));

    for (const key of KEYS) {
      const k = refEnglish.filter((l) => has(l.themes, key)).length;
      const acc = pairs.length ? accuracy(pairs, key) : null;
      accuracyBy[platform][key] = acc;
      const est = {
        reference: { share: refEnglish.length ? k / refEnglish.length : NaN, ci: wilson(k, refEnglish.length), positives: k },
        rules: { review: reviewShare(apps, key), app: appShare(apps, key) },
        accuracy: acc,
      };
      if (acc) {
        const boot = { review: [], app: [] };
        for (let i = 0; i < B; i++) {
          const a = accuracy(refDraws[i], key);
          boot.review.push(correct(reviewShare(appDraws[i], key), a.sensitivity, a.specificity));
          boot.app.push(correct(appShare(appDraws[i], key), a.sensitivity, a.specificity));
        }
        const reviewCI = interval(boot.review);
        const appCI = interval(boot.app);
        // A correction without a stable interval is not reported.
        est.corrected = {
          review: Number.isFinite(reviewCI[0]) ? correct(est.rules.review, acc.sensitivity, acc.specificity) : NaN,
          reviewCI,
          app: Number.isFinite(appCI[0]) ? correct(est.rules.app, acc.sensitivity, acc.specificity) : NaN,
          appCI,
        };
      }
      p.estimates[key] = est;
    }
    result.platforms[platform] = p;
  }

  // Breakdowns: corrected app shares, each app corrected with its own store's accuracy.
  const correctedApp = (apps, key) => {
    const eligible = apps.filter((a) => a.n >= MIN_APP_REVIEWS);
    const values = eligible.map((a) => {
      const acc = accuracyBy[a.platform][key];
      return acc ? correct(a.k[key] / a.n, acc.sensitivity, acc.specificity) : NaN;
    }).filter(Number.isFinite);
    return values.length ? values.reduce((s, v) => s + v, 0) / values.length : NaN;
  };
  for (const [field, target] of [["category", result.byCategory], ["band", result.byBand]]) {
    for (const v of [...new Set(allApps.map((a) => a[field]))].sort()) {
      const subset = allApps.filter((a) => a[field] === v);
      target[v] = { apps: subset.filter((a) => a.n >= MIN_APP_REVIEWS).length };
      for (const key of KEYS) target[v][key] = correctedApp(subset, key);
    }
  }
  for (const stars of [1, 2, 3, 4]) {
    const subset = appCounts(allRules.filter((r) => r.stars === stars));
    result.byStars[stars] = { reviews: subset.reduce((s, a) => s + a.n, 0) };
    for (const key of KEYS) result.byStars[stars][key] = reviewShare(subset, key);
  }

  // 4 stars next to 3 stars or fewer, both from reference labels.
  for (const platform of PLATFORMS) {
    const four = fourLabels.filter((l) => l.english && goldSample.get(l.key).platform === platform);
    const low = [...goldLabels.values()].filter((l) => l.english && goldSample.get(l.key).platform === platform);
    const share = (ls, key) => {
      const k = ls.filter((l) => has(l.themes, key)).length;
      return { share: ls.length ? k / ls.length : NaN, ci: wilson(k, ls.length), positives: k };
    };
    result.fourStar[platform] = {
      labelled: fourLabels.filter((l) => goldSample.get(l.key).platform === platform).length,
      english: four.length,
      complaintShare: four.length ? four.filter((l) => l.complaint).length / four.length : NaN,
      lowComplaintShare: low.length ? low.filter((l) => l.complaint).length / low.length : NaN,
      estimates: Object.fromEntries(KEYS.map((key) => [key, { four: share(four, key), low: share(low, key) }])),
    };
  }

  fs.mkdirSync(RESULTS, { recursive: true });
  writeJson(path.join(RESULTS, "summary.json"), result);
  fs.writeFileSync(path.join(RESULTS, "summary.md"), markdown(result));
  log(`wrote results/summary.json and results/summary.md (${allRules.length} English reviews by rules, ${allGoldLabels.size} reference labels)`);
}

const pct = (x) => (Number.isFinite(x) ? `${(100 * x).toFixed(1)}%` : "n/a");
const range = ([lo, hi]) => (Number.isFinite(lo) ? `${pct(lo)} to ${pct(hi)}` : "n/a");
const num = (x) => (x == null ? "" : x.toLocaleString("en-US"));
const dec = (x) => (Number.isFinite(x) ? x.toFixed(2) : "n/a");

function markdown(r) {
  const c = r.corpus;
  const L = [];
  L.push("# Results", "", `Generated ${r.generatedAt.slice(0, 10)}. How these were made: [../README.md](../README.md).`, "");
  L.push("## Corpus", "", "| | App Store | Google Play |", "|---|---|---|");
  const row = (label, f) => L.push(`| ${label} | ${f(c.platforms.apple)} | ${f(c.platforms.play)} |`);
  row("Apps", (p) => num(p.apps));
  row("Apps with reviews in the window", (p) => num(p.appsWithReviews));
  row("Storefronts", (p) => num(p.countries));
  row("Reviews in the corpus", (p) => num(p.corpus));
  row(`Rated ${r.method.maxStars} stars or lower`, (p) => num(p.lowRated));
  row(`Of those, ${r.method.minWords}+ words and not duplicated`, (p) => num(p.population));
  row("Rated 4 stars", (p) => num(p.fourStar));
  row("Of those, 4+ words and not duplicated", (p) => num(p.fourStarPopulation));
  row("Median days covered per app", (p) => num(p.medianDaysCovered));
  L.push("", `Total: ${num(c.totals.corpus)} reviews.`, "");

  for (const platform of PLATFORMS) {
    const p = r.platforms[platform];
    L.push(`## ${STORE[platform]}`, "");
    L.push(`Reference sample: ${p.reference.labelled} reviews labelled one by one, ${p.reference.english} in English, ${pct(p.reference.complaintShare)} of them complaints. Rules: ${num(p.rules.reviews)} English reviews from ${p.rules.apps} apps.`, "");
    L.push("| Theme | Reference share | 95% interval | Corrected review share | 95% interval | Corrected app share | 95% interval | Rule kappa |", "|---|---|---|---|---|---|---|---|");
    const keys = KEYS.slice().sort((a, b) => (p.estimates[b].reference.share || 0) - (p.estimates[a].reference.share || 0));
    for (const k of keys) {
      const e = p.estimates[k];
      const co = e.corrected || {};
      L.push(`| ${k} | ${pct(e.reference.share)} | ${range(e.reference.ci)} | ${pct(co.review)} | ${co.reviewCI ? range(co.reviewCI) : "n/a"} | ${pct(co.app)} | ${co.appCI ? range(co.appCI) : "n/a"} | ${dec(e.accuracy?.kappa)} |`);
    }
    L.push("");
  }

  L.push("## How good the rules are", "", "Measured against the reference labels. Sensitivity: share of true cases the rules catch. Precision: share of rule hits that are true. Corrections are skipped where the rules are near chance.", "");
  L.push("| Theme | Store | True cases | Sensitivity | Specificity | Precision | Kappa |", "|---|---|---|---|---|---|---|");
  for (const k of KEYS) for (const platform of PLATFORMS) {
    const a = r.platforms[platform].estimates[k].accuracy;
    if (a) L.push(`| ${k} | ${STORE[platform]} | ${a.positives} | ${pct(a.sensitivity)} | ${pct(a.specificity)} | ${pct(a.precision)} | ${dec(a.kappa)} |`);
  }
  L.push("");

  const table = (title, obj, first) => {
    L.push(`## ${title}`, "", `| ${first} | Apps or reviews | ${KEYS.join(" | ")} |`, `|${"---|".repeat(KEYS.length + 2)}`);
    for (const [v, e] of Object.entries(obj)) L.push(`| ${v} | ${num(e.apps ?? e.reviews)} | ${KEYS.map((k) => pct(e[k])).join(" | ")} |`);
    L.push("");
  };
  table("By category (corrected app share, both stores)", r.byCategory, "Category");
  table("By chart rank band (corrected app share, both stores)", r.byBand, "Band");
  table("By star rating (rule review share, uncorrected)", r.byStars, "Stars");

  L.push("## 4 stars next to 3 stars or fewer", "", "Reference labels only. Share of English reviews in each sample that state the theme. The 4-star share counts every 4-star review, with or without a complaint.", "");
  for (const platform of PLATFORMS) {
    const f = r.fourStar[platform];
    if (!f) continue;
    L.push(`### ${STORE[platform]}`, "", `4-star sample: ${f.labelled} reviews, ${f.english} in English, ${pct(f.complaintShare)} of them complaints (3 stars or fewer: ${pct(f.lowComplaintShare)}).`, "");
    L.push("| Theme | 4 stars | 95% interval | 3 stars or fewer | 95% interval |", "|---|---|---|---|---|");
    const keys = KEYS.slice().sort((a, b) => (f.estimates[b].four.share || 0) - (f.estimates[a].four.share || 0));
    for (const k of keys) {
      const e = f.estimates[k];
      L.push(`| ${k} | ${pct(e.four.share)} | ${range(e.four.ci)} | ${pct(e.low.share)} | ${range(e.low.ci)} |`);
    }
    L.push("");
  }
  return L.join("\n") + "\n";
}

if (import.meta.url === `file://${process.argv[1]}`) await main();
