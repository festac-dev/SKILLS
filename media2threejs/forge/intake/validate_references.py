#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from shared.io import read_json,sha256_path,write_json
def main():
 p=argparse.ArgumentParser();p.add_argument("--manifest",type=Path,required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args();m=read_json(a.manifest);checks=[];errors=[]
 for ref in m.get("references",[]):
  local=ref.get("localPath");item={"id":ref.get("id"),"localPath":local,"status":"unverified"}
  if local:
   path=Path(local).expanduser();item["status"]="readable" if path.is_file() else "missing"
   if path.is_file():item["sha256"]=sha256_path(path)
   else:errors.append(f"{ref.get('id')}: missing local reference {path}")
  elif ref.get("path") or ref.get("url"):item["status"]="remote-unverified";errors.append(f"{ref.get('id')}: remote reference must be acquired and hashed")
  else:errors.append(f"{ref.get('id')}: no path or URL")
  checks.append(item)
 value={"schemaVersion":"0.1.0","status":"failed" if errors else "passed","checks":checks,"errors":errors};write_json(a.out,value);print(json.dumps(value));return 1 if errors else 0
if __name__=="__main__":raise SystemExit(main())
