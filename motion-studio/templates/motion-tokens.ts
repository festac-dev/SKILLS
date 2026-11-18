export const motion = {
  ease: {enter: [0.16, 1, 0.3, 1] as const, move: [0.65, 0, 0.35, 1] as const},
  spring: {hero: {mass: 1, stiffness: 140, damping: 24}, ui: {mass: 0.8, stiffness: 220, damping: 28}},
  duration: {feedback: 0.2, ui: 0.32, move: 0.48, hero: 0.9},
  stagger: 0.064, grid: 8,
};
export const expo = (p: number) => p <= 0 ? 0 : p >= 1 ? 1 : 1 - 2 ** (-10 * p);
export const clamp = (p: number) => Math.min(1, Math.max(0, p));
export const atFrame = (seconds: number, fps: number) => Math.round(seconds * fps);
