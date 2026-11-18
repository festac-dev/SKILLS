#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--state",type=Path,required=True);a=p.parse_args();m=json.loads(a.manifest.read_text());s=json.loads(a.state.read_text());errors=[]
 for k in ("sceneSpecPath","assetRegistryPath","motionSpecPath","reviewManifestPath"):
  if k in m and m[k] and not Path(m[k]).expanduser().is_file():errors.append(f"missing {k}: {m[k]}")
 for key,value in s.get("steps",{}).items():
  if key not in {"review/integration", "handoff"} and value.get("status")=="pending":errors.append(f"pending step: {key}")
 value={"status":"failed" if errors else "passed","errors":errors};print(json.dumps(value));return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
