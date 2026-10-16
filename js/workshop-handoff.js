(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.workshop-handoff')];
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const sync = () => slides.forEach(slide => {
    const frame = slide.querySelector('iframe[data-art-src]');
    if (slide.classList.contains('active') && !reduced.matches) {
      if (!frame.hasAttribute('src')) frame.src = frame.dataset.artSrc;
    } else if (frame.hasAttribute('src')) frame.removeAttribute('src');
  });
  slides.forEach(slide => new MutationObserver(sync).observe(slide, {attributes:true, attributeFilter:['class']}));
  reduced.addEventListener('change', sync);
  sync();
})();
