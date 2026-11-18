from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "forge"))

from route import route  # noqa: E402
from scene.solve_camera import solve  # noqa: E402
from shared.project_state import (  # noqa: E402
    ProjectStateError, load_project_state, mark_project_step, new_project_state,
    next_payload, record_correction, save_project_state,
)
from shared.schema_validation import validate  # noqa: E402


def reference(kind: str, semantic: str | None = None) -> dict:
    item = {"id": kind, "type": kind, "role": "layout" if kind == "video" else "object-fidelity", "path": f"fixture.{ 'mp4' if kind == 'video' else 'png'}", "confidence": 1, "provenance": {"kind": "fixture"}}
    if semantic: item["semantic"] = semantic
    return item


class RouteTests(unittest.TestCase):
    def test_image_object(self): self.assertEqual(route({"references":[reference("image","object")]})["mode"], "image-object")
    def test_image_character(self): self.assertEqual(route({"references":[reference("image","character")]})["mode"], "image-character")
    def test_image_scene(self): self.assertEqual(route({"references":[reference("image","scene")]})["mode"], "image-scene")
    def test_video_scene(self): self.assertEqual(route({"references":[reference("video")]})["mode"], "video-scene")
    def test_hybrid(self): self.assertEqual(route({"references":[reference("video"),reference("image","object")]})["mode"], "hybrid")
    def test_ambiguous_image_requests_input(self):
        value=route({"references":[reference("image")]}); self.assertEqual(value["status"],"request-input"); self.assertTrue(value["blockingAmbiguities"])
    def test_extension_does_not_guess_semantics(self):
        completed=subprocess.run([sys.executable,str(ROOT/"forge/route.py"),"--input","unknown.png","--json"],capture_output=True,text=True)
        self.assertEqual(completed.returncode,3); self.assertEqual(json.loads(completed.stdout)["mode"],"request-input")


class StateTests(unittest.TestCase):
    def make_state(self, folder: Path, mode: str="image-object", max_per_stage: int=3):
        media=folder/"input.bin"; media.write_bytes(b"one")
        assets=[{"id":"primary","kind":"object"}] if mode=="hybrid" else []
        manifest=folder/"project-manifest.json"; manifest.write_text(json.dumps({"projectId":"test","mode":mode,"references":[{"id":"source","localPath":str(media),"sha256":"7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed"}],"assets":assets}))
        return manifest,new_project_state(manifest,max_per_stage=max_per_stage,max_total=2)
    def test_project_state_initialization_and_explicit_skips(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp)); self.assertEqual(next_payload(state)["nextStep"],"project/intake")
            self.assertEqual(state["steps"]["scene/spatial-facts"]["status"],"skipped"); self.assertTrue(state["steps"]["scene/spatial-facts"]["reason"])
    def test_parent_child_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);_,state=self.make_state(folder,"hybrid"); evidence=folder/"e.json";evidence.write_text("{}")
            with self.assertRaises(ProjectStateError): mark_project_step(state,"assets/primary/assessment","done",[str(evidence)],"")
    def test_skipped_requires_reason(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp));
            with self.assertRaises(ProjectStateError): mark_project_step(state,"project/intake","skipped",[],"")
    def test_missing_evidence_cannot_continue(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp));
            with self.assertRaises(ProjectStateError): mark_project_step(state,"project/intake","done",[],"")
    def test_correction_budget_hard_stop(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp),max_per_stage=1);record_correction(state,"camera","refine-camera");record_correction(state,"camera","refine-camera");self.assertEqual(state["status"],"stopped")
    def test_total_corrections_are_unlimited(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp),max_per_stage=2)
            for index in range(8): record_correction(state,f"stage-{index}","refine-asset-code")
            self.assertNotEqual(state["status"],"stopped");self.assertEqual(len(state["reviewActions"]),8);self.assertNotIn("maxTotal",state["correctionBudget"])
    def test_deterministic_next_command(self):
        with tempfile.TemporaryDirectory() as tmp:
            _,state=self.make_state(Path(tmp));self.assertEqual(next_payload(state),next_payload(state))
    def test_resume_after_process_restart(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);_,state=self.make_state(folder);path=folder/"state.json";save_project_state(path,state)
            first=subprocess.run([sys.executable,str(ROOT/"forge/next.py"),"--state",str(path)],capture_output=True,text=True,check=True).stdout
            second=subprocess.run([sys.executable,str(ROOT/"forge/next.py"),"--state",str(path)],capture_output=True,text=True,check=True).stdout
            self.assertEqual(json.loads(first)["nextCommand"],json.loads(second)["nextCommand"])
    def test_input_hash_change_invalidates_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);manifest,state=self.make_state(folder);evidence=folder/"e.json";evidence.write_text("{}")
            mark_project_step(state,"project/intake","done",[str(evidence)],"");path=folder/"state.json";save_project_state(path,state)
            (folder/"input.bin").write_bytes(b"two");loaded=load_project_state(path)
            self.assertNotEqual(loaded["referenceHashes"]["source"],state["referenceHashes"]["source"])
            self.assertEqual(loaded["steps"]["project/routing"]["status"],"pending")
    def test_spec_hash_change_invalidates_scene_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);media=folder/"input.bin";media.write_bytes(b"one");spec=folder/"scene.json";spec.write_text('{"revision":1}')
            manifest=folder/"project-manifest.json";manifest.write_text(json.dumps({"projectId":"test","mode":"image-scene","references":[{"id":"source","localPath":str(media)}],"sceneSpecPath":str(spec)}))
            state=new_project_state(manifest);state["steps"]["scene/spatial-facts"]["status"]="done";path=folder/"state.json";save_project_state(path,state);spec.write_text('{"revision":2}')
            loaded=load_project_state(path);self.assertEqual(loaded["steps"]["scene/spatial-facts"]["status"],"pending");self.assertIn("specification hash",loaded["steps"]["scene/spatial-facts"]["reason"])


class SchemaTests(unittest.TestCase):
    def validate_example(self,name: str,path: Path):
        schema=json.loads((ROOT/"schemas"/name).read_text());instance=json.loads(path.read_text());self.assertEqual(validate(instance,schema),[])
    def test_scene_schema(self): self.validate_example("scene-spec.schema.json",ROOT/"examples/hybrid-room/scene-spec.json")
    def test_asset_registry_schema(self): self.validate_example("asset-registry.schema.json",ROOT/"examples/hybrid-room/asset-registry.json")
    def test_motion_schema(self): self.validate_example("motion-spec.schema.json",ROOT/"examples/hybrid-room/motion-spec.json")


class IntegrationContractTests(unittest.TestCase):
    def test_integration_validator_allows_pending_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp)
            specs={}
            for key,name in (("sceneSpecPath","scene.json"),("assetRegistryPath","assets.json"),("motionSpecPath","motion.json"),("reviewManifestPath","review.json")):
                path=folder/name;path.write_text("{}");specs[key]=str(path)
            manifest=folder/"manifest.json";manifest.write_text(json.dumps(specs))
            state=folder/"state.json";state.write_text(json.dumps({"steps":{"project/intake":{"status":"done"},"review/integration":{"status":"pending"},"handoff":{"status":"pending"}}}))
            completed=subprocess.run([sys.executable,str(ROOT/"forge/review/validate_project.py"),"--manifest",str(manifest),"--state",str(state)],capture_output=True,text=True)
            self.assertEqual(completed.returncode,0,completed.stdout+completed.stderr)
            self.assertEqual(json.loads(completed.stdout)["status"],"passed")
    def test_camera_solver_regression(self):
        value=solve({"aspect":16/9,"search":{"x":[0,0],"z":[0,0],"y":[1,1],"pitch":[0,0],"hfov":[60]},"landmarks":[{"name":"center","x":5,"y":1,"z":0,"frac":.5,"verticalFraction":.5,"weight":2}]})
        self.assertAlmostEqual(value["rmsResidual"],0,places=7);self.assertIn("vertical",value["residuals"][0])
    def test_camera_solver_rejects_back_facing_periodic_solution(self):
        value=solve({"aspect":16/9,"search":{"x":[0,0],"z":[0,0],"y":[1,1],"pitch":[0,0],"hfov":[60]},"landmarks":[{"name":"ahead","x":0,"y":1,"z":-5,"frac":.5,"verticalFraction":.5}]})
        heading=value["camera"]["headingDegrees"];self.assertTrue(-100<=heading<=-80,heading)
    def test_proxy_transform_preservation_contract(self):
        text=(ROOT/"templates/vite-threejs/src/scene/assetSwapSystem.ts").read_text();self.assertIn("const anchor = new THREE.Group()",text);self.assertNotIn("value.anchor.position.copy",text)
    def test_timeline_target_preservation_contract(self):
        text=(ROOT/"templates/vite-threejs/src/scene/assetSwapSystem.ts").read_text();self.assertIn("timelineTarget: anchor",text);self.assertIn("value.anchor.add(finalAsset.root)",text)
    def test_license_and_notices(self):
        self.assertIn("Apache License",(ROOT/"LICENSE").read_text());self.assertIn("MIT License",(ROOT/"licenses/video2threejs-MIT.txt").read_text());self.assertTrue((ROOT/"THIRD_PARTY_NOTICES.md").is_file())
    def test_no_blue_room_core_assumptions(self):
        for base in (ROOT/"forge",ROOT/"templates/vite-threejs/src"):
            for path in base.rglob("*"):
                if "tests" not in path.parts and path.is_file() and path.suffix in {".py",".ts",".js"}: self.assertNotIn("Blue Room",path.read_text(errors="ignore"))


class SkillContractTests(unittest.TestCase):
    def test_skill_metadata(self):
        lines=(ROOT/"SKILL.md").read_text().splitlines();self.assertEqual(lines[0],"---");front=lines[1:lines.index("---",1)];values=dict(line.split(":",1) for line in front if ":" in line and not line.startswith(" "));self.assertEqual(values["name"].strip(),"media2threejs");self.assertEqual(values["version"].strip(),"0.1.1")
    def test_interactive_world_contract_is_routed_and_enforced(self):
        contract=ROOT/"grimoire/scene/interactive_world_contract.md";self.assertTrue(contract.is_file())
        text=contract.read_text();self.assertIn("Two independent gates",text);self.assertIn("Traversal topology",text);self.assertIn("Physical support and occupancy",text);self.assertIn("Hard-fail completion",text)
        for path in (ROOT/"SKILL.md",ROOT/"grimoire/routes/video-scene.md",ROOT/"grimoire/routes/image-scene.md",ROOT/"grimoire/routes/hybrid.md",ROOT/"grimoire/scene/scene_verification.md"):
            self.assertIn("interactive_world_contract.md",path.read_text(),path)
    def test_only_one_invokable_skill(self):
        skills=[path for path in ROOT.rglob("SKILL.md") if ".git" not in path.parts and "node_modules" not in path.parts];self.assertEqual(skills,[ROOT/"SKILL.md"])
    def test_three_offline_smoke_fixtures(self):
        for name in ("image-object","video-scene","hybrid-scene"):self.assertTrue((ROOT/"forge/tests/fixtures"/name/"references.json").is_file())
    def test_no_nested_skill_collision(self):
        self.assertFalse(any(path.name=="SKILL.md" for path in (ROOT/"profiles").rglob("SKILL.md")))


if __name__ == "__main__": unittest.main()
