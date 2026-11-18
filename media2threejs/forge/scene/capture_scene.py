#!/usr/bin/env python3
from __future__ import annotations
import argparse,subprocess,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--capture-id",action="append",default=[]);p.add_argument("--headed",action="store_true");a=p.parse_args();script=Path(__file__).resolve().parents[2]/"scripts/capture_threejs_playwright.py";command=[sys.executable,str(script),"--manifest",str(a.manifest)];
 for value in a.capture_id:command += ["--capture-id",value]
 if a.headed:command.append("--headed")
 return subprocess.run(command).returncode
if __name__=="__main__":raise SystemExit(main())
