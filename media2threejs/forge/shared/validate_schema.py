#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from schema_validation import validate
def main():
 p=argparse.ArgumentParser();p.add_argument("schema",type=Path);p.add_argument("instance",type=Path);a=p.parse_args();s=json.loads(a.schema.read_text());v=json.loads(a.instance.read_text());e=validate(v,s);print(json.dumps({"status":"failed" if e else "passed","errors":e},indent=2));return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())
