/* Screen 1 — Hub Landing */
window.renderHub = function(root) {
  root.innerHTML = `
  <section class="hero graph-paper">
    <svg class="hero__drafting" viewBox="0 0 520 380" fill="none" stroke="currentColor" stroke-width="0.6">
      <!-- House section (architectural line drawing) -->
      <g stroke="#7a9424" stroke-linecap="square" stroke-linejoin="miter">
        <!-- ground line -->
        <line x1="10" y1="340" x2="510" y2="340"/>
        <!-- hatching -->
        <g stroke-width="0.4">
          <line x1="20" y1="340" x2="12" y2="352"/>
          <line x1="50" y1="340" x2="42" y2="352"/>
          <line x1="80" y1="340" x2="72" y2="352"/>
          <line x1="110" y1="340" x2="102" y2="352"/>
          <line x1="140" y1="340" x2="132" y2="352"/>
          <line x1="170" y1="340" x2="162" y2="352"/>
          <line x1="200" y1="340" x2="192" y2="352"/>
          <line x1="230" y1="340" x2="222" y2="352"/>
          <line x1="260" y1="340" x2="252" y2="352"/>
          <line x1="290" y1="340" x2="282" y2="352"/>
          <line x1="320" y1="340" x2="312" y2="352"/>
          <line x1="350" y1="340" x2="342" y2="352"/>
          <line x1="380" y1="340" x2="372" y2="352"/>
          <line x1="410" y1="340" x2="402" y2="352"/>
          <line x1="440" y1="340" x2="432" y2="352"/>
          <line x1="470" y1="340" x2="462" y2="352"/>
          <line x1="500" y1="340" x2="492" y2="352"/>
        </g>
        <!-- house outline -->
        <path d="M90 340 L90 180 L260 80 L430 180 L430 340 Z"/>
        <!-- roof line inner -->
        <path d="M90 180 L260 95 L430 180"/>
        <!-- eaves -->
        <line x1="70" y1="180" x2="450" y2="180"/>
        <!-- walls inner -->
        <line x1="110" y1="340" x2="110" y2="195"/>
        <line x1="410" y1="340" x2="410" y2="195"/>
        <!-- insulation hatch between walls -->
        <g stroke-width="0.3">
          <line x1="90" y1="195" x2="110" y2="195"/>
          <line x1="90" y1="215" x2="110" y2="215"/>
          <line x1="90" y1="235" x2="110" y2="235"/>
          <line x1="90" y1="255" x2="110" y2="255"/>
          <line x1="90" y1="275" x2="110" y2="275"/>
          <line x1="90" y1="295" x2="110" y2="295"/>
          <line x1="90" y1="315" x2="110" y2="315"/>
          <line x1="90" y1="335" x2="110" y2="335"/>
        </g>
        <!-- floor -->
        <line x1="90" y1="320" x2="430" y2="320"/>
        <line x1="90" y1="316" x2="430" y2="316"/>
        <!-- windows -->
        <rect x="150" y="230" width="60" height="80"/>
        <line x1="180" y1="230" x2="180" y2="310"/>
        <line x1="150" y1="270" x2="210" y2="270"/>
        <rect x="310" y="230" width="60" height="80"/>
        <line x1="340" y1="230" x2="340" y2="310"/>
        <line x1="310" y1="270" x2="370" y2="270"/>
        <!-- dim lines -->
        <g stroke-width="0.35">
          <line x1="60" y1="340" x2="40" y2="340"/>
          <line x1="60" y1="180" x2="40" y2="180"/>
          <line x1="50" y1="180" x2="50" y2="340"/>
          <path d="M47 184 L50 180 L53 184"/>
          <path d="M47 336 L50 340 L53 336"/>
        </g>
        <!-- sun/angle indicator -->
        <g stroke-width="0.4">
          <circle cx="80" cy="80" r="14"/>
          <line x1="80" y1="56" x2="80" y2="62"/>
          <line x1="80" y1="98" x2="80" y2="104"/>
          <line x1="56" y1="80" x2="62" y2="80"/>
          <line x1="98" y1="80" x2="104" y2="80"/>
          <line x1="63" y1="63" x2="67" y2="67"/>
          <line x1="93" y1="93" x2="97" y2="97"/>
        </g>
      </g>
    </svg>

    <div class="hero__inner">
      <div class="hero__eyebrow">
        <span class="hero__eyebrow-line"></span>
        <span class="hero__eyebrow-text">Documentation · v2026.1 · Unified Hub</span>
      </div>
      <h1 class="hero__title">Passive House Tools <em>— Documentation</em></h1>
      <p class="hero__sub">
        // Open-source building performance tools by <b style="color:var(--fg); font-weight:400;">bldgtyp, LLC</b><br>
        // Grasshopper · Python · Honeybee · WUFI · PHPP · Phius
      </p>
    </div>

    <div class="hero__meta">
      <b>SYSTEM STATUS</b>
      ACTIVE · 4 LIBRARIES<br>
      LAST BUILD · 2026.04.17<br>
      MIT LICENSE · PUBLIC
    </div>
  </section>

  <!-- Library cards -->
  <section class="libraries">
    <div class="libraries__head">
      <h2>Choose a library</h2>
      <span class="count">04 / LIBRARIES</span>
    </div>

    <div class="lib-grid">
      <a class="lib-card graph-paper-subtle" data-go="honeybee-ph" href="#honeybee-ph">
        <div class="lib-card__idx">
          <span class="lib-card__idx-num">01</span>
          <span class="lib-card__idx-dash"></span>
          <span>GRASSHOPPER · PYTHON</span>
        </div>
        <div class="lib-card__tag">Modeling</div>
        <h3 class="lib-card__name">Honeybee-PH</h3>
        <p class="lib-card__desc">Grasshopper-native Passive House modeling. Build PH-compliant models inside Rhino using familiar Honeybee components.</p>
        <div class="lib-card__footer">
          <span class="lib-card__cta">→ View Docs <span class="arr">↗</span></span>
          <div class="lib-card__stats">
            <span><b>v1.8.2</b></span>
            <span>142 components</span>
          </div>
        </div>
      </a>

      <a class="lib-card graph-paper-subtle" data-go="honeybee-ph" href="#phx">
        <div class="lib-card__idx">
          <span class="lib-card__idx-num">02</span>
          <span class="lib-card__idx-dash"></span>
          <span>PYTHON · DATA MODEL</span>
        </div>
        <div class="lib-card__tag">Exchange</div>
        <h3 class="lib-card__name">PHX</h3>
        <p class="lib-card__desc">Passive House Exchange data model &amp; file I/O. Convert between WUFI XML, PHPP Excel, and Phius report formats.</p>
        <div class="lib-card__footer">
          <span class="lib-card__cta">→ View Docs <span class="arr">↗</span></span>
          <div class="lib-card__stats">
            <span><b>v1.4.0</b></span>
            <span>WUFI · PHPP · Phius</span>
          </div>
        </div>
      </a>

      <a class="lib-card graph-paper-subtle" data-go="honeybee-ph" href="#honeybee-revive">
        <div class="lib-card__idx">
          <span class="lib-card__idx-num">03</span>
          <span class="lib-card__idx-dash"></span>
          <span>GRASSHOPPER · ANALYSIS</span>
        </div>
        <div class="lib-card__tag">Analysis</div>
        <h3 class="lib-card__name">Honeybee-REVIVE</h3>
        <p class="lib-card__desc">Carbon &amp; energy analysis for building design. Resilience &amp; embodied-carbon workflows for deep retrofits and new builds.</p>
        <div class="lib-card__footer">
          <span class="lib-card__cta">→ View Docs <span class="arr">↗</span></span>
          <div class="lib-card__stats">
            <span><b>v0.9.1</b></span>
            <span>Phius REVIVE</span>
          </div>
        </div>
      </a>

      <a class="lib-card graph-paper-subtle" data-go="reference" href="#reference">
        <div class="lib-card__idx">
          <span class="lib-card__idx-num">04</span>
          <span class="lib-card__idx-dash"></span>
          <span>SCHEMAS · MAPPINGS · LLM</span>
        </div>
        <div class="lib-card__tag">Reference</div>
        <h3 class="lib-card__name">Reference Docs</h3>
        <p class="lib-card__desc">Schema maps, file formats &amp; LLM reference. Stable URLs for humans and agents fetching canonical field definitions.</p>
        <div class="lib-card__footer">
          <span class="lib-card__cta">→ View Docs <span class="arr">↗</span></span>
          <div class="lib-card__stats">
            <span><b>LLM-ready</b></span>
            <span>5 schemas</span>
          </div>
        </div>
      </a>
    </div>
  </section>

  <!-- Quick strip -->
  <section class="quick-strip">
    <div class="quick-strip__item">
      <span class="k">New here</span>
      <span class="v"><a data-go="honeybee-ph" href="#">Start with Getting Started →</a></span>
    </div>
    <div class="quick-strip__item">
      <span class="k">Install</span>
      <span class="v mono" style="font-size:13.5px;">pip install honeybee-ph</span>
    </div>
    <div class="quick-strip__item">
      <span class="k">Release notes</span>
      <span class="v"><a href="#">Changelog · v2026.1 →</a></span>
    </div>
    <div class="quick-strip__item">
      <span class="k">Contribute</span>
      <span class="v"><a href="#">github.com/bldgtyp →</a></span>
    </div>
  </section>

  <footer class="site-footer">
    <div class="site-footer__left">
      <span>PH-TOOLS</span>
      <span>·</span>
      <a href="#">bldgtyp, LLC</a>
      <span>·</span>
      <a href="#">GitHub</a>
      <span>·</span>
      <a href="#">MIT License</a>
    </div>
    <div class="site-footer__right">
      <span>docs.passivehousetools.com</span>
      <span class="version-badge">v 2026.1.0</span>
    </div>
  </footer>
  `;
};
