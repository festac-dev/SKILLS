# Modern Web Platform Features (use with support checks)

Check current browser support (caniuse, MDN baseline status) and provide fallbacks via progressive enhancement (`@supports`, feature detection). Prefer platform features over libraries when they meet the need.

## CSS
| Feature | Use for | Notes |
|---|---|---|
| Container queries (`@container`, `container-type`) | Components that adapt to their own space | Widely supported; replace many media queries |
| `:has()` | Parent/sibling state styling (form validity, empty states) | Avoid expensive broad selectors |
| Nesting, `@layer`, `@scope` | Organization and specificity control | Layers make third-party CSS predictable |
| `color-mix()`, `oklch()`, relative colors, `light-dark()` | Token ramps, theming | Define fallbacks for older engines |
| `@property` | Typed custom properties; animate gradients/numbers | Enables smooth gradient and counter animation |
| Subgrid | Aligned nested grids | |
| Logical properties, `dvh/svh/lvh` | RTL and mobile browser UI chrome | Use `svh` for stable heroes |
| `text-wrap: balance / pretty` | Typographic polish | Progressive enhancement |
| `content-visibility: auto` | Skip rendering off-screen sections | Provide `contain-intrinsic-size` |
| Scroll-driven animations (`animation-timeline: scroll()/view()`) | Progress bars, reveals, parallax without JS | Compositor-friendly; check support and provide static fallback |
| View Transitions API (same-document, and cross-document where supported) | Shared-element and page transitions | Respect reduced motion; keep durations short |
| `@starting-style`, `transition-behavior: allow-discrete` | Enter/exit animation for `display` and popover/dialog | |
| Anchor positioning | Tooltips/popovers tied to anchors | Check support; polyfill if needed |
| Popover API, `<dialog>` | Accessible overlays with built-in focus/escape handling | Prefer over custom modals |
| `field-sizing`, `interpolate-size` | Auto-growing inputs; animate to `auto` | Newer; progressive enhancement |
| `accent-color`, `appearance`, `::marker`, `::backdrop` | Native control theming | |
| Forced-colors, `prefers-contrast`, `prefers-reduced-data` | User preference adaptation | |

## JavaScript and platform APIs
- Web Animations API (`element.animate`) for programmatic, compositor-friendly animation with promises and `finished`.
- IntersectionObserver / ResizeObserver / MutationObserver for visibility, size and DOM changes without polling.
- Pointer Events (unified mouse/touch/pen), `setPointerCapture`, `touch-action`; `matchMedia('(hover:hover) and (pointer:fine)')` to gate cursor effects.
- `requestAnimationFrame`, `requestIdleCallback`/`scheduler.postTask`, `AbortController`, `structuredClone`, `Intl` (DateTimeFormat, NumberFormat, RelativeTimeFormat, ListFormat, Segmenter, PluralRules), `URLPattern`, `Temporal` (check status), `Navigation API`.
- Storage: IndexedDB, Cache API, OPFS (Origin Private File System), `navigator.storage.persist()`, Storage Foundation patterns; avoid localStorage for large or sensitive data.
- Networking: `fetch` streaming, `EventSource` (SSE), WebSocket, WebTransport (emerging), WebRTC data channels, Background Sync (limited), Beacon API for analytics.
- Performance: `PerformanceObserver` (LCP, INP, CLS via web-vitals), Long Animation Frames, Speculation Rules (prefetch/prerender), `fetchpriority`, `<link rel=preload/modulepreload>`, `103 Early Hints`.
- Graphics/compute: Canvas 2D, OffscreenCanvas + workers, WebGL2, WebGPU, WebCodecs, WebAssembly (SIMD, threads), Web Audio, MediaStream, Screen Capture.
- Device and UX: Web Share, Clipboard (async), File System Access, Badging, Web Push, Vibration, Wake Lock, Screen Orientation, Device Orientation (permission on iOS), Payment Request, WebAuthn/passkeys, Credential Management, Web Locks.
- Security: CSP with nonces/hashes, Trusted Types, SRI, `SameSite` cookies, CORP/COOP/COEP, `Permissions-Policy`, `Referrer-Policy`, Fetch Metadata headers, `Sanitizer` API (emerging) or a vetted sanitizer such as DOMPurify.

## Animation tool selection
| Need | Choose |
|---|---|
| State transitions, hovers | CSS transitions |
| Sequenced/looping effects | CSS keyframes or WAAPI |
| Scroll-linked effects | CSS scroll-driven animations first; GSAP ScrollTrigger or Motion for complex choreography and broader support |
| Layout/shared-element transitions | View Transitions, FLIP, Motion layout animations |
| Complex timelines, SVG morph, text splitting | GSAP |
| React-centric springs/gestures | Motion (formerly Framer Motion), react-spring |
| Designer-authored vector animation | Lottie/dotLottie (After Effects export), Rive (interactive state machines) |
| 3D scenes | Three.js, React Three Fiber, Babylon.js; Theatre.js for authored camera/timeline |
| Particles and fields | Canvas 2D or WebGL/WebGPU (see `specialists/creative-coding-webgl-and-shaders.md`) |
Keep payload proportional: do not ship a 100 KB library for a hover effect.

## Progressive enhancement pattern
```css
.card { transition: transform .2s; }
@supports (animation-timeline: view()) {
  .reveal { animation: fade-in linear both; animation-timeline: view(); animation-range: entry 0% entry 60%; }
  @keyframes fade-in { from { opacity: 0; translate: 0 24px; } to { opacity: 1; translate: 0 0; } }
}
@media (prefers-reduced-motion: reduce) { .reveal { animation: none; opacity: 1; translate: none; } }
```
Content must be fully usable without the enhancement.

## Failure modes
Relying on a new feature without fallback, animating layout properties, scroll hijacking, ignoring reduced motion, huge polyfills for marginal features, using `100vh` on mobile.
