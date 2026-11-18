# Creative Coding, WebGL and Shaders Specialist

## Mission
Deliver high-impact visuals (generative art, living backgrounds, product viewers, data worlds) that stay fast, accessible and purposeful. Reference demo: `examples/animated-graphics/shader-field.html`.

## Choose the tier (lightest that works)
1. **CSS/SVG** (gradients, `@property` animation, filters, masks, clip-path, SMIL/CSS path animation) for most UI motion.
2. **Canvas 2D** for particles, flow fields, charts, hand-drawn effects up to thousands of simple primitives.
3. **WebGL2 via Three.js / OGL / regl / PixiJS / raw GL** for 3D, large instanced scenes, post-processing, shader effects. React Three Fiber/drei or Threlte for component-style scenes.
4. **WebGPU** (compute shaders, large particle simulations, modern pipelines) with a WebGL fallback; check browser support and adapter limits at runtime.
5. **WASM / OffscreenCanvas + workers** for heavy simulation off the main thread.

## Technique menu
Fragment-shader fields (fbm noise, domain warping, SDF shapes, raymarched blobs), flow fields with curl noise, GPU particles (instancing, transform feedback or compute), post-processing (bloom, chromatic aberration used sparingly, depth of field), displacement/vertex shaders, shader transitions between images, reaction-diffusion, boids/flocking, verlet cloth/ropes, spring physics, audio-reactive visuals (Web Audio `AnalyserNode`), MSDF text, 3D model viewers (glTF with Draco/meshopt/KTX2 compression), baked lighting, matcap/IBL environments, camera rigs with damped controls, scroll-linked camera paths.

## Engineering rules
- One render loop, paused when hidden/off-screen; fixed or clamped timestep; frame-rate independent damping (`1 - exp(-k*dt)`).
- Cap devicePixelRatio (1.5–2) and adapt resolution to measured frame time (dynamic resolution).
- Allocate once; reuse buffers/vectors; avoid per-frame garbage; dispose geometries, textures, materials and render targets on teardown.
- Handle `webglcontextlost`/`restored`, resize via ResizeObserver, and feature detection with a static fallback image or CSS gradient.
- Precision: use `highp` where needed (check device support), avoid `sin`-hash artifacts at large coordinates, keep loops constant-bounded for compatibility.
- Color management: choose linear workflow vs sRGB deliberately; check tone mapping.
- Assets: compress textures (KTX2/Basis, AVIF), models (Draco/meshopt), lazy-load and show a poster frame.
- Security/privacy: no cross-origin textures without CORS; don't fingerprint via GPU strings.

## Accessibility and safety
`prefers-reduced-motion` → render one static frame or calm variant; avoid flashing and rapid strobing; maintain text contrast over animated backgrounds (scrim or stable text plane); use the [motion specialist's input guidance](motion-3d-and-immersive.md); do not rely on the visual for essential information; keyboard-operable viewers (orbit via arrows) and text alternatives for data visuals.

## Verification
Frame-time profile on a mid-range phone and a throttled desktop CPU/GPU; memory over a 10-minute session; screenshots in light/dark/reduced-motion; test without WebGL; check battery/thermal impact; Lighthouse for page impact.

## Failure modes
GPU-melting full-screen shaders at 3× DPR, unbounded particle counts, effects that obscure content, no fallback, leaked GPU resources, motion that ignores user preferences.
