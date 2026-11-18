// Step 6: check the labels.
// 1. Re-label a random subset at higher effort and measure agreement per theme.
// 2. Write a sheet for a person to label the same subset by hand; once it is
//    filled in, --score compares it with both model runs.
// Usage: node 6-validate.mjs | node 6-validate.mjs --score
// Output: data/validation/*, results/validation.json, results/validation-human.json

import fs from "node:fs";
import { EFFORT, VALIDATION_SIZE, VALIDATION_EFFORT, SEED } from "./config.mjs";
import { THEME_IDS } from "./lib/taxonomy.mjs";
import { runBatches } from "./lib/claude.mjs";
import { dataPath, readJsonlGz, writeJson, rng, shuffle, args, log, RESULTS } from "./lib/util.mjs";

// Cohen's kappa for one binary label over paired observations.
export function kappa(a, b) {
  const n = a.length;
  if (!n) return null;
  let agree = 0;
  let pa = 0;
  let pb = 0;
  for (let i = 0; i < n; i++) {
    if (a[i] === b[i]) agree++;
    if (a[i]) pa++;
    if (b[i]) pb++;
  }
  const po = agree / n;
  const pe = (pa / n) * (pb / n) + (1 - pa / n) * (1 - pb / n);
  return pe === 1 ? 1 : (po - pe) / (1 - pe);
}

export function agreement(pairs) {
  const out = {};
  for (const t of THEME_IDS) {
    const a = pairs.map(([x]) => x.themes.includes(t));
    const b = pairs.map(([, y]) => y.themes.includes(t));
    out[t] = {
      n: pairs.length,
      positiveA: a.filter(Boolean).length,
      positiveB: b.filter(Boolean).length,
      agreement: a.filter((v, i) => v === b[i]).length / pairs.length,
      kappa: kappa(a, b),
    };
  }
  out.complaint = { kappa: kappa(pairs.map(([x]) => x.complaint), pairs.map(([, y]) => y.complaint)) };
  out.primary = { agreement: pairs.filter(([x, y]) => x.primary === y.primary).length / pairs.length };
  return out;
}

const csvCell = (s) => `"${String(s ?? "").replace(/"/g, '""')}"`;

export function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let quoted = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (quoted) {
      if (c === '"' && text[i + 1] === '"') {
        cell += '"';
        i++;
      } else if (c === '"') quoted = false;
      else cell += c;
    } else if (c === '"') quoted = true;
    else if (c === ",") {
      row.push(cell);
      cell = "";
    } else if (c === "\n") {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = "";
    } else if (c !== "\r") cell += c;
  }
  if (cell || row.length) {
    row.push(cell);
    rows.push(row);
  }
  return rows;
}

async function main() {
  const opts = args();
  const sample = readJsonlGz(dataPath("sample.jsonl.gz"));
  const labels = new Map(readJsonlGz(dataPath("labels.jsonl.gz")).map((l) => [l.key, l]));
  const subset = shuffle(sample.filter((s) => labels.has(s.key)), rng(SEED ^ 0xa11ce)).slice(0, VALIDATION_SIZE);
  const sheet = dataPath("validation", "human.csv");

  if (!opts.score) {
    const { labelled } = await runBatches({
      items: subset,
      effort: VALIDATION_EFFORT,
      stateFile: dataPath("validation", "state.json"),
      outFile: dataPath("validation", "labels-high.jsonl.gz"),
    });
    const pairs = subset.filter((s) => labelled.has(s.key)).map((s) => [labels.get(s.key), labelled.get(s.key)]);
    writeJson(`${RESULTS}/validation.json`, { size: pairs.length, compared: `effort ${EFFORT} vs ${VALIDATION_EFFORT}`, themes: agreement(pairs) });
    if (!fs.existsSync(sheet)) {
      const header = ["key", "store", "stars", "title", "text", "complaint (y/n)", "themes (comma separated)"];
      const lines = [header.map(csvCell).join(",")];
      for (const s of subset) lines.push([s.key, s.platform, s.review.rating, s.review.title, s.review.text, "", ""].map(csvCell).join(","));
      fs.writeFileSync(sheet, lines.join("\n") + "\n");
    }
    log(`agreement written to results/validation.json; hand-label ${sheet} and run --score`);
    return;
  }

  const rows = parseCsv(fs.readFileSync(sheet, "utf8")).slice(1).filter((r) => r[5]);
  const human = new Map(
    rows.map((r) => [
      r[0],
      {
        complaint: /^y/i.test(r[5].trim()),
        themes: r[6].split(",").map((t) => t.trim()).filter((t) => THEME_IDS.includes(t)),
      },
    ]),
  );
  const high = new Map(readJsonlGz(dataPath("validation", "labels-high.jsonl.gz")).map((l) => [l.key, l]));
  const keys = [...human.keys()].filter((k) => labels.has(k));
  writeJson(`${RESULTS}/validation-human.json`, {
    humanLabelled: keys.length,
    lowVsHuman: agreement(keys.map((k) => [labels.get(k), human.get(k)])),
    highVsHuman: agreement(keys.filter((k) => high.has(k)).map((k) => [high.get(k), human.get(k)])),
  });
  log(`compared ${keys.length} hand labels; written to results/validation-human.json`);
}

if (import.meta.url === `file://${process.argv[1]}`) await main();
