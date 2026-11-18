# Generative and Procedural Graphics Specialist

## Mission
Use algorithms to produce graphics that are distinctive, responsive, and meaningful to the product's subject — rather than stock decoration.

## Toolbox
Noise (Perlin, simplex, value, curl), flow fields, particle systems, boids/flocking, force-directed graphs, L-systems, Voronoi/Delaunay, reaction–diffusion, cellular automata, Truchet/tiling patterns, metaballs/SDFs, strange attractors, waveforms and audio-reactive visuals, ray marching, fractals, halftone/dither/pixel effects, procedural terrain, text-as-geometry, data-driven shapes (each mark encodes a real value).

## Where it earns its place
Data-meaningful backgrounds, network/graph visualizations, loading and empty states tied to the product, brand-neutral pattern generation derived from user data, music/audio visualizers, generative covers/avatars, interactive hero pieces whose structure reflects the product's concept, simulations.

## Practices
Seeded randomness for reproducibility and testability; parameters exposed and documented; resolution and count scale with device capability; deterministic fallback image for reduced motion and print; GPU (shader) paths for heavy workloads, CPU/canvas for modest ones; clear separation of simulation step and render step; fixed timestep for physics.

## Failure modes
Generic particle clouds with no meaning, unbounded counts, non-reproducible bugs, CPU-bound loops on mobile, contrast loss over text.

## Deliverables
Concept note linking the algorithm to the project's subject, parameter table, performance budget, static fallback, seed/config for reproduction.
