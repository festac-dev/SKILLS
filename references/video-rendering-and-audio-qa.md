# Video Rendering and Audio QA Helper

Use [Motion Studio QA](../motion-studio/references/qa-checklist.md) for the maintained visual, timing, listening and delivery checklist. This reference documents the toolkit's independent [media audit helper](../scripts/media_audit.py), which complements Motion Studio's frame, contrast, ducking and mastering helpers.

The helper uses installed ffprobe/ffmpeg, installs nothing, makes no network calls and prints JSON to stdout. Metadata, decoder success and signal measurements do not prove polish, factual accuracy, pronunciation, synchronization or human listening.

```sh
python scripts/media_audit.py final.mp4 --width 1920 --height 1080 --fps 60 --video-codec h264 --require-audio --decode
python scripts/media_audit.py final.mp4 --loudness --target-lufs -14 --max-true-peak -1
python scripts/media_audit.py final.mp4 --sample-times 0,12.5,25 --frames-dir /tmp/demo-frames
```

All targets come from the current brief. Nonzero exit indicates an unmet target or tool failure. Frame extraction refuses to overwrite existing sample files. `loudnorm` measurements do not alter the input; use Motion Studio's two-pass mastering helper when correction is needed. Silence has no finite integrated loudness and must fail a requested loudness target.
