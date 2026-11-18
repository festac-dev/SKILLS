import * as THREE from 'three';
const KEY='media2threejs.camera.v1';
export function persistCamera(camera:THREE.PerspectiveCamera):void{localStorage.setItem(KEY,JSON.stringify({position:camera.position.toArray(),quaternion:camera.quaternion.toArray(),fov:camera.fov}));}
export function restoreCamera(camera:THREE.PerspectiveCamera):boolean{const raw=localStorage.getItem(KEY);if(!raw)return false;const v=JSON.parse(raw) as {position:number[];quaternion:number[];fov:number};camera.position.fromArray(v.position);camera.quaternion.fromArray(v.quaternion);camera.fov=v.fov;camera.updateProjectionMatrix();return true;}
