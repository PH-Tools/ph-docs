/* Screen 2 — Library Landing (Honeybee-PH Overview) */
window.renderLibrary = function(root) {
  root.innerHTML = `
  <div class="with-sidebar">
    <aside class="sidebar">
      <div class="sidebar__label">Library · Honeybee-PH</div>
      <ul class="nav-tree">
        <li><a class="is-active" href="#"><span class="num">01</span>Overview</a></li>
        <li class="group is-open">
          <button aria-expanded="true"><span class="num">02</span>Getting Started
            <svg class="chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="m3 2 4 3-4 3"/></svg>
          </button>
          <ul class="children">
            <li><a href="#">Installation</a></li>
            <li><a href="#">Rhino + Grasshopper setup</a></li>
            <li><a href="#">Your first PH model</a></li>
            <li><a href="#">Export to WUFI / PHPP</a></li>
          </ul>
        </li>
        <li class="group">
          <button><span class="num">03</span>Component Reference
            <svg class="chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="m3 2 4 3-4 3"/></svg>
          </button>
        </li>
        <li class="group">
          <button><span class="num">04</span>Developer Guide
            <svg class="chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="m3 2 4 3-4 3"/></svg>
          </button>
        </li>
        <li class="group">
          <button><span class="num">05</span>API Reference
            <svg class="chev" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="m3 2 4 3-4 3"/></svg>
          </button>
        </li>
        <li><a href="#"><span class="num">06</span>Release Notes</a></li>
        <li><a href="#"><span class="num">07</span>FAQ</a></li>
      </ul>

      <div class="sidebar__label" style="margin-top: 24px;">Resources</div>
      <ul class="nav-tree">
        <li><a href="#"><span class="num">↗</span>GitHub repo</a></li>
        <li><a href="#"><span class="num">↗</span>Issue tracker</a></li>
        <li><a href="#"><span class="num">↗</span>Food4Rhino</a></li>
      </ul>
    </aside>

    <div>
      <header class="lib-head">
        <div class="lib-head__tag">
          <span class="idx">01</span>
          <span class="sep">·</span>
          <span>Honeybee-PH</span>
          <span class="sep">·</span>
          <span>Overview</span>
        </div>
        <h1 class="lib-head__title">A Grasshopper-native<br>Passive House modeler.</h1>
        <p class="lib-head__sub">
          Honeybee-PH extends Ladybug Tools with the geometry, metadata, and export pipelines needed to produce PH-compliant models for certification. Use familiar Honeybee components inside Rhino / Grasshopper, then write your project to WUFI-Passive XML, PHPP Excel, or Phius packages.
        </p>
        <div class="lib-head__chips">
          <a class="pill pill--accent" href="#">v 1.8.2 — latest</a>
          <a class="pill" href="#">PH-EU · PH-US · Phius 2024</a>
          <a class="pill" href="#">Rhino 7 / 8</a>
        </div>
      </header>

      <section class="quick-links">
        <div class="quick-links__label">— Quick links</div>
        <div class="quick-links__row">
          <a class="pill" href="#">↓ Install</a>
          <a class="pill" href="#">⌗ Component Reference</a>
          <a class="pill" href="#">▶ Worked Examples</a>
          <a class="pill" href="#">↗ GitHub</a>
          <a class="pill" href="#">✎ Changelog</a>
        </div>
      </section>

      <section class="feature-grid">
        <div class="feature-grid__label">What's in this library</div>
        <div class="f-grid">

          <div class="f-cell">
            <span class="f-cell__idx">01 / GRASSHOPPER</span>
            <h3 class="f-cell__title">Component Types</h3>
            <p class="f-cell__desc">142 typed Grasshopper components covering envelopes, ventilation, DHW, equipment, and certification parameters.</p>
            <a class="f-cell__link" href="#">Browse components →</a>
          </div>

          <div class="f-cell">
            <span class="f-cell__idx">02 / PYTHON</span>
            <h3 class="f-cell__title">Python API</h3>
            <p class="f-cell__desc">Scriptable classes mirror every GH component. Use honeybee_ph_rhino outside Grasshopper in CI pipelines or tests.</p>
            <a class="f-cell__link" href="#">API reference →</a>
          </div>

          <div class="f-cell">
            <span class="f-cell__idx">03 / GUIDES</span>
            <h3 class="f-cell__title">Worked Examples</h3>
            <p class="f-cell__desc">Step-through projects for single-family retrofit, multi-family new build, and Phius CORE/ZERO workflows.</p>
            <a class="f-cell__link" href="#">Open gallery →</a>
          </div>

          <div class="f-cell">
            <span class="f-cell__idx">04 / EXPORT</span>
            <h3 class="f-cell__title">WUFI + PHPP Export</h3>
            <p class="f-cell__desc">Write compliant WUFI-Passive XML and PHPP Excel from any Honeybee-PH model — round-trip friendly via PHX.</p>
            <a class="f-cell__link" href="#">Export reference →</a>
          </div>

          <div class="f-cell">
            <span class="f-cell__idx">05 / INTEROP</span>
            <h3 class="f-cell__title">REVIVE Integration</h3>
            <p class="f-cell__desc">Share geometry, constructions, and loads directly with Honeybee-REVIVE for embodied-carbon and resilience analysis.</p>
            <a class="f-cell__link" href="#">Integration guide →</a>
          </div>

          <div class="f-cell">
            <span class="f-cell__idx">06 / COMMUNITY</span>
            <h3 class="f-cell__title">Contributing</h3>
            <p class="f-cell__desc">Architectural decisions, component authoring guide, test suite, and the PR checklist for new contributions.</p>
            <a class="f-cell__link" href="#">Developer guide →</a>
          </div>

        </div>
      </section>

      <footer class="site-footer">
        <div class="site-footer__left">
          <span>PH-TOOLS</span><span>·</span>
          <a href="#">Edit this page</a><span>·</span>
          <a href="#">Report issue</a>
        </div>
        <div class="site-footer__right">
          <span>Last updated 2026-04-12</span>
          <span class="version-badge">v 1.8.2</span>
        </div>
      </footer>
    </div>
  </div>
  `;

  // Wire sidebar collapsing
  root.querySelectorAll('.nav-tree .group > button').forEach(btn => {
    btn.addEventListener('click', () => {
      btn.parentElement.classList.toggle('is-open');
    });
  });
};
