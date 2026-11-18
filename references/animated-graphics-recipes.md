# Animated Graphics Recipes

Vanilla, dependency-free starting points. Adapt to the project's stack and design; they are patterns, not mandated visuals. Every recipe must be paired with a reduced-motion path and performance check.

## 0. Shared helpers
```js
const reduced = matchMedia('(prefers-reduced-motion: reduce)');
const finePointer = matchMedia('(hover: hover) and (pointer: fine)');
const lerp = (a, b, t) => a + (b - a) * t;
const damp = (a, b, k, dt) => lerp(a, b, 1 - Math.exp(-k * dt)); // frame-rate independent
const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
```

## 1. Continuous rotation (SVG or any element)
```css
.spin { animation: spin 24s linear infinite; transform-origin: 50% 50%; transform-box: fill-box; }
@keyframes spin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .spin { animation: none; } }
```
Layer counter-rotations at different speeds for depth (orbits: 20 s, 35 s, 60 s, alternating direction).

## 2. Pointer parallax with moving layers
```html
<div class="stage" id="stage">
  <div class="layer" data-depth="0.02"></div>
  <div class="layer" data-depth="0.05"></div>
  <div class="layer" data-depth="0.10"></div>
</div>
```
```js
const stage = document.getElementById('stage');
const layers = [...stage.querySelectorAll('.layer')];
let tx = 0, ty = 0, x = 0, y = 0, last = performance.now(), running = false, raf;
function onMove(e) {
  const r = stage.getBoundingClientRect();
  tx = ((e.clientX - r.left) / r.width - 0.5) * 2;   // -1..1
  ty = ((e.clientY - r.top) / r.height - 0.5) * 2;
}
function frame(now) {
  const dt = Math.min(0.05, (now - last) / 1000); last = now;
  x = damp(x, tx, 8, dt); y = damp(y, ty, 8, dt);
  for (const el of layers) {
    const d = parseFloat(el.dataset.depth);
    el.style.transform = `translate3d(${x * d * 400}px, ${y * d * 400}px, 0)`;
  }
  raf = requestAnimationFrame(frame);
}
if (!reduced.matches && finePointer.matches) {
  stage.addEventListener('pointermove', onMove, { passive: true });
  stage.addEventListener('pointerleave', () => { tx = ty = 0; });
  new IntersectionObserver(([en]) => {
    if (en.isIntersecting && !running) { running = true; last = performance.now(); raf = requestAnimationFrame(frame); }
    else if (!en.isIntersecting) { running = false; cancelAnimationFrame(raf); }
  }).observe(stage);
}
```

## 3. 3D card tilt with glare
```js
function tilt(card, max = 10) {
  card.addEventListener('pointermove', e => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--rx', ((0.5 - py) * max * 2).toFixed(2) + 'deg');
    card.style.setProperty('--ry', ((px - 0.5) * max * 2).toFixed(2) + 'deg');
    card.style.setProperty('--gx', (px * 100) + '%');
    card.style.setProperty('--gy', (py * 100) + '%');
  });
  card.addEventListener('pointerleave', () => { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); });
}
```
```css
.card { transform: perspective(900px) rotateX(var(--rx,0)) rotateY(var(--ry,0)); transition: transform 180ms cubic-bezier(.22,1,.36,1); }
.card::after { content:""; position:absolute; inset:0; pointer-events:none;
  background: radial-gradient(circle at var(--gx,50%) var(--gy,50%), rgba(255,255,255,.18), transparent 55%); }
```

## 4. Flowing connections along SVG paths
Dashed flow (cheap):
```css
.flow { stroke-dasharray: 6 10; animation: flow 1.2s linear infinite; }
@keyframes flow { to { stroke-dashoffset: -16; } }
@media (prefers-reduced-motion: reduce) { .flow { animation: none; } }
```
Particles travelling along a curve:
```js
const path = document.querySelector('#link');
const len = path.getTotalLength();
const dots = [...document.querySelectorAll('.pulse')];
function step(t) {
  dots.forEach((d, i) => {
    const p = path.getPointAtLength(((t / 4000 + i / dots.length) % 1) * len);
    d.setAttribute('cx', p.x); d.setAttribute('cy', p.y);
  });
  requestAnimationFrame(step);
}
requestAnimationFrame(step);
```
Make the flow encode truth: speed or density = throughput, direction = data direction, color or dash = state (healthy/degraded), and keep a legend.

## 5. Canvas network that reacts to the cursor
```js
const cvs = document.querySelector('canvas'); const ctx = cvs.getContext('2d');
let w, h, dpr, pts = [], mouse = { x: -9999, y: -9999 };
function resize() {
  dpr = Math.min(devicePixelRatio || 1, 2);
  w = cvs.clientWidth; h = cvs.clientHeight;
  cvs.width = w * dpr; cvs.height = h * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  const n = Math.round(clamp(w * h / 14000, 30, 140));          // scale with area, capped
  pts = Array.from({ length: n }, () => ({ x: Math.random() * w, y: Math.random() * h, vx: (Math.random() - .5) * .3, vy: (Math.random() - .5) * .3 }));
}
addEventListener('resize', resize); resize();
cvs.addEventListener('pointermove', e => { const r = cvs.getBoundingClientRect(); mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top; });
cvs.addEventListener('pointerleave', () => { mouse.x = mouse.y = -9999; });
function draw() {
  ctx.clearRect(0, 0, w, h);
  for (const p of pts) {
    const dx = p.x - mouse.x, dy = p.y - mouse.y, d2 = dx * dx + dy * dy;
    if (d2 < 140 * 140) { const f = (1 - Math.sqrt(d2) / 140) * 0.6; p.vx += dx / Math.sqrt(d2 + 1) * f * .05; p.vy += dy / Math.sqrt(d2 + 1) * f * .05; } // repel
    p.x += p.vx; p.y += p.vy; p.vx *= .985; p.vy *= .985;
    if (p.x < 0 || p.x > w) p.vx *= -1; if (p.y < 0 || p.y > h) p.vy *= -1;
  }
  ctx.lineWidth = 1;
  for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) {
    const a = pts[i], b = pts[j], dx = a.x - b.x, dy = a.y - b.y, d = dx * dx + dy * dy;
    if (d < 120 * 120) { ctx.globalAlpha = 1 - Math.sqrt(d) / 120; ctx.strokeStyle = 'currentColor'; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
  }
  ctx.globalAlpha = 1; requestAnimationFrame(draw);
}
```
For many nodes, use a spatial grid instead of O(n²) pair checks.

## 6. Magnetic button
```js
function magnetic(el, strength = 0.3, radius = 90) {
  el.addEventListener('pointermove', e => {
    const r = el.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    el.style.transform = `translate(${(e.clientX - cx) * strength}px, ${(e.clientY - cy) * strength}px)`;
  });
  el.addEventListener('pointerleave', () => { el.style.transform = ''; });
}
```
Keep the click target stable; keyboard focus must not depend on the effect.

## 7. Spotlight / lens reveal
```css
.reveal { --x: 50%; --y: 50%;
  mask-image: radial-gradient(circle 140px at var(--x) var(--y), #000 40%, transparent 100%); }
```
Update `--x/--y` from `pointermove`; make sure hidden content is also reachable without a pointer.

## 8. Scroll-linked progress (CSS, verify support)
```css
@supports (animation-timeline: scroll()) {
  .bar { animation: grow linear both; animation-timeline: scroll(root); }
  @keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
}
```
Provide an IntersectionObserver or static fallback.

## 9. FLIP layout transition
Measure first rect, apply layout change, measure last rect, apply inverse transform, then animate to identity with Web Animations API (`el.animate([{transform:`translate(${dx}px,${dy}px) scale(${sx},${sy})`},{transform:'none'}],{duration:320,easing:'cubic-bezier(.22,1,.36,1)'})`).

## 10. Visibility and fallback wrapper
```js
function startWhenVisible(el, startFn, stopFn) {
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  let visible = false;
  const sync = () => visible && !document.hidden && !preference.matches ? startFn() : stopFn();
  const observer = new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; sync(); });
  observer.observe(el);
  document.addEventListener('visibilitychange', sync);
  preference.addEventListener('change', sync);
  return () => {
    observer.disconnect();
    document.removeEventListener('visibilitychange', sync);
    preference.removeEventListener('change', sync);
    stopFn();
  };
}
```
Render a composed initial frame before attaching the loop. Let the scene respond to its chosen scroll, visibility, pointer or automatic trigger. Follow the [motion specialist](../specialists/motion-3d-and-immersive.md) for input behavior; these recipes do not require a playback toolbar.

## Review checklist
- [ ] Purpose stated for each moving element.
- [ ] Reduced-motion and touch behavior defined.
- [ ] One rAF loop; paused offscreen and when hidden.
- [ ] DPR capped; counts scale with area/device.
- [ ] Contrast preserved over moving backgrounds.
- [ ] Frame time measured on a mid-range device.
