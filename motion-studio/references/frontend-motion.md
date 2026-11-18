# Motion Studio Frontend Implementation

Inspect the existing stack. Choose one primary animation owner; do not run GSAP and a React animation library against the same transform. Keep native scroll unless smooth-scroll coordination is part of the intended experience. The [landing starter](../templates/landing-page-starter/index.html) works without dependencies and is the fallback reference.

## GSAP, ScrollTrigger and Lenis

```sh
npm install gsap lenis
```

```ts
import gsap from 'gsap';
import {ScrollTrigger} from 'gsap/ScrollTrigger';
import Lenis from 'lenis';
gsap.registerPlugin(ScrollTrigger);
const mm = gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)', () => {
  const lenis = new Lenis({autoRaf:false});
  const tick = (seconds:number) => lenis.raf(seconds * 1000);
  const refresh = () => ScrollTrigger.update();
  lenis.on('scroll', refresh); gsap.ticker.add(tick);
  const tl = gsap.timeline({scrollTrigger:{trigger:'.story',start:'top top',end:'+=1200',scrub:0.5,pin:true}});
  tl.to('.sheet', {y:(i:number)=>-i*64,rotationY:12,stagger:.064,ease:'none'});
  tl.to('.proof', {x:160,opacity:1,duration:.5}, '<.2');
  return () => {gsap.ticker.remove(tick);lenis.off('scroll',refresh);lenis.destroy();};
});
// Component teardown: mm.revert(); dispose WebGL resources separately.
```

Refresh ScrollTrigger after fonts/media layout settles. Reserve media dimensions. Do not pin a section so long that users traverse empty space; the reduced-motion layout must remove the pin and its spacer. Linear interpolation is appropriate for scroll progress; the choreography's entrances still use the shared easing.

## Framer Motion / Motion for React

```sh
npm install motion
```

```tsx
import {motion, useReducedMotion} from 'motion/react';
export function Evidence({children}:{children:React.ReactNode}) {
  const reduced = useReducedMotion();
  return <motion.article initial={reduced?false:{opacity:0,y:32}}
    whileInView={{opacity:1,y:0}} viewport={{once:true,amount:.35}}
    transition={{type:'spring',stiffness:140,damping:24,mass:1}}
    whileHover={reduced?{}:{y:-4}} whileFocus={reduced?{}:{y:-4}}>
    {children}
  </motion.article>;
}
```

Older projects may already use `framer-motion`; keep that installed API instead of forcing a migration. Use layout projection only when measured and useful; don't animate unknown-height content by repeatedly writing `height`.

## Native scroll and route transitions

```css
html {scroll-behavior:smooth}
@supports (animation-timeline: view()) {
  .sheet {animation:lift both linear; animation-timeline:view(); animation-range:entry 0% cover 50%}
  @keyframes lift {from{transform:translateY(64px) rotateX(12deg)}to{transform:none}}
}
@media(prefers-reduced-motion:reduce) {
  html {scroll-behavior:auto}
  .sheet {animation:none;transform:none}
}
```

```ts
const commit = () => router.navigate(destination);
if (!matchMedia('(prefers-reduced-motion: reduce)').matches && document.startViewTransition) {
  document.startViewTransition(commit);
} else commit();
```

Treat View Transitions as an enhancement. Preserve focus and selected records; test route reload/back behavior in the supported browser. If the router's asynchronous commit is not awaitable, integrate its actual completion signal rather than claiming snapshot continuity.

## Three.js, SVG, Lottie and Rive

Use Three.js for a spatial subject whose geometry matters. Limit pixel ratio, bound catch-up delta, stop offscreen, dispose geometries/materials/textures and handle context loss. Don't replace a requested detailed object with a few unrelated rings.

```ts
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5));
const dt = Math.min(clock.getDelta(), 0.05);
if (visible && !document.hidden && !reduced) group.rotation.y += dt * 0.18;
renderer.render(scene, camera);
```

SVG draws a meaningful connector without layout changes:

```tsx
<path d="M 0 40 C 120 40 120 120 240 120" pathLength={1}
  fill="none" stroke="currentColor" strokeWidth={3}
  strokeDasharray={1} strokeDashoffset={1-progress}/>
```

Lottie (`lottie-web`) suits authored vector timelines; Rive (`@rive-app/canvas`) suits authored state machines. Load an actual supplied/licensed animation, tie its state to real UI data, suspend it offscreen, and provide a meaningful still composition on reduced motion. Do not fabricate an animation file or load a random CDN asset.

## Common failures and fixes

- Jank: record a trace, remove layout writes from the scroll loop, cap canvas DPR, simplify blur and detach hidden render loops.
- Pointer-only interaction: supply visible focus feedback and touch behavior; keep magnetic displacement small and never move the actual hit target.
- Animation resumes with a jump: reset the elapsed clock on visibility change and clamp delta.
- Live reduced-motion changes ignored: subscribe to the media query, rebuild static/animated states and remove scroll spacers.
- UI looks animated only on hover: add viewport/scroll/automatic subject choreography when the brief requests a moving page.

For quick asynchronous actions, loading state can start and finish before a browser paints a frame. Keep the actual control visibly busy for a short automatic minimum interval and until its request settles; prevent duplicate taps and clear timers on unmount. Verify changing rendered frames or computed transforms, not just a loading class. Preserve a clear static busy state for reduced motion.
