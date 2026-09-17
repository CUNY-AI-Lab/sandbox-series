(() => {
  const dialog = document.getElementById('image-dialog');
  const close = document.getElementById('close-image');
  const zoom = document.getElementById('zoom-image');
  const stage = document.getElementById('image-stage');
  const expanded = dialog.querySelector('img');
  let trigger;
  function fit() {
    stage.classList.remove('is-zoomed');
    stage.scrollTop=0; stage.scrollLeft=0;
    zoom.textContent='Zoom in';
    zoom.setAttribute('aria-pressed','false');
  }
  function zoomIn() {
    stage.classList.add('is-zoomed');
    zoom.textContent='Fit image';
    zoom.setAttribute('aria-pressed','true');
  }
  function updateZoom() {
    if (!dialog.open || !expanded.naturalWidth || !expanded.naturalHeight) return;
    const fitted=Math.min(stage.clientWidth,stage.clientHeight*expanded.naturalWidth/expanded.naturalHeight,expanded.naturalWidth);
    const width=Math.min(expanded.naturalWidth,Math.max(fitted*2,stage.clientWidth*2));
    stage.style.setProperty('--zoom-width',width+'px');
    zoom.disabled=width<=fitted+1;
  }
  function open(image) {
    trigger=image;
    fit(); zoom.disabled=true;
    expanded.src=image.src;
    expanded.alt=image.alt;
    expanded.style.setProperty('--screenshot-max-width',image.style.getPropertyValue('--screenshot-max-width'));
    dialog.querySelector('p').textContent=image.closest('figure')?.querySelector('figcaption')?.textContent || '';
    dialog.showModal(); updateZoom(); close.focus();
  }
  expanded.addEventListener('load',()=>{
    updateZoom();
    if(dialog.open && stage.clientWidth<=600 && !zoom.disabled) zoomIn();
  });
  zoom.addEventListener('click',()=>{
    if(stage.classList.contains('is-zoomed')) fit();
    else zoomIn();
  });
  window.addEventListener('resize',()=>{ if(dialog.open){fit();updateZoom();} });
  close.addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>trigger?.focus());
  dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});
  document.querySelectorAll('.screenshot-img').forEach(image=>{
    image.tabIndex=0; image.setAttribute('role','button'); image.setAttribute('aria-label',image.alt+'. Expand screenshot');
    image.addEventListener('click',()=>open(image));
    image.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();open(image);}});
  });
})();
