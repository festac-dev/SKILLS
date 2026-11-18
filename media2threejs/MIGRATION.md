# Upstream migration

Audit date: 2026-08-30. Exact revisions and remotes are locked in `UPSTREAM.lock.json`. `copied`
means substantially preserved Apache-licensed img2threejs implementation; `adapted` means an
upstream implementation changed to fit unified contracts; `rewritten` means a clean project-level
implementation based on behavior/requirements rather than copied text.

| Upstream path | New path | Status | Adaptation reason | Associated tests |
| --- | --- | --- | --- | --- |
| img2threejs/SKILL.md | SKILL.md + grimoire/routes/* | rewritten | One concise router and progressive route disclosure | test_skill_contract |
| img2threejs/forge/state.py, next.py, _shared/workflow_state.py | forge/state.py, forge/next.py, forge/shared/project_state.py | adapted | Add project/scene/multi-asset/motion hierarchy while retaining v1 compatibility | test_project_state, upstream test_workflow_state |
| img2threejs/forge/stage1_intake/* | forge/intake/* and compatibility forge/stage1_intake/* | adapted | Shared media intake namespace; compatibility retained in v0.1 | upstream intake tests |
| img2threejs/forge/stage2_spec/* | forge/asset/* and compatibility forge/stage2_spec/* | adapted | ObjectSculptSpec becomes hero-asset spec behind project registry | upstream spec/pipeline tests |
| img2threejs/forge/stage3_build/* | forge/asset/* and compatibility forge/stage3_build/* | adapted | Factories adopt shared coordinate and asset interface | upstream generation tests |
| img2threejs/forge/stage4_review/* | forge/review/* and compatibility forge/stage4_review/* | adapted | Asset gates feed unified review actions | upstream review tests |
| img2threejs/forge/stage5_rig/* | forge/character/* and compatibility forge/stage5_rig/* | adapted | Character subflow shares asset IDs and serializable motion targets | upstream rig tests |
| img2threejs/forge/materials/* | forge/material/* and compatibility forge/materials/* | adapted | Materials become a namespaced asset evidence stage | upstream material tests |
| img2threejs/grimoire/intake, build, character, feedback, readiness, review/* | grimoire/asset, character, material, review, feedback/* | copied | Preserve detailed Apache-2.0 quality contracts; route progressively | documentation contract test |
| img2threejs CS2 scripts/docs | profiles/cs2 + compatibility paths | deferred | Optional profile migration cannot influence default routing | route isolation test |
| img2threejs GLB bridge docs/scripts | profiles/glb-reference + compatibility paths | deferred | Optional structural baseline only | route isolation test |
| img2threejs external neural integrations | profiles/external-generation | deferred | Explicit policy opt-in only | asset policy test |
| video2threejs/forge/solve_camera.py | forge/scene/solve_camera.py | adapted | Add vertical fractions, height, pitch, weights, residuals and JSON while keeping `frac` | test_camera_solver |
| video2threejs/forge/extract_frames.sh | forge/scene/extract_frames.py | rewritten | Cross-platform argument-safe FFmpeg wrapper with explicit skips | test_scene_tools |
| video2threejs/forge/shot.sh | forge/scene/capture_scene.py | deferred | Browser capture uses shared runtime; Playwright adapter follows | browser smoke test |
| video2threejs/forge/compare.sh | forge/review/compare_scene_frames.py | deferred | Asset comparison remains available; scene metric adapter follows | review smoke test |
| video2threejs/forge/sample_colors.sh | forge/scene/sample_colors.py | deferred | Palette schema is defined; extraction adapter follows | scene schema test |
| video2threejs/grimoire/intake/* | grimoire/scene/frame_extraction.md, multi_view_analysis.md | adapted | Move video observation into Scene Pipeline | documentation contract test |
| video2threejs/grimoire/space/* | grimoire/scene/coordinate_system.md, layout_contract.md, perspective_solving.md | adapted | Enforce common meters/Y-up/+Z contract | scene schema/layout tests |
| video2threejs/grimoire/build/* | grimoire/scene/camera_matching.md, lighting.md, live_preview.md, motion_timeline.md | adapted | Separate data specs from runtime implementation | template build |
| video2threejs/grimoire/feedback/user_signals.md | grimoire/feedback/user_rejection_memory.md | adapted | Unified correction actions and budgets | correction budget test |
| video2threejs/grimoire/review/* | grimoire/scene/scene_verification.md + grimoire/handoff/* | adapted | Three-layer review and evidence manifest | review schema test |
| video2threejs/templates/lib.js | templates/vite-threejs/src/runtime/* | rewritten | Strict TypeScript, deterministic capture/debug runtime | typecheck/build |
| video2threejs/templates/room.template.js | examples/video-room scene spec only | dropped | Blue Room constants are not a general template | test_no_blue_room_core |
| video2threejs/examples/blue-room.md | examples/video-room/README.md | deferred | Example data may be retained only after decoupling | test_no_blue_room_core |
| video2threejs/examples/golden-hour.md | examples/video-room/README.md | deferred | Convert narrative example into evidence-backed fixture later | smoke fixtures |
| both upstream .git, caches, generated captures | none | dropped | Audit-only, never distributable project content | repository hygiene test |
