# Audio and Sonic Design Specialist

## When it helps
Games, creative tools, music/media products, accessibility cues, confirmation feedback, ambient brand moments. Skip when it would annoy or when users are likely in quiet/shared settings without control.

## Principles
- **Never autoplay with sound.** Browsers block it anyway; start after a user gesture; provide mute and volume; remember the choice.
- Sound communicates state (success, error, progress, notification) and must have a visual/haptic equivalent; never the only signal.
- Short, soft, consistent palette; avoid ear fatigue; mix quiet and dynamic range appropriately; respect system volume and silent modes.

## Web Audio engineering
`AudioContext` created/resumed on user gesture; decode assets to buffers; sprite sheets for many short sounds; gain nodes for categories (UI, music, ambience); compressors/limiters to prevent clipping; scheduling with `audioContext.currentTime`, not `setTimeout`; spatial audio via `PannerNode` when meaningful; `AudioWorklet` for custom DSP; `AnalyserNode` for audio-reactive visuals; streaming for long music; preload strategy; formats (Opus/AAC with fallback); license tracking for samples; subtitles/captions/transcripts for speech.

## Speech and voice
Text-to-speech/speech recognition via platform APIs or services with consent and clear indicators; handle noise, accents, latency; provide text alternatives; store recordings only with permission and retention rules (`voice-and-conversational-experiences.md`).

## Accessibility
Captions for all meaningful audio, adjustable volume per category, no sudden loud sounds, visual alternatives to audio cues, `prefers-reduced-motion` and user setting for sound effects separately.

## Failure modes
Autoplay attempts, sound as sole feedback, clipped audio, memory bloat from uncompressed buffers, licensing ambiguity.
