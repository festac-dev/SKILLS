import * as THREE from 'three';
export function createCamera(canvas: HTMLCanvasElement): THREE.PerspectiveCamera { const camera=new THREE.PerspectiveCamera(50,canvas.clientWidth/Math.max(canvas.clientHeight,1),0.01,500);camera.position.set(5,3,7);camera.lookAt(0,1,0);return camera; }
