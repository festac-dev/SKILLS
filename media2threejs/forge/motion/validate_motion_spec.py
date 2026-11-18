#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
def validate(v):
 errors=[]
 for i,t in enumerate(v.get("tracks",[])):
  for k in ("assetId","targetType","targetId","sceneTime","sourceVideoTime","keyframes","confidence","supportingFrameIds"):
   if k not in t:errors.append(f"tracks[{i}] missing {k}")
  if t.get("targetType") not in {"node","socket"}:errors.append(f"tracks[{i}].targetType invalid")
  if any("Object3D" in str(x) for x in t.values()):errors.append(f"tracks[{i}] contains a renderer object reference")
 return errors
def main():
 p=argparse.ArgumentParser();p.add_argument("spec",type=Path);a=p.parse_args();e=validate(json.loads(a.spec.read_text()));print(json.dumps({"status":"failed" if e else "passed","errors":e}));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())
