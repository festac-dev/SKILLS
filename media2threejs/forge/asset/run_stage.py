#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
COMPAT={"assessment":"forge/stage2_spec/new_pre_spec_assessment.py","spec":"forge/stage2_spec/new_sculpt_spec.py","blockout":"forge/stage3_build/generate_threejs_factory.py","structural":"forge/stage3_build/orchestrate_passes.py","form":"forge/stage3_build/orchestrate_passes.py","material":"forge/stage1_intake/analyze_texture.py","interaction":"forge/stage4_review/check_part_coverage.py","optimization":"forge/stage3_build/orchestrate_passes.py"}
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--asset-id",required=True);p.add_argument("--stage",choices=tuple(COMPAT),required=True);a=p.parse_args();m=json.loads(a.manifest.read_text());assets={x.get("id"):x for x in m.get("assets",[])}
 if a.asset_id not in assets and not (a.asset_id=="primary" and m.get("mode") in {"image-object","image-character"}):print(json.dumps({"status":"error","reason":"unknown asset"}));return 2
 print(json.dumps({"status":"ready","assetId":a.asset_id,"stage":a.stage,"compatibilityEntry":COMPAT[a.stage],"note":"Run the compatibility entry with the asset spec, record evidence, then mark this project step."}));return 0
if __name__=="__main__":raise SystemExit(main())
