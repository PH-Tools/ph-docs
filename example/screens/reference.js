/* Screen 3 — Reference Docs (WUFI XML Schema) */
window.renderReference = function(root) {
  root.innerHTML = `
  <div class="with-sidebar">
    <aside class="sidebar">
      <div class="sidebar__label">Reference Docs</div>
      <ul class="nav-tree">
        <li><a class="is-active" href="#"><span class="num">01</span>WUFI XML Schema</a></li>
        <li><a href="#"><span class="num">02</span>PHPP Field Mapping</a></li>
        <li><a href="#"><span class="num">03</span>Phius Excel Mapping</a></li>
        <li><a href="#"><span class="num">04</span>PHX Model Reference</a></li>
        <li><a href="#"><span class="num">05</span>METr JSON Schema</a></li>
      </ul>

      <div class="sidebar__label" style="margin-top:24px;">On this page</div>
      <ul class="nav-tree">
        <li><a href="#"><span class="num">§</span>Overview</a></li>
        <li><a href="#"><span class="num">§</span>Fetch this doc</a></li>
        <li><a href="#"><span class="num">§</span>Top-level elements</a></li>
        <li><a href="#"><span class="num">§</span>BuildingSegments</a></li>
        <li><a href="#"><span class="num">§</span>Zones</a></li>
        <li><a href="#"><span class="num">§</span>Components</a></li>
      </ul>
    </aside>

    <div>
      <header class="ref-head">
        <div class="ref-head__crumb">
          <span>Reference Docs</span>
          <span class="sep">›</span>
          <span class="current">WUFI XML</span>
        </div>
        <h1 class="ref-head__title">WUFI Passive XML Schema</h1>
        <p class="ref-head__desc">
          A canonical map of the WUFI-Passive project XML as produced and consumed by PHX. This document is written for two audiences: human engineers cross-walking between WUFI-Passive, PHPP, and Phius models, and LLM agents resolving field definitions at runtime via a stable URL.
        </p>
        <div class="ref-head__meta">
          <div class="ref-head__meta-item">
            <span class="k">Schema version</span>
            <span class="v">WUFI-Passive 3.3.4</span>
          </div>
          <div class="ref-head__meta-item">
            <span class="k">Last reviewed</span>
            <span class="v">2026-03-28</span>
          </div>
          <div class="ref-head__meta-item">
            <span class="k">Maintainer</span>
            <span class="v">@ed.may</span>
          </div>
          <div class="ref-head__meta-item">
            <span class="k">Source</span>
            <span class="v">ph-reference-docs / wufi-xml-schema.md</span>
          </div>
        </div>
      </header>

      <div class="fetch-callout">
        <div class="fetch-callout__inner">
          <div>
            <div class="fetch-callout__head">
              <span class="bullet"></span>
              LLM-ready · Fetch this doc
            </div>
            <p class="fetch-callout__body">
              This page is mirrored at a stable URL for programmatic retrieval. Point your LLM tool at the URL below and it will always receive the current canonical schema in plain Markdown.
            </p>
            <div class="fetch-callout__url">
              <span class="method">GET</span>
              <span>https://ph-tools.github.io/ph-reference-docs/wufi-xml-schema</span>
            </div>
          </div>
          <button class="copy-btn" id="copyFetchUrl">
            <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="9" y="9" width="11" height="11" rx="1.5"/><path d="M5 15V5a1 1 0 0 1 1-1h10"/></svg>
            Copy URL
          </button>
        </div>
      </div>

      <section class="schema-section">
        <div class="section-label">§ 01 · Top-Level Elements</div>
        <h3>Project root structure</h3>
        <p class="section-intro">
          Every WUFI-Passive project file begins with a <code class="mono" style="color:var(--fg);">&lt;Project&gt;</code> root element containing three top-level collections. Required fields are marked <span class="mono" style="color:var(--highlight); font-size:10.5px;">REQ</span>.
        </p>

        <table class="schema-table">
          <thead>
            <tr>
              <th style="width:28%;">Field</th>
              <th style="width:18%;">Type</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="field">BuildingSegments <span class="req">REQ</span></td>
              <td class="type">Array&lt;Segment&gt;</td>
              <td>The set of thermally-distinct building segments. Each segment is exported as an independent WUFI calculation unit and contains its own zones, components, and certification parameters. Typical single-family projects have one segment; mixed-use projects may have several.</td>
            </tr>
            <tr>
              <td class="field">Zones <span class="req">REQ</span></td>
              <td class="type">Array&lt;Zone&gt;</td>
              <td>Thermal zones nested inside a <code class="mono">BuildingSegment</code>. A zone aggregates floor area, ventilation, internal gains, and the set of constructions that bound it. Zone IDs must be unique across the project.</td>
            </tr>
            <tr>
              <td class="field">Components <span class="req">REQ</span></td>
              <td class="type">Array&lt;Component&gt;</td>
              <td>Opaque and transparent envelope components (walls, roofs, floors, windows, doors, thermal bridges). Each component references an <code class="mono">Assembly</code> and is assigned to one or more zones via <code class="mono">ZoneReference</code>.</td>
            </tr>
            <tr>
              <td class="field">Variants</td>
              <td class="type">Array&lt;Variant&gt;</td>
              <td>Optional design variants for comparative analysis. A variant may override any component or system while inheriting geometry from the base project. Used by PHX for Phius alternate-compliance reports.</td>
            </tr>
            <tr>
              <td class="field">CertificationSettings <span class="req">REQ</span></td>
              <td class="type">Object</td>
              <td>Certification track (PH-EU · PH-US · Phius CORE · Phius ZERO), climate zone, occupancy assumptions, and target thresholds. PHX uses this object to select the correct export pipeline and report template.</td>
            </tr>
          </tbody>
        </table>

        <div class="section-label" style="margin-top:48px;">§ 02 · BuildingSegments</div>
        <h3>Segment definition</h3>
        <p class="section-intro">
          A segment describes a contiguous thermal envelope, its internal zoning, and all mechanical systems that serve only that envelope.
        </p>

        <table class="schema-table">
          <thead>
            <tr>
              <th style="width:28%;">Field</th>
              <th style="width:18%;">Type</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="field">id <span class="req">REQ</span></td>
              <td class="type">string · uuid</td>
              <td>Stable identifier for the segment. Generated by PHX on first export; preserved across round-trips.</td>
            </tr>
            <tr>
              <td class="field">name</td>
              <td class="type">string</td>
              <td>Human-readable label shown in WUFI-Passive. Defaults to the Honeybee-PH model name when exported.</td>
            </tr>
            <tr>
              <td class="field">geometry</td>
              <td class="type">Object</td>
              <td>Oriented bounding box, treated floor area (TFA), and net conditioned volume. Computed from the Honeybee geometry; editable in WUFI.</td>
            </tr>
            <tr>
              <td class="field">ventilation</td>
              <td class="type">Object</td>
              <td>Whole-segment ventilation strategy: balanced/exhaust/infiltration-only, HRV/ERV reference, design airflow rates per <code class="mono">Zone</code>.</td>
            </tr>
            <tr>
              <td class="field">dhw</td>
              <td class="type">Object</td>
              <td>Domestic hot water system: generator type, tank volumes, distribution losses. Referenced by zones via <code class="mono">dhw_ref</code>.</td>
            </tr>
          </tbody>
        </table>
      </section>

      <footer class="site-footer">
        <div class="site-footer__left">
          <span>PH-TOOLS</span><span>·</span>
          <a href="#">Edit on GitHub</a><span>·</span>
          <a href="#">Report inaccuracy</a>
        </div>
        <div class="site-footer__right">
          <span>ph-reference-docs · commit a7f3d91</span>
          <span class="version-badge">Schema 3.3.4</span>
        </div>
      </footer>
    </div>
  </div>
  `;

  const copyBtn = root.querySelector('#copyFetchUrl');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const url = 'https://ph-tools.github.io/ph-reference-docs/wufi-xml-schema';
      if (navigator.clipboard) navigator.clipboard.writeText(url);
      copyBtn.innerHTML = '<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-11"/></svg> Copied';
      setTimeout(() => {
        copyBtn.innerHTML = '<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="9" y="9" width="11" height="11" rx="1.5"/><path d="M5 15V5a1 1 0 0 1 1-1h10"/></svg> Copy URL';
      }, 1500);
    });
  }
};
