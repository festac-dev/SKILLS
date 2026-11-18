# What users complain about: the review study

The skill puts user friction ahead of looks because of what people write in low-rated app reviews. This folder is the study behind that claim: the code that collects the reviews, the method, and the results. Raw review text is not published; anyone can re-run the pipeline.

The first version (105,027 App Store reviews from 299 apps) matched keywords against each app's newest reviews. That had three problems this version fixes:

1. **One week of complaints.** Apple's feed returns at most the 500 newest reviews per app and storefront. For a big app, 500 reviews cover a few days, so the old numbers were mostly about each app's latest release.
2. **Keywords count words, not complaints.** "Crash" in "I crashed my car" counted as a crash, and lag, crashes, and bugs shared one bucket.
3. **Big apps dominated.** Every review counted once, so the busiest apps set the result.

## Method

All parameters live in [config.mjs](config.mjs).

**Apps.** For each of 21 categories, on each store, 22 apps from the US top-free chart, drawn at random from three rank bands: 1 to 10, 11 to 50, and 51 to 100 (Apple's chart feed stops at 100). Seeded, so the same draw comes out every time. About 460 apps per store.

App Store apps return fewer recent reviews than Google Play apps, so more App Store apps were added in further rounds: every app left in each category's top-free 100, then the top-free charts of the UK, India, Canada, and Australia. A round from the top-paid charts was drawn and then dropped before collection, so both stores are free-chart apps only. Google Play's second round took every remaining app down to rank 200, as a fourth band, "deep". `data/apps.json` records each app's round and band, and the results break estimates down by band.

Each store was collected until it reached its target (2 million App Store reviews, 3 million Google Play reviews), then stopped. Within a round, apps are collected in rotation across categories, so a round stopped part way still covers every category evenly.

**Reviews.** English-language storefronts. App Store: twenty, the US, the UK, Canada, Australia, New Zealand, Ireland, India, Singapore, South Africa, the Philippines, Malaysia, Nigeria, Kenya, Ghana, Pakistan, the UAE, Hong Kong, Jamaica, Malta, and Sri Lanka. Google Play: the first ten. Google Play was collected from the first ten for every app; a top-up with the second ten was stopped part way and is not used (see Corpus).

- App Store: Apple's public customer-reviews feed, both newest-first and most-helpful order.
- Google Play: the open-source [google-play-scraper](https://github.com/facundoolano/google-play-scraper), newest-first and most-helpful order, at a polite rate.
- Each app's storefronts are visited in a seeded random order, alternating sort orders, with at most 150 reviews from any one storefront-and-order pass and 2,400 per app. A big app's reviews therefore come from several storefronts and both orders instead of one week in one country.
- Only reviews from the 24 months before collection are kept.
- Review ids, star ratings, titles, texts, dates, app versions, and helpful-vote counts are stored. Reviewer names are not.

**Corpus.** Every review of every app whose collection finished without a failed pass ([lib/corpus.mjs](lib/corpus.mjs)). The final counts are in [results/summary.md](results/summary.md). Results are reported per store.

**Population.** Corpus reviews of 4 stars or fewer with at least 4 words, after removing duplicate texts within an app. The headline numbers are about the low-rated part, 3 stars or fewer. 4-star reviews are reported on their own, to show what still bothers people who mostly like an app.

**Themes.** Fifteen complaint themes with written boundaries, in [lib/taxonomy.mjs](lib/taxonomy.mjs). Crashes, slowness, and bugs are separate themes. A review can state several. Labels describe what the reviewer says, not a guess at the cause.

**Reference sample.** 600 low-rated reviews per store, drawn uniformly at random from the store's whole low-rated population, plus 150 4-star reviews per store drawn the same way from its 4-star reviews. Each was labelled one by one against the theme definitions: English or not, complaint or not, every theme stated. The labelling was done by Claude, in five parallel sessions that each read 300 reviews against the definitions in [lib/taxonomy.mjs](lib/taxonomy.mjs); no keyword matching, and none of them saw the rules or their output. These labels are the reference: they give a direct estimate of each theme's share with a Wilson 95% interval, and they measure the rules below.

**Rules on everything.** A rule classifier ([lib/rules.mjs](lib/rules.mjs)) labels every review in the population. It covers every app, which the reference sample cannot, but it makes mistakes. Its sensitivity, specificity, precision, and Cohen's kappa per theme are measured against the reference labels and published.

**Corrected estimates.** The rule shares are corrected for the rules' measured errors with the Rogan-Gladen estimator. Two numbers per theme and store:

- **Review share:** the share of low-rated reviews that state the theme.
- **App share:** the average over apps of each app's share, so every app counts once and the busiest apps cannot set the result.

95% intervals come from a bootstrap that resamples both the reference sample and the apps, because reviews of the same app are not independent. Where the rules are close to chance for a theme, no correction is reported. The stores are reported separately because their reviews cover different time spans.

**Optional: Claude labels.** With an `ANTHROPIC_API_KEY`, `5-classify.mjs` labels up to 30 reviews per app with Claude through the Message Batches API, and `6-validate.mjs` re-labels 500 of them at higher effort to measure agreement. The published results do not use this path.

## Limits

- **Low-rated reviews are not all users.** People who leave a 1-star review are not a random sample of users, and many unhappy users never write one.
- **Play reaches less far back.** Google Play has no date filter. For busy apps, newest-first reviews cover hours, so Play leans on most-helpful order and its windows are shorter than Apple's. The results report the median span covered per app.
- **Top charts only.** Apps outside the top 100 of their category are not in the study.
- **The stores have different app mixes.** The App Store side has more apps, more of them from ranks 11 to 100. Compare stores theme by theme with that in mind, or compare within a rank band.
- **The reference labels are a model's.** Claude read and labelled each reference review; no person checked them. Each review was labelled once. The labelling sessions reported a few borderline cases they decided differently (for example, an app that "freezes" was sometimes a crash and sometimes slowness, and paying for no ads but still seeing them was sometimes a bug and sometimes an interruption). A person, or a second independent pass, labelling the same 1,500 would measure how far to trust each theme; `6-validate.mjs --score` compares such a sheet.
- **The rules are weak on some themes.** Their agreement with the reference (Cohen's kappa, in [results/summary.md](results/summary.md)) is 0.6 to 0.8 for login, interruptions, lag, and crashes, but 0.2 to 0.4 for bugs, the service behind the app, and missing features. Corrected estimates are not reported where the correction is unstable; the reference shares are the headline numbers.
- **Rules miss context.** Sarcasm, negation, and indirect complaints slip past them. The correction fixes the totals, not individual reviews.
- **What reviews cannot show.** A review says an app feels slow; it does not measure it.

## Running it

```bash
npm install
node 1-apps.mjs              # choose apps            -> data/apps.json
node 2-collect-apple.mjs     # App Store reviews      -> data/raw/apple/
node 3-collect-play.mjs      # Google Play reviews    -> data/raw/play/
node 4-sample.mjs            # population, reference sample, batches to label -> data/gold/
node 5-rules.mjs             # rule labels for every review                   -> data/rules.jsonl.gz
# label data/gold/batch-NN.json into data/gold/labels-NN.jsonl, one JSON object per line:
# {"key": "...", "english": true, "complaint": true, "themes": ["crash"], "primary": "crash"}
node 7-analyze.mjs           # estimates                                      -> results/summary.md
```

Collection resumes where it stopped. The optional Claude path (`5-classify.mjs`, `6-validate.mjs`) needs an `ANTHROPIC_API_KEY`. Charts and reviews change daily, so a re-run gives a fresh sample, not the same reviews; the method and seed stay fixed.

`data/` is not committed. `results/` is.
