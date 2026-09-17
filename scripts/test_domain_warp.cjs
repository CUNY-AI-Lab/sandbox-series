/* Rendering lifecycle contracts, without requiring a GPU in CI. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../js/domain-warp.js'), 'utf8');
let checks = 0;
function check(value, message) { assert.ok(value, message); checks++; }
function environment({reduced = false, webgl = true, shader = true, active = true} = {}) {
  const callbacks = new Map();
  const listeners = new Map();
  const media = {matches: reduced, addEventListener(_, callback) { this.change = callback; }};
  const button = () => ({textContent: '', addEventListener(_, fn) { this.click = fn; }, setAttribute(name, value) { this[name] = value; }});
  const motion = button(), pattern = button(), controls = {style: {}};
  const draws = [];
  const gl = new Proxy({
    createShader: () => ({}), getShaderParameter: () => shader,
    createProgram: () => ({}), getProgramParameter: () => true,
    createBuffer: () => ({}), getAttribLocation: () => 0,
    getUniformLocation: (_, name) => name,
    drawArrays: () => draws.push(true)
  }, {get: (target, key) => key in target ? target[key] : () => {}});
  const canvas = {width: 0, height: 0, style: {}, getContext: () => webgl ? gl : null,
    addEventListener(name, fn) { listeners.set(name, fn); }};
  const cover = {clientWidth: 3840, clientHeight: 2160, dataset: {warpVariant: '0'},
    classList: {contains: () => active}, querySelector: selector => ({
      '.warp-canvas': canvas, '[data-warp-motion]': motion,
      '[data-warp-pattern]': pattern, '.cover-controls': controls
    })[selector]};
  const document = {hidden: false, querySelector: () => cover, addEventListener(name, fn) {listeners.set(name, fn);}};
  let mutate;
  let id = 0;
  vm.runInNewContext(source, {
    document, window: {addEventListener(name, fn) {listeners.set(name, fn);}},
    devicePixelRatio: 2, matchMedia: () => media,
    MutationObserver: class {constructor(fn) {mutate = fn;} observe() {}},
    ResizeObserver: class {constructor(fn) {this.fn = fn;} observe() {this.fn();}},
    requestAnimationFrame(fn) {callbacks.set(++id, fn); return id;},
    cancelAnimationFrame(key) {callbacks.delete(key);}
  });
  return {cover, canvas, controls, motion, pattern, media, document, draws, callbacks,
    event(name, event = {}) {listeners.get(name)(event);},
    activate(value) {active = value; mutate();},
    tick(now) {const pending = [...callbacks.values()]; callbacks.clear(); pending.forEach(fn => fn(now));}};
}
const live = environment();
check(live.canvas.width * live.canvas.height <= 960 * 600, '4K displays stay within pixel budget');
check(live.cover.dataset.warpState === 'running' && live.callbacks.size === 1, 'visible title runs one loop');
live.tick(1); live.tick(51);
check(live.draws.length >= 2, 'animation draws successive frames');
live.motion.click();
const stopped = live.draws.length;
live.tick(101);
check(live.callbacks.size === 0 && live.draws.length === stopped, 'pause stops work');
live.pattern.click();
check(live.cover.dataset.warpVariant === '1' && live.draws.length === stopped + 1, 'variation redraws while paused');
live.pattern.click(); live.pattern.click();
check(live.cover.dataset.warpVariant === '0', 'three variations cycle predictably');
live.activate(false);
check(live.cover.dataset.warpState === 'idle' && live.callbacks.size === 0, 'other slides stop rendering');
const offscreen = live.draws.length;
live.pattern.click();
check(live.draws.length === offscreen, 'offscreen changes do not draw');
live.activate(true);
check(live.cover.dataset.warpState === 'paused' && live.callbacks.size === 0, 'navigation preserves pause');
live.motion.click();
live.document.hidden = true; live.event('visibilitychange');
check(live.callbacks.size === 0, 'background tabs stop rendering');
live.document.hidden = false; live.event('visibilitychange');
check(live.callbacks.size === 1, 'visible tab resumes one loop');
live.event('beforeprint');
check(live.callbacks.size === 0, 'printing stops rendering');
live.event('afterprint');
check(live.callbacks.size === 1, 'printing does not lose motion preference');
live.event('webglcontextlost', {preventDefault() {}});
check(live.cover.dataset.warpState === 'lost' && live.callbacks.size === 0, 'context loss stops rendering');
live.event('webglcontextrestored');
check(live.cover.dataset.warpState === 'running' && live.callbacks.size === 1, 'context restore resumes');
const quiet = environment({reduced: true});
check(quiet.cover.dataset.warpState === 'paused' && quiet.callbacks.size === 0 && quiet.draws.length > 0, 'reduced motion paints a still image');
const away = environment({active: false});
check(away.draws.length === 0 && away.callbacks.size === 0, 'deep links skip background work');
for (const options of [{webgl: false}, {shader: false}]) {
  const fallback = environment(options);
  check(fallback.cover.dataset.warpState === 'fallback' && fallback.controls.style.display === 'none', 'unavailable WebGL keeps CSS fallback without broken controls');
}
console.log(`Passed ${checks} background checks.`);
