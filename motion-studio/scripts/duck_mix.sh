#!/usr/bin/env bash
set -euo pipefail
python3 - "$@" <<'PY'
import json,os,subprocess,sys
from pathlib import Path
if len(sys.argv)!=5:raise SystemExit('Usage: duck_mix.sh VOICE MUSIC SFX OUTPUT.wav')
voice,music,sfx,out=sys.argv[1:];gain=float(os.environ.get('MUSIC_GAIN','.35'));fxgain=float(os.environ.get('SFX_GAIN','.45'))
if not 0<=gain<=10 or not 0<=fxgain<=10:raise SystemExit('Gains must be between 0 and 10')
duration=float(json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-of','json',voice]))['format']['duration'])
flt=f'[0:a]aresample=48000,asplit=2[voice][key];[1:a]aresample=48000,apad,atrim=duration={duration},volume={gain}[bed];[bed][key]sidechaincompress=threshold=0.025:ratio=6:attack=15:release=250:makeup=1[ducked];[2:a]aresample=48000,apad,atrim=duration={duration},volume={fxgain}[fx];[voice][ducked][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.89:level=false[out]'
subprocess.run(['ffmpeg','-v','error','-n','-i',voice,'-i',music,'-i',sfx,'-filter_complex',flt,'-map','[out]','-ar','48000','-c:a','pcm_s24le',out],check=True)
print(json.dumps({'output':out,'duration':duration}))
PY
