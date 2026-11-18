#!/usr/bin/env python3
"""Zero-spend speech wrapper; provider alignment or explicitly identified local ASR words."""
import argparse,base64,difflib,json,os,re,subprocess,sys,urllib.error,urllib.request,wave
from pathlib import Path

def clean(s):return re.sub(r'[^\w]', '', s.lower(),flags=re.UNICODE)
def srt(words):
 def stamp(t):
  ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
 cues=[];group=[]
 for w in words:
  if group and (len(group)>=7 or len(' '.join(x['word'] for x in group))+len(w['word'])>52 or w['start']-group[-1]['end']>.6):cues.append(group);group=[]
  group.append(w)
  if re.search(r'[.!?]$',w['word']):cues.append(group);group=[]
 if group:cues.append(group)
 return '\n\n'.join(f'{i+1}\n{stamp(c[0]["start"])} --> {stamp(min(c[-1]["end"]+.18,cues[i+1][0]["start"] if i+1<len(cues) else float("inf")))}\n'+ ' '.join(w['word'] for w in c) for i,c in enumerate(cues))+'\n'
def char_words(a):
 text=''.join(a['characters']);starts=a['character_start_times_seconds'];ends=a['character_end_times_seconds']
 if not(len(text)==len(starts)==len(ends)):raise ValueError('Invalid provider alignment lengths')
 return [{'word':m.group(),'start':starts[m.start()],'end':ends[m.end()-1]} for m in re.finditer(r'\S+',text)]
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--text',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
 p.add_argument('--backend',choices=['auto','piper','coqui','elevenlabs','openai'],default='auto')
 p.add_argument('--model');p.add_argument('--voice');p.add_argument('--asr-model',default='tiny.en');p.add_argument('--length-scale',type=float,default=1.08)
 p.add_argument('--tempo',type=float,default=.77,help='Pitch-preserving pace for new local speech; existing recordings are unchanged')
 p.add_argument('--align-audio',type=Path,help='Align an existing recording without synthesizing or calling a speech API')
 a=p.parse_args();text=a.text.read_text().strip()
 if not text:p.error('Empty narration')
 if a.out.exists():p.error('Output exists; reuse it instead of generating twice')
 if a.length_scale<=0:p.error('Length scale must be positive')
 if not .5<=a.tempo<=2:p.error('Tempo must be between 0.5 and 2')
 backend=a.backend
 if a.align_audio:
  if not a.align_audio.is_file():p.error('--align-audio must name an existing recording')
  backend='existing'
 elif backend=='auto':backend='elevenlabs' if os.environ.get('ELEVENLABS_API_KEY') else 'piper'
 if backend=='openai':p.error('OpenAI TTS has no verified zero-cost entitlement here; use Piper/Coqui or import existing audio')
 words=None;provenance='local ASR; review transcript and pronunciation'
 if backend=='elevenlabs':
  key=os.environ.get('ELEVENLABS_API_KEY')
  if not key:p.error('ELEVENLABS_API_KEY is absent')
  def request(endpoint,payload=None):
   req=urllib.request.Request('https://api.elevenlabs.io'+endpoint,data=None if payload is None else json.dumps(payload).encode(),headers={'xi-api-key':key,'Content-Type':'application/json'})
   try:
    with urllib.request.urlopen(req,timeout=180) as r:return json.load(r)
   except urllib.error.HTTPError as e:raise RuntimeError(f'ElevenLabs HTTP {e.code}; no automatic retry') from None
  try:sub=request('/v1/user/subscription')
  except (urllib.error.URLError,RuntimeError,TimeoutError):
   if a.backend!='auto':raise
   print('Cannot establish free provider allowance; using local speech.',file=sys.stderr)
   sub={}
  remaining=sub.get('character_limit',0)-sub.get('character_count',0)
  free=sub.get('tier')=='free' and sub.get('can_extend_character_limit',False) is False
  if not free or remaining<len(text):
   if a.backend=='auto':backend='piper'
   else:p.error('A free tier, disabled overage and sufficient included characters are required')
  else:
   if not a.voice:p.error('--voice is required for ElevenLabs')
   a.out.mkdir(parents=True)
   result=request('/v1/text-to-speech/'+a.voice+'/with-timestamps?output_format=mp3_44100_128',{'text':text,'model_id':'eleven_multilingual_v2','voice_settings':{'stability':.58,'similarity_boost':.75,'style':.12,'speed':.98}})
   (a.out/'source.mp3').write_bytes(base64.b64decode(result['audio_base64']))
   alignment=result.get('alignment') or result.get('normalized_alignment')
   (a.out/'provider-alignment.json').write_text(json.dumps(alignment))
   words=char_words(alignment);provenance='ElevenLabs character alignment, converted to word spans'
   subprocess.run(['ffmpeg','-v','error','-i',str(a.out/'source.mp3'),'-ar','48000',str(a.out/'narration.wav')],check=True)
 if backend in ['piper','coqui']:
  if not a.model:p.error('Supply a licensed local Piper .onnx model, or a Coqui model identifier')
  a.out.mkdir(parents=True)
  if backend=='piper':
   from piper import PiperVoice,SynthesisConfig
   voice=PiperVoice.load(a.model)
   with wave.open(str(a.out/'narration.wav'),'wb') as wav:
    voice.synthesize_wav(text,wav,syn_config=SynthesisConfig(length_scale=a.length_scale))
  else:
   from TTS.api import TTS
   TTS(model_name=a.model,progress_bar=False).to('cpu').tts_to_file(text=text,file_path=str(a.out/'narration.wav'))
  if a.tempo!=1:
   (a.out/'narration.wav').rename(a.out/'source-local.wav')
   subprocess.run(['ffmpeg','-v','error','-n','-i',str(a.out/'source-local.wav'),'-af',f'atempo={a.tempo}','-ar','48000',str(a.out/'narration.wav')],check=True)
 if backend=='existing':
  a.out.mkdir(parents=True)
  subprocess.run(['ffmpeg','-v','error','-n','-i',str(a.align_audio),'-ar','48000',str(a.out/'narration.wav')],check=True)
 if backend in ['piper','coqui','existing']:
  from faster_whisper import WhisperModel
  model=WhisperModel(a.asr_model,device='cpu',compute_type='int8',cpu_threads=2)
  segments,_=model.transcribe(str(a.out/'narration.wav'),word_timestamps=True,beam_size=5,condition_on_previous_text=False,vad_filter=True,vad_parameters={'min_silence_duration_ms':200},hallucination_silence_threshold=.5)
  words=[{'word':w.word.strip(),'start':w.start,'end':w.end} for s in segments for w in (s.words or [])]
 if not words:raise RuntimeError('No aligned words returned; narration is preserved for recovery')
 (a.out/'words.raw.json').write_text(json.dumps({'words':words,'provenance':provenance},indent=2))
 if any(w['end']<=w['start'] or w['start']<0 for w in words) or any(b['start']<a['start'] for a,b in zip(words,words[1:])):raise RuntimeError('Non-monotonic or zero-length word alignment')
 expected=[clean(w) for w in text.split() if clean(w)];heard=[clean(w['word']) for w in words if clean(w['word'])]
 match=expected==heard
 (a.out/'words.json').write_text(json.dumps({'words':words,'provenance':provenance,'transcriptMatchesInput':match,'text':text},indent=2))
 (a.out/'captions.srt').write_text(srt(words))
 print(json.dumps({'backend':backend,'audio':str(a.out/'narration.wav'),'words':len(words),'transcriptMatchesInput':match}))
 if not match:
  print('Transcript differs from the supplied text; review before using these cues. Audio was preserved; do not regenerate blindly.',file=sys.stderr);return 2
 return 0
if __name__=='__main__':
 try:sys.exit(main())
 except Exception as e:print(type(e).__name__+': '+str(e),file=sys.stderr);sys.exit(1)
