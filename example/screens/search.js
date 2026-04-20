/* Screen 4 — Site-wide search modal */
window.renderSearchModal = function(root) {
  const data = [
    {
      lib: 'Honeybee-PH',
      badge: 'HB-PH',
      results: [
        { title: 'HB_PH Envelope Component', crumb: 'Honeybee-PH › Component Reference › Envelope', excerpt: 'Defines opaque envelope <mark>assemblies</mark> with PH-specific thermal bridging, air-tightness metadata, and Phius-compliant U-value reporting.' },
        { title: 'Installing on Rhino 8', crumb: 'Honeybee-PH › Getting Started › Install', excerpt: 'Run <mark>pip install</mark> from the Rhino Python shell, then drop the .gha file into the Grasshopper Libraries folder.' },
        { title: 'Exporting to WUFI-Passive', crumb: 'Honeybee-PH › Worked Examples › Export', excerpt: 'Use the <mark>HB_PH Write WUFI XML</mark> component to serialize any Honeybee-PH model into a schema-valid Passive.xml file.' }
      ]
    },
    {
      lib: 'PHX',
      badge: 'PHX',
      results: [
        { title: 'PhxProject model', crumb: 'PHX › Python API › Core › PhxProject', excerpt: 'The root container. Every <mark>assembly</mark>, zone, and system is attached to a single PhxProject instance, which maps 1:1 to a WUFI project file.' },
        { title: 'XML round-trip tests', crumb: 'PHX › Developer Guide › Testing', excerpt: 'Use pytest to verify every supported <mark>assembly</mark> type survives WUFI ↔ PHX ↔ PHPP conversion with identical numerics.' }
      ]
    },
    {
      lib: 'Reference Docs',
      badge: 'REF',
      results: [
        { title: 'WUFI XML: Components section', crumb: 'Reference Docs › WUFI XML › Components', excerpt: 'Opaque envelope components reference an <mark>Assembly</mark> and are assigned to one or more zones via ZoneReference.' }
      ]
    }
  ];

  const query = 'assembly';

  const html = `
  <div class="search-input-wrap">
    <svg class="s-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round">
      <circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>
    </svg>
    <input class="search-input" id="searchInput" type="text" value="${query}" placeholder="Search all PH-Tools docs..." autocomplete="off" spellcheck="false" />
    <button class="esc" id="closeSearch">ESC</button>
  </div>

  <div class="search-results" id="searchResults">
    ${data.map(group => `
      <div class="search-group">
        <div class="search-group__head">
          <div class="search-group__title"><span class="dot"></span>${group.lib}</div>
          <div class="search-group__count">${group.results.length} result${group.results.length === 1 ? '' : 's'}</div>
        </div>
        ${group.results.map((r, i) => `
          <div class="search-result ${group.lib === 'Honeybee-PH' && i === 0 ? 'is-focused' : ''}">
            <div>
              <div class="search-result__crumb">
                ${r.crumb.split(' › ').map((s, idx, arr) => `<span>${s}</span>${idx < arr.length - 1 ? '<span class="tri">›</span>' : ''}`).join('')}
              </div>
              <div class="search-result__title">${r.title}</div>
              <div class="search-result__excerpt">${r.excerpt}</div>
            </div>
            <div class="search-result__side">
              <span class="search-badge">${group.badge}</span>
              <span class="search-result__enter">↵ Open</span>
            </div>
          </div>
        `).join('')}
      </div>
    `).join('')}
  </div>

  <div class="search-footer">
    <div class="search-footer__kbds">
      <span><span class="k">↑↓</span> Navigate</span>
      <span><span class="k">↵</span> Open</span>
      <span><span class="k">⌘K</span> Toggle</span>
    </div>
    <div>6 results across 3 libraries · 42ms</div>
  </div>
  `;

  root.innerHTML = html;
};
