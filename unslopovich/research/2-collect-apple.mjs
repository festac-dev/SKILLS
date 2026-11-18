// Step 2: App Store reviews from Apple's public customer-reviews feed.
// Output: data/raw/apple/<app id>.jsonl.gz and .meta.json, one pair per app.
// Usage: node 2-collect-apple.mjs [--limit N] [--concurrency N] [--stop-at REVIEWS]

import { APPLE_COUNTRIES, APPLE_SORTS, REQUEST_DELAY_MS } from "./config.mjs";
import { collectPlatform } from "./lib/collect.mjs";
import { getJson, args } from "./lib/util.mjs";

export function parseAppleEntry(e) {
  if (!e?.["im:rating"]) return null;
  return {
    id: `a${e.id.label}`,
    rating: Number(e["im:rating"].label),
    title: e.title?.label ?? "",
    text: e.content?.label ?? "",
    date: e.updated?.label ? new Date(e.updated.label).toISOString() : null,
    version: e["im:version"]?.label ?? null,
    votes: Number(e["im:voteCount"]?.label ?? 0),
  };
}

async function* fetchPass(app, { country, sort }) {
  for (let page = 1; page <= 10; page++) {
    const url = `https://itunes.apple.com/${country}/rss/customerreviews/page=${page}/id=${app.id}/sortby=${sort}/json`;
    const feed = await getJson(url, { minDelay: REQUEST_DELAY_MS });
    const entries = [].concat(feed?.feed?.entry ?? []);
    const reviews = entries.map(parseAppleEntry).filter(Boolean);
    if (!reviews.length) return;
    yield reviews;
    if (reviews.length < 50) return;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  await collectPlatform("apple", { countries: APPLE_COUNTRIES, sorts: APPLE_SORTS, fetchPass, limit: args().limit, concurrency: args().concurrency, stopAt: args()["stop-at"] });
}
