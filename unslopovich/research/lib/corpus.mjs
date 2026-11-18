// The study corpus: every review collected for every app whose collection
// finished without a failed pass.
//
// Collection stopped at each store's target (CORPUS.stopAt), so the last
// round of each store was collected only in part. Within a round apps are
// collected in rotation across categories (lib/collect.mjs), so a round
// stopped part way still covers every category evenly. Apps never reached
// have no meta file and are not in the corpus.

import fs from "node:fs";
import path from "node:path";
import { DATA, dataPath, readJson, readJsonlGz } from "./util.mjs";

const metaFile = (app) => path.join(DATA, "raw", app.platform, `${app.id}.meta.json`);

// An app is in the corpus when its collection finished with no failed pass.
export function completeMeta(meta) {
  return Boolean(meta) && Array.isArray(meta.passes) && !meta.passes.some((p) => p.error);
}

export function inCorpusApp(app) {
  const f = metaFile(app);
  return fs.existsSync(f) && completeMeta(readJson(f));
}

export function corpusRows(app) {
  if (!inCorpusApp(app)) return [];
  return readJsonlGz(path.join(DATA, "raw", app.platform, `${app.id}.jsonl.gz`));
}

export function corpusApps() {
  return readJson(dataPath("apps.json")).apps.filter(inCorpusApp);
}
