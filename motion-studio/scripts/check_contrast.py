#!/usr/bin/env python3
"""Check authored RGB colors or explicit pixel pairs; never infer a whole-frame WCAG pass."""
import argparse,json,sys
from pathlib import Path

def rgb(value):
 value=value.lstrip('#')
 if len(value)==3:value=''.join(c*2 for c in value)
 if len(value)!=6:raise ValueError('Use #RGB or #RRGGBB')
 return tuple(int(value[i:i+2],16) for i in (0,2,4))
def luminance(color):
 v=[c/255 for c in color];v=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in v]
 return sum(a*b for a,b in zip(v,[.2126,.7152,.0722]))
def contrast(a,b):
 a,b=sorted([luminance(a),luminance(b)],reverse=True);return (a+.05)/(b+.05)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--foreground');p.add_argument('--background');p.add_argument('--large',action='store_true');p.add_argument('--frame',type=Path);p.add_argument('--pairs',type=Path);a=p.parse_args();rows=[]
 if a.frame:
  if not a.pairs:p.error('--frame requires --pairs')
  from PIL import Image
  image=Image.open(a.frame).convert('RGB')
  for pair in json.loads(a.pairs.read_text()):
   points=[tuple(pair[k]) for k in ['foreground','background']]
   if any(len(q)!=2 or not(0<=q[0]<image.width and 0<=q[1]<image.height) for q in points):p.error('Sample lies outside frame')
   ratio=contrast(*(image.getpixel(q) for q in points));limit=3 if pair.get('large',False) else 4.5
   rows.append({'label':pair.get('label','sample'),'ratio':round(ratio,3),'minimum':limit,'passed':ratio>=limit})
 elif a.foreground and a.background:
  ratio=contrast(rgb(a.foreground),rgb(a.background));limit=3 if a.large else 4.5
  rows.append({'label':'authored colors','ratio':round(ratio,3),'minimum':limit,'passed':ratio>=limit})
 else:p.error('Supply --foreground/--background or --frame/--pairs')
 if not rows:p.error('At least one sample is required')
 print(json.dumps({'checks':rows,'scope':'Only specified colors or pixels, not a whole-frame accessibility audit.'},indent=2));return 0 if all(r['passed'] for r in rows) else 1
if __name__=='__main__':sys.exit(main())
