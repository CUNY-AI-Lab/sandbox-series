(() => {
  const key = 'sandbox-series-theme';
  let saved = 'dark';
  try { saved = localStorage.getItem(key) || 'dark'; } catch (_) {}
  const theme = saved === 'light' ? 'light' : 'dark';

  function apply(value) {
    document.documentElement.dataset.theme = value;
    document.querySelectorAll('[data-theme-brand]').forEach(image => {
      image.src = value === 'light' ? image.dataset.logoLight : image.dataset.logoDark;
    });
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.setAttribute('aria-label', value === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
      button.setAttribute('aria-pressed', String(value === 'light'));
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const button = document.createElement('button');
    button.id = 'theme-toggle';
    button.type = 'button';
    button.className = 'theme-toggle';
    button.innerHTML = '<svg class="theme-sun" aria-hidden="true" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg><svg class="theme-moon" aria-hidden="true" viewBox="0 0 24 24"><path d="M20.3 15.2A8.6 8.6 0 0 1 8.8 3.7 8.7 8.7 0 1 0 20.3 15.2Z"/></svg>';
    button.addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
      try { localStorage.setItem(key, next); } catch (_) {}
      apply(next);
    });
    document.body.append(button);
    apply(theme);
  });
})();
