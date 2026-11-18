# demo-video

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill that scaffolds and renders storytelling-driven [Remotion](https://remotion.dev) demo videos for any project. Free voiceover with Edge TTS, word-synced captions, and tight audio-visual timing out of the box.

## What it does

When you run `/demo-video`, Claude will:

1. **Analyze your project** -- reads README, package.json, theme files, and docs to understand features, colors, tech stack, and the problem the product solves
2. **Write a story-driven video plan** -- proposes a 5-act narrative arc (hook, problem, turn, journey, resolution) with full voiceover script drafts and visual sync notes
3. **Scaffold a Remotion project** -- creates a complete `remotion/` directory with scenes, components, animations, timing data, and sync scripts
4. **Generate code** -- builds every scene with device mockups, gradient backgrounds, spring animations, and narration-synced visuals
5. **Generate voiceovers** -- runs Edge TTS (free, no API key) to produce narration with word-level subtitle timing
6. **Sync audio to visuals** -- parses subtitle timing into `timing.ts` so elements appear when the narrator mentions them
7. **Render to MP4** -- outputs 1920x1080 video (plus optional WebM, GIF, or vertical 9:16)

## Install

```bash
npx claude-code skills add ajanaku1/demo-video-skill
```

## Usage

Inside any project directory in Claude Code:

```
/demo-video
```

Or with a description:

```
/demo-video my-awesome-app
```

## Storytelling approach

Every demo video follows a narrative arc instead of listing features:

| Act | Purpose | Example |
|-----|---------|---------|
| Hook | Provocative question or bold stat | "What if you never had to..." |
| Problem | Dramatize the pain | "Spreadsheets. Manual processes." |
| Turn | Introduce the product | "Meet [Product]." |
| Journey | Features as solutions | "Remember that pain? Watch this." |
| Resolution | Circle back, end with confidence | "Stop [old way]. Start [new way]." |

Voiceover scripts are written as storytelling, not feature specs. Visuals are synced to narration timing so elements appear when the narrator mentions them.

## Components included

The skill generates these reusable Remotion components:

**Device Mockups**
- **DeviceFrame** -- iPhone mockup with Dynamic Island
- **AndroidFrame** -- Android phone mockup
- **TabletFrame** -- iPad/tablet mockup (landscape or portrait)
- **BrowserFrame** -- Chrome browser mockup
- **SafariFrame** -- Safari browser mockup
- **TerminalFrame** -- CLI/terminal mockup with blinking cursor
- **DesktopFrame** -- Generic desktop window

**Animation and Layout**
- **GradientBackground** -- Animated gradient with floating orbs (5 variants)
- **FadeSlide** -- Spring-based entrance animations
- **SyncedCaption** -- Word-synced karaoke captions (highlights current word)
- **Caption** -- Basic subtitle overlay (fallback)
- **TypewriterText** -- Character-by-character text reveal
- **FeatureBadge** -- Pill-shaped tech stack badges
- **SceneTransition** -- Crossfade wrappers between scenes
- **BackgroundMusic** -- Looping ambient music with volume ducking
- **ScreenRecording** -- Composite real recordings into device frames

## Scene templates

Pre-built scene patterns are available for common project types:

- **SaaS/Dashboard** -- split-screen chaos vs. clean UI, dashboard panels, export flows
- **Mobile App** -- notification reveals, user flow walkthroughs, App Store badges
- **CLI/Developer Tool** -- terminal commands, error-to-success flows, ASCII art
- **API/SDK** -- code snippets, boilerplate reduction, language badges

## Audio-visual sync

Edge TTS generates word-level subtitle timing (WebVTT). The skill parses this into `timing.ts` so:

- UI mockups appear when the voiceover mentions them
- Text elements appear as their corresponding sentence starts
- Captions highlight the currently spoken word (karaoke-style)
- Scene duration equals audio duration + 0.5s crossfade (no dead air)

## TTS providers

| Provider | Cost | API Key | Word Timing |
|----------|------|---------|-------------|
| Edge TTS (default) | Free | None needed | Yes (VTT) |
| ElevenLabs | Paid | Required | No |
| Microsoft Azure | Paid | Required | No |

## Requirements

- Node.js 18+
- Python 3 with `edge-tts` (`pip install edge-tts`)
- `ffmpeg` and `ffprobe` installed locally

## Reference implementation

The [WellEarned](https://github.com/ajanaku1/WellEarned) project contains a complete reference implementation in its `remotion/` directory with 9 scenes, all components, full voiceover scripts, and scene-synced audio.

## License

MIT
