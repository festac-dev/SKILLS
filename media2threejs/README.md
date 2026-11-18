# media2threejs

![version](https://img.shields.io/badge/version-0.1.1-green.svg)

`media2threejs` is one Codex Agent Skill for reconstructing objects, characters, rooms, and animated
scenes from images, videos, or hybrid reference sets as editable TypeScript + Three.js projects.
It unifies the gated procedural asset work of img2threejs with a scene/layout/camera/motion pipeline
derived from video2threejs. It does not produce NeRFs, Gaussian splats, automatic meshes, or pretend
that an unrelated downloaded model is a reconstruction.

## Relationship to img2threejs and video2threejs

This repository is an independent downstream integration of two open-source projects. It is not a
new official release of either upstream project.

| Upstream | Relationship to media2threejs | License |
| --- | --- | --- |
| [img2threejs](https://github.com/img2threejs/img2threejs) | The Git history and the asset/object/character pipeline come from img2threejs. Its intake, procedural specification, build, material, rigging, and review foundations remain available through compatibility paths while new public ownership is organized under `forge/asset`, `forge/character`, `forge/material`, and `forge/review`. | Apache-2.0 |
| [video2threejs](https://github.com/cpppppp7/video2threejs) | The video probe, frame extraction, spatial reasoning, camera solving, lighting, live-preview, motion, and handoff ideas were adapted into a new typed Scene Pipeline. video2threejs was not copied as a nested repository and its Git history was not merged. | MIT |

`media2threejs` adds the common router, project manifest, resumable state graph, schemas, stable
asset registry/swap contract, TypeScript runtime, integration review, and one root Codex Skill that
selects object, character, scene, video, or hybrid reconstruction routes.

The audited upstream revisions are pinned in [`UPSTREAM.lock.json`](UPSTREAM.lock.json). The
path-by-path migration status (`copied`, `adapted`, `rewritten`, `deferred`, or `dropped`) is recorded
in [`MIGRATION.md`](MIGRATION.md). License attribution is preserved in
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and
[`licenses/video2threejs-MIT.txt`](licenses/video2threejs-MIT.txt).

## Install for Codex

```bash
./scripts/install-codex.sh
```

This creates `$HOME/.agents/skills/media2threejs` as a symlink to the checkout. Use `--force` only
to replace an existing symlink. For a repo-scoped install, link this checkout at
`<project>/.agents/skills/media2threejs`.

## How it works

1. Agent observations label images as object, character, or scene; suffixes identify media type only.
2. The router selects one of five modes and writes a common project manifest.
3. A local state graph provides the only next command, dependencies, evidence, hashes, skips, and
   per-stage correction safeguards without a cumulative project correction cap.
4. Scene/video modes establish scale, shell, camera, lighting, proxies, and motion before hero work.
5. Hero objects and characters enter the quality-gated procedural asset pipeline.
6. A stable instance anchor swaps reviewed assets for proxies without losing transforms or timeline.
7. Scene, asset, and integration reviews produce explicit measurements and comparison evidence.

The coordinate contract is meters, right-handed, Y-up, and local asset forward +Z. Hidden surfaces
from a single view are always approximations. Exact fidelity is never claimed without passing the
corresponding evidence gates.

## Start a project

```bash
python3 forge/route.py --manifest references.json --write project-manifest.json
python3 forge/state.py init --manifest project-manifest.json --state .media2threejs/state.json
python3 forge/next.py --state .media2threejs/state.json
```

See `schemas/reference-manifest.schema.json` and the runnable fixtures in `examples/`.

## Codex examples

Single object:

```text
$media2threejs rebuild ./references/robot.png as an animation-ready procedural Three.js game asset.
```

Video scene:

```text
$media2threejs rebuild ./references/room.mp4 as an explorable Three.js room with matched camera, lighting, objects, characters, and motion timeline.
```

Hybrid:

```text
$media2threejs use ./references/room.mp4 for scene layout, camera, lighting, and motion; use ./references/chair.png for the hero chair and ./references/girl.png for the main character.
```

`examples/hybrid-room` includes timestamped video-frame records, a scene spec, proxy instances, hero
asset entries, a generated factory reference, the shared swap system, a motion target, and comparison
evidence. Fixtures are deliberately synthetic and network-free.

Project-specific reconstructions, source recordings, generated frames, review captures, and rendered
comparisons remain local. The public repository contains only synthetic, network-free fixtures.

## Development verification

Python 3.10 or newer is required (the macOS system Python 3.9 is not sufficient).

```bash
python3 -m compileall forge
python3 -m unittest discover -s forge/tests -p "test_*.py"
cd templates/vite-threejs
npm install
npm run typecheck
npm run build
```

FFmpeg/browser smoke checks run when those optional tools exist and otherwise report an explicit skip.

## Limits

- Reference images and monocular videos contain scale/depth ambiguity and invisible regions.
- The camera solver is deterministic and reports residuals, but landmark quality limits its answer.
- Procedural-only assets may approximate highly irregular microgeometry or patterned finishes.
- Projection requires declared policy and de-lit evidence; external generation is opt-in.
- v0.1 retains legacy img2threejs script paths as compatibility entry points while their public
  ownership is namespaced under asset/character/material/review.

See `ARCHITECTURE.md`, `MIGRATION.md`, and `THIRD_PARTY_NOTICES.md` for design and provenance.
