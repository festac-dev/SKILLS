# Specialist: Motion, 3D and Immersive Experiences

Use when graphics explain a process, support spatial interaction or deliver an explicitly requested visual experience. Motion, 3D, AR/VR/MR, spatial audio and haptics are optional capabilities. Select them from the brief, device support and production cost; labels such as 4D/5D/6D need a project-specific definition.

## Choose the representation

For supplied references, read [reference analysis](../references/visual-reference-analysis.md). Distinguish the demonstrated product’s motion from recording edits, camera movement and overlays. Define the focal object, action, trajectory, depth, camera, transition interval, hold and reset before choosing a renderer.

| Method | Appropriate use | Cost or limit to check |
|---|---|---|
| CSS/SVG | Typography, interface transitions, logos, paths and layered diagrams | Layout work, filter cost and legibility |
| Canvas | Dense drawing or custom 2D interaction | Pixel density, hit testing and accessible content |
| Live GPU geometry | Spatial inspection, changing objects, live state or authored 3D scenes | Geometry, textures, draw calls, hardware support and resource lifetime |
| Rendered video/frame sequence | A fixed cinematic shot | Loading, seeking, decoded memory and poster/fallback |
| Original/licensed imagery | A detailed subject better represented as imagery | Rights, crop, resolution and responsive art direction |

Use the least complex representation that achieves the requested fidelity. A detailed physical subject may need authored geometry, textures or imagery; boxes and rings are prototypes unless they achieve the intended style. Do not imply a fixed video is interactive geometry. Verify APIs against the installed renderer version.

## Make the motion specific

An explicit request for moving graphics is an acceptance requirement. Define what visibly moves and implement automatic motion when requested; hover-only movement does not fulfill autoplay. Page illustrations should follow scroll progress, viewport entry, pointer movement or an authored automatic sequence. Do not add play/pause buttons, step selectors, scrubbers, speed sliders or rotation toolbars unless explicitly requested. Preserve essential information outside the animation.

Build readable beats around actual product behavior: layers separate for inspection, a signal arrives, a gate responds, the result settles. Pick one focal action per beat and coordinate secondary movement with it. Layering, curved paths, camera pushes, material contrast and staggered assembly are options, not a prescribed aesthetic. Distinct products need different compositions and actions beyond palette changes or faster spins.

Keep the dominant object large enough to read and reserve room for its full travel. Check intermediate frames, occlusion and lighting in every supported theme. Keep labels in stable HTML when perspective would impair reading. Mark illustrative states as such; an animated completion must never imply an actual payment, verification or approval.

Drive geometry, phase labels and illustrative outcomes from one progress source. Use elapsed time rather than frame count, intentional holds, and a continuous reset or final resting state. A reduced-motion preference needs a composed static state, including when changed while mounted.

## Choreograph the whole page

Describe how the heading, focal scene, supporting content and next section relate through each beat. If a scene stays in view while its layers separate, define when surrounding content moves and when the section releases. Avoid adding unrelated floating or pulsing effects to an unchanged page.

For scroll progression, map actual section bounds and available travel to progress. Support slow movement, fast jumps, reversal, resize and restored scroll position without trapping normal scrolling. If autoplay and scroll coexist, define clock ownership, transfer and resume position. Pointer response supplements touch and keyboard use. Reduce or remove extended scroll distance in the reduced-motion layout.

Use interface transitions to preserve orientation: retain selected records, focus and return position across list/detail or workspace navigation. Native view transitions can progressively enhance this; navigation must work without them. Keep controls stable and never hide essential information behind hover.

## Budget and own the runtime

At 60 Hz, the whole frame has about 16.7 ms; rendering cannot claim the entire budget. Measure the appropriate target before choosing pixel density, geometry detail, texture size, frame rate or effects. Do not turn software-browser QA into a hardware performance claim.

For frame sequences, estimate decoded memory as width × height × four bytes × resident frames. Preload a bounded neighborhood, release obsolete frames and show a useful poster while loading. Avoid eagerly decoding hundreds of full-resolution images.

For live geometry, own and dispose geometries, materials, textures, animation frames, listeners and observers. Resize drawing buffers deliberately, bound pixel density, suspend unnecessary offscreen/background work and cap catch-up after suspension. Check shader precision, color space, transparency and overdraw on target hardware. Handle lost GPU context and asset failure. A vector fallback needs independent legibility and depth/layer review; renderer availability does not prove visual equivalence.

## Verify the experience

Validate one representative scene in its actual layout before propagating infrastructure or running expensive builds. Inspect opening, major phases, intermediate motion, loop seam and section handoff on desktop and narrow screens. Review continuously where available; timed frames establish states and approximate intervals, not fluidity or audio synchronization.

Check keyboard/touch behavior, reduced motion, fast/reverse scroll, dynamic resize, background suspension, repeated navigation, load failure and rendering fallback where relevant. Verify the linked product task still works. Evaluate applicable sustained-motion, flashing and control criteria; reduced motion alone does not establish accessibility conformance. Do not add interface audio just because a reference film has sound.

When the result “still feels the same,” compare subject detail and scale, silhouette, content order, trajectory, depth, camera, timing and scroll relationship. Correct the actual mismatch; another loop or recolored primitive is not evidence of a new direction.

Report observed environments, frame/memory measurements when taken, rendering method, defects fixed and remaining gaps. Record actual playback/frame/audio inspection methods. Do not claim GPU quality or full audiovisual review from screenshots.

Related: [Spatial experiences](3d-spatial-and-immersive-experiences.md), [design systems](design-systems-and-ui.md), [platform coverage](../references/platform-compatibility-matrix.md), [direction brief](../templates/VISUAL_DIRECTION_AND_MOTION_BRIEF.md).

## Technique references and examples

Use [animation recipes](../references/animated-graphics-recipes.md) and the [runnable graphics examples](../examples/animated-graphics/index.html) for rotation, moving layers and connection flow. Keep pointer input clamped and smoothed without obscuring native controls; recompute connector geometry when endpoints move. Detailed owners cover [scroll narratives](scroll-driven-and-narrative-experiences.md), [pointer response](pointer-and-cursor-responsive-design.md), [procedural graphics](generative-and-procedural-graphics.md) and [shaders](creative-coding-webgl-and-shaders.md). Apply only the techniques needed for the requested scene.
