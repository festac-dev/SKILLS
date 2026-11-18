#!/usr/bin/env bash
set -euo pipefail
python3 - "$@" <<'PY'
import json,re,subprocess,sys,tempfile
from pathlib import Path
if len(sys.argv) not in (3,4):raise SystemExit('Usage: loudnorm.sh INPUT OUTPUT.wav [LUFS]')
source,target=map(Path,sys.argv[1:3]);level=float(sys.argv[3]) if len(sys.argv)==4 else -14
if not -70<=level<=-5:raise SystemExit('LUFS must be between -70 and -5')
if target.exists():raise SystemExit('Output already exists')
first=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',str(source),'-vn','-af',f'loudnorm=I={level}:TP=-1.5:LRA=9:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
blocks=re.findall(r'\{\s*"input_i"[\s\S]*?\}',first.stderr)
if not blocks:raise SystemExit('No loudness measurement returned')
d=json.loads(blocks[-1]);keys=['input_i','input_tp','input_lra','input_thresh','target_offset']
if any(str(d[k]).lower() in ['-inf','inf','nan'] for k in keys):raise SystemExit('Cannot normalize silent or invalid audio')
flt=f'loudnorm=I={level}:TP=-1.5:LRA=9:measured_I={d["input_i"]}:measured_TP={d["input_tp"]}:measured_LRA={d["input_lra"]}:measured_thresh={d["input_thresh"]}:offset={d["target_offset"]}:linear=true'
target.parent.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(dir=target.parent,prefix='.loudnorm-') as temp:
 pending=Path(temp)/target.name
 codec=['-c:a','pcm_s24le'] if target.suffix.lower()=='.wav' else ['-c:a','aac','-b:a','192k']
 subprocess.run(['ffmpeg','-v','error','-i',str(source),'-vn','-af',flt,'-ar','48000',*codec,str(pending)],check=True)
 pending.replace(target)
print(json.dumps({'output':str(target),'target_lufs':level,'premaster_peak':-1.5,'measured_input':d}))
PY
