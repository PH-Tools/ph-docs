# UI Migration Plan: ph-docs → Brand Design System

**Goal**: Replace the experimental ph-docs design with the official bldgtyp brand system (`tokens.css` + `components.css`), bringing visual consistency with passivehousetools.com and other PH-Tools properties.

**Scope**: UI/UX only — no content changes. Structural Astro components (routing, content collections, Pagefind search) stay unchanged.

**Key references**:
- Brand tokens CDN: `https://bldgtyp.github.io/branding/tokens/tokens.css`
- Brand components CDN: `https://bldgtyp.github.io/branding/tokens/components.css`
- Brand guidelines: https://bldgtyp.github.io/branding/
- Reference implementation: https://passivehousetools.com/

---

## What Changes

| Aspect | Current (experimental) | Target (brand system) |
|--------|----------------------|----------------------|
| Accent color | Olive green `#7a9424` | Steel blue `#3E93AE` |
| Highlight color | Red `#DC2626` | Magenta `#E23489` |
| Token variable names | Custom (`--bg`, `--fg`, `--fg-muted`) | Brand standard (`--bg-page`, `--text-primary`, `--text-secondary`) |
| Component CSS | 1,819 lines of custom CSS in `global.css` | Import brand `components.css` + minimal overrides |
| Graph paper SVGs | Hardcoded green `rgba(122,148,36,...)` | Brand token-aware (blue-based) |
| Dark theme vars | Custom overrides in `[data-theme="dark"]` | Brand system handles this automatically |
| Font imports | Outfit 300/500/600 + JetBrains Mono 300/400 | Same fonts, add Outfit 200/400/700 weights |
| Component classes | Custom naming (`.lib-card`, `.skill-card`, etc.) | Brand naming (`.doc-card`, `.service-card`, etc.) |

---

## Migration Phases

### Phase 0: Setup & Foundation
> Import brand system, establish token mapping, remove custom overrides.

- [x] **0.1** — Add `components.css` CDN import alongside existing `tokens.css` import in `global.css`
- [x] **0.2** — Remove all custom `:root` token overrides (lines 11–43 in `global.css`) that duplicate/shadow brand tokens: `--accent`, `--accent-light`, `--accent-dark`, `--highlight*`, `--bg`, `--bg-elev`, `--bg-sunken`, `--fg`, `--fg-muted`, `--fg-faint`, `--border`, `--border-strong`, `--ease`
- [x] **0.3** — Remove custom `[data-theme="dark"]` overrides (lines 45–57) — brand tokens handle this
- [x] **0.4** — Create a thin `overrides.css` (or section in `global.css`) for **docs-specific** tokens not in the brand system (e.g. `--sidebar-width`, `--header-height`, article typography)
- [x] **0.5** — Update Google Fonts import to include full Outfit weight range (200–700) per brand spec
- [x] **0.6** — Map old variable names → brand variable names across all files. Key mappings:
  - `--bg` → `--bg-page`
  - `--bg-elev` → `--bg-elev` (same name, different value)
  - `--bg-sunken` → `--bg-section-alt`
  - `--fg` → `--text-primary`
  - `--fg-muted` → `--text-secondary`
  - `--fg-faint` → `--text-muted`
  - `--border` → `--border-subtle`
  - `--border-strong` → `--border-strong`
  - `--font-sans` → `--font-primary`
  - `--font-mono` → `--font-mono` (same)
  - `--grid-minor` / `--grid-major` → deferred to Phase 9 (definitions removed, references remain)
- [x] **0.7** — Verify site still builds and renders after token swap (`pnpm build`)

### Phase 1: Header & Navigation
> Replace custom header with brand nav patterns.

- [x] **1.1** — Refactor `Header.astro` to use brand component classes (chevron `.nav-group__chevron` → `.chev`)
- [x] **1.2** — N/A — Header.astro had no inline `<style>` blocks
- [x] **1.3** — Removed ~120 lines of duplicated header CSS from `global.css`; kept docs-specific overrides (active indicator, two-line dropdown items, mobile nav, nav-tools). Replaced hardcoded dark `#b3cc4a` with `var(--accent-text)`.
- [x] **1.4** — Verified: build clean, light + dark themes, active library highlight uses brand accent

### Phase 2: Footer
> Replace custom footer with brand footer pattern.

- [x] **2.1** — Footer.astro already uses brand classes — no markup changes needed
- [x] **2.2** — Removed all footer CSS from `global.css` (21 lines) — fully covered by brand components.css
- [x] **2.3** — Verified: build clean, footer layout, links, version badge render correctly

### Phase 3: Sidebar Navigation
> Adopt brand sidebar and nav-tree components.

- [x] **3.1** — Sidebar.astro already uses brand classes — no markup changes needed
- [x] **3.2** — Removed ~65 lines of duplicated sidebar/nav-tree CSS from `global.css`. Kept docs-specific: sticky positioning, scroll behavior, nested depth indentation, `.num` badges. Removed all `[data-theme="dark"]` hardcoded `#b3cc4a` overrides.
- [x] **3.3** — Verified: nav tree expand/collapse, active page highlight (brand accent blue), numbered sections, light + dark themes

### Phase 4: Homepage (Hub Landing)
> Restyle hero, library cards, and quick-links strip.

- [x] **4.1** — Updated hero SVG stroke from hardcoded `#7a9424` → `var(--accent)`. Hero title `em` uses `var(--accent-text)`. Removed dark `#b3cc4a` override. Graph-paper bg deferred to Phase 9.
- [x] **4.2** — Renamed all `lib-card` → `doc-card` classes in `LibraryCard.astro`. Removed `graph-paper-subtle` class (broken, will use brand graph-paper in Phase 9).
- [x] **4.3** — Quick-strip kept as docs-specific; updated hover color to `var(--accent-text)`.
- [x] **4.4** — Removed ~90 lines of `.lib-card*` CSS from `global.css` — fully covered by brand `.doc-card*`. Kept `.lib-grid` wrapper (docs-specific 2-col layout).
- [x] **4.5** — Verified: card layout, hover animations, CTA arrows, accent colors in light + dark themes. Graph-paper bg deferred to Phase 9.

### Phase 5: Library Landing Pages
> Restyle the per-library index pages.

- [x] **5.1** — Library landing components are docs-specific (no brand equivalent). Kept markup as-is.
- [x] **5.2** — FeatureCell is docs-specific — kept as `.f-cell`. Replaced `var(--accent)` → `var(--accent-text)` for theme-aware colors.
- [x] **5.3** — Removed 7 `[data-theme="dark"]` hardcoded `#b3cc4a` overrides from pills, `.lib-head__tag .idx`, `.f-cell__idx`, `.f-cell__link`. All now use `var(--accent-text)`.
- [x] **5.4** — Verified: feature grid, quick-links pills, section headings, accent pill styling in light + dark themes

### Phase 6: Content / Reference Pages
> Restyle article typography, callouts, tables, code blocks.

- [x] **6.1** — Article heading styles are docs-specific — kept as-is (no brand equivalent).
- [x] **6.2** — Removed all custom callout CSS (~40 lines) — brand `.callout`, `.callout--note`, `.callout--warning` provide full styling with graph-paper overlay. Kept `.article .callout__body p { margin-bottom: 0 }`.
- [x] **6.3** — Updated schema table `.type` column to `var(--accent-text)`. Removed dark override.
- [x] **6.4** — Updated fetch-callout: dark bg gradient from olive `rgba(122,148,36,...)` → blue `rgba(62,147,174,...)`. Dark head/method colors → `var(--accent-text)`. Bullet box-shadow → blue rgba.
- [x] **6.5** — Code block styles are docs-specific — kept as-is.
- [x] **6.6** — Updated `.article a` color to `var(--accent-text)`. Removed dark override.
- [x] **6.7** — Updated breadcrumb `.current` color to `var(--accent-text)` in both content-head and ref-head. Removed dark overrides.
- [x] **6.8** — Removed ~45 lines of duplicated/overridden CSS. Remaining article CSS is docs-specific layout.
- [x] **6.9** — Verified: schema tables, fetch callout, breadcrumbs, article links in light + dark themes

### Phase 7: Search Modal
> Restyle search overlay with brand tokens.

- [x] **7.1** — Updated search modal dark overrides: result focus bg → blue rgba, mark/badge colors → `var(--accent-text)`.
- [x] **7.2** — Search CSS is docs-specific (no brand equivalent modal) — kept as-is, only dark overrides updated.
- [x] **7.3** — Build verified clean.

### Phase 8: Utility Components & Remaining
> Catch anything not covered above.

- [x] **8.1** — PageToc uses existing sidebar/nav tokens — no changes needed.
- [x] **8.2** — VersionBadge handled by brand `.version-badge` since Phase 2.
- [x] **8.3** — Updated guide-head breadcrumb to `var(--accent-text)`. Updated skill-card dark overrides (dl, meta code) to brand accent tokens.
- [x] **8.4** — Guide page CSS is docs-specific — kept as-is, only dark overrides updated.
- [x] **8.5** — Responsive overrides are docs-specific (sidebar collapse, grid changes) — kept. **All `#b3cc4a` and `rgba(122,148,36,...)` removed from entire codebase.**

### Phase 9: Graph Paper Backgrounds
> Replace hardcoded SVG grid patterns with brand graph-paper classes.

- [x] **9.1** — Removed custom `.graph-paper` and `.graph-paper-subtle` CSS (17 lines) using broken `--grid-*` tokens. Brand `components.css` now provides `.graph-paper` via `::before` pseudo-element with brand blue SVGs.
- [x] **9.2** — `--grid-minor/major/width` tokens were already removed in Phase 0.2. No references remain.
- [x] **9.3** — Verified: hero graph paper renders in both light and dark themes using brand blue pattern.

### Phase 10: Cleanup & QA
> Final audit of CSS, remove dead code, full-site test.

- [x] **10.1** — Audited `global.css`: 1,375 lines (down from 1,819, -444 lines / -24%). Remaining CSS is docs-specific layout (article typography, schema tables, search modal, guide pages, responsive overrides). Zero old olive green colors, zero old token names, zero duplicated brand CSS.
- [x] **10.2** — No `.astro` files have inline `<style>` that duplicates brand CSS. Only 2 inline style attrs remain (Header logo separator, SearchModal fallback message) — both use brand tokens.
- [x] **10.3** — Visual QA: tested homepage, library landing (PHX), content page (API ref), reference page (schema tables), guide pages (LLM setup, Phius certification) in both light and dark themes.
- [ ] **10.4** — Responsive QA: not yet tested at breakpoints (deferred — requires browser resize tooling).
- [x] **10.5** — Pagefind search works — 167 pages indexed on every build.
- [x] **10.6** — All navigation links functional across tested pages.
- [x] **10.7** — `pnpm build` clean: 170 pages, zero warnings, zero errors.

---

## Variable Name Migration Reference

Quick-reference for the find-and-replace pass in Phase 0.6:

```
OLD (custom)              →  NEW (brand tokens.css)
──────────────────────────────────────────────────
--accent                  →  --accent              (value changes: #7a9424 → #3E93AE)
--accent-light            →  --accent-light         (value changes: #e8ecd8 → #d6ebf1)
--accent-dark             →  --accent-dark          (value changes: #4a5916 → #2d6b80)
--highlight               →  --highlight            (value changes: #DC2626 → #E23489)
--highlight-light         →  --highlight-light       (value changes)
--highlight-dark          →  --highlight-dark        (value changes)
--highlight-darker        →  --highlight-darker      (value changes)
--bg                      →  --bg-page
--bg-elev                 →  --bg-elev
--bg-sunken               →  --bg-section-alt
--fg                      →  --text-primary
--fg-muted                →  --text-secondary
--fg-faint                →  --text-muted
--border                  →  --border-subtle
--border-strong           →  --border-strong
--font-sans               →  --font-primary
--font-mono               →  --font-mono            (same name)
--ease                    →  --ease                  (same name, same value)
```

## Component Class Migration Reference

```
OLD (custom)              →  NEW (brand components.css)
──────────────────────────────────────────────────
.lib-card                 →  .doc-card
.lib-card index           →  .doc-card__idx
.lib-card tag             →  .doc-card__tag
.lib-card name            →  .doc-card__name
.lib-card desc            →  .doc-card__desc
.lib-card footer          →  .doc-card__footer
.pill                     →  .btn-ghost / .btn-primary
.pill--accent             →  .btn-primary
.icon-btn                 →  .icon-btn              (same)
header styles             →  .site-header, .site-header__logo
footer styles             →  .site-footer, .site-footer__left/right
sidebar                   →  .sidebar, .sidebar__label
nav tree                  →  .nav-tree, .nav-tree .group, .is-active
search button             →  .search-btn
callout--note             →  .callout--note          (same name, brand styling)
callout--warning          →  .callout--warning       (same name, brand styling)
graph-paper               →  .graph-paper            (same name, brand SVGs)
```

---

## Notes

- **No content changes** — markdown files, nav.yml, libraries.yml, fetch_spokes.py are all untouched.
- **Astro structure unchanged** — same layouts, same routing, same content collections.
- **Brand components.css provides ~40 ready-made classes** — the goal is to use them and delete custom CSS, not to rebuild from scratch.
- **Phase 0 is the riskiest** — the variable rename touches every file. Do it first, verify the build, then proceed phase-by-phase.
- **Each phase ends with a verify step** — don't move to the next phase until the current one renders correctly.
