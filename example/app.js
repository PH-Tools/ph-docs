/* ============================================
   App shell — routing + theme + search
   ============================================ */

(function () {
  const screens = {
    'hub':           { el: document.getElementById('screen-hub'),         nav: null,             render: window.renderHub },
    'honeybee-ph':   { el: document.getElementById('screen-honeybee-ph'), nav: 'honeybee-ph',    render: window.renderLibrary },
    'reference':    { el: document.getElementById('screen-reference'),   nav: 'reference',      render: window.renderReference }
  };

  // Render all up-front so switching is instant
  Object.entries(screens).forEach(([key, s]) => {
    if (s.render && s.el) s.render(s.el);
  });

  // Search modal content is pre-rendered too
  const searchModal = document.getElementById('searchModal');
  const searchScrim = document.getElementById('searchScrim');
  window.renderSearchModal(searchModal);

  // ---------- Navigation ----------
  function go(name) {
    if (name === 'search') { openSearch(); return; }
    if (!screens[name]) return;

    Object.entries(screens).forEach(([k, s]) => {
      s.el.hidden = (k !== name);
    });

    // primary nav active state
    document.querySelectorAll('#primaryNav a').forEach(a => {
      a.classList.toggle('is-active', a.dataset.go === screens[name].nav);
    });

    // switcher active state
    document.querySelectorAll('.screen-switcher button').forEach(b => {
      b.classList.toggle('is-active', b.dataset.go === name);
    });

    // persist
    try { localStorage.setItem('ph-docs:screen', name); } catch (e) {}

    window.scrollTo({ top: 0, behavior: 'instant' });
  }

  document.body.addEventListener('click', (e) => {
    const t = e.target.closest('[data-go]');
    if (!t) return;
    const dest = t.dataset.go;
    if (dest) {
      e.preventDefault();
      go(dest);
    }
  });

  // Restore last screen
  let initial = 'hub';
  try {
    const saved = localStorage.getItem('ph-docs:screen');
    if (saved && screens[saved]) initial = saved;
  } catch (e) {}
  go(initial);

  // ---------- Theme toggle ----------
  const themeBtn = document.getElementById('themeToggle');
  const iconSun = themeBtn.querySelector('.icon-sun');
  const iconMoon = themeBtn.querySelector('.icon-moon');

  function setTheme(t) {
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem('ph-docs:theme', t); } catch (e) {}
    if (t === 'dark') { iconSun.style.display = 'none'; iconMoon.style.display = ''; }
    else              { iconSun.style.display = '';     iconMoon.style.display = 'none'; }
  }

  try {
    const saved = localStorage.getItem('ph-docs:theme');
    if (saved) setTheme(saved);
  } catch (e) {}

  themeBtn.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    setTheme(cur === 'dark' ? 'light' : 'dark');
  });

  // ---------- Search modal ----------
  function openSearch() {
    searchScrim.classList.add('is-open');
    searchScrim.setAttribute('aria-hidden', 'false');
    const input = document.getElementById('searchInput');
    if (input) setTimeout(() => input.focus(), 40);
    // mark switcher
    document.querySelectorAll('.screen-switcher button').forEach(b => {
      b.classList.toggle('is-active', b.dataset.go === 'search');
    });
  }
  function closeSearch() {
    searchScrim.classList.remove('is-open');
    searchScrim.setAttribute('aria-hidden', 'true');
    // restore switcher active state
    const cur = localStorage.getItem('ph-docs:screen') || 'hub';
    document.querySelectorAll('.screen-switcher button').forEach(b => {
      b.classList.toggle('is-active', b.dataset.go === cur);
    });
  }

  document.getElementById('openSearch').addEventListener('click', openSearch);
  searchScrim.addEventListener('click', (e) => {
    if (e.target === searchScrim) closeSearch();
  });
  document.addEventListener('keydown', (e) => {
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      if (searchScrim.classList.contains('is-open')) closeSearch();
      else openSearch();
    }
    if (e.key === 'Escape' && searchScrim.classList.contains('is-open')) closeSearch();
  });
  searchModal.addEventListener('click', (e) => {
    const t = e.target.closest('#closeSearch');
    if (t) closeSearch();
  });

})();
