#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

def validate(value: dict) -> list[str]:
    errors=[]; world=value.get("world",{})
    for key,expected in (("units","meters"),("handedness","right"),("up","+Y"),("assetForward","+Z")):
        if world.get(key)!=expected: errors.append(f"world.{key} must be {expected}")
    ids=set()
    for i,item in enumerate(value.get("layout",[])):
        for key in ("id","position","rotation","scale","dimensions","relationship","supportingFrameIds","confidence","approximationNotes"):
            if key not in item: errors.append(f"layout[{i}] missing {key}")
        if not (item.get("assetId") or item.get("proceduralRecipe")): errors.append(f"layout[{i}] needs assetId or proceduralRecipe")
        if item.get("id") in ids: errors.append(f"duplicate layout id {item.get('id')}")
        ids.add(item.get("id"))
    return errors
def main():
    p=argparse.ArgumentParser();p.add_argument("spec",type=Path);a=p.parse_args(); errors=validate(json.loads(a.spec.read_text()));print(json.dumps({"status":"failed" if errors else "passed","errors":errors},indent=2));return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
