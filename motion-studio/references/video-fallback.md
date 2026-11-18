# Motion Studio Browser and Diagram Rendering

Use when Remotion cannot run reliably on the host. Keep its React scene authoring when possible, but expose a deterministic `window.renderAt(seconds)` in the browser. Rendering the same timestamp twice must produce identical pixels.

```js
// Playwright installed in the dedicated production folder.
const browser = await chromium.launch({executablePath: process.env.CHROME_PATH,
  args:['--no-sandbox','--disable-dev-shm-usage']});
const page = await browser.newPage({viewport:{width:1920,height:1080}});
await page.goto('http://127.0.0.1:4173');
await page.evaluate(async()=>{await document.fonts.ready;
  await Promise.all([...document.images].map(i=>i.decode()));});
for (let frame=0; frame<duration*60; frame++) {
  await page.evaluate(t=>window.renderAt(t),frame/60);
  // renderAt must finish synchronous layout/painting state, or return a readiness promise.
  await page.screenshot({path:`frames/${String(frame).padStart(6,'0')}.png`});
}
await browser.close();
```

For long work, pipe JPEG/PNG frames to FFmpeg or encode recoverable chunks to avoid thousands of retained frames. Await pipe backpressure. Raw RGBA can be faster than JPEG encoding on constrained CPUs; measure transfer cost. Never silently halve motion frame rate and label the result 60fps.

```sh
ffmpeg -framerate 60 -i frames/%06d.png -i mastered.wav \
  -vf 'scale=1920:1080:out_color_matrix=bt709:out_range=tv,format=yuv420p' \
  -c:v libx264 -preset veryfast -b:v 24M -maxrate 30M -bufsize 48M \
  -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 192k -movflags +faststart -shortest out/demo.mp4
```

The above accepts RGB screenshots. For existing YUV footage, inspect its actual matrix/range and specify `in_color_matrix` and `in_range`. Normalize sources individually before concatenating; a global range assumption is wrong for mixed full/limited-range clips.

For CSS/Web Animations, pause and set `animation.currentTime = seconds*1000`. Disable timers and random values, await image decode, and handle animations created during the seek. An explicit scene render function is easier to audit than manipulating arbitrary page clocks.

## Manim for technical diagrams

Use Manim when mathematical/algorithmic geometry is the subject; preserve product identity and narration cues. A short pattern:

```py
from manim import *
class CausalFlow(Scene):
    def construct(self):
        a = RoundedRectangle(width=3, height=1.2).shift(LEFT*2.5)
        b = RoundedRectangle(width=3, height=1.2).shift(RIGHT*2.5)
        edge = Arrow(a.get_right(), b.get_left(), buff=.2)
        self.play(Create(a), run_time=.8)
        self.play(Create(edge), Create(b), run_time=1.0)
```

```sh
manim -qh --fps 60 --resolution 1920,1080 scene.py CausalFlow
```

For narration, replace example durations with differences between actual word cues. Do not add static waits longer than two seconds; keep the explanatory trace advancing while text remains readable. Install Manim only if this mode is useful; it is not a prerequisite for browser films.

## Common failures and fixes

- Live capture runs at variable frame rate: author a deterministic clock and encode constant-rate frames.
- Browser capture is too slow: cache assets, reduce unnecessary filters, mount fewer scenes, profile image encoding and use bounded chunks.
- Frames become black on low-memory Chromium: lower concurrency and use a fresh browser per chunk; inspect the first and last frame before resuming.
- Encoding changes colors: explicitly convert range/matrix, rather than only attaching metadata.
