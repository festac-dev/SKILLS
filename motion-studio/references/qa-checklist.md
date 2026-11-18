# Motion Studio Verification

Required checks must pass before delivery. Keep evidence inside the work folder; do not add an unsolicited report document. Record unavailable checks honestly. A sampled frame is evidence of that frame, not of the entire film's motion or sound.

## Rendered video

1. Confirm actual product claims against source, captured results and fixture labels. Check every changing amount/status against the artifact at that moment.
   For a hackathon or launch film, check the closing screen for internal URLs, development ports, setup commands and production annotations. Use product language and a verified public link when one exists; never invent a deployed URL.
2. Inspect before/after every scene boundary and meaningful state change, plus intermediate motion and each close-up. Use the frame extraction helper with the actual timeline.
3. Check safe margins, clipping, text overflow, readable code, caption line breaks, contrast and intentional 8px alignment. Read the frame at the intended viewing size. Pixel sample contrast alone cannot locate all text.
4. Play the entire export. Check matched transitions, purposeful evolving graphics, no unchanged holds over two seconds, caption/VO timing and the final tail. Look for dropped/duplicated frames and discontinuities when playback crosses chunk boundaries.
5. Listen to the full mix. Check names, abbreviations, edits, background audibility, sidechain pumping and transients. If listening is unavailable, disclose that gap; do not mark it passed from LUFS alone.
6. Verify metadata, exact expected frame count, 60fps, dimensions, H.264, `yuv420p`, color range, final audio and complete decoding. Measure −14 LUFS ±1 and true peak ≤−1dBTP on the encoded result. Test seeking and download links.

```sh
bash scripts/extract_frames.sh out/demo.mp4 work/timeline.json work/frames 60
python scripts/check_contrast.py --foreground '#F0F5F7' --background '#081118'
python scripts/check_contrast.py --frame work/frames/0001.png --pairs work/pixels.json
ffprobe -v error -show_streams -show_format -of json out/demo.mp4
ffmpeg -v error -i out/demo.mp4 -f null -
```

`pixels.json` contains explicit foreground/background points chosen from the visible text and its backdrop, for example `[{"label":"caption","foreground":[200,980],"background":[190,980],"large":false}]`. Sample solid glyph interiors; antialiased edges require human interpretation. The helper does not detect text, infer semantic roles or certify a whole frame.

## Animated frontend

- Verify the primary journey after motion is added. Click actual destinations and exercise success, failure and loading states.
- Observe automatic/scroll motion, slow/fast/reverse scroll, resizing, restored scroll positions, direct section links and page transitions.
- Check mouse, touch and keyboard, visible focus, Escape where applicable and 200% zoom. Magnetic visuals must not displace the hit target.
- Check 1440px desktop, 390px mobile and 320px narrow layouts. Reserve image dimensions, avoid horizontal overflow and measure layout shifts.
- Toggle reduced motion while mounted. Ensure animations/scroll spacers stop and readable content remains. Hide/restore the tab and navigate repeatedly to detect leaked loops.
- Measure frame pacing in the target environment. A 60Hz target gives 16.7ms total budget. Name software rendering and hardware gaps instead of claiming device performance from a synthetic average.

## Common failures and fixes

- “All checks passed” based on a build: run the actual moving journey and inspect the export.
- Screenshot passes but captions drift: inspect beginning, middle and end against final word timestamps and playback.
- Frames pass but a transition snaps: sample intermediate poses and compare velocity across the handoff.
- Accessibility fallback blanks the page: show the final composed state, remove pinned height and preserve navigation.
- Revised soundtrack invalidates evidence: re-check audio and full decode; unchanged encoded video-stream hashes allow the prior visual checks to remain applicable.
