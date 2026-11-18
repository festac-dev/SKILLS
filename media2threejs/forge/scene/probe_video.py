#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil, subprocess
from pathlib import Path

def probe(path: Path) -> dict:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe is required; install FFmpeg and retry")
    command = [executable, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)]
    completed = subprocess.run(command, check=True, capture_output=True, text=True)
    value = json.loads(completed.stdout); value["source"] = str(path); return value

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("video", type=Path); parser.add_argument("--out", type=Path); args = parser.parse_args()
    try: value = probe(args.video)
    except (RuntimeError, subprocess.CalledProcessError, OSError) as error:
        print(json.dumps({"status": "error", "reason": str(error)})); return 2
    text = json.dumps(value, indent=2)
    if args.out: args.out.parent.mkdir(parents=True, exist_ok=True); args.out.write_text(text + "\n")
    else: print(text)
    return 0
if __name__ == "__main__": raise SystemExit(main())
