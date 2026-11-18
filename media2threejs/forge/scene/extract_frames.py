#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil, subprocess
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("video", type=Path); parser.add_argument("--out-dir", type=Path, required=True); parser.add_argument("--fps", type=float, default=1.0); parser.add_argument("--scene-threshold", type=float); args = parser.parse_args()
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg: print(json.dumps({"status":"skipped","reason":"ffmpeg not installed"})); return 4
    args.out_dir.mkdir(parents=True, exist_ok=True)
    select = f"select='gt(scene,{args.scene_threshold})'" if args.scene_threshold is not None else f"fps={args.fps}"
    command = [ffmpeg, "-hide_banner", "-loglevel", "error", "-i", str(args.video), "-vf", select, "-vsync", "vfr", str(args.out_dir / "frame-%05d.png")]
    try: subprocess.run(command, check=True)
    except subprocess.CalledProcessError as error: print(json.dumps({"status":"error","code":error.returncode})); return 2
    frames = sorted(str(path) for path in args.out_dir.glob("frame-*.png")); print(json.dumps({"status":"ok","frames":frames})); return 0
if __name__ == "__main__": raise SystemExit(main())
