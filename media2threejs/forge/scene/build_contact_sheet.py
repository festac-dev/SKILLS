#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,math,shutil,subprocess
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("--frames",type=Path,required=True);p.add_argument("--out",type=Path,required=True);p.add_argument("--columns",type=int,default=4);a=p.parse_args();files=sorted(a.frames.glob("*.png"));ffmpeg=shutil.which("ffmpeg")
 if not ffmpeg:print(json.dumps({"status":"skipped","reason":"ffmpeg not installed"}));return 4
 if not files:print(json.dumps({"status":"error","reason":"no PNG frames"}));return 2
 rows=math.ceil(len(files)/a.columns);a.out.parent.mkdir(parents=True,exist_ok=True);command=[ffmpeg,"-hide_banner","-loglevel","error","-pattern_type","glob","-i",str(a.frames/"*.png"),"-vf",f"scale=320:-1,tile={a.columns}x{rows}:padding=4:margin=4","-frames:v","1","-y",str(a.out)];subprocess.run(command,check=True);print(json.dumps({"status":"ok","frames":len(files),"output":str(a.out)}));return 0
if __name__=="__main__":raise SystemExit(main())
