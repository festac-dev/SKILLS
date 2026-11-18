# Motion Studio Remotion Production

Copy the [starter](../templates/remotion-starter/package.json) into the dedicated production folder and copy `templates/motion-tokens.ts` beside that folder, preserving its relative import. Install there; keep the project being demonstrated read-only. Pin all Remotion packages to the same version. Use the existing compatible Node version and inspect renderer licensing for the actual organization; do not assume installing a package grants every commercial use.

```sh
npm install
npx remotion compositions src/index.tsx
npx remotion still src/index.tsx Demo out/frame.png --frame=180
npx remotion render src/index.tsx Demo out/demo.mp4 \
  --codec=h264 --video-bitrate=24M --pixel-format=yuv420p --color-space=bt709 \
  --x264-preset=veryfast --concurrency=1
```

The starter supplies typed `TypingCode`, `Terminal`, `DiagramDraw`, `Caption` and `Reveal` components. Replace the sample operation with captured project artifacts. Do not assume scaffold content is real product evidence. A 60-second, 60fps composition has 3600 frames; choose the final duration from the speech plus intentional opening/closing space.

```tsx
import {Composition, Sequence, useCurrentFrame, useVideoConfig, spring} from 'remotion';
const enter = spring({frame:Math.max(0, frame-cueFrame), fps,
  config:{mass:1, stiffness:140, damping:24}});
<Sequence from={Math.round(scene.start*fps)} durationInFrames={Math.round(scene.duration*fps)}>
  <FeatureScene />
</Sequence>
```

`useCurrentFrame()` inside a Sequence is local. Keep absolute word times in the root or subtract the scene start exactly once. This prevents double offsets. Avoid a scene timer, CSS animation timer and VO timer all progressing independently.

## Word-driven choreography

```ts
export type Word = {word:string; start:number; end:number};
const clean = (s:string) => s.toLowerCase().replace(/[^\p{L}\p{N}]/gu,'');
function cue(words:Word[], term:string, occurrence=0) {
  const found = words.filter(w=>clean(w.word)===clean(term))[occurrence];
  if (!found) throw new Error(`Missing spoken cue: ${term}`);
  return Math.round(found.start * fps);
}
// A success state lands after the spoken action, not before it:
const verifiedFrame = Math.round(verificationPhraseLastWord.end * fps);
```

Use a phrase matcher for multiword commands and repeated words; never silently default a missing cue to frame zero. Derive the entire scene's actions from a small set of meaningful words. Between those beats, use shared token durations and stagger. Convert provider character timestamps into exact token spans; when trimming narration, trim both waveform and timestamps and rebase all cues.

Syntax highlight the full source with Prism or Shiki, then reveal token text by a character budget derived from cue frames. Do not use colored spans unrelated to actual tokens. Terminals must retain actual stdout, stderr and exit status in the working evidence. Label a faithful reconstruction if it is not a live recording.

## Render reliably

Load fonts/images before capture with `delayRender`/`continueRender`. Use local assets and seeded procedural values. Restrict mounted scenes to the transition neighborhood. Avoid permanent CSS blur on multiple 1080p layers. Use SVG/WebGL or an authored mesh for graphics where geometry matters.

Start with one representative animated slice; inspect both its images and frame pacing. If long renders are fragile, render bounded frame ranges to `.pending.mp4`, atomically rename completed chunks, and record the hash of source, assets and timeline. Reuse only matching chunks. Keep encoder settings and color range identical across chunks. The screenshot time must be `frame/fps`, not wall-clock elapsed time.

A render at 60fps is not evidence that the web UI itself sustains 60fps. Verify the actual stream with `ffprobe`; reject missing frames, wrong duration, unintended full-range color or absent audio.

Before concat-copying chunks, inspect every stream's `time_base` as well as its fps. Two 60fps files may use different MP4 track clocks, especially after one is processed with system FFmpeg. Normalize differing clocks without re-encoding:

```sh
ffmpeg -i chunk.mp4 -map 0:v:0 -an -c:v copy \
  -video_track_timescale 90000 chunk-normalized.mp4
```

Then concatenate the normalized files and assert the expected **total frame count**. A correct reported fps alone does not catch a missing ending or a timestamp gap.

## Common failures and fixes

- Renderer package versions disagree: pin matching `remotion`, `@remotion/bundler` and `@remotion/renderer` versions.
- Unsupported native renderer binary: test the browser; then use the deterministic HTML/Playwright fallback and system FFmpeg.
- Browser disappears between sessions: inspect its executable path, install a project-local browser and keep its cache outside the skill ZIP.
- Captions drift after editing speech: rebuild words and cues from the final recording, not the original narration text.
- A concatenated film loses its ending: compare chunk time bases, normalize the MP4 track clocks and remux again; do not trim the narration to hide the mismatch.
- A video becomes a presentation: vary composition and preserve object continuity between scenes; remove generic left-title/right-card repetition.
