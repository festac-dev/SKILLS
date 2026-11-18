// Step 3: Google Play reviews through google-play-scraper.
// Output: data/raw/play/<package>.jsonl.gz and .meta.json, one pair per app.
// Usage: node 3-collect-play.mjs [--limit N] [--concurrency N] [--stop-at REVIEWS]

import gplay from "google-play-scraper";
import { PLAY_COUNTRIES, PLAY_SORTS, REQUEST_DELAY_MS } from "./config.mjs";
import { collectPlatform } from "./lib/collect.mjs";
import { sleep, args } from "./lib/util.mjs";

export function parsePlayReview(r) {
  return {
    id: `p${r.id}`,
    rating: Number(r.score),
    title: r.title ?? "",
    text: r.text ?? "",
    date: r.date ? new Date(r.date).toISOString() : null,
    version: r.version ?? null,
    votes: Number(r.thumbsUp ?? 0),
  };
}

async function page(appId, country, sort, token) {
  for (let attempt = 0; ; attempt++) {
    await sleep(REQUEST_DELAY_MS);
    try {
      return await gplay.reviews({
        appId,
        country,
        lang: "en",
        sort: gplay.sort[sort],
        num: 150,
        paginate: true,
        nextPaginationToken: token,
      });
    } catch (err) {
      if (attempt >= 4 || /not found|404/i.test(err.message)) throw err;
      await sleep(1500 * 2 ** attempt);
    }
  }
}

async function* fetchPass(app, { country, sort }) {
  let token;
  for (let i = 0; i < 20; i++) {
    const res = await page(app.id, country, sort, token);
    const reviews = (res.data || []).map(parsePlayReview);
    if (!reviews.length) return;
    yield reviews;
    token = res.nextPaginationToken;
    if (!token) return;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  await collectPlatform("play", { countries: PLAY_COUNTRIES, sorts: PLAY_SORTS, fetchPass, limit: args().limit, concurrency: args().concurrency, stopAt: args()["stop-at"] });
}
