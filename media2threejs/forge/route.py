#!/usr/bin/env python3
"""Route reference media into the unified media2threejs pipeline.

File suffixes identify media transport only. Semantic routing requires explicit
observations in a reference manifest; ambiguous images fail closed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shared.io import read_json, sha256_path, write_json  # noqa: E402

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff"}
VIDEO_SUFFIXES = {".mp4", ".mov", ".mkv", ".webm", ".avi", ".m4v"}
SEMANTICS = {"object", "character", "scene"}


def media_type(path: str) -> str:
    suffix = Path(path.split("?", 1)[0]).suffix.lower()
    if suffix in IMAGE_SUFFIXES:
        return "image"
    if suffix in VIDEO_SUFFIXES:
        return "video"
    return "unknown"


def normalize_reference(raw: dict[str, Any], index: int, base_dir: Path = Path.cwd()) -> dict[str, Any]:
    source = str(raw.get("localPath") or raw.get("path") or raw.get("url") or "")
    kind = raw.get("type") or media_type(source)
    semantic = raw.get("semantic") or raw.get("subjectType") or raw.get("observedContent")
    local_source = raw.get("localPath") or (source if source and not source.startswith(("http://", "https://")) else None)
    if local_source:
        candidate = Path(str(local_source)).expanduser()
        if not candidate.is_absolute(): candidate = base_dir / candidate
        local_source = str(candidate.resolve())
    result = {
        "id": raw.get("id", f"reference-{index + 1}"),
        "type": kind,
        "role": raw.get("role", "unclassified"),
        "path": raw.get("path") or raw.get("url"),
        "localPath": local_source,
        "sha256": raw.get("sha256"),
        "timeRange": raw.get("timeRange"),
        "parentVideoId": raw.get("parentVideoId"),
        "frameTime": raw.get("frameTime"),
        "observedRegions": raw.get("observedRegions", []),
        "confidence": raw.get("confidence", 1.0 if semantic in SEMANTICS else 0.0),
        "provenance": raw.get("provenance", {"kind": "user-supplied"}),
        "semantic": semantic,
    }
    local = result["localPath"]
    if not result["sha256"] and local and Path(local).expanduser().is_file():
        result["sha256"] = sha256_path(local)
    return result


def classify(refs: list[dict[str, Any]], explicit_mode: str | None = None) -> tuple[str, float, list[str], list[str]]:
    if explicit_mode:
        return explicit_mode, 1.0, ["Mode was explicitly supplied by the manifest."], []
    videos = [r for r in refs if r["type"] == "video"]
    images = [r for r in refs if r["type"] in {"image", "extracted-frame"}]
    reasons: list[str] = []
    ambiguities: list[str] = []
    if videos and images:
        reasons.append("Video supplies temporal/scene evidence and images supply supplemental fidelity evidence.")
        return "hybrid", min(float(r.get("confidence", 0.8)) for r in refs), reasons, ambiguities
    if videos:
        reasons.append("At least one video requires scene, camera, layout, and motion analysis.")
        return "video-scene", 0.95, reasons, ambiguities
    semantics = {r.get("semantic") for r in images if r.get("semantic") in SEMANTICS}
    if len(semantics) != 1:
        ambiguities.append("Image semantics must explicitly resolve to exactly one of object, character, or scene.")
        return "request-input", 0.0, reasons, ambiguities
    semantic = next(iter(semantics))
    mode = {"object": "image-object", "character": "image-character", "scene": "image-scene"}[semantic]
    reasons.append(f"All image observations identify a {semantic} reconstruction target.")
    return mode, min(float(r.get("confidence", 1.0)) for r in images), reasons, ambiguities


def route(manifest: dict[str, Any], base_dir: Path = Path.cwd()) -> dict[str, Any]:
    refs = [normalize_reference(item, i, base_dir) for i, item in enumerate(manifest.get("references", []))]
    mode, confidence, reasons, ambiguities = classify(refs, manifest.get("mode"))
    pipelines = {
        "image-object": ["intake", "asset", "review"],
        "image-character": ["intake", "asset", "character", "review"],
        "image-scene": ["intake", "scene", "review"],
        "video-scene": ["intake", "scene", "motion", "review"],
        "hybrid": ["intake", "scene", "asset", "character-optional", "motion", "integration-review"],
    }.get(mode, ["intake", "routing"])
    project_id = manifest.get("projectId", "media-project")
    output = {
        "schemaVersion": "0.1.0",
        "projectId": project_id,
        "mode": mode,
        "status": "request-input" if mode == "request-input" else "ready",
        "confidence": confidence,
        "intent": manifest.get("intent", "editable real-time procedural Three.js reconstruction"),
        "fidelityTarget": manifest.get("fidelityTarget", "evidence-gated"),
        "assetPolicy": manifest.get("assetPolicy", "procedural-only"),
        "coordinateSystem": {"units": "meters", "handedness": "right", "up": "+Y", "assetForward": "+Z"},
        "references": refs,
        "assets": manifest.get("assets", []),
        "requiredPipelines": pipelines,
        "optionalProfiles": manifest.get("optionalProfiles", []),
        "reasoningSummary": reasons,
        "blockingAmbiguities": ambiguities,
        "sceneSpecPath": manifest.get("sceneSpecPath", "scene-spec.json"),
        "assetRegistryPath": manifest.get("assetRegistryPath", "asset-registry.json"),
        "motionSpecPath": manifest.get("motionSpecPath", "motion-spec.json"),
        "reviewManifestPath": manifest.get("reviewManifestPath", "review-manifest.json"),
        "statePath": manifest.get("statePath", ".media2threejs/state.json"),
        "outputDirectory": manifest.get("outputDirectory", "dist/media2threejs"),
    }
    output["nextCommand"] = ("request semantic observations for ambiguous images" if mode == "request-input" else
        f"python3 forge/state.py init --manifest project-manifest.json --state {output['statePath']}")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="append", default=[])
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    if args.manifest:
        manifest = read_json(args.manifest)
    else:
        manifest = {"references": [{"path": value} for value in args.input]}
    if not manifest.get("references"):
        parser.error("provide --input or --manifest with references")
    result = route(manifest, args.manifest.parent.resolve() if args.manifest else Path.cwd())
    if args.write:
        write_json(args.write, result)
    if args.json or not args.write:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"wrote {args.write} ({result['mode']}, {result['status']})")
    return 3 if result["status"] == "request-input" else 0


if __name__ == "__main__":
    raise SystemExit(main())
