from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any

from .io import read_json, sha256_path, write_json

PROJECT_STEPS = ["intake", "routing", "reference-analysis"]
SCENE_STEPS = ["spatial-facts", "coordinate-frame", "layout-contract", "camera-solve", "lighting", "scene-blockout"]
ASSET_STEPS = ["assessment", "spec", "blockout", "structural", "form", "material", "interaction", "optimization"]
CHARACTER_STEPS = ["anatomy", "head", "hair", "rig", "animation-readiness"]
MOTION_STEPS = ["scene-table", "paths", "poses", "transitions"]
REVIEW_STEPS = ["scene-frames", "asset-turntables", "motion-scenes", "integration"]


class ProjectStateError(ValueError):
    pass


def step(status: str = "pending", *, reason: str = "") -> dict[str, Any]:
    return {"status": status, "reason": reason, "evidence": [], "inputHashes": {}}


def command_for(step_id: str, manifest_path: str) -> str:
    safe = step_id.replace("/", "-")
    commands = {
        "project/intake": f"python3 forge/intake/validate_references.py --manifest {manifest_path} --out evidence/intake.json",
        "project/routing": f"python3 forge/route.py --manifest {manifest_path} --write project-manifest.json",
        "project/reference-analysis": f"python3 forge/intake/analyze_references.py --manifest {manifest_path} --out evidence/reference-analysis.json",
        "scene/spatial-facts": f"python3 forge/scene/build_spatial_facts.py --manifest {manifest_path} --out spatial-facts.json",
        "scene/layout-contract": "python3 forge/scene/validate_layout_contract.py scene-spec.json",
        "scene/camera-solve": "python3 forge/scene/solve_camera.py camera-landmarks.json --json --out camera-solution.json",
        "motion/scene-table": "python3 forge/motion/validate_motion_spec.py motion-spec.json",
        "review/integration": "python3 forge/review/validate_project.py --manifest project-manifest.json --state .media2threejs/state.json",
        "handoff": "python3 forge/report.py --state .media2threejs/state.json --out media2threejs-report.json",
    }
    if step_id.startswith("assets/"):
        asset_id, asset_step = step_id.split("/")[1:3]
        return f"python3 forge/asset/run_stage.py --manifest {manifest_path} --asset-id {asset_id} --stage {asset_step}"
    return commands.get(step_id, f"python3 forge/state.py mark {step_id} --state .media2threejs/state.json --evidence evidence/{safe}.json")


def _asset_ids(manifest: dict[str, Any]) -> list[tuple[str, str]]:
    assets = manifest.get("assets", [])
    found = []
    for item in assets:
        if isinstance(item, dict) and item.get("id"):
            found.append((str(item["id"]), str(item.get("kind", "object"))))
    return found


def new_project_state(manifest_path: Path, *, max_per_stage: int = 3, max_total: int | None = None) -> dict[str, Any]:
    manifest = read_json(manifest_path)
    mode = manifest.get("mode")
    if mode not in {"image-object", "image-character", "image-scene", "video-scene", "hybrid"}:
        raise ProjectStateError("manifest mode must be a resolved media2threejs route")
    steps: dict[str, dict[str, Any]] = {f"project/{name}": step() for name in PROJECT_STEPS}
    scene_needed = mode in {"image-scene", "video-scene", "hybrid"}
    motion_needed = mode in {"video-scene", "hybrid"}
    skip_scene = "Single asset route has no scene reconstruction."
    skip_motion = "Single-image route has no source motion timeline."
    for name in SCENE_STEPS:
        steps[f"scene/{name}"] = step() if scene_needed else step("skipped", reason=skip_scene)
    assets = _asset_ids(manifest)
    if not assets and mode in {"image-object", "image-character"}:
        assets = [("primary", "character" if mode == "image-character" else "object")]
    for asset_id, kind in assets:
        for name in ASSET_STEPS:
            steps[f"assets/{asset_id}/{name}"] = step()
        if kind == "character":
            for name in CHARACTER_STEPS:
                steps[f"assets/{asset_id}/{name}"] = step()
    for name in MOTION_STEPS:
        steps[f"motion/{name}"] = step() if motion_needed else step("skipped", reason=skip_motion)
    for name in REVIEW_STEPS:
        relevant = not ((name == "scene-frames" and not scene_needed) or (name == "motion-scenes" and not motion_needed))
        steps[f"review/{name}"] = step() if relevant else step("skipped", reason="Review does not apply to this route.")
    steps["handoff"] = step()
    reference_hashes: dict[str, str | None] = {}
    for reference in manifest.get("references", []):
        if not isinstance(reference, dict) or not reference.get("id"): continue
        digest = reference.get("sha256")
        local = reference.get("localPath") or reference.get("path")
        if local:
            candidate = Path(local).expanduser()
            if not candidate.is_absolute(): candidate = manifest_path.parent / candidate
            if candidate.is_file(): digest = sha256_path(candidate)
        reference_hashes[str(reference["id"])] = digest
    spec_hashes: dict[str, str] = {}
    for key in ("sceneSpecPath", "assetRegistryPath", "motionSpecPath", "reviewManifestPath"):
        value = manifest.get(key)
        if value:
            candidate = Path(value).expanduser()
            if not candidate.is_absolute(): candidate = manifest_path.parent / candidate
            if candidate.is_file(): spec_hashes[key] = sha256_path(candidate)
    return {
        "schemaVersion": "0.1.0", "kind": "media2threejs-project-state", "status": "active",
        "projectId": manifest.get("projectId", "media-project"), "mode": mode,
        "manifestPath": str(manifest_path), "manifestHash": sha256_path(manifest_path),
        "referenceHashes": reference_hashes, "steps": steps, "reviewActions": [],
        "proxyReplacements": {}, "correctionBudget": {"maxPerStage": max_per_stage},
        "artifacts": {"screenshots": [], "reviews": [], "specHashes": spec_hashes}, "stopReason": "",
    }


def load_project_state(path: Path) -> dict[str, Any]:
    state = read_json(path)
    if state.get("kind") != "media2threejs-project-state":
        raise ProjectStateError("not a media2threejs project state")
    budget = state.setdefault("correctionBudget", {})
    budget.pop("maxTotal", None)
    reason = str(state.get("stopReason") or "")
    total_stop = re.match(r"Correction budget exhausted for .+ \((\d+)/(\d+), total \d+/\d+\)\.", reason)
    if state.get("status") == "stopped" and total_stop and int(total_stop.group(1)) < int(total_stop.group(2)):
        state["status"] = "active"
        state["stopReason"] = ""
    manifest = Path(state["manifestPath"])
    if manifest.is_file():
        value = read_json(manifest)
        for reference in value.get("references", []):
            local = reference.get("localPath") or reference.get("path")
            if local:
                candidate = Path(local).expanduser()
                if not candidate.is_absolute(): candidate = manifest.parent / candidate
                if candidate.is_file(): reference["sha256"] = sha256_path(candidate)
        invalidate_changed_inputs(state, value, sha256_path(manifest))
        latest_specs: dict[str, str] = {}
        for key in ("sceneSpecPath", "assetRegistryPath", "motionSpecPath", "reviewManifestPath"):
            spec_path = value.get(key)
            if spec_path:
                candidate = Path(spec_path).expanduser()
                if not candidate.is_absolute(): candidate = manifest.parent / candidate
                if candidate.is_file(): latest_specs[key] = sha256_path(candidate)
        previous_specs = state.get("artifacts", {}).get("specHashes", {})
        changed_specs = {key for key in set(previous_specs) | set(latest_specs) if previous_specs.get(key) != latest_specs.get(key)}
        if changed_specs:
            prefixes = []
            if "sceneSpecPath" in changed_specs: prefixes += ["scene/", "review/"]
            if "assetRegistryPath" in changed_specs: prefixes += ["assets/", "review/"]
            if "motionSpecPath" in changed_specs: prefixes += ["motion/", "review/"]
            if "reviewManifestPath" in changed_specs: prefixes += ["review/"]
            for step_id, record in state["steps"].items():
                if any(step_id.startswith(prefix) for prefix in prefixes) and record["status"] == "done":
                    record.update(status="pending", evidence=[], reason="Invalidated by specification hash change.")
            state["artifacts"]["specHashes"] = latest_specs
    return state


def invalidate_changed_inputs(state: dict[str, Any], manifest: dict[str, Any], manifest_hash: str) -> None:
    changed = False
    latest = {r["id"]: r.get("sha256") for r in manifest.get("references", []) if isinstance(r, dict) and r.get("id")}
    if latest != state.get("referenceHashes", {}):
        changed = True
    if manifest_hash != state.get("manifestHash"):
        changed = True
    if changed:
        for step_id, record in state["steps"].items():
            if step_id != "project/intake" and record["status"] == "done":
                record.update(status="pending", evidence=[], reason="Invalidated by manifest or input hash change.")
        state["manifestHash"] = manifest_hash
        state["referenceHashes"] = latest


def dependencies(state: dict[str, Any], step_id: str) -> list[str]:
    mode = state["mode"]
    if step_id == "project/intake": return []
    if step_id == "project/routing": return ["project/intake"]
    if step_id == "project/reference-analysis": return ["project/routing"]
    if step_id.startswith("scene/"):
        prior = [key for key in state["steps"] if key.startswith("scene/")]
        return ["project/reference-analysis"] + prior[:prior.index(step_id)]
    if step_id.startswith("assets/"):
        parts = step_id.split("/"); prefix = "/".join(parts[:2]) + "/"
        prior = [key for key in state["steps"] if key.startswith(prefix)]
        base = ["project/reference-analysis"]
        if mode in {"video-scene", "hybrid"}:
            base += ["scene/spatial-facts", "scene/coordinate-frame", "scene/layout-contract", "scene/camera-solve"]
        return base + prior[:prior.index(step_id)]
    if step_id.startswith("motion/"): return ["scene/scene-blockout"]
    if step_id.startswith("review/"): return [k for k, v in state["steps"].items() if k != step_id and not k.startswith("review/") and k != "handoff" and v["status"] != "skipped"]
    if step_id == "handoff": return [k for k in state["steps"] if k.startswith("review/") and state["steps"][k]["status"] != "skipped"]
    return []


def next_payload(state: dict[str, Any]) -> dict[str, Any]:
    if state["status"] == "stopped":
        return {"status": "stopped", "nextStep": None, "nextCommand": "", "stopReason": state["stopReason"]}
    for step_id, record in state["steps"].items():
        if record["status"] != "pending": continue
        deps = dependencies(state, step_id)
        if all(state["steps"][dep]["status"] in {"done", "skipped"} for dep in deps):
            return {"status": "active", "nextStep": step_id, "nextCommand": command_for(step_id, state["manifestPath"]), "stopReason": ""}
    incomplete = [key for key, value in state["steps"].items() if value["status"] == "pending"]
    if incomplete:
        return {"status": "blocked", "nextStep": None, "nextCommand": "", "stopReason": f"Unsatisfied dependencies for: {', '.join(incomplete)}"}
    return {"status": "complete", "nextStep": None, "nextCommand": "", "stopReason": ""}


def mark_project_step(state: dict[str, Any], step_id: str, status: str, evidence: list[str], reason: str) -> None:
    if step_id not in state["steps"]:
        raise ProjectStateError(f"unknown step: {step_id}")
    if status == "skipped" and not reason.strip():
        raise ProjectStateError("skipped steps require --reason")
    if status == "done" and not evidence:
        raise ProjectStateError("done steps require at least one --evidence path")
    missing = [path for path in evidence if not Path(path).expanduser().exists()]
    if missing:
        raise ProjectStateError(f"evidence does not exist: {', '.join(missing)}")
    deps = dependencies(state, step_id)
    unmet = [dep for dep in deps if state["steps"][dep]["status"] not in {"done", "skipped"}]
    if status == "done" and unmet:
        raise ProjectStateError(f"dependencies incomplete: {', '.join(unmet)}")
    state["steps"][step_id] = {"status": status, "reason": reason, "evidence": evidence, "inputHashes": {p: sha256_path(p) for p in evidence}}
    for path in evidence:
        suffix = Path(path).suffix.lower()
        if suffix in {".png", ".jpg", ".jpeg", ".webp"} and path not in state["artifacts"]["screenshots"]: state["artifacts"]["screenshots"].append(path)
        if "review" in Path(path).name.lower() and path not in state["artifacts"]["reviews"]: state["artifacts"]["reviews"].append(path)


def record_correction(state: dict[str, Any], stage: str, action: str) -> None:
    if action not in {"refine-route", "refine-scene-spec", "refine-camera", "refine-lighting", "refine-asset-spec", "refine-asset-code", "refine-motion"}:
        raise ProjectStateError("action is not a correction action")
    stage_count = sum(1 for item in state["reviewActions"] if item["stage"] == stage)
    budget = state["correctionBudget"]
    if stage_count >= budget["maxPerStage"]:
        state["status"] = "stopped"
        state["stopReason"] = f"Stage correction budget exhausted for {stage} ({stage_count}/{budget['maxPerStage']})."
        return
    state["reviewActions"].append({"stage": stage, "action": action})


def save_project_state(path: Path, state: dict[str, Any]) -> None:
    write_json(path, copy.deepcopy(state))
