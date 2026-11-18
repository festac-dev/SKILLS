import React from 'react';
import {spring} from 'remotion';
import {motion} from '../../motion-tokens';
import Prism from 'prismjs';
import 'prismjs/components/prism-typescript';
import 'prismjs/components/prism-haskell';
export type Word={word:string;start:number;end:number};
export const clamp=(p:number)=>Math.min(1,Math.max(0,p));
export function Reveal({frame,fps,at,children}:{frame:number;fps:number;at:number;children:React.ReactNode}){
 const p=frame<at?0:spring({frame:frame-at,fps,config:motion.spring.hero});
 return <div style={{opacity:clamp(p),transform:`translateY(${(1-p)*48}px)`}}>{children}</div>;
}
export function TypingCode({code,frame,start,end,language='typescript',theme='dark'}:{code:string;frame:number;start:number;end:number;language?:string;theme?:'light'|'dark'}){
 let remaining=Math.floor(code.length*clamp((frame-start)/Math.max(1,end-start)));
 const colors:Record<string,string>=theme==='light'?{keyword:'#31588A',string:'#276345',number:'#805224',function:'#725727',operator:'#34645F',comment:'#51695B'}:{keyword:'#91C6FF',string:'#B6E7BD',number:'#F1C98D',function:'#E7DBAD',operator:'#9EE4DD',comment:'#97A9B8'};
 function show(tokens:(string|Prism.Token)[]):React.ReactNode{return tokens.map((token,i)=>{
  if(typeof token==='string'){const visible=token.slice(0,remaining);remaining=Math.max(0,remaining-token.length);return visible;}
  const content=typeof token.content==='string'?[token.content]:Array.isArray(token.content)?token.content:[token.content];
  return <span key={i} style={{color:colors[token.type]}}>{show(content)}</span>;
 });}
 return <pre style={{fontFamily:'monospace',fontSize:26,lineHeight:1.65,whiteSpace:'pre-wrap',overflowWrap:'anywhere',margin:0}}>{show(Prism.tokenize(code,Prism.languages[language]||Prism.languages.typescript))}</pre>;
}
export function Terminal({command,output,frame,commandAt,outputAt,theme='dark'}:{command:string;output:string;frame:number;commandAt:number;outputAt:number;theme?:'light'|'dark'}){
 const typed=command.slice(0,Math.floor(command.length*clamp((frame-commandAt)/Math.max(1,outputAt-commandAt))));
 return <div style={{fontFamily:'Mono,monospace',fontSize:24,lineHeight:1.7,whiteSpace:'pre-wrap',overflowWrap:'anywhere'}}><span style={{color:theme==='light'?'#276345':'#77E3D1'}}>$ </span>{typed}{output&&<pre style={{whiteSpace:'pre-wrap',marginTop:24,opacity:frame>=outputAt?1:0}}>{output}</pre>}</div>;
}
export function DiagramDraw({progress,color='#77E3D1'}:{progress:number;color?:string}){
 return <svg viewBox="0 0 1000 240" style={{width:'100%'}}>{[0,1,2].map(i=><g key={i} opacity={clamp(progress*4-i)}><rect x={32+i*336} y={80} width={256} height={104} rx={16} fill="#152734" stroke={color}/><text x={160+i*336} y={144} fill="#F0F5F7" textAnchor="middle" fontSize={24}>{['Request','Check','Record'][i]}</text></g>)}{[0,1].map(i=><path key={i} d={`M${288+i*336} 132 H${368+i*336}`} fill="none" stroke={color} strokeWidth={4} pathLength={1} strokeDasharray={1} strokeDashoffset={1-clamp(progress*4-1-i)}/>)}</svg>;
}
export function Caption({words,time}:{words:Word[];time:number}){
 const groups:Word[][]=[];let current:Word[]=[];
 for(const w of words){if(current.length&&(current.length>=7||current.map(x=>x.word).join(' ').length+w.word.length>52||w.start-current[current.length-1].end>.6)){groups.push(current);current=[];}current.push(w);if(/[.!?]$/.test(w.word)){groups.push(current);current=[];}}
 if(current.length)groups.push(current);
 const group=groups.find((g,i)=>time>=g[0].start&&time<Math.min(g[g.length-1].end+.18,groups[i+1]?.[0].start??Infinity));
 if(!group)return null;
 return <div style={{position:'absolute',bottom:48,left:96,right:96,display:'flex',justifyContent:'center'}}><div style={{background:'#060C13F2',borderRadius:8,padding:'16px 24px',fontSize:30,display:'flex',gap:9,flexWrap:'wrap',justifyContent:'center'}}>{group.map((w,i)=><span key={i} style={{color:time>=w.start&&time<w.end?'#77E3D1':'#F0F5F7'}}>{w.word}</span>)}</div></div>;
}
