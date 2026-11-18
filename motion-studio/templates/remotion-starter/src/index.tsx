import React from 'react';
import {registerRoot,Composition,AbsoluteFill,useCurrentFrame,useVideoConfig} from 'remotion';
import {Caption,DiagramDraw,TypingCode,Reveal,Word} from './components';
export type DemoProps={words:Word[];code:string};
export function Demo({words,code}:DemoProps){
 const frame=useCurrentFrame(),{fps}=useVideoConfig(),t=frame/fps;
 const cue=(term:string)=>{const w=words.find(w=>w.word.toLowerCase().replace(/\W/g,'')===term);if(!w)throw new Error('Missing word cue: '+term);return Math.round(w.start*fps)};
 // Supply actual speech words and real project code; the scaffold does not invent evidence.
 const start=words.length?cue('request'):0;
 return <AbsoluteFill style={{background:'#081118',color:'#F0F5F7',fontFamily:'sans-serif',padding:96}}>
  <Reveal frame={frame} fps={fps} at={start}><h1 style={{fontSize:104,margin:0,letterSpacing:-4}}>Follow the request.</h1></Reveal>
  <div style={{marginTop:64}}><DiagramDraw progress={(t-start/fps)/3}/></div>
  <div style={{marginTop:64,padding:40,background:'#13232E',borderRadius:16}}><TypingCode code={code} frame={frame} start={start+fps} end={start+fps*3}/></div>
  <Caption words={words} time={t}/>
 </AbsoluteFill>;
}
registerRoot(()=> <Composition id="Demo" component={Demo} durationInFrames={3600} fps={60} width={1920} height={1080} defaultProps={{words:[],code:'// Supply captured project code and aligned narration.'}}/>);
