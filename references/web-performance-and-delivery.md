# Web Performance and Delivery Reference

- Measure with field data (CrUX/RUM) and lab tools; track Core Web Vitals (LCP, INP, CLS) and the project's own journeys.
- Reduce JavaScript: split by route, lazy-load heavy libraries (3D, charts, editors), tree-shake, avoid unneeded polyfills, audit dependencies.
- Images: modern formats (AVIF/WebP) with fallbacks, responsive `srcset/sizes`, correct dimensions, lazy-loading below the fold, priority hints for the LCP image.
- Fonts: subset, `font-display`, preload critical files, limit families/weights, consider variable fonts.
- CSS: critical CSS where it helps, avoid huge frameworks without purge, containment (`contain`, `content-visibility`) for heavy sections.
- Network: HTTP/2/3, compression (Brotli/gzip), CDN, caching headers with immutable hashed assets, preconnect/prefetch judiciously, service workers only with a cache strategy.
- Rendering: SSR/SSG/ISR/streaming chosen by content freshness; hydration cost awareness; avoid layout shift by reserving space.
- Runtime: avoid long main-thread tasks, use web workers/OffscreenCanvas for heavy computation, virtualize long lists, debounce expensive handlers.
- Animation: compositor properties, single rAF loop, pause offscreen, adaptive quality.
- Third parties: audit tags, load async/defer, consent-gate, remove unused.
- Budgets in CI: fail builds that exceed agreed bundle and Lighthouse-style thresholds, with human review for exceptions.
