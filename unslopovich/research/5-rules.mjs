// Step 5: label every review in the population with the rule classifier.
// Output: data/rules.jsonl.gz (one row per review: store, app, category,
// band, stars, English or not, themes). No text is copied.

import { population } from "./4-sample.mjs";
import { classifyByRules } from "./lib/rules.mjs";
import { dataPath, writeJsonlGz, log } from "./lib/util.mjs";
import { corpusApps, corpusRows } from "./lib/corpus.mjs";

async function main() {
  const out = [];
  for (const info of corpusApps()) {
    for (const r of population(corpusRows(info))) {
      const label = classifyByRules(r);
      out.push({ id: r.id, platform: info.platform, app: info.id, category: info.category, band: info.band, stars: r.rating, english: label.english, themes: label.themes });
    }
  }
  writeJsonlGz(dataPath("rules.jsonl.gz"), out);
  log(`labelled ${out.length} reviews by rules (${out.filter((r) => r.english).length} English)`);
}

if (import.meta.url === `file://${process.argv[1]}`) await main();
