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
      button.textContent = value === 'light' ? 'Dark mode' : 'Light mode';
      button.setAttribute('aria-label', value === 'light' ? 'Switch to dark mode' : 'Switch to light mode');
      button.setAttribute('aria-pressed', String(value === 'light'));
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    const button = document.createElement('button');
    button.id = 'theme-toggle';
    button.type = 'button';
    button.className = 'theme-toggle';
    button.addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'light' ? 'dark' : 'light';
      try { localStorage.setItem(key, next); } catch (_) {}
      apply(next);
    });
    document.body.append(button);
    apply(theme);
  });
})();
