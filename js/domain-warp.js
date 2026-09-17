/* Monochrome domain warping for workshop covers.
 * Visual reference: https://creative-clawing.com/artifacts/domainwarp.html
 * No framework, textures, external requests, or background work on other slides.
 */
(() => {
  'use strict';
  const cover = document.querySelector('.workshop-cover');
  if (!cover) return;
  const canvas = cover.querySelector('.warp-canvas');
  const motionButton = cover.querySelector('[data-warp-motion]');
  const patternButton = cover.querySelector('[data-warp-pattern]');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const gl = canvas.getContext('webgl', {
    alpha: false, antialias: false, depth: false, stencil: false,
    preserveDrawingBuffer: false, powerPreference: 'low-power'
  });
  let program;
  let vertexBuffer;
  let uniforms;
  let frame = 0;
  let lastTime = 0;
  let elapsed = 0;
  let paused = reducedMotion.matches;
  let lost = false;
  let printing = false;
  let pattern = Number(cover.dataset.warpVariant || 0) % 3;
  const FRAME_MS = 1000 / 24;
  const MAX_PIXELS = 960 * 600;

  const vertex = `
    attribute vec2 position;
    varying vec2 uv;
    void main() {
      uv = position * 0.5 + 0.5;
      gl_Position = vec4(position, 0.0, 1.0);
    }
  `;
  const fragment = `
    #ifdef GL_FRAGMENT_PRECISION_HIGH
    precision highp float;
    #else
    precision mediump float;
    #endif
    varying vec2 uv;
    uniform vec2 resolution;
    uniform float time;
    uniform float variation;

    float hash(vec2 p) {
      vec3 q = fract(vec3(p.xyx) * 0.1031);
      q += dot(q, q.yzx + 33.33);
      return fract((q.x + q.y) * q.z);
    }
    float noise(vec2 p) {
      vec2 cell = floor(p);
      vec2 f = fract(p);
      vec2 blend = f * f * (3.0 - 2.0 * f);
      return mix(mix(hash(cell), hash(cell + vec2(1.0, 0.0)), blend.x),
                 mix(hash(cell + vec2(0.0, 1.0)), hash(cell + 1.0), blend.x), blend.y);
    }
    float fbm(vec2 p) {
      float value = 0.0;
      float amplitude = 0.5;
      for (int i = 0; i < 4; i++) {
        value += amplitude * noise(p);
        p = mat2(1.6, -1.2, 1.2, 1.6) * p + 2.7;
        amplitude *= 0.5;
      }
      return value;
    }
    void main() {
      vec2 p = (uv - 0.5) * vec2(resolution.x / resolution.y, 1.0);
      p = p * (2.8 + variation * 0.35) + variation * vec2(5.3, 2.1);
      float drift = time * 0.012;
      vec2 q = vec2(fbm(p + drift), fbm(p + vec2(3.1, 7.9) - drift * 0.6));
      vec2 r = vec2(fbm(p + 3.8 * q + vec2(8.2, 1.7)),
                    fbm(p + 3.8 * q + vec2(2.8, 6.3) + drift * 0.25));
      float field = fbm(p + 3.6 * r);
      float folds = pow(0.5 + 0.5 * cos(field * (18.0 + variation * 7.0)), 5.0);
      float clouds = smoothstep(0.3, 0.83, field);
      float light = mix(folds, clouds, 0.28 + step(0.5, variation) * 0.3);
      float edge = smoothstep(0.08, 0.65, length((uv - 0.5) * vec2(1.0, 0.85)));
      float vignette = 1.0 - smoothstep(0.35, 0.8, length(uv - 0.5));
      // Spatial grain stays fixed, without flicker. Every channel receives one luminance.
      float grain = (hash(floor(uv * resolution)) - 0.5) / 255.0;
      float luminance = light * mix(0.13, 0.34, edge) * vignette + grain;
      gl_FragColor = vec4(vec3(max(0.0, luminance)), 1.0);
    }
  `;

  function fallback() {
    cancelAnimationFrame(frame);
    frame = 0;
    canvas.style.display = 'none';
    cover.dataset.warpState = 'fallback';
    // Keep the CSS gradients and the complete title if WebGL is unavailable.
    cover.querySelector('.cover-controls').style.display = 'none';
  }
  if (!gl) { fallback(); return; }

  function compile(kind, source) {
    const shader = gl.createShader(kind);
    gl.shaderSource(shader, source);
    gl.compileShader(shader);
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
      gl.deleteShader(shader);
      throw new Error('Background shader unavailable');
    }
    return shader;
  }
  function initialize() {
    const vs = compile(gl.VERTEX_SHADER, vertex);
    const fs = compile(gl.FRAGMENT_SHADER, fragment);
    program = gl.createProgram();
    gl.attachShader(program, vs);
    gl.attachShader(program, fs);
    gl.linkProgram(program);
    gl.deleteShader(vs);
    gl.deleteShader(fs);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error('Background program unavailable');
    gl.useProgram(program);
    vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, 'position');
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    uniforms = Object.fromEntries(['resolution', 'time', 'variation'].map(name => [name, gl.getUniformLocation(program, name)]));
  }
  function visible() {
    return cover.classList.contains('active') && !document.hidden && !printing;
  }
  function draw() {
    if (lost || !visible()) return;
    gl.uniform2f(uniforms.resolution, canvas.width, canvas.height);
    gl.uniform1f(uniforms.time, elapsed);
    gl.uniform1f(uniforms.variation, pattern);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }
  function resize() {
    if (lost || !visible()) return;
    const width = cover.clientWidth;
    const height = cover.clientHeight;
    if (!width || !height) return;
    const scale = Math.min(devicePixelRatio || 1, 1.25, Math.sqrt(MAX_PIXELS / (width * height)));
    const w = Math.max(1, Math.floor(width * scale));
    const h = Math.max(1, Math.floor(height * scale));
    if (canvas.width !== w || canvas.height !== h) {
      canvas.width = w;
      canvas.height = h;
      gl.viewport(0, 0, w, h);
    }
    draw();
  }
  function tick(now) {
    frame = 0;
    if (!visible() || paused || lost) return;
    if (!lastTime) lastTime = now;
    if (now - lastTime >= FRAME_MS) {
      elapsed += Math.min((now - lastTime) / 1000, 0.1);
      lastTime = now;
      draw();
    }
    frame = requestAnimationFrame(tick);
  }
  function sync() {
    cancelAnimationFrame(frame);
    frame = 0;
    lastTime = 0;
    motionButton.textContent = paused ? 'Resume motion' : 'Pause motion';
    motionButton.setAttribute('aria-pressed', String(paused));
    cover.dataset.warpState = lost ? 'lost' : !visible() ? 'idle' : paused ? 'paused' : 'running';
    if (lost || !visible()) return;
    resize();
    if (!paused) frame = requestAnimationFrame(tick);
  }
  try { initialize(); } catch { fallback(); return; }
  motionButton.addEventListener('click', () => { paused = !paused; sync(); });
  patternButton.addEventListener('click', () => {
    pattern = (pattern + 1) % 3;
    cover.dataset.warpVariant = String(pattern);
    draw();
  });
  reducedMotion.addEventListener('change', event => { paused = event.matches; sync(); });
  document.addEventListener('visibilitychange', sync);
  new MutationObserver(sync).observe(cover, {attributes: true, attributeFilter: ['class']});
  new ResizeObserver(resize).observe(cover);
  window.addEventListener('beforeprint', () => { printing = true; sync(); });
  window.addEventListener('afterprint', () => { printing = false; sync(); });
  canvas.addEventListener('webglcontextlost', event => {
    event.preventDefault(); lost = true; sync();
  });
  canvas.addEventListener('webglcontextrestored', () => {
    try { initialize(); lost = false; sync(); } catch { fallback(); }
  });
  sync();
})();
