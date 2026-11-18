# Motion Studio Speech and Sound

Use a warm, authoritative voice with conversational sentences under 150 words per minute. The default is zero spend. Existing authorized recordings may be reused. A key in the environment does not establish free usage: OpenAI TTS is paid absent a separately established entitlement, so the zero-spend wrapper refuses it. ElevenLabs is permitted only if the subscription reports a free tier, overage is disabled and included quota covers the complete request. Otherwise choose Piper/Coqui locally.

## Local setup and unified speech

```sh
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python piper-tts faster-whisper pillow
# Download a licensed Piper .onnx model and matching .onnx.json into work/models/.
.venv/bin/python skill/scripts/tts.py --text narration.txt --out work/speech \
  --backend piper --model work/models/en_US-lessac-medium.onnx
```

Check the voice model card and redistribution license. Keep models and engine dependencies outside the skill package. The wrapper generates a WAV, `words.json`, and `.srt`. Piper/Coqui speech is aligned with local faster-whisper (`tiny.en` by default; pass a downloaded model directory with `--asr-model`, or a larger model when recognition needs it); this is ASR-derived alignment and requires checking against the intended text. A mismatch fails the normal run while preserving its output for correction. If alignment was interrupted, use `--align-audio` with the preserved WAV and a new output folder; never regenerate successful speech just to retry alignment. Do not call duration-weighted guessed word times “word alignment.”

```sh
# Recover alignment from a preserved take, using a downloaded local ASR model:
python skill/scripts/tts.py --text narration.txt --out work/aligned \
  --align-audio work/speech/narration.wav --asr-model work/models/whisper-tiny.en

python skill/scripts/tts.py --text narration.txt --out work/speech \
  --backend elevenlabs --voice VOICE_ID
```

Never put a key in a command argument. `ELEVENLABS_API_KEY` is read only from the environment. Character timestamps are converted into exact word spans. The wrapper refuses duplicate generation into an existing output folder. Resume from the generated files, not a second provider call.

Reuse already recorded narration with its saved alignment when it fits the revised brief. Trim whole phrases with small lead/tail margins, rebase timestamps to the concatenated audio, and inspect edit seams. A shorter film needs an edited argument, not simply accelerated speech. New local speech uses Piper length scale 1.08 and a pitch-preserving tempo of 0.77. Adjust `--tempo` after measuring the finished take to remain below 150 words per minute; `--align-audio` preserves its supplied recording exactly apart from sample-rate conversion. The wrapper preserves raw alignment evidence before rejecting invalid spans.

## Mixing and mastering

```sh
bash skill/scripts/duck_mix.sh voice.wav music.wav effects.wav work/mix.wav
bash skill/scripts/loudnorm.sh work/mix.wav work/master.wav -14
ffmpeg -i visual.mp4 -i work/master.wav -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k -movflags +faststart -shortest out/demo.mp4
ffmpeg -i out/demo.mp4 -af loudnorm=I=-14:TP=-1:print_format=json -f null -
```

The ducking helper uses the voice envelope to compress the music, with 15ms attack and 250ms release. Adjust the bed's input gain first. Start with music roughly 16–22 LU below speech; measure a representative voice-free bed and listen at ordinary playback volume. An inaudible −46 LUFS bed underneath −14 LUFS narration is not a finished sound design. Do not blindly normalize sparse SFX to a music loudness target.

Author cues with the same word clock: a paper sweep accompanies separation; a small click marks a committed state; a whoosh follows a camera handoff. Give transients attack/release envelopes to prevent clicks. Keep speech in the foreground and avoid an impact on every word. Use stereo width for supporting sound, not phase-inverted narration.

The loudness helper uses measured two-pass `loudnorm`, leaves true-peak headroom at −1.5dBTP before AAC, and preserves a 48kHz master. Re-measure the encoded file: AAC can increase peaks. Target −14 LUFS ±1 and encoded peak ≤−1dBTP. Listen for clipping, truncated words, noise, mispronunciation and over-ducking; signal measurements cannot establish those subjective properties.

## Common failures and fixes

- No key or exhausted quota: use local TTS; do not start a billed request or claim free credits exist.
- Offline ASR repeats words over silence: disable transcript prompting and previous-text conditioning, enable VAD, and reject zero-length spans. Do not strip unexpected words merely to obtain a match.
- Offline ASR changes a product name: compare the recording with the script; use provider alignment or a proper forced aligner, or correct only a reviewed token mapping.
- Speech sounds detached: remove unnecessary pauses, put the product's strongest result early, and align motion to nouns and verbs.
- Music is technically present but inaudible: measure it separately, raise its base gain, then re-check speech intelligibility and peaks.
- Mix is 3dB louder than expected: duplicate mono into stereo before the final loudness measurement, not after normalization.
- Audio format rejected: inspect permitted output formats; do not retry paid calls blindly or regenerate a successful take.
