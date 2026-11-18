# Motion Studio Visual System

Extract the logo, brand colors, existing type and actual product artifacts first. Default only when the project has no identity. A dark starting palette is ink `#081118`, surface `#13232E`, text `#F0F5F7`, secondary `#B4C6D1`, accent `#77E3D1`. This is a starting point, not a compulsory template. Use distinct composition and subjects for sibling products.

```css
:root {
  --ink:#081118; --surface:#13232e; --text:#f0f5f7;
  --secondary:#b4c6d1; --accent:#77e3d1; --grid:8px;
  --display: 'Inter', sans-serif; --mono: 'JetBrains Mono', monospace;
  --enter:cubic-bezier(.16,1,.3,1); --move:cubic-bezier(.65,0,.35,1);
}
.stage { color:var(--text); background:var(--ink); padding:calc(12 * var(--grid)); }
.artifact { border:1px solid #45616f; box-shadow:0 24px 64px #0006; }
```

Load licensed local font files before capture; do not rely on a network font arriving in time. Package fonts with outputs only if their licenses permit redistribution. Use one display family at several weights and one mono family; mixing many fonts is not visual hierarchy.

For 1080p, start at 96px safe margins, 88–144px hook type, 56–88px scene titles, 28–36px explanatory text, and 26–32px captions. Code smaller than 24px should be a deliberate close-up target. Use an 8px spacing grid; font sizes may need optical adjustments. Keep CTA commands readable for several seconds while their supporting diagram continues to resolve.

Depth comes from occlusion, light, material and a coherent camera. Use three purposeful planes: context, focal object and annotation. Keep perspective shallow enough to read UI. Grain should remain subordinate to text: a small static texture at 1–3% opacity, optionally shifted on a deterministic clock. Cache grain; do not generate millions of random pixels each frame. Animate a pseudo-element's opacity for glow instead of recomputing a large blur on every web frame.

```ts
// Deterministic parallax: speech cue owns the camera; no wall-clock randomness.
const push = Math.min(1, Math.max(0, (t - cue.start) / 1.2));
const camera = {scale: 1 + push * 0.08, x: -push * 48};
const foregroundX = camera.x * 1.2;
const backgroundX = camera.x * 0.3;
```

## Common failures and fixes

- Black levels change between chunks: normalize each source's actual color range/matrix before concatenating; never relabel full-range pixels as limited range.
- Tiny workspace screenshot: crop to the demonstrated control and reframe the rest in the next shot.
- A whole film repeats title-left/card-right: alternate typographic, artifact, macro, code and diagram compositions with a shared object connecting them.
- Gloss and gradients hide weak composition: remove effects, fix silhouette and hierarchy, then restore restrained depth.
- Imported icon looks like a different brand: preserve the actual logo system instead of inventing a replacement.
