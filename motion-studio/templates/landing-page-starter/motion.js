const reduce=matchMedia('(prefers-reduced-motion: reduce)');
const stage=document.querySelector('.stage'),sheets=[...document.querySelectorAll('.sheet')];
let visible=true,raf=0,last=0,clock=0,progress=0,target=0;
const reveal=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('seen');reveal.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.reveal').forEach((el,i)=>{el.style.transitionDelay=`${(i%3)*64}ms`;reveal.observe(el)});
new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;start()},{rootMargin:'80px'}).observe(stage);
function measure(){const box=stage.getBoundingClientRect();target=Math.max(0,Math.min(1,(innerHeight*.6-box.top)/(innerHeight*.7)));}
function tick(now){raf=0;if(reduce.matches||document.hidden||!visible)return;const dt=last?Math.min((now-last)/1000,.05):0;last=now;clock+=dt;progress+=(target-progress)*(1-Math.exp(-10*dt));sheets.forEach((sheet,i)=>{const depth=(2-i)*(innerWidth<760?.45:1);sheet.style.transform=`translate3d(${depth*(22+progress*28)}px,${-depth*(32+progress*48)+Math.sin(clock*.7+i)*5}px,${-depth*48}px) rotateX(${10-progress*6}deg) rotateY(${-12+Math.sin(clock*.3)*4}deg) rotateZ(${-depth*3}deg)`});document.querySelector('.signal').style.transform=`translateX(${-120*(.5+.5*Math.sin(clock))}px)`;raf=requestAnimationFrame(tick)}
function start(){if(raf)cancelAnimationFrame(raf);raf=0;last=0;if(!reduce.matches&&!document.hidden&&visible)raf=requestAnimationFrame(tick)}
addEventListener('scroll',measure,{passive:true});addEventListener('resize',measure);document.addEventListener('visibilitychange',start);reduce.addEventListener('change',start);measure();start();
document.querySelectorAll('.button').forEach(button=>{const inner=button.querySelector('.magnetic');button.addEventListener('pointermove',e=>{if(reduce.matches||e.pointerType==='touch')return;const r=button.getBoundingClientRect();inner.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.06}px,${(e.clientY-r.top-r.height/2)*.1}px)`});button.addEventListener('pointerleave',()=>inner.style.transform='')});
