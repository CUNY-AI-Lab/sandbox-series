(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.slide')];
  const total = slides.length;
  const progress = document.getElementById('slide-progress');
  const announcer = document.getElementById('slide-announcer');
  const outline = document.getElementById('outline-dialog');
  const outlineList = document.getElementById('outline-list');
  let current = 0;
  let fragment = 0;
  const fragments = slides.map(slide => [...slide.querySelectorAll('[data-fragment-step]')]);
  document.getElementById('nav-total').textContent = total;
  progress.max = total;
  slides.forEach((slide, index) => {
    const item = document.createElement('li');
    const button = document.createElement('button');
    const number = document.createElement('span');
    number.className = 'outline-number'; number.textContent = String(index + 1);
    const title = document.createElement('span'); title.textContent = slide.dataset.title;
    button.append(number, title);
    button.addEventListener('click', () => { goTo(index); outline.close(); document.getElementById('overview-button').focus(); });
    item.append(button); outlineList.append(item);
  });
  function readHash() {
    const match = location.hash.match(/^#(\d+)$/);
    return match ? Math.min(total - 1, Math.max(0, Number(match[1]) - 1)) : 0;
  }
  function updateFragment() {
    slides[current].scrollTop = 0;
    fragments.forEach((steps, slideIndex) => steps.forEach((step, stepIndex) => {
      const visible = slideIndex === current && stepIndex === fragment;
      if (!visible && step.contains(document.activeElement)) document.getElementById('arrow-next').focus();
      step.hidden = !visible;
      step.inert = !visible;
      step.setAttribute('aria-hidden', String(!visible));
    }));
    document.getElementById('arrow-prev').disabled = current === 0 && fragment === 0;
    document.getElementById('arrow-next').disabled = current === total - 1 && fragment === Math.max(0, fragments[current].length - 1);
    const label = slides[current].dataset.fragmentLabel || 'image';
    announcer.textContent = slides[current].getAttribute('aria-label') + (fragments[current].length ? ', ' + label + ' ' + (fragment + 1) + ' of ' + fragments[current].length : '');
  }
  function goTo(index, step = 0) {
    if (!Number.isInteger(index) || index < 0 || index >= total) return;
    const old = slides[current];
    if (old.contains(document.activeElement)) document.getElementById('arrow-next').focus();
    current = index;
    fragment = Math.min(Math.max(0, step), Math.max(0, fragments[current].length - 1));
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === current);
      slide.inert = i !== current;
      slide.setAttribute('aria-hidden', String(i !== current));
      if (i === current) slide.setAttribute('aria-current', 'step');
      else slide.removeAttribute('aria-current');
    });
    slides[current].scrollTop = 0;
    document.getElementById('nav-current').textContent = current + 1;
    progress.value = current + 1;
    progress.setAttribute('aria-valuetext', slides[current].getAttribute('aria-label'));
    [...outlineList.querySelectorAll('button')].forEach((button, i) => {
      if (i === current) button.setAttribute('aria-current', 'step');
      else button.removeAttribute('aria-current');
    });
    history.replaceState(null, '', '#' + (current + 1));
    updateFragment();
  }
  function advance(direction) {
    if (direction > 0 && fragment < fragments[current].length - 1) {
      fragment++;
      updateFragment();
    } else if (direction < 0 && fragment > 0) {
      fragment--;
      updateFragment();
    } else if (direction < 0 && current > 0) {
      goTo(current - 1, Math.max(0, fragments[current - 1].length - 1));
    } else {
      goTo(current + direction);
    }
  }
  function openOutline() { outline.showModal(); outline.scrollTop = 0; document.getElementById('close-outline').focus(); }
  document.getElementById('overview-button').addEventListener('click', openOutline);
  document.getElementById('close-outline').addEventListener('click', () => outline.close());
  document.getElementById('arrow-prev').addEventListener('click', () => advance(-1));
  document.getElementById('arrow-next').addEventListener('click', () => advance(1));
  progress.addEventListener('input', () => goTo(Number(progress.value) - 1));
  // Keep the labeled footer target and support quick touch swipes on slides.
  const swipeArea = document.querySelector('.nav-info');
  if (swipeArea) {
    const hint = document.createElement('span');
    hint.className = 'nav-swipe-hint';
    hint.textContent = '← Swipe →';
    swipeArea.append(hint);
    swipeArea.setAttribute('role', 'group');
    swipeArea.setAttribute('aria-label', 'Swipe left for next slide; swipe right for previous slide');
    enableSwipe(swipeArea, false);
  }
  const deck = document.getElementById('deck');
  if (deck) enableSwipe(deck, true);
  function enableSwipe(area, touchOnly) {
    let swipeStart = null;
    const protectedTarget = 'a,button,input,textarea,select,[contenteditable="true"],.prompt-block';
    area.addEventListener('pointerdown', event => {
      const selection = window.getSelection();
      if (!event.isPrimary || event.button !== 0 ||
          (touchOnly && (event.pointerType !== 'touch' || event.target.closest(protectedTarget))) ||
          (selection && !selection.isCollapsed) || document.querySelector('dialog[open]')) {
        swipeStart = null;
        return;
      }
      swipeStart = {id: event.pointerId, x: event.clientX, y: event.clientY, time: event.timeStamp};
      area.setPointerCapture(event.pointerId);
    });
    area.addEventListener('pointerup', event => {
      const start = swipeStart;
      swipeStart = null;
      if (!start || start.id !== event.pointerId || document.querySelector('dialog[open]')) return;
      const selection = window.getSelection();
      if (selection && !selection.isCollapsed) return;
      if (touchOnly && event.timeStamp - start.time > 650) return;
      const dx = event.clientX - start.x;
      const dy = event.clientY - start.y;
      if (Math.abs(dx) >= 48 && Math.abs(dx) > Math.abs(dy) * 1.5) advance(dx < 0 ? 1 : -1);
    });
    area.addEventListener('pointercancel', () => { swipeStart = null; });
    area.addEventListener('lostpointercapture', () => { swipeStart = null; });
  }
  document.addEventListener('keydown', (event) => {
    if (event.shiftKey || event.altKey || event.ctrlKey || event.metaKey || document.querySelector('dialog[open]')) return;
    if (event.target.closest('input,textarea,select,[contenteditable="true"]')) return;
    if (event.key === 'Escape') { event.preventDefault(); openOutline(); return; }
    // Let selection and native text-navigation gestures finish without changing slides.
    const selection = window.getSelection();
    if (selection && !selection.isCollapsed) return;
    if (event.target.closest('.prompt-block') && ['ArrowUp','ArrowDown',' ','Home','End'].includes(event.key)) return;
    if (event.target.closest('button,a') && [' ','Enter'].includes(event.key)) return;
    if (['ArrowRight','PageDown',' '].includes(event.key)) { event.preventDefault(); advance(1); }
    else if (['ArrowLeft','PageUp'].includes(event.key)) { event.preventDefault(); advance(-1); }
    else if (event.key === 'Home') { event.preventDefault(); goTo(0); }
    else if (event.key === 'End') { event.preventDefault(); goTo(total - 1); }
  });
  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      const source = document.getElementById(button.dataset.copy);
      const label = button.textContent;
      try {
        if (!navigator.clipboard) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(source.textContent);
        button.textContent = 'Copied'; announcer.textContent = 'Prompt copied';
      } catch {
        const selection = window.getSelection(); const range = document.createRange();
        range.selectNodeContents(source); selection.removeAllRanges(); selection.addRange(range);
        button.textContent = 'Text selected'; announcer.textContent = 'Clipboard unavailable. Prompt selected; use your copy shortcut.';
      }
      setTimeout(() => { button.textContent = label; }, 2200);
    });
  });
  // Content gestures remain available for scrolling and selecting text.
  window.addEventListener('hashchange', () => {
    if (location.hash !== '#deck') goTo(readHash());
  });
  window.deckEngine = {goTo, advance, currentSlide:()=>current, currentFragment:()=>fragment, totalSlides:()=>total};
  goTo(readHash());
})();
