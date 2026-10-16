(() => {
  'use strict';
  const slides = [...document.querySelectorAll('.workshop-handoff')];
  slides.forEach(slide => {
    const signpost = slide.querySelector('details');
    signpost.addEventListener('pointerdown', event => event.stopPropagation());
    signpost.querySelector('summary').addEventListener('keydown', event => {
      if (event.key === ' ' || event.key === 'Enter') event.stopPropagation();
    });
  });
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
