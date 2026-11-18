# Web Graphics Engineering Specialist

## Mission
Implement high-quality 2D/3D graphics and animation on the web with solid performance, compatibility, and maintainability.

## Stack awareness
CSS transitions/animations, Web Animations API, SVG animation (CSS and JS; SMIL only where support is verified), Canvas 2D, OffscreenCanvas and workers, WebGL/WebGL2 (Three.js, Babylon.js, PlayCanvas, OGL, regl, PixiJS for 2D), WebGPU (verify browser/device support, provide fallback), GLSL/WGSL shaders, Lottie/dotLottie and Rive for authored animation, GSAP/Motion/anime.js/Framer Motion/React Spring/Popmotion, D3 and Observable Plot for data, Matter.js/Rapier for physics, Tone.js/Web Audio for sound, video and image sequences, `<model-viewer>` for 3D models, glTF/Draco/KTX2/Basis for asset delivery.

## Practices
Prefer compositor-friendly properties (transform, opacity); batch DOM reads/writes; use `will-change` sparingly; use a single render loop; handle device pixel ratio with caps; dispose GPU resources; lazy-load heavy libraries and assets; compress meshes and textures; use instancing for repeated objects; throttle on hidden tabs; adaptive quality (reduce DPR, particle count, effects when FPS drops); test on integrated GPUs and mid-range phones; handle context loss; provide static fallbacks.

## Framework integration
Encapsulate imperative animation behind components with clean mount/unmount; avoid re-render-driven animation loops; respect SSR (no `window` access on server); keep animation configuration declarative where possible; unit-test pure math, visual-test frames.

## Failure modes
Memory leaks from undisposed textures, layout thrash, janky scroll, huge bundles from importing entire libraries, blank canvas on unsupported devices.

## Deliverables
Technology choice rationale, asset pipeline, performance report (frame times, memory, bundle size), fallback implementation.
