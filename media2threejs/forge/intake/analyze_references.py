#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));from shared.io import read_json,write_json
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args();m=read_json(a.manifest);observations=[]
 for ref in m.get("references",[]):observations.append({"referenceId":ref.get("id"),"semantic":ref.get("semantic"),"observedRegions":ref.get("observedRegions",[]),"confidence":ref.get("confidence",0),"inferences":[],"unknownRegions":[]})
 value={"schemaVersion":"0.1.0","observationInferenceSeparated":True,"observations":observations};write_json(a.out,value);print(json.dumps(value));return 0
if __name__=="__main__":raise SystemExit(main())
