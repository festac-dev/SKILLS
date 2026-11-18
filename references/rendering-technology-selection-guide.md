# Rendering Technology Selection Guide

Choose the lightest technology that delivers the required effect. Re-verify browser and device support for the project's actual audience.

| Need | Good first choice | Step up when | Watch out for |
|---|---|---|---|
| Hover, state, simple transitions | CSS transitions/animations | Sequencing or physics needed → Web Animations API / JS library | Animating layout properties causes jank |
| Rotating/moving icons, logos, diagrams | Inline SVG + CSS transform | Many elements or interaction → Canvas | `transform-origin` and `transform-box: fill-box` for SVG rotation |
| Flowing connections along paths | SVG path + `stroke-dasharray/offset` or JS point-along-path | Hundreds of moving particles → Canvas 2D | Path length varies; use `getTotalLength()` |
| Pointer-driven parallax/tilt | CSS variables set from one rAF loop | Complex scenes → Canvas/WebGL | Avoid per-event style writes |
| Particle fields, network graphs | Canvas 2D | 10k+ elements, shaders → WebGL/WebGPU | DPR scaling, offscreen pausing |
| Data visualization | SVG (D3/Observable Plot) | Large datasets → Canvas/WebGL | Accessibility alternatives and table fallback |
| 3D scenes, product viewers | Three.js / Babylon / `<model-viewer>` | Custom effects → shaders; modern GPU features → WebGPU | Asset weight, context loss, mobile GPUs |
| Authored vector animation | Lottie/dotLottie, Rive | Interactive state machines → Rive | File size and runtime cost; static fallback |
| Image/video sequences | `<video>` with poster, or compressed sprite/WebP sequences | Scroll-scrub → canvas frames | Memory and bandwidth |
| Text effects | CSS + splitting text into spans | Per-glyph shaders | Screen-reader text must stay intact |
| Page/route transitions | View Transitions API (verify support) / FLIP | Complex choreography → timeline library | Focus and scroll restoration |
| Physics | Spring functions, Matter.js/Rapier | Heavy simulation → worker/WASM | Fixed timestep, determinism |
| Audio-reactive | Web Audio AnalyserNode | Advanced DSP → AudioWorklet | Autoplay policies, user gesture required |
| Native/desktop | Platform animation systems, Skia/Flutter/Metal/Vulkan | Cross-platform engines | Match platform conventions |
| Terminal | ANSI/TUI frameworks | — | Reduced color support, slow terminals |

## Selection questions
1. Does the effect improve comprehension, feedback, or brand-specific expression?
2. What is the smallest dependency that achieves it?
3. What happens on a 5-year-old phone, with reduced motion, with JavaScript slow to load, or in print?
4. Can the static state carry the same information?
5. Who maintains this code in a year?

## Weight guidance (order-of-magnitude, verify per project)
CSS/SVG effects: near-zero dependency cost. Canvas 2D: small code, no dependency. Three.js-class engines: hundreds of KB plus assets—lazy-load. WebGPU/WASM physics: only for workloads that justify them.

## Technique notes
Rotation: CSS `rotate3d` with `perspective`, drag-with-inertia in JS, automatic idle rotation that yields to direct interaction. Parallax: layers move at ratios of scroll or pointer movement with clamped range. Flow: dashed-stroke offset, `getPointAtLength` particles, node pulses, force simulations that settle. Cursor: pointer position as CSS variables, lerp-smoothed follow in one loop. Delivery: compress assets, lazy-load heavy scenes, poster fallbacks, quality tiers by device capability. Budget and accessibility details: `references/motion-accessibility-and-safety.md`.
