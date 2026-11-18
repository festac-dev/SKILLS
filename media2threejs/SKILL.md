---
name: media2threejs
description: Rebuild an object, character, room, or full scene from one or more reference
  images or a video as modular, animation-ready procedural Three.js code. Route single-subject
  images to gated asset sculpting, videos and environment images to scene/layout/camera/motion
  reconstruction, and hybrid references through both pipelines. Do not use for NeRF,
  Gaussian splats, automatic mesh extraction, or downloaded asset packs unless explicitly
  requested.
license: Apache-2.0
metadata:
  upstream_headers:
    version: 0.1.1
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# media2threejs

Create editable TypeScript + plain Three.js projects from reference media. The output is procedural
scene code, structured specifications, stable asset/runtime interfaces, and review evidence. Never
claim 1:1 reconstruction without measurements and passing camera, layout, asset, material, motion,
and frame-level reviews.

## Trigger and exclusions

Use for one or more reference images, videos, or a video plus high-resolution hero references when
the desired result is a modular Three.js object, character, environment, or animated scene. Use the
default real-time browser target when intent is unspecified.

Do not use as a NeRF, Gaussian-splat, photogrammetry, video-to-mesh, or lookalike-asset downloader.
Do not paste a reference onto a plane as geometry. Neural 3D, GLB baselines, and external packs are
opt-in profiles and never silently replace the procedural TypeScript authority.

## Required input

Require readable media plus either an Agent observation or explicit manifest semantic for every
image: `object`, `character`, or `scene`. File extensions identify image versus video only. Also
record intended use when supplied; otherwise use `editable real-time browser scene`. A single view
cannot reveal hidden geometry: mark hidden regions approximate and request more views when that
uncertainty blocks the fidelity target.

## First commands and state authority

Create `references.json`, separating observation from inference, then always run:

```bash
python3 forge/route.py --manifest references.json --write project-manifest.json
python3 forge/state.py init --manifest project-manifest.json --state .media2threejs/state.json
python3 forge/next.py --state .media2threejs/state.json
```

Run `next.py` again at every resume and before every modification or correction. Its one
`nextCommand` is authoritative; never recover progress from conversation memory. Exit 3 or
`status=stopped` is a hard stop.

## Routes

| Mode | Evidence | Pipeline |
| --- | --- | --- |
| `image-object` | object observation from one/more images | intake → asset → asset review |
| `image-character` | character observation from one/more images | intake → asset → character/rig → review |
| `image-scene` | environment/scene observation | intake → spatial facts → scene/camera/light → review |
| `video-scene` | video | intake/frames → spatial facts → proxy scene → camera/light → motion → review |
| `hybrid` | video plus fidelity images | video-scene proxy first → hero asset pipelines → swap → integration review |

Ambiguous image semantics produce `request-input`; do not guess. Read the selected route document
in `grimoire/routes/` before acting. Read only the relevant detailed contracts as their stages are
unlocked.

For an interactive/explorable scene, or whenever the user supplies spatial browser feedback, MUST
read `grimoire/scene/interactive_world_contract.md` before changing geometry or declaring review
complete.

## Shared build rules

- Meters, right-handed, Y-up, local asset forward +Z, semantic base at y=0, stable pivots and IDs.
- Scene specs reference `assetId`, never implementation paths. The registry resolves factories.
- Establish world scale, shell, camera, lighting, occlusion, and paths with proxies before hero work.
- Treat reference-view fidelity and allowed-camera world closure as independent requirements. A
  matching canonical frame does not excuse exposed world edges, finite road caps, or broken reverse
  views; a closed world does not excuse a mismatched reference composition.
- Model roads, paths, shoulders, junctions, and entrances as connected spatial topology rather than
  decorative overlapping planes. Keep utility fixtures and supports outside traffic and traversal
  occupancy zones, and ground objects from their semantic support surfaces.
- Hero assets use the gated image asset pipeline: suitability → observation → assessment → spec →
  blockout → structural → form → material → interaction → optimization.
- Characters add anatomy, head before hair, shared skeleton, rig-payload validation, and pose stress.
- Motion targets serializable `assetId/nodeId` or `assetId/socketId`, never an Object3D reference.
- All procedural noise uses explicit deterministic seeds.
- A final asset replaces its proxy under the same stable instance anchor. Preserve world transform,
  timeline target, sockets, and attachments; scale from bounds and ground from the semantic base.
  Restore the proxy and emit diagnostics on failure.
- Patterned identity surfaces may use a de-lit projected reference only when necessary and declared
  as `reference-projected`. External assets require explicit `external-assets-allowed` policy.

Legacy `forge/stage1_intake` through `stage5_rig` paths remain v0.1 compatibility entry points for
the namespaced `forge/asset`, `character`, `material`, and `review` pipeline. They are not a second
Skill. CS2, GLB-reference, and external-generation behavior lives under `profiles/` and does not
participate in ordinary routing.

For a legacy asset-only state, the compatibility command remains
`forge/next.py --state .img2threejs/state.json`. A selected CS2 profile MUST read `grimoire/intake/cs2_intake_contract.md` completely. Before a legacy asset review, MUST read
   `grimoire/review/gates_reference.md`, then run `forge/stage4_review/diagnose_render.py`,
`forge/stage4_review/diagnose_render_multi_angle.py`, and finally
`forge/stage4_review/check_part_coverage.py`. These compatibility gates do not alter default routes.

## Evidence and review

Deterministic gates measure; Agent vision judges comparison sheets. A global score cannot override
a critical camera, hero feature, attachment, or motion failure.

Scene evidence: selected spatial, lighting, action, first, and last frames; camera landmark and RMS
residuals; topology, presence, placement, scale, relationships, palette, real-light and shadow
checks; side-by-side captures. Interactive scenes additionally require named adversarial captures
at the allowed orbit/pan/zoom extremes plus recorded camera envelope, world-boundary exposure,
path connectivity, occupancy, and grounding results.

Hero evidence: front/right/rear/left turntable, silhouette and feature scores, material crops,
self-intersection, chirality, attachment anchors, part coverage, pivot/bounds, rig payload, and pose
stress where applicable.

Integration evidence: proxy replacement diagnostics, grounded bounds/feet, stable timeline target,
socket alignment, colliders, typecheck/build, browser error-free capture, and a working debug URL.

Every completed state step needs existing evidence paths. `skipped` requires a reason. Video and
hybrid routes cannot unlock formal asset work before spatial facts, coordinate frame, layout
contract, and camera solve pass. `image-object` explicitly skips Scene and Motion.

## Correction actions and hard stops

Choose exactly one after review: `continue`, `refine-route`, `refine-scene-spec`, `refine-camera`,
`refine-lighting`, `refine-asset-spec`, `refine-asset-code`, `refine-motion`, `request-input`, or
`stop`. Corrections are bounded per stage to prevent a single review pass from looping forever, but
there is no cumulative project-wide correction limit. Exhausting a stage budget hard-stops that
stage. Other hard stops include changed input hashes, unreadable media, unresolved image semantics,
missing mandatory evidence, failed critical features, unsafe projection, invalid schemas, and
impossible fidelity from the supplied views.

Treat spatial browser annotations as localized evidence: reproduce the annotated URL, time,
viewport, and camera pose where possible; identify the marked feature before editing. If the same
visible rejection survives a correction, reclassify the failure instead of repeatedly tuning the
same assumed subsystem.

## Output and completion

Deliver project/reference/scene/asset/motion/review specs; TypeScript Three.js factories and scene;
proxy/final registry; deterministic timeline; screenshots, comparison sheets, diagnostics and review
history; plus a handoff report describing measured results and approximations.

Complete only when the selected route is fully reviewed, every hero proxy is safely replaced,
timeline targets survive, schemas validate, Python tests pass, the Vite template typechecks/builds,
browser runtime has no errors, required captures exist, action-ready hierarchy passes, and
`.media2threejs/state.json` reaches handoff. Interactive scenes must also pass the world-closure,
topology, occupancy, and grounding gates. A dev server alone is never completion.
