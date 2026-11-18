#!/usr/bin/env python3
from __future__ import annotations
import argparse,subprocess,sys
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("--reference",type=Path,required=True);p.add_argument("--render",type=Path,required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args();script=Path(__file__).resolve().parents[1]/"stage4_review/make_comparison_sheet.py";return subprocess.run([sys.executable,str(script),"--reference",str(a.reference),"--render",str(a.render),"--out",str(a.out),"--json"]).returncode
if __name__=="__main__":raise SystemExit(main())
