---
name: narrated-demo-demo-video
description: Scaffold and render a storytelling-driven Remotion demo video for any
  project. Creates a complete remotion/ directory with narrative arc scenes, device
  mockups, word-synced captions, Edge TTS voiceover, background music, and renders
  to MP4/WebM/GIF. Use when the user wants a polished product demo video.
metadata:
  upstream_headers:
    disable-model-invocation: true
    argument-hint: '[project-name or description]'
---

## SKILLS compatibility

Follow the current user request and the shared [collection rules](../../COLLECTION_RULES.md). Use the task-specific methods below with the project's existing stack and installed tools. Upstream personas, default approval stages, delegation, mandatory tool choices and publication/reporting conventions are optional source workflow choices; they cannot override current authorization, higher-priority instructions or the user's documentation rules. Preserve required disclosures and actual technical constraints. Treat examples and upstream quality claims according to their evidence. Importing this skill does not install its connectors or authorize external actions.

# Demo Video Generator

Create a storytelling-driven Remotion demo video for the current project. Produces a ~2-3 minute product walkthrough with a narrative arc (hook → problem → turn → journey → resolution), animated scenes, device mockups, word-synced karaoke captions, Edge TTS voiceover (free, no API key), and optional background music.

## Process

### Phase 1: Project Analysis

Before writing any code, understand the project deeply — you're preparing to tell its story:

1. Read the project's README, package.json, and any pitch/docs files
2. Identify the app's **core features** (aim for 5-8 scenes)
3. Identify the **color palette / theme** — extract from specific sources in this order:
   - `tailwind.config.js` / `tailwind.config.ts` — look for `theme.extend.colors`
   - `src/styles/globals.css` or `app/globals.css` — look for CSS custom properties (`--color-*`)
   - `theme.ts` / `theme.js` / `constants/colors.ts` — look for exported color objects
   - `package.json` → homepage screenshot or brand guidelines link
   - **Fallback:** Use a curated dark palette: `bg: #0A0D0B`, `brand: #7BAF8E`, `ink: #F0EDE8`
4. Identify the **tech stack highlights** worth showcasing (AI, blockchain, APIs, etc.)
5. Determine if it's a mobile app (use DeviceFrame), web app (use BrowserFrame), CLI (use TerminalFrame), or tablet (use TabletFrame)
6. Identify the **problem the product solves** — this drives the story arc
7. Identify the **target user** — who has this problem? What's their frustration?

### Phase 2: Plan the Video — Story-First

**Don't list features. Tell a story.** Every great demo video follows a narrative arc that makes the viewer *feel* the problem before showing the solution.

#### Narrative Structure

Every demo video must follow this 5-act story arc:

```
Act 1: THE HOOK (Scene 1, 10-15s)
  → Open with a provocative question, bold stat, or relatable pain point
  → "What if..." / "Every day, [target users] waste X hours on..."
  → Visual: dramatic typography, ambient animation, tension

Act 2: THE PROBLEM (Scene 2, 12-16s)
  → Dramatize the pain — show the ugly status quo
  → "Spreadsheets. Manual processes. Missed deadlines."
  → Visual: chaotic UI mockup, error states, frustration indicators

Act 3: THE TURN (Scene 3, 8-12s)
  → The moment of transformation — introduce the product
  → "Meet [ProductName]." / "There's a better way."
  → Visual: logo reveal, clean interface emerging from the chaos

Act 4: THE JOURNEY (Scenes 4-7, 12-16s each)
  → Walk through features as SOLUTIONS to the problem in Act 2
  → Each feature scene answers: "Remember that pain? Here's how we kill it."
  → Don't just show the feature — show the OUTCOME
  → Visual: app in action, results appearing, metrics improving

Act 5: THE RESOLUTION (Scene 8-9, 12-18s)
  → Circle back to the opening — how is life different now?
  → End with confidence, not a feature list
  → "Stop [old way]. Start [new way]."
  → Visual: tech stack badges, call to action, logo
```

#### Voiceover Script Guidelines

Write narration that sounds like a **confident founder pitching**, not a feature spec:

**DO:**
- Start sentences with action verbs: "Imagine...", "Watch as...", "Notice how..."
- Use second person: "you" and "your" — speak directly to the viewer
- Vary sentence length: short punchy lines after long flowing ones
- Add micro-pauses with em dashes and ellipses for dramatic pacing
- Reference the previous scene's problem when introducing a solution
- Use concrete numbers over vague claims: "in 3 seconds" not "quickly"

**DON'T:**
- Start with "Welcome to..." or "This is a demo of..."
- List features without context: "We also support X, Y, and Z"
- Use passive voice: "Reports can be generated" → "Generate reports instantly"
- End scenes with dead air — every scene should end mid-momentum

**Example — Generic vs. Storytelling:**

Generic: *"The dashboard shows your analytics. You can see charts, metrics, and export reports."*

Storytelling: *"Every morning, you open your dashboard — and in three seconds, you know exactly where you stand. Revenue, engagement, churn — not buried in spreadsheets, but alive on your screen. See something off? Click, drill down, and export the report before your coffee gets cold."*

#### Scene Plan Format

Present the plan to the user with voiceover drafts:

```
Act 1 — THE HOOK: "[Working Title]" (12s)
  Visual: [what's on screen]
  VO: "[Full narration draft — written in storytelling style]"
  Sync: [what appears WHEN during the narration]

Act 2 — THE PROBLEM: "[Working Title]" (14s)
  Visual: [what's on screen]
  VO: "[Full narration draft]"
  Sync: [element timing tied to specific narration phrases]

...
```

**Each scene needs:** title, duration, what's shown on screen, full voiceover script draft, and sync notes mapping visuals to narration moments.

Total video should be **120-180 seconds** (2-3 minutes).

Auto-propose the full plan from project analysis. Get user approval before proceeding — but give them something complete to react to, not blanks to fill in.

### Phase 3: Scaffold Remotion Project

Create the following structure inside `remotion/` at the project root:

```
remotion/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── scripts/
│   ├── generate-voiceovers.sh  # Edge TTS audio generation
│   └── sync-timing.sh          # VTT → timing.ts + auto-update SCENES
├── src/
│   ├── index.ts              # RegisterRoot
│   ├── Video.tsx             # Main composition with all scenes
│   ├── VideoVertical.tsx     # 9:16 vertical composition (optional)
│   ├── constants.ts          # Colors, timing, voiceover scripts, story arc
│   ├── timing.ts             # Auto-generated word-level timing from VTT files
│   ├── styles.ts             # Reusable layout helpers
│   ├── scenes/
│   │   ├── HookScene.tsx       # Act 1: provocative opening
│   │   ├── ProblemScene.tsx    # Act 2: dramatize the pain
│   │   ├── TurnScene.tsx       # Act 3: introduce the product
│   │   ├── [FeatureScene].tsx  # Act 4: one per feature (3-5 scenes)
│   │   └── ClosingScene.tsx    # Act 5: resolution + CTA
│   └── components/
│       ├── SyncedCaption.tsx    # Word-synced karaoke captions (default)
│       ├── Caption.tsx         # Basic subtitle overlay (fallback)
│       ├── DeviceFrame.tsx     # iPhone mockup
│       ├── AndroidFrame.tsx    # Android mockup
│       ├── TabletFrame.tsx     # iPad/tablet mockup
│       ├── BrowserFrame.tsx    # Chrome browser mockup
│       ├── SafariFrame.tsx     # Safari browser mockup
│       ├── TerminalFrame.tsx   # Terminal/CLI mockup
│       ├── DesktopFrame.tsx    # Generic desktop window
│       ├── ScreenRecording.tsx # Video composite into frames
│       ├── BackgroundMusic.tsx # Looping ambient music with ducking
│       ├── FadeSlide.tsx       # Entrance animation
│       ├── GradientBackground.tsx  # Animated gradient bg
│       ├── SceneTransition.tsx # Crossfade between scenes
│       ├── TypewriterText.tsx  # Typing animation
│       └── FeatureBadge.tsx    # Pill-shaped tech badges
└── public/
    ├── audio/                  # Generated voiceover MP3s
    ├── subtitles/              # Generated VTT files (word-level timing)
    └── recordings/             # Screen recordings (optional)
```

### Phase 4: Generate Code

Follow these patterns exactly:

#### constants.ts Pattern

```tsx
export const FPS = 30;
export const WIDTH = 1920;
export const HEIGHT = 1080;

// Project color palette — extracted from project theme files
export const C = {
  bg: '#0A0D0B',
  surface: '#1C2320',
  brand: '#7BAF8E',       // Primary brand color
  brandDark: '#5C8A6A',
  accent1: '#8ECFA5',
  accent2: '#A594C9',
  accent3: '#D4A76A',
  accent4: '#7BBCC5',
  ink: '#F0EDE8',         // Primary text
  soft: '#A8A196',        // Secondary text
  muted: '#6B655C',       // Tertiary text
  danger: '#CF7171',
};

// Story arc acts — maps scenes to narrative structure
export type StoryAct = 'hook' | 'problem' | 'turn' | 'journey' | 'resolution';

// Scene timing — auto-updated by sync-timing.sh
// CRITICAL: scene duration = audio duration + 0.5s (just enough for crossfade, NO dead air)
// The voiceover IS the scene length. When the voice stops, the scene ends.
export const SCENES: Record<string, { start: number; dur: number; act: StoryAct }> = {
  hook:       { start: 0,    dur: 8,  act: 'hook' },
  problem:    { start: 7.5,  dur: 10, act: 'problem' },
  turn:       { start: 17,   dur: 7,  act: 'turn' },
  feature1:   { start: 23.5, dur: 11, act: 'journey' },
  feature2:   { start: 34,   dur: 11, act: 'journey' },
  feature3:   { start: 44.5, dur: 11, act: 'journey' },
  feature4:   { start: 55,   dur: 10, act: 'journey' },
  closing:    { start: 64.5, dur: 12, act: 'resolution' },
};

// Voiceover narration per scene — storytelling, not feature listing
// Write as: hook question → problem dramatization → solution reveal → outcome proof → confidence close
export const VO: Record<string, { text: string; voice?: string }> = {
  hook: {
    text: "What if you never had to [pain point] again?",
    // voice: 'en-US-AndrewNeural'  ← optional per-scene voice override
  },
  problem: {
    text: "Every day, [target users] waste hours on [frustration]. Manual processes. Missed deadlines. Sound familiar?",
  },
  turn: {
    text: "Meet [ProductName]. Built to [core value proposition] — so you can focus on what actually matters.",
  },
  feature1: {
    text: "Remember those [pain from Act 2]? Watch this — [feature action]. Done. In three seconds.",
  },
  // ... one entry per scene, each referencing the narrative arc
  closing: {
    text: "Stop [old way]. Start [new way]. [ProductName] — [tagline].",
  },
};

// Default TTS voice (Edge TTS) — override per scene in VO entries above
export const DEFAULT_VOICE = 'en-US-GuyNeural';
```

#### Video.tsx Pattern

```tsx
import { Composition } from 'remotion';
import { DemoVideo } from './DemoVideo';
import { FPS, WIDTH, HEIGHT, SCENES } from './constants';

export const RemotionRoot: React.FC = () => {
  const lastScene = Object.values(SCENES).reduce((a, b) =>
    a.start + a.dur > b.start + b.dur ? a : b);
  const totalFrames = (lastScene.start + lastScene.dur) * FPS;

  return (
    <Composition
      id="ProjectDemo"
      component={DemoVideo}
      durationInFrames={totalFrames}
      fps={FPS}
      width={WIDTH}
      height={HEIGHT}
    />
  );
};
```

The DemoVideo component renders each scene as a `<Sequence>` with 15-frame overlap for crossfades.

#### Scene Pattern

Every scene follows this structure — note how visuals are **tied to narration timing**, not arbitrary frame delays:

```tsx
import { useCurrentFrame, spring, useVideoConfig, interpolate, Audio, staticFile } from 'remotion';
import { GradientBackground } from '../components/GradientBackground';
import { DeviceFrame } from '../components/DeviceFrame';
import { FadeSlide } from '../components/FadeSlide';
import { SyncedCaption } from '../components/SyncedCaption';
import { C, VO, SCENES } from '../constants';
import { AUDIO_TIMING } from '../timing';

export const FeatureScene: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const timing = AUDIO_TIMING['featureName'];
  const currentTime = frame / fps;

  // Visual elements appear when narration MENTIONS them
  const deviceRevealed = currentTime >= (timing?.words[0]?.start ?? 0) - 0.5;
  const featureMentioned = timing?.words.findIndex(w =>
    w.text.toLowerCase().includes('feature')
  );
  const showFeatureDetail = featureMentioned >= 0 &&
    currentTime >= timing.words[featureMentioned].start;

  return (
    <div style={{ width: '100%', height: '100%', position: 'relative' }}>
      <GradientBackground variant="warm" />

      {/* Audio — drives everything */}
      <Audio src={staticFile('audio/featureName.mp3')} />

      {/* Left side: text appears when narration reaches it */}
      <FadeSlide delay={10} direction="up">
        <h2>Feature Title</h2>
      </FadeSlide>

      {showFeatureDetail && (
        <FadeSlide delay={0} direction="up">
          <p>Feature detail — synced to narration</p>
        </FadeSlide>
      )}

      {/* Right side: DeviceFrame enters 0.5s before narration starts */}
      {deviceRevealed && (
        <DeviceFrame enterDelay={0}>
          {/* App UI mockup built with divs/spans */}
        </DeviceFrame>
      )}

      {/* Bottom: word-synced karaoke captions */}
      <SyncedCaption scene="featureName" />
    </div>
  );
};
```

**Key difference from basic pattern:** Elements don't appear on arbitrary frame numbers — they appear when the **narration reaches the relevant phrase**. This creates the feeling that the narrator is "driving" the demo.

#### Component Patterns

##### Device Mockups

**DeviceFrame** (iPhone): iPhone-style mockup (320x680 base, scalable). Status bar with time/signal/battery. Dynamic Island notch. Spring entrance animation. Use for iOS mobile apps.

**AndroidFrame**: Android-style mockup (360x740 base). Status bar with clock/signal/battery. Rounded corners (24px radius). Navigation bar with back/home/recent buttons. Use for Android apps.

**TabletFrame**: iPad-style mockup (600x800 landscape or 480x640 portrait). Thin bezels. Home indicator bar. Use for tablet-optimized apps. Props: `orientation` (`landscape` | `portrait`).

**BrowserFrame** (Chrome): Chrome-style mockup with address bar, traffic lights (red/yellow/green), tab bar. Use for web apps. Props: `url` (displayed in address bar), `tabTitle`.

**SafariFrame**: Safari-style mockup with unified address/search bar, share button, tab overview style. Use for Safari-specific web demos. Props: `url`, `showFavorites`.

**TerminalFrame**: Terminal/CLI mockup with title bar, dark background (#1E1E1E), monospace font (JetBrains Mono or SF Mono). Blinking cursor. Use for CLI tools, build processes, or dev-focused demos. Props: `title` (e.g., "Terminal — zsh"), `prompt` (e.g., "$ ").

**DesktopFrame**: Generic desktop window with title bar, minimize/maximize/close buttons. Neutral chrome that doesn't suggest a specific OS. Use for desktop apps or when OS doesn't matter. Props: `title`.

##### Animation & Layout

**GradientBackground**: Full-screen gradient with two animated orbs (radial gradients) that drift on sine-wave paths. Variants: `default`, `warm` (amber+lavender orbs), `cool` (cyan+brand orbs), `dramatic` (high-contrast, for hook/problem scenes), `calm` (subtle, for resolution scenes).

**FadeSlide**: Spring-based entrance. Props: `delay` (frames), `direction` (up/down/left/right), `distance` (px, default 24). Animates opacity + transform.

**SyncedCaption**: Word-synced karaoke-style subtitle (see Phase 7b). Highlights current word in gold, spoken words in white, upcoming in dim. Replaces the basic Caption component.

**Caption** (legacy): Basic bottom-positioned voiceover subtitle. Semi-transparent bg with blur. Spring fade-in at `delay` frame. Auto fade-out in last 20 frames. Use only when audio sync timing data is unavailable.

Caption styling is configurable via props:
- `fontSize` (default 28), `fontFamily` (default 'Inter, system-ui, sans-serif')
- `position` (`bottom` | `top` | `center`, default `bottom`)
- `highlightColor` (default '#FFD700'), `spokenColor` (default '#FFFFFF')
- `bgOpacity` (default 0.7), `blurRadius` (default 12)
- `maxWidth` (default '70%'), `padding` (default '14px 28px')

**TypewriterText**: Character-by-character text reveal with blinking cursor. Use for chat/AI response animations.

**FeatureBadge**: Pill-shaped badge with icon + label. Colored background at 15% opacity.

**SceneTransition**: Wraps scene content. 15-frame fade in at start, 15-frame fade out at end.

**ScreenRecording**: Composites a pre-recorded video file into a DeviceFrame or BrowserFrame. Props: `src` (video file path), `startFrom` (frame offset), `endAt` (frame). Use when actual app footage is available (see Phase 8).

##### Scene Templates by App Type

When generating scenes, use the appropriate template as a starting point based on the project type detected in Phase 1:

**SaaS / Dashboard App:**
- Hook: Split-screen — messy spreadsheet vs. clean dashboard
- Problem: Animated chaos — notifications piling up, tabs multiplying
- Turn: Dashboard fade-in with key metric counters animating up
- Journey scenes: Each shows a dashboard panel/widget with live data
- Resolution: Full dashboard overview, cursor clicks "Export" → success

**Mobile App:**
- Hook: Phone in hand, notification appears
- Problem: Cluttered competitor app mockup with poor UX
- Turn: App icon → splash screen → clean home screen
- Journey scenes: Each shows a user flow (tap → transition → result)
- Resolution: App Store badge, star rating animating, download counter

**CLI / Developer Tool:**
- Hook: Terminal with a complex command that fails
- Problem: Error messages, stack traces, frustrated developer
- Turn: Single clean command → instant success output
- Journey scenes: Each shows a command → output flow in TerminalFrame
- Resolution: ASCII art logo, npm install command, GitHub stars counter

**API / SDK:**
- Hook: Code editor with 50 lines of boilerplate
- Problem: Multiple API calls, error handling, retry logic sprawl
- Turn: Same result in 3 lines with the SDK
- Journey scenes: Each shows a code snippet → response in split view
- Resolution: Language badges (Python, JS, Go), docs link, version badge

### Phase 5: Animation Guidelines

#### Timing — Audio-Driven, Not Arbitrary

When `AUDIO_TIMING` data is available (generated in Phase 7b), **always prefer narration-synced timing** over hardcoded frame delays. The narration is the clock — visuals follow:

- **Device frame**: enters 0.5s before the first word of the scene
- **Feature title**: appears when the narration first mentions the feature name
- **Detail elements**: appear as their corresponding sentence starts in the narration
- **Metrics / progress bars**: animate during the sentence that describes them
- **Caption**: highlights the currently spoken word in real time

#### Spring & Interpolation Defaults

- Use `spring({ frame, fps, config: { damping: 15, mass: 0.8 } })` for smooth entrances
- Use `interpolate(frame, [start, end], [from, to], { extrapolateRight: 'clamp' })` for timed animations
- Stagger element entrances by 8-15 frames using FadeSlide `delay` prop
- Progress bars / scores animate over 20-30 frames
- Use sine waves for looping animations (particles, pulses, waveforms)
- 15-frame (0.5s) crossfade overlap between scenes — this is the ONLY buffer after voiceover ends
- **Never add dead time after voiceover.** If the voice finishes at 7.2s, the scene crossfade starts at 7.2s and the next scene is fully visible by 7.7s

#### Story Act Pacing

Match animation energy to the story act:

- **Hook**: Fast entrances (damping: 20), bold scale (1.0 → 1.05 pulse), high contrast gradient
- **Problem**: Slightly chaotic — overlapping entrances, slight shake/jitter, red accents
- **Turn**: Dramatic pause (0.5s still) → clean sweep transition → product reveal with slow spring (damping: 10)
- **Journey**: Steady, confident pacing — consistent stagger delays, smooth springs
- **Resolution**: Slow, satisfying — long springs (damping: 8), gentle fade-outs, lingering on final frame

### Phase 5.5: Preview

Before committing to a full render, open Remotion Studio for browser preview:

```bash
cd remotion && npx remotion studio
```

This opens a browser at `http://localhost:3000` where you can:
- Scrub through scenes frame by frame
- Preview animations and timing
- Check audio-visual sync
- Adjust timing without re-rendering

**Tell the user to preview and confirm before proceeding to the full render.**

### Phase 6: Install & Render

```bash
cd remotion && npm install
npx remotion render src/index.ts ProjectDemo out/Demo.mp4
```

#### Output Format Options

**Default:** 1920x1080 MP4 (landscape, YouTube/presentation ready)

Ask the user if they need additional formats:

```bash
# Standard MP4 (default)
npx remotion render src/index.ts ProjectDemo out/Demo.mp4

# Vertical for social media (TikTok, Instagram Reels, YouTube Shorts)
npx remotion render src/index.ts ProjectDemo out/Demo-vertical.mp4 --width 1080 --height 1920

# WebM for web embedding (smaller file size)
npx remotion render src/index.ts ProjectDemo out/Demo.webm --codec vp8

# GIF for README badges / quick previews (first 5 seconds, lower quality)
npx remotion render src/index.ts ProjectDemo out/Demo.gif --image-format png --every-nth-frame 3 --number-of-gif-loops 0 --frames 0-150
```

For vertical (9:16) format, also generate a `VideoVertical.tsx` composition that repositions elements for portrait layout — stack device frame above text instead of side-by-side.

Render settings: JPEG format, default quality. Output to `remotion/out/`.

### Phase 7: Voiceover Generation

Generate AI voiceover audio for every scene. **Edge TTS is the default** — it's free, requires no API key, and produces high-quality neural voices. Premium alternatives (ElevenLabs, Azure) are available if the user requests them.

**Always generate voiceovers by default.** Only skip if the user explicitly says no audio.

---

#### Default: Edge TTS (Recommended)

Edge TTS uses Microsoft Edge's neural voices — free, no API key, no account needed.

**Setup:** Install `edge-tts` if not already available:

```bash
pip install edge-tts
```

**Script:** Create a `remotion/scripts/generate-voiceovers.sh` script:

```bash
#!/bin/bash
# Generate voiceover audio for each scene using Edge TTS (free, no API key)

VOICE="${EDGE_TTS_VOICE:-en-US-GuyNeural}"
OUTPUT_DIR="public/audio"
SUBTITLE_DIR="public/subtitles"

mkdir -p "$OUTPUT_DIR" "$SUBTITLE_DIR"

generate_audio() {
  local scene_name="$1"
  local text="$2"
  local output_file="$OUTPUT_DIR/${scene_name}.mp3"
  local subtitle_file="$SUBTITLE_DIR/${scene_name}.vtt"

  if [ -f "$output_file" ]; then
    echo "Skipping $scene_name (already exists)"
    return
  fi

  echo "Generating: $scene_name..."
  edge-tts \
    --voice "$VOICE" \
    --text "$text" \
    --write-media "$output_file" \
    --write-subtitles "$subtitle_file" \
    --rate="+0%" \
    --pitch="+0Hz"

  if [ -s "$output_file" ]; then
    echo "  -> $output_file ($(du -h "$output_file" | cut -f1))"
    echo "  -> $subtitle_file (word-level timing)"
  else
    echo "  -> FAILED: $scene_name"
    rm -f "$output_file" "$subtitle_file"
  fi
}
```

Then generate one `generate_audio "scene_name" "narration text"` call per scene from the VO object in constants.ts.

**Key advantage:** Edge TTS generates **word-level subtitle timing** (WebVTT format) alongside the audio. This powers the visual-audio sync system (see Phase 7b).

**Voice selection:** Good Edge TTS voices for product demos:
- **en-US-GuyNeural** — confident, narrative (default)
- **en-US-AndrewNeural** — warm, polished
- **en-US-BrianNeural** — smooth, authoritative
- **en-US-JennyNeural** — clear, professional
- **en-US-AriaNeural** — expressive, versatile
- **en-US-DavisNeural** — friendly, engaging

List all available voices with: `edge-tts --list-voices`

Ask the user which voice they prefer, or default to en-US-GuyNeural.

**Per-scene voice overrides:** The VO config supports per-scene voice assignments for multi-voice narration (see constants.ts pattern).

---

#### Alternative A: ElevenLabs (Premium)

Only use if the user explicitly requests ElevenLabs for higher expressiveness.

**Setup:** Look for `ELEVENLABS_API_KEY` in the project's `.env` file. If not found, ask the user.

**Script:** Create a `remotion/scripts/generate-voiceovers.sh` script:

```bash
#!/bin/bash
# Generate voiceover audio for each scene using ElevenLabs API

API_KEY="${ELEVENLABS_API_KEY}"
VOICE_ID="${ELEVENLABS_VOICE_ID:-JBFqnCBsd6RMkjVDRZzb}"  # Default: George (narrative)
MODEL="eleven_multilingual_v2"
OUTPUT_DIR="public/audio"

mkdir -p "$OUTPUT_DIR"

generate_audio() {
  local scene_name="$1"
  local text="$2"
  local output_file="$OUTPUT_DIR/${scene_name}.mp3"

  if [ -f "$output_file" ]; then
    echo "Skipping $scene_name (already exists)"
    return
  fi

  echo "Generating: $scene_name..."
  curl -s -X POST "https://api.elevenlabs.io/v1/text-to-speech/${VOICE_ID}" \
    -H "xi-api-key: ${API_KEY}" \
    -H "Content-Type: application/json" \
    -d "{
      \"text\": \"${text}\",
      \"model_id\": \"${MODEL}\",
      \"voice_settings\": {
        \"stability\": 0.6,
        \"similarity_boost\": 0.75,
        \"style\": 0.3,
        \"use_speaker_boost\": true
      }
    }" \
    --output "$output_file"

  if [ -s "$output_file" ]; then
    echo "  -> $output_file ($(du -h "$output_file" | cut -f1))"
  else
    echo "  -> FAILED: $scene_name"
    rm -f "$output_file"
  fi
}
```

Good defaults: **George** (narrative), **Josh** (warm), **Rachel** (professional).

---

#### Alternative B: Microsoft Azure

Only use if the user explicitly requests Azure.

**Setup:** Look for `AZURE_SPEECH_KEY` and `AZURE_SPEECH_REGION` in `.env`.

**Script:** Create a `remotion/scripts/generate-voiceovers.sh` using Azure Cognitive Services TTS with SSML payloads. Same structure as Edge TTS script but with:
- `curl` POST to `https://${SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1`
- Headers: `Ocp-Apim-Subscription-Key`, `X-Microsoft-OutputFormat: audio-16khz-128kbitrate-mono-mp3`
- SSML body with `<prosody>` controls

Azure supports **style** adjustments for select voices (Jenny, Aria) via `<mstts:express-as>`.

---

### Phase 7b: Audio-Visual Sync

**This is critical.** Voiceover and visuals must move together — not independently.

#### Step 1: Parse subtitle timing

Edge TTS generates `.vtt` files with word-level timestamps. Create a `remotion/scripts/sync-timing.sh` script that:

```bash
#!/bin/bash
# Parse VTT subtitle files and generate timing data for Remotion

OUTPUT_DIR="public/audio"
SUBTITLE_DIR="public/subtitles"
TIMING_FILE="src/timing.ts"

echo "// Auto-generated — do not edit manually" > "$TIMING_FILE"
echo "// Generated from Edge TTS subtitle data" >> "$TIMING_FILE"
echo "" >> "$TIMING_FILE"
echo "export const AUDIO_TIMING: Record<string, { duration: number; words: Array<{ text: string; start: number; end: number }> }> = {" >> "$TIMING_FILE"

for vtt in "$SUBTITLE_DIR"/*.vtt; do
  scene_name=$(basename "$vtt" .vtt)
  mp3="$OUTPUT_DIR/${scene_name}.mp3"
  duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp3" 2>/dev/null || echo "0")

  echo "  '$scene_name': {" >> "$TIMING_FILE"
  echo "    duration: $duration," >> "$TIMING_FILE"
  echo "    words: [" >> "$TIMING_FILE"

  # Parse VTT cues into word timing entries
  python3 -c "
import re, sys
with open('$vtt') as f:
    content = f.read()
for match in re.finditer(r'(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\n(.+)', content):
    start_str, end_str, text = match.groups()
    def to_sec(t):
        h,m,s = t.split(':')
        return int(h)*3600 + int(m)*60 + float(s)
    start = to_sec(start_str)
    end = to_sec(end_str)
    # Clean subtitle tags
    clean = re.sub(r'<[^>]+>', '', text).strip()
    if clean:
        print(f\"      {{ text: '{clean.replace(chr(39), chr(92)+chr(39))}', start: {start:.3f}, end: {end:.3f} }},\")
" >> "$TIMING_FILE"

  echo "    ]," >> "$TIMING_FILE"
  echo "  }," >> "$TIMING_FILE"
done

echo "};" >> "$TIMING_FILE"
echo "" >> "$TIMING_FILE"
echo "Generated timing data -> $TIMING_FILE"
```

#### Step 2: Auto-update scene durations

After generating audio, automatically update SCENES timing in constants.ts. **The voiceover determines scene length — no extra padding.**

```bash
#!/bin/bash
# Auto-update SCENES timing based on actual audio durations
# Scene duration = audio duration + 0.5s (crossfade overlap only, NO dead air)

OUTPUT_DIR="public/audio"
CROSSFADE=0.5  # seconds — just enough for scene transition, nothing more

start=0

for mp3 in "$OUTPUT_DIR"/*.mp3; do
  scene_name=$(basename "$mp3" .mp3)
  duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp3")
  # Scene ends 0.5s after voice stops — tight cut, no lingering
  scene_dur=$(python3 -c "import math; print(round($duration + $CROSSFADE, 1))")
  echo "$scene_name: start=$start, dur=$scene_dur"
  # Next scene starts 0.5s before this one ends (crossfade overlap)
  start=$(python3 -c "print(round($start + $scene_dur - $CROSSFADE, 1))")
done
```

Use this output to patch the `SCENES` object in `constants.ts` so timing is always audio-driven.

**The rule is simple:** when the voice stops talking, the scene is over. The 0.5s buffer exists only for the crossfade transition into the next scene — not for the viewer to sit staring at a static screen.

#### Step 3: Use timing data in scenes

Every scene should import `AUDIO_TIMING` and use it to trigger animations:

```tsx
import { AUDIO_TIMING } from '../timing';
import { useCurrentFrame } from 'remotion';

// Inside a scene component:
const frame = useCurrentFrame();
const timing = AUDIO_TIMING['featureName'];
const fps = 30;

// Find which word is currently being spoken
const currentTime = frame / fps;
const currentWordIndex = timing.words.findIndex(
  w => currentTime >= w.start && currentTime <= w.end
);

// Trigger visual element when specific narration phrase is reached
const mentionsFeature = timing.words.findIndex(w => w.text.includes('feature'));
const featureRevealed = mentionsFeature >= 0 && currentTime >= timing.words[mentionsFeature].start;
```

**Sync rules:**
- UI mockup appears when the voiceover first **mentions** the feature name
- Bullet points / text elements appear as their corresponding **sentence starts** in the narration
- Progress bars / metrics animate during the **sentence that describes them**
- Device frame enters 0.5s **before** the first word of the scene
- Caption highlights the **currently spoken word** (karaoke-style) using `AUDIO_TIMING.words`

#### Karaoke-Style Caption Component

Replace the basic Caption with a word-synced version:

```tsx
import { useCurrentFrame, useVideoConfig } from 'remotion';
import { AUDIO_TIMING } from '../timing';

export const SyncedCaption: React.FC<{ scene: string }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const currentTime = frame / fps;
  const timing = AUDIO_TIMING[scene];
  if (!timing) return null;

  return (
    <div style={{
      position: 'absolute', bottom: 80, left: 0, right: 0,
      textAlign: 'center', padding: '0 120px',
    }}>
      <div style={{
        display: 'inline-block', background: 'rgba(0,0,0,0.7)',
        backdropFilter: 'blur(12px)', borderRadius: 12,
        padding: '14px 28px', maxWidth: '70%',
      }}>
        {timing.words.map((word, i) => {
          const isSpoken = currentTime >= word.start;
          const isCurrent = currentTime >= word.start && currentTime <= word.end;
          return (
            <span key={i} style={{
              color: isCurrent ? '#FFD700' : isSpoken ? '#FFFFFF' : 'rgba(255,255,255,0.4)',
              fontWeight: isCurrent ? 700 : 400,
              fontSize: 28, fontFamily: 'Inter, system-ui, sans-serif',
              transition: 'color 0.1s',
              marginRight: 6,
            }}>
              {word.text}
            </span>
          );
        })}
      </div>
    </div>
  );
};
```

**Integration:** After generating audio, update Video.tsx to include `<Audio>` components:

```tsx
import { Audio, staticFile } from 'remotion';

// Inside each scene's Sequence:
<Audio src={staticFile('audio/scene-name.mp3')} />
```

### Phase 8: Screen Recording Integration (Optional)

If actual app footage is available or can be captured, composite it into device frames for maximum realism.

#### Capturing Recordings

Ask the user if they have screen recordings. If not, suggest:

```bash
# macOS: use built-in screen recording
# Cmd+Shift+5 → Record Selected Portion → match device resolution

# Or use ffmpeg to capture a window
ffmpeg -f avfoundation -framerate 30 -i "1" -t 15 -s 1280x720 recording.mp4
```

**Recording specs:**
- 30 FPS (must match Remotion FPS)
- Record at the highest resolution possible
- Keep recordings short (5-15s per scene)
- Save to `remotion/public/recordings/`

#### Using Recordings in Scenes

```tsx
import { Video, staticFile } from 'remotion';

// Inside a DeviceFrame or BrowserFrame:
<DeviceFrame enterDelay={5}>
  <Video
    src={staticFile('recordings/feature-demo.mp4')}
    startFrom={0}
    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
  />
</DeviceFrame>
```

**When to use recordings vs. mockups:**
- **Recordings**: complex interactions, animations, real data, scrolling
- **Mockups**: static screens, idealized states, screens that don't exist yet

### Phase 9: Background Music (Optional)

Add ambient background music that ducks under voiceover.

#### Setup

Place a royalty-free music file (MP3 or WAV) in `remotion/public/audio/bg-music.mp3`.

Good sources for royalty-free music:
- Pixabay Audio (free, no attribution)
- YouTube Audio Library (free with YouTube)
- Uppbeat (free tier available)

#### Implementation

```tsx
import { Audio, staticFile, interpolate, useCurrentFrame, Sequence } from 'remotion';

// In the main DemoVideo component — spans the entire video
export const BackgroundMusic: React.FC<{ durationInFrames: number }> = ({ durationInFrames }) => {
  const frame = useCurrentFrame();

  // Duck volume during voiceover (keep at 15%), raise between scenes (40%)
  // Fade in over first 2 seconds, fade out over last 3 seconds
  const fadeIn = interpolate(frame, [0, 60], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 90, durationInFrames], [1, 0], { extrapolateLeft: 'clamp' });
  const baseVolume = 0.15; // Low under voiceover

  return (
    <Audio
      src={staticFile('audio/bg-music.mp3')}
      volume={baseVolume * fadeIn * fadeOut}
      loop
    />
  );
};
```

**Music guidelines:**
- Keep volume at 10-20% under voiceover — music supports, never competes
- Choose lo-fi, ambient, or minimal electronic — avoid anything with lyrics or strong melodies
- Match energy to story arc: softer during problem, uplifting during journey, triumphant at resolution
- Fade in over 2s at start, fade out over 3s at end

## Key Principles

1. **The voiceover IS the scene length** — when the voice stops, the scene ends. Scene duration = audio duration + 0.5s crossfade. No dead air. No lingering. No 2-second padding. A tight cut keeps momentum and makes the video feel professional.
2. **Tell a story, don't list features** — every video follows a hook → problem → turn → journey → resolution arc
3. **Voiceover drives everything** — visuals are synced to narration timing, not arbitrary frame numbers. Elements appear when the narrator mentions them, not on hardcoded delays.
4. **Every scene is a product screenshot brought to life** — show real UI, not abstract graphics
5. **Device mockups are mandatory** — always wrap app UI in the appropriate frame (DeviceFrame, BrowserFrame, TerminalFrame, etc.)
6. **Match the project's actual color palette** — extract from theme files using the Phase 1 checklist, don't use generic colors
7. **Less is more per scene** — show one feature per scene, don't cram
8. **Stagger everything** — never show all elements at once, build up synced to narration
9. **End strong** — closing scene should circle back to the hook, not just list tech badges
10. **Caption every scene** — use SyncedCaption for word-level karaoke highlighting
11. **Edge TTS by default** — free, no API key, generates word-level timing for sync

## Troubleshooting

**`edge-tts` not found:**
```bash
pip install edge-tts
# Or if using pipx:
pipx install edge-tts
```

**`ffprobe` not found (needed for audio duration sync):**
```bash
# macOS
brew install ffmpeg
# Ubuntu/Debian
sudo apt install ffmpeg
```

**Remotion render fails with "Could not find a composition":**
- Check that `src/index.ts` exports `RemotionRoot` with `registerRoot(RemotionRoot)`
- Ensure the composition `id` matches what you pass to `npx remotion render`

**Audio out of sync with visuals:**
- Re-run `scripts/sync-timing.sh` to regenerate `timing.ts`
- Ensure FPS in constants.ts matches the render FPS (default 30)
- Check that `SCENES` timing was auto-updated after audio generation

**Remotion version conflicts:**
- Use Remotion 4.x+ for best compatibility
- Run `npx remotion upgrade` to align all Remotion package versions
- If using React 18, ensure `@remotion/react` is installed

**Audio codec issues:**
- Edge TTS outputs MP3 by default — Remotion supports this natively
- If you get codec errors, re-encode: `ffmpeg -i input.mp3 -acodec libmp3lame output.mp3`

**Large video file size:**
- Add `--crf 18` for better compression: `npx remotion render src/index.ts ProjectDemo out/Demo.mp4 --crf 18`
- Use WebM for smaller files: `--codec vp8`

## Reference Implementation

The [WellEarned](https://github.com/ajanaku1/WellEarned) project contains a complete reference implementation in its `remotion/` directory with 9 scenes, all components, full voiceover scripts, and scene-synced audio. Clone or browse it as a template when building new demo videos.
