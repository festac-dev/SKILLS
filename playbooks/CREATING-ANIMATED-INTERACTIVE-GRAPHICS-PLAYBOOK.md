# Playbook: Creating Animated, Interactive Graphics

Use when the user asks for graphics that move, rotate, flow, layer, or respond to the cursor, or when discovery shows motion materially helps the project.

1. **Confirm the purpose** — fill `INTERACTIVE_GRAPHICS_BRIEF.md`. If the user explicitly requested motion, do it well; do not argue the request away. If motion is only an idea, justify it.
2. **Concept** — derive the graphic from the project subject (see `specialists/distinctive-product-craft-and-differentiation.md`). Sketch what each layer, connection, and moving part means.
3. **Choose technology** — `references/rendering-technology-selection-guide.md`. Start with CSS/SVG, escalate only when needed.
4. **Build static first** — the composition must work still: hierarchy, contrast, labels, legend.
5. **Add layered depth** — separate planes (background, mid, foreground) with distinct speeds; keep text on a stable plane.
6. **Add continuous motion** — rotations, orbits, flows with long, calm cycles; one primary motion.
7. **Add flowing connections** — path-following dashes or particles; encode real direction, rate, or state.
8. **Add input response** — pointer parallax/tilt/attraction using one rAF loop, smoothing, touch and keyboard equivalents; pause when hidden.
9. **Tune** — easing, durations, stagger, spring parameters; check feel at 60 and 120 Hz and under load.
10. **Fallbacks** — reduced motion, no-JS, low power, no WebGL, print.
11. **Measure** — frame time on a mid-range phone and an integrated-GPU laptop; memory over five minutes; bundle weight.
12. **Review** — `MOTION_AND_INTERACTIVE_GRAPHICS_GATE.md` and `DISTINCTIVENESS_AND_CRAFT_GATE.md`.

Starter code: `references/animated-graphics-recipes.md` and `examples/animated-graphics/index.html`.

Replace sample media with final licensed assets and record sources (`references/sample-and-placeholder-asset-policy.md`).
