#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));from shared.io import read_json,write_json
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args();m=read_json(a.manifest);frames=[r["id"] for r in m.get("references",[]) if r.get("type") in {"video","extracted-frame","image"}]
 value={"schemaVersion":"0.1.0","coordinateSystem":m.get("coordinateSystem"),"supportingReferenceIds":frames,"observedFacts":[],"inferredFacts":[],"contradictions":[],"status":"requires-agent-observation","note":"Populate facts from visible multi-frame evidence; empty facts are not completion evidence."};write_json(a.out,value);print(json.dumps(value));return 0
if __name__=="__main__":raise SystemExit(main())
