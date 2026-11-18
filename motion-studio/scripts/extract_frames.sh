#!/usr/bin/env bash
set -euo pipefail
python3 - "$@" <<'PY'
import json,subprocess,sys
from pathlib import Path
if len(sys.argv) not in (4,5):raise SystemExit('Usage: extract_frames.sh VIDEO TIMELINE_JSON OUT_DIR [FPS]')
video,timing,out=map(Path,sys.argv[1:4]);fps=float(sys.argv[4]) if len(sys.argv)==5 else 60
if fps<=0:raise SystemExit('FPS must be positive')
duration=float(json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-of','json',str(video)]))['format']['duration'])
data=json.loads(timing.read_text());boundaries=data if isinstance(data,list) else [v for s in data['scenes'] for v in (s['start'],s['end'])]
times=sorted({round(max(0,min(duration-1/fps,float(b)+offset)),6) for b in boundaries for offset in (-1/fps,0,1/fps)})
out.mkdir(parents=True,exist_ok=True)
for i,t in enumerate(times):
 path=out/f'{i:04}-{t:.3f}.png'
 if path.exists():raise SystemExit(f'Refusing to overwrite {path}')
 # Seek a tiny fraction of a frame early to avoid rounding beyond the final PTS.
 seek=f'{max(0,t-1/(fps*1000)):.9f}'
 subprocess.run(['ffmpeg','-v','error','-ss',seek,'-i',str(video),'-frames:v','1',str(path)],check=True)
 if not path.exists() or path.stat().st_size==0:raise SystemExit(f'No decoded frame at {t:.6f}s')
print(json.dumps({'frames':len(times),'times':times}))
PY
