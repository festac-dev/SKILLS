#!/usr/bin/env python3
"""Inspect a local video with optional brief-specific checks; no network or installs."""

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import re
import subprocess
import sys


def finite_number(value):
    try:
        number = float(value)
    except (ValueError, TypeError, OverflowError):
        return None
    return number if math.isfinite(number) else None


def frame_rate(value):
    try:
        return finite_number(Fraction(str(value)))
    except (ValueError, ZeroDivisionError):
        return None


def summarize_probe(data):
    streams = data.get("streams", [])
    video = next((s for s in streams if s.get("codec_type") == "video"
                  and not s.get("disposition", {}).get("attached_pic")), None)
    if video is None:
        raise ValueError("No video stream found")
    audio = [s for s in streams if s.get("codec_type") == "audio"]
    duration = finite_number(video.get("duration"))
    if duration is None:
        duration = finite_number(data.get("format", {}).get("duration"))
    return {"video_stream_index": video.get("index", 0),
            "width": video.get("width"), "height": video.get("height"),
            "video_codec": video.get("codec_name"), "pixel_format": video.get("pix_fmt"),
            "average_fps": frame_rate(video.get("avg_frame_rate")),
            "nominal_fps": frame_rate(video.get("r_frame_rate")),
            "duration_seconds": duration, "audio_streams": len(audio),
            "audio_codecs": [s.get("codec_name") for s in audio]}


def criteria_errors(metadata, args):
    errors = []
    for key in ("width", "height", "video_codec"):
        expected = getattr(args, key)
        if expected is not None and metadata[key] != expected:
            errors.append(f"{key}: expected {expected}, observed {metadata[key]}")
    if args.fps is not None and (metadata["average_fps"] is None or abs(metadata["average_fps"] - args.fps) > 0.02):
        errors.append(f"average_fps: expected {args.fps}, observed {metadata['average_fps']}")
    duration = metadata["duration_seconds"]
    if args.min_duration is not None and (duration is None or duration < args.min_duration):
        errors.append(f"duration below requested minimum {args.min_duration}: {duration}")
    if args.max_duration is not None and (duration is None or duration > args.max_duration):
        errors.append(f"duration above requested maximum {args.max_duration}: {duration}")
    if args.require_audio and not metadata["audio_streams"]:
        errors.append("Required audio stream is absent")
    return errors


def run(command, timeout):
    result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
    if result.returncode:
        raise ValueError(f"{command[0]} failed ({result.returncode}): {result.stderr[-1200:].strip()}")
    return result


def loudness_values(stderr):
    for block in reversed(re.findall(r"\{[^{}]*\}", stderr, re.S)):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if "input_i" in data and "input_tp" in data:
            return {"integrated_lufs": finite_number(data["input_i"]),
                    "true_peak_dbtp": finite_number(data["input_tp"])}
    raise ValueError("FFmpeg returned no loudness measurement")


def numeric(text):
    value = finite_number(text)
    if value is None:
        raise argparse.ArgumentTypeError("Expected a finite number")
    return value


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("input", type=Path)
    result.add_argument("--width", type=int)
    result.add_argument("--height", type=int)
    result.add_argument("--fps", type=numeric)
    result.add_argument("--video-codec")
    result.add_argument("--min-duration", type=numeric)
    result.add_argument("--max-duration", type=numeric)
    result.add_argument("--require-audio", action="store_true")
    result.add_argument("--decode", action="store_true", help="Decode the whole file to detect decoder errors")
    result.add_argument("--loudness", action="store_true", help="Measure the first audio stream without altering the input")
    result.add_argument("--target-lufs", type=numeric)
    result.add_argument("--loudness-tolerance", type=numeric, default=1.0)
    result.add_argument("--max-true-peak", type=numeric)
    result.add_argument("--sample-times", help="Comma-separated timestamps in seconds")
    result.add_argument("--frames-dir", type=Path)
    result.add_argument("--timeout", type=numeric, default=120, help="Maximum seconds for each external command")
    return result


def main(argv=None):
    cli = parser()
    args = cli.parse_args(argv)
    for key in ("width", "height", "fps", "timeout"):
        value = getattr(args, key)
        if value is not None and value <= 0:
            cli.error(f"--{key} must be positive")
    for key in ("min_duration", "max_duration", "loudness_tolerance"):
        value = getattr(args, key)
        if value is not None and value < 0:
            cli.error(f"--{key.replace('_', '-')} must be nonnegative")
    if args.min_duration is not None and args.max_duration is not None and args.min_duration > args.max_duration:
        cli.error("Minimum duration exceeds maximum duration")
    if bool(args.sample_times) != bool(args.frames_dir):
        cli.error("--sample-times and --frames-dir must be supplied together")
    report = {"input": str(args.input.resolve()), "checks": {}, "errors": [],
              "limits": "Metadata, decode and signal checks do not prove visual quality, content accuracy or audiovisual sync."}
    try:
        source = args.input.resolve(strict=True)
        if not source.is_file():
            raise ValueError("Input must be a local file")
        probe = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(source)], args.timeout)
        metadata = summarize_probe(json.loads(probe.stdout))
        video_map = f"0:{metadata['video_stream_index']}"
        report["metadata"] = metadata
        report["errors"].extend(criteria_errors(metadata, args))
        report["checks"]["metadata"] = "passed"
        if args.decode:
            run(["ffmpeg", "-nostdin", "-v", "error", "-xerror", "-i", str(source),
                 "-map", video_map, "-map", "0:a?", "-f", "null", "-"], args.timeout)
            report["checks"]["decode"] = "passed"
        if args.loudness or args.target_lufs is not None or args.max_true_peak is not None:
            if not metadata["audio_streams"]:
                raise ValueError("Loudness measurement requires an audio stream")
            measured = run(["ffmpeg", "-nostdin", "-hide_banner", "-i", str(source),
                            "-map", "0:a:0", "-af", "loudnorm=print_format=json", "-f", "null", "-"], args.timeout)
            loudness = loudness_values(measured.stderr)
            report["loudness"] = loudness
            report["checks"]["loudness_measurement"] = "passed"
            observed = loudness["integrated_lufs"]
            if args.target_lufs is not None and (observed is None or abs(observed - args.target_lufs) > args.loudness_tolerance):
                report["errors"].append(f"Integrated loudness {observed} does not meet {args.target_lufs} ± {args.loudness_tolerance} LUFS")
            peak = loudness["true_peak_dbtp"]
            if args.max_true_peak is not None and (peak is None or peak > args.max_true_peak):
                report["errors"].append(f"True peak {peak} does not meet maximum {args.max_true_peak} dBTP")
        if args.sample_times:
            times = [finite_number(t.strip()) for t in args.sample_times.split(",")]
            duration = metadata["duration_seconds"]
            if any(t is None or t < 0 or (duration is not None and t >= duration) for t in times):
                raise ValueError("Sample times must be finite, nonnegative and before the video ends")
            destination = args.frames_dir.resolve()
            targets = [destination / f"frame-{i:04d}-{t:.3f}.png" for i, t in enumerate(times)]
            if any(target.exists() or target.is_symlink() for target in targets):
                raise ValueError("A sample frame already exists; choose a fresh output directory")
            destination.mkdir(parents=True, exist_ok=True)
            report["frames"] = []
            for timestamp, target in zip(times, targets):
                run(["ffmpeg", "-nostdin", "-v", "error", "-n", "-ss", str(timestamp), "-i", str(source),
                     "-map", video_map, "-frames:v", "1", str(target)], args.timeout)
                if not target.is_file() or not target.stat().st_size:
                    raise ValueError(f"No frame extracted at {timestamp}")
                report["frames"].append(str(target))
            report["checks"]["frame_extraction"] = "passed"
    except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
        report["errors"].append(str(exc))
    report["passed"] = not report["errors"]
    print(json.dumps(report, indent=2, allow_nan=False))
    return int(not report["passed"])


if __name__ == "__main__":
    sys.exit(main())
