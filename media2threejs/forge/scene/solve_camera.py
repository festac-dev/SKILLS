#!/usr/bin/env python3
"""Deterministic coarse-to-fine camera solver, compatible with video2threejs landmarks."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

def project(camera: dict, landmark: dict, aspect: float) -> tuple[float, float]:
    dx, dy, dz = landmark["x"]-camera["x"], landmark.get("y", 0)-camera["y"], landmark["z"]-camera["z"]
    heading = camera["heading"]; pitch = camera.get("pitch", 0.0)
    horizontal = (math.atan2(dz, dx)-heading+math.pi)%(2*math.pi)-math.pi
    distance = max(1e-9, math.hypot(dx, dz)); vertical = math.atan2(dy, distance)-pitch
    ht = math.tan(math.radians(camera["hfov"])/2); vt = ht/aspect
    if abs(horizontal) >= math.pi / 2:
        return 9.0, 9.0
    return 0.5+math.tan(horizontal)/(2*ht), 0.5-math.tan(vertical)/(2*vt)

def solve(config: dict) -> dict:
    landmarks = config["landmarks"]; aspect=float(config.get("aspect",16/9)); search=config.get("search",{})
    xs=search.get("x",[-2,10]); zs=search.get("z",[-2,10]); ys=search.get("y",[config.get("y",1.05)]*2); pitches=search.get("pitch",[config.get("pitch",0),config.get("pitch",0)])
    fovs=search.get("hfov",[60,65,70,75,80,85,90,95]); best=None
    for hfov in fovs:
      for i in range(21):
       for j in range(21):
        for yi in range(3 if ys[0]!=ys[1] else 1):
         for pi in range(5 if pitches[0]!=pitches[1] else 1):
          cam={"x":xs[0]+(xs[1]-xs[0])*i/20,"z":zs[0]+(zs[1]-zs[0])*j/20,"y":ys[0]+(ys[1]-ys[0])*(yi/(2 if ys[0]!=ys[1] else 1)),"pitch":math.radians(pitches[0]+(pitches[1]-pitches[0])*(pi/(4 if pitches[0]!=pitches[1] else 1))),"hfov":float(hfov)}
          for hi in range(72):
           cam["heading"]=-math.pi+hi*math.pi/36; residuals=[]; total=0.0; weight_total=0.0
           for lm in landmarks:
            px,py=project(cam,lm,aspect); weight=float(lm.get("weight",1)); ex=px-float(lm.get("frac",lm.get("horizontalFraction"))); ey=0.0 if "verticalFraction" not in lm and "vfrac" not in lm else py-float(lm.get("verticalFraction",lm.get("vfrac")))
            total+=weight*(ex*ex+ey*ey); weight_total+=weight; residuals.append({"name":lm.get("name","landmark"),"horizontal":ex,"vertical":ey,"weightedSquared":weight*(ex*ex+ey*ey)})
           score=math.sqrt(total/max(weight_total,1e-9))
           if best is None or score<best[0]: best=(score,dict(cam),residuals)
    rms,cam,residuals=best; vfov=2*math.degrees(math.atan(math.tan(math.radians(cam["hfov"])/2)/aspect)); distance=float(config.get("targetDistance",6)); cam["headingDegrees"]=math.degrees(cam["heading"]); cam["pitchDegrees"]=math.degrees(cam["pitch"]); cam["vfov"]=vfov
    target={"x":cam["x"]+distance*math.cos(cam["heading"])*math.cos(cam["pitch"]),"y":cam["y"]+distance*math.sin(cam["pitch"]),"z":cam["z"]+distance*math.sin(cam["heading"])*math.cos(cam["pitch"])}
    return {"schemaVersion":"0.1.0","camera":cam,"target":target,"rmsResidual":rms,"residuals":residuals}

def main() -> int:
    p=argparse.ArgumentParser();p.add_argument("input",type=Path);p.add_argument("--json",action="store_true");p.add_argument("--out",type=Path);a=p.parse_args(); result=solve(json.loads(a.input.read_text()))
    text=json.dumps(result,indent=2)
    if a.out:a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(text+"\n")
    if a.json or not a.out:print(text)
    return 0
if __name__=="__main__":raise SystemExit(main())
