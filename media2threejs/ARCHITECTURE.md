# Architecture

`route.py` converts observed references into one resolved project mode. `state.py` materializes the
dependency graph and `next.py` exposes one resumable command. Video/environment routes lock spatial
facts, coordinates, layout, camera, lighting, and proxy scene before hero assets unlock.

Scene specs contain only stable asset IDs. `AssetRegistry` resolves IDs to factories returning the
same `AssetFactoryResult`. `AssetSwapSystem` owns a stable instance anchor, so swapping a reviewed
final asset preserves world transform and the timeline target. Bounds-derived scale and base
alignment ground the new asset; exceptions restore the proxy and return diagnostics.

Motion specs serialize targets as asset/node or asset/socket IDs. Reviews are scene-level,
asset-level, then integration-level. Deterministic gates never claim aesthetic judgment. Optional
CS2, GLB-reference, and external generation profiles are outside the default route graph.
