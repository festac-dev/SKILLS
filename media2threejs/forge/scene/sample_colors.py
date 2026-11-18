#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from collections import Counter
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"stage1_intake"));from extract_pbr_evidence import load_image
def main():
 p=argparse.ArgumentParser();p.add_argument("image",type=Path);p.add_argument("--count",type=int,default=6);p.add_argument("--out",type=Path);a=p.parse_args();image=load_image(a.image);pixels=image[2];bins=Counter((pixel[0]//32*32,pixel[1]//32*32,pixel[2]//32*32) for pixel in pixels);palette=[{"hex":"#%02x%02x%02x"%rgb,"samples":n} for rgb,n in bins.most_common(a.count)];value={"schemaVersion":"0.1.0","source":str(a.image),"palette":palette,"method":"deterministic-32-level-histogram"};text=json.dumps(value,indent=2)
 if a.out:a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(text+"\n")
 else:print(text)
 return 0
if __name__=="__main__":raise SystemExit(main())
