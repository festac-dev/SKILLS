# Frontend and Client Stack Selection Guide

Preserve the existing stack unless it is the problem. For greenfield, choose by rendering needs, team skills, interactivity level, SEO, offline needs and longevity. Verify current versions and support.

## 1. Rendering strategy first
| Need | Strategy |
|---|---|
| Content, SEO, speed, few interactions | Static generation / islands (Astro, Eleventy, Hugo, Next.js static) |
| Mostly server-rendered pages with sprinkles | Server templates + HTMX/Alpine/Hotwire/Unpoly; progressive enhancement |
| Rich interactive app behind login | SPA (React/Vue/Svelte/Solid) or server-driven UI (LiveView, Hotwire) |
| Mixed: marketing + app + SEO | Meta-framework with server rendering and streaming (Next.js, Remix/React Router, SvelteKit, Nuxt) |
| Offline-first / local-first | PWA + IndexedDB/SQLite-WASM + sync engine (CRDT or server reconciliation) |
| Real-time collaborative | WebSocket/WebRTC + CRDT (Yjs, Automerge) or OT |
| Embeddable widget / design-system primitives | Web Components (Lit) or framework-agnostic core |
| Heavy graphics/3D/video editing | Canvas/WebGL/WebGPU, WASM modules, OffscreenCanvas + workers |

## 2. UI framework profiles
- **React** (+ Next.js, Remix/React Router, Vite): largest ecosystem and talent pool; choose state/data libraries deliberately; watch bundle size and re-render discipline.
- **Vue** (+ Nuxt, Vite): approachable, strong conventions, good for teams mixing designers/developers.
- **Svelte/SvelteKit**: small bundles, compiled reactivity, great for interactive graphics and content apps.
- **SolidJS**: fine-grained reactivity, React-like syntax, very fast; smaller ecosystem.
- **Angular**: opinionated enterprise apps, DI, forms, long-lived large teams.
- **Qwik**: resumability for fast startup on content-heavy sites; evaluate maturity for your needs.
- **HTMX / server-driven**: small teams, CRUD-heavy products, minimal JS budget.
- **Web Components/Lit**: interoperable widgets and design-system primitives across frameworks.

## 3. State and data
Server state (TanStack Query, SWR, RTK Query, Apollo/urql for GraphQL) ≠ client UI state (local state, Zustand, Jotai, Pinia, signals, XState for finite-state flows). URL is state too (filters, tabs, selection). Keep forms on a proven library or native constraint validation; validate on the server regardless.

## 4. Styling
CSS Modules, Tailwind (utility-first), vanilla-extract/Panda (typed, static extraction), plain modern CSS (nesting, `@layer`, container queries, `:has()`, logical properties). Prefer design tokens as CSS custom properties; support theming without rebuilds. Avoid runtime CSS-in-JS in performance-critical paths.

## 5. Build and tooling
Vite (most), Turbopack/webpack (framework-bundled), esbuild/SWC/Rolldown, pnpm/npm/yarn/bun workspaces, Turborepo/Nx for monorepos, Biome/ESLint + Prettier, TypeScript strictness, Playwright for e2e, Vitest/Jest for units, Storybook for component workbench.

## 6. Mobile and desktop clients
| Need | Options |
|---|---|
| Best platform fidelity | Swift/SwiftUI (iOS), Kotlin/Jetpack Compose (Android) |
| One codebase, native-feeling | Flutter, React Native (Expo), Kotlin Multiplatform for shared logic |
| Web team shipping to stores | Capacitor/Ionic, PWA first if store features are not required |
| Desktop | Tauri (small, Rust core), Electron (web parity, heavier), native toolkits, Qt, .NET MAUI/WPF |
| Terminal | Bubble Tea (Go), Ratatui (Rust), Textual (Python), Ink (React-like), see `references/go-bubble-tea-and-tui-framework-guidance.md` |

## 7. Graphics and motion stack
CSS transitions/animations, WAAPI, View Transitions, scroll-driven animations → Canvas 2D → SVG (+ SMIL/CSS/JS) → Three.js / React Three Fiber / Babylon.js → raw WebGL2 / WebGPU shaders → GSAP, Motion (Framer Motion), Lottie/dotLottie, Rive, Theatre.js for authored choreography. Detail in `references/rendering-technology-selection-guide.md`.

## 8. Performance and quality budgets
Core Web Vitals targets at p75 on real devices: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. Ship less JS, split by route, lazy-load below the fold, preload critical fonts/images, use modern image formats (AVIF/WebP), set explicit dimensions, avoid layout shift, cache aggressively with hashed assets. See `references/web-performance-and-delivery.md` and `references/performance-budgets-and-benchmarks.md`.

## 9. Recommendation heuristics
- Marketing/docs/portfolio with showpiece graphics → Astro or Next.js static + islands; canvas/WebGL only for the hero moment.
- SaaS dashboard → React/Vue/Svelte SPA or meta-framework, a typed API client, accessible component primitives (Radix, React Aria, Headless UI, Ark, Melt UI), a charting library matched to data volume.
- Content + commerce → server rendering with strong caching, headless or classic CMS, image pipeline.
- Internal tool → fastest path with solid defaults (server-driven or admin framework); invest in data correctness, not decoration.

## 10. Anti-patterns
SPA for a brochure site; heavy animation library for one hover; global state for everything; client-only auth checks; no loading/error/empty states; ignoring keyboard and screen readers; unpinned dependencies; shipping dev builds.
