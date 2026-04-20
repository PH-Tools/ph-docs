# PH-Docs Hub — Implementation Plan

**Stack**: Astro 5 · TypeScript · Pagefind · GitHub Actions · GitHub Pages  
**Repo**: `PH-Tools/ph-docs`  
**Live URL**: `docs.passivehousetools.com`  
**Date**: April 2026

---

## 1. What This Is

A unified documentation hub for PH-Tools open-source libraries. Documentation is **authored in each library's own repo** (spoke) and **assembled + published from this hub**. The hub contains no original content — only the build machinery and design system.

**Spoke repos** (all already have `docs/index.md`, `docs/nav.yml`, and `notify-hub.yml`):
- `PH-Tools/honeybee_ph`
- `PH-Tools/PHX`
- `PH-Tools/honeybee_revive`

`ph-reference-docs` is deferred. The hub is built to handle missing/skipped spokes gracefully.

---

## 2. Why Astro, Not MkDocs

The Claude Design mockup requires:
- Custom hero with SVG linework + graph-paper backgrounds
- Library card grid with hover animations and numbered indices
- Custom sidebar with dashed tree lines, accent-bar active states, numbered items
- Schema tables with type/field/description columns and styled REQ badges
- Fetch callout component (LLM-ready URL block)
- Grouped search modal with per-library result sections

MkDocs Material is opinionated about all of these. Matching the mockup would require overriding ~70% of Material's Jinja2 templates and fighting its CSS specificity — fragile and painful on upgrades. Astro gives full UI control while staying content/Markdown-native.

**What carries over unchanged from the strategy doc**:
- Hub-and-spoke content model
- `libraries.yml` registry format (+ minor additions)
- `fetch_spokes.py` logic (adapted destination path)
- `notify-hub.yml` spoke trigger pattern (already deployed)
- GitHub Actions build/deploy structure
- bldgtyp design tokens from CDN

---

## 3. Hub Repository Structure

```
ph-docs/
├── astro.config.ts             # Astro config: output=static, Pagefind integration
├── tsconfig.json
├── package.json
├── libraries.yml               # Registry of spoke repos (extended — see §5)
├── CNAME                       # docs.passivehousetools.com
│
├── scripts/
│   └── fetch_spokes.py         # Fetches spoke /docs into src/content/docs/
│
├── src/
│   ├── content/
│   │   └── docs/               # Git-ignored. Populated at build time.
│   │       ├── honeybee-ph/
│   │       │   └── index.md
│   │       ├── phx/
│   │       │   ├── index.md
│   │       │   ├── nav.yml
│   │       │   ├── dev/
│   │       │   │   ├── architecture.md
│   │       │   │   └── exporter-patterns.md
│   │       │   └── reference/
│   │       │       └── ...
│   │       └── honeybee-revive/
│   │           └── index.md
│   │
│   ├── layouts/
│   │   ├── HubLayout.astro         # Screen 1 — hub landing shell
│   │   ├── LibraryLayout.astro     # Screen 2 — library landing + sidebar shell
│   │   └── ContentLayout.astro     # Screen 2 — article page + sidebar shell
│   │
│   ├── components/
│   │   ├── Header.astro            # Sticky nav: logo + primary nav + search + theme
│   │   ├── Footer.astro            # Shared footer
│   │   ├── Sidebar.astro           # Collapsible nav tree from nav.yml
│   │   ├── SearchModal.astro       # Grouped search overlay (Pagefind)
│   │   ├── LibraryCard.astro       # Hub landing grid card
│   │   ├── FeatureCell.astro       # Library landing section card
│   │   ├── FetchCallout.astro      # LLM-ready URL callout block
│   │   └── SchemaTable.astro       # MDX component for schema field tables
│   │
│   ├── pages/
│   │   ├── index.astro             # Hub landing (Screen 1)
│   │   ├── [lib]/
│   │   │   ├── index.astro         # Library landing (Screen 2)
│   │   │   └── [...slug].astro     # Content page (markdown rendered)
│   │
│   ├── lib/
│   │   ├── nav.ts                  # nav.yml parser + NavTree type
│   │   ├── libraries.ts            # libraries.yml parser + LibraryMeta type
│   │   └── frontmatter.ts          # Front-matter schema + parser
│   │
│   └── styles/
│       └── global.css              # Design system (ported from mockup + bldgtyp CDN import)
│
└── .github/
    └── workflows/
        ├── build.yml               # Main build + deploy workflow
        └── validate.yml            # PR check: does hub build cleanly?
```

---

## 4. Content Pipeline

### 4.1 `fetch_spokes.py`

Logic is identical to the strategy doc spec. The only change is the destination path: content lands in `src/content/docs/<lib-id>/` instead of `assembled/<lib-id>/`.

```
Input:  libraries.yml
Output: src/content/docs/<lib-id>/   (sparse-cloned from each spoke's /docs)
        build_manifest.json          (which spokes succeeded / skipped)
```

Graceful degradation is unchanged: any spoke failure is logged, skipped, and the build continues. Exit code is always 0.

### 4.2 Build sequence

```
python scripts/fetch_spokes.py   →   npm run build   →   deploy to gh-pages
```

MkDocs's `build_nav.py` step is eliminated — Astro reads nav.yml directly at build time via `src/lib/nav.ts`.

---

## 5. `libraries.yml` — Extended Format

The existing format from the strategy doc is extended with card metadata for the **hub landing library cards** (Screen 1). These fields are hub-controlled (not spoke-controlled) because the hub landing is a hub concern.

```yaml
libraries:
  - id:          honeybee-ph
    repo:        PH-Tools/honeybee_ph
    label:       Honeybee-PH
    docs_path:   docs/
    branch:      main
    enabled:     true
    # Hub landing card metadata:
    index:       "01"
    tag_line:    "GRASSHOPPER · PYTHON"
    category:    "Modeling"
    description: "Grasshopper-native Passive House modeling. Build PH-compliant
                  models inside Rhino using familiar Honeybee components."

  - id:          phx
    repo:        PH-Tools/PHX
    label:       PHX
    enabled:     true
    index:       "02"
    tag_line:    "PYTHON · DATA MODEL"
    category:    "Exchange"
    description: "Passive House Exchange data model & file I/O. Convert between
                  WUFI XML, PHPP Excel, and Phius report formats."

  - id:          honeybee-revive
    repo:        PH-Tools/honeybee_revive
    label:       Honeybee-REVIVE
    enabled:     true
    index:       "03"
    tag_line:    "GRASSHOPPER · ANALYSIS"
    category:    "Analysis"
    description: "Carbon & energy analysis for building design. Resilience &
                  embodied-carbon workflows for Phius REVIVE."
```

---

## 6. Content Conventions in Spoke Repos

### 6.1 `docs/index.md` — Library landing front-matter

Each spoke's `docs/index.md` provides the header content for its library landing page (Screen 2: the large title, description, and pill tags).

```yaml
---
title: PHX
subtitle: "Passive House Exchange — format conversion between Honeybee-PH, PHPP, and WUFI-Passive."
version: "1.4.0"
pills:
  - "v1.4.0 — latest"
  - "WUFI · PHPP · Phius"
  - "Python 3.10+"
---
```

If any of these are absent, the hub falls back to the `label` from `libraries.yml` and renders the library landing without pills or version.

### 6.2 Section card front-matter (feature grid on library landing)

The library landing page (Screen 2) shows a feature grid — one card per **top-level nav group** (not leaves, not Overview). Cards link to the group's first page.

**Convention**: Card metadata lives in the **first file listed under each top-level nav group**.

For PHX `nav.yml`:
```yaml
nav:
  - Overview: index.md
  - Developer:
    - Architecture: dev/architecture.md        ← card data lives here
    - Exporter & Importer Patterns: dev/exporter-patterns.md
  - Reference:
    - PHX Model Reference: reference/phx-model-reference.md  ← card data lives here
    - WUFI XML Schema: reference/wufi-xml-schema.md
```

So `dev/architecture.md` and `reference/phx-model-reference.md` each get front-matter:

```yaml
---
title: Developer Guide
card_title: Developer Guide
card_description: "Architecture decisions, exporter/importer patterns, and
                   the conventions for extending PHX."
card_index: "01"
---
```

The hub's `nav.ts` parser reads nav.yml, finds all top-level groups, then reads front-matter from each group's first file to build the feature grid. If a spoke has no groups (e.g., honeybee-ph currently has only `Overview: index.md`), the feature grid section is simply omitted from that library's landing page.

**Why first-file-per-group, not arbitrary files**: 
The first file in a nav group is the natural "section landing page" — the entry point when someone clicks the group in the sidebar. Putting card metadata there is intuitive. A contributor editing the Developer section would look at `dev/architecture.md` first. Making this an explicit convention (documented in spoke repo READMEs) makes it predictable.

### 6.3 `nav.yml` format

No format changes required. The existing MkDocs-style format is parsed by `src/lib/nav.ts`:

```yaml
nav:
  - Overview: index.md                          # leaf: {label: path}
  - Developer:                                  # group: {label: [items]}
    - Architecture: dev/architecture.md
    - Exporter & Importer Patterns: dev/exporter-patterns.md
  - Reference:
    - PHX Model Reference: reference/phx-model-reference.md
```

Parsed into TypeScript:
```ts
type NavLeaf  = { label: string; path: string };
type NavGroup = { label: string; children: NavItem[] };
type NavItem  = NavLeaf | NavGroup;
type NavTree  = NavItem[];
```

---

## 7. Astro Pages & Routing

### 7.1 Hub landing — `src/pages/index.astro`
- Renders Screen 1 from the mockup exactly
- Reads `libraries.yml` for library card data
- Hero section with graph-paper background + SVG architectural linework (ported from mockup)
- Library card grid (2-column, `LibraryCard` component × N libraries)
- Quick strip (static content: Getting Started, install command, Changelog, GitHub)
- Footer

### 7.2 Library landing — `src/pages/[lib]/index.astro`
- `getStaticPaths()` returns one entry per enabled library in `libraries.yml`
- Renders Screen 2 from the mockup
- Reads `src/content/docs/[lib]/index.md` for front-matter (title, subtitle, version, pills)
- Reads `src/content/docs/[lib]/nav.yml` → builds sidebar nav tree
- Reads card front-matter from first file of each top-level nav group → builds feature grid
- Quick links row (pills linking to first page of each nav group + GitHub)

### 7.3 Content page — `src/pages/[lib]/[...slug].astro`
- `getStaticPaths()` reads nav.yml from each library and generates one path per leaf
- Renders the markdown file through `ContentLayout` (sidebar + article area)
- Sidebar is identical to library landing sidebar, with current page highlighted
- Markdown body is rendered with Astro's built-in Markdown pipeline
- MDX optional: `FetchCallout` and `SchemaTable` can be imported as components in `.mdx` files

---

## 8. Design System

All styles are ported directly from the mockup (`styles.css` + `screens.css`). Structure in `src/styles/global.css`:

```css
@import url('https://bldgtyp.github.io/branding/tokens/tokens.css'); /* bldgtyp CDN */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;600&family=JetBrains+Mono:wght@300;400&display=swap');

/* CSS custom properties (light + dark) */
/* Graph paper utilities (.graph-paper, .graph-paper-subtle) */
/* Typography primitives (.label, .mono, .h-display, etc.) */
/* Header / nav */
/* Buttons / pills */
/* Layout shells (.screen, .with-sidebar) */
/* Sidebar */
/* Main content */
/* Modal / search */
/* Screen-specific (hero, lib cards, feature grid, schema tables, fetch callout, search) */
```

No CSS adapter layer is needed — the mockup already uses bldgtyp tokens directly. The tokens CDN import is the only external dependency.

Theme toggle wires to `data-theme="light" | "dark"` on `<html>`, matching the mockup's implementation.

---

## 9. Search (Pagefind)

Pagefind is a static search library that runs at build time, indexes all rendered HTML, and produces a client-side search bundle. It produces grouped results naturally (one group per library) which matches Screen 4 of the mockup.

Integration:
1. `astro-pagefind` integration added to `astro.config.ts` — runs automatically after `astro build`
2. `SearchModal.astro` wraps the Pagefind UI with the mockup's search modal styles
3. The existing `⌘K` keyboard handler from the mockup is preserved
4. Search results are scoped per library via Pagefind's built-in filtering (data attributes on page wrappers)

---

## 10. GitHub Actions

### 10.1 Secrets (already configured)
- `ph-docs-hub-dispatch` — PAT with `workflow` scope on `PH-Tools/ph-docs`. Used by spoke repos' `notify-hub.yml` to trigger hub rebuilds when `/docs/**` changes.
- `ph-docs-pages-deploy` — PAT with `contents: write` on `PH-Tools/ph-docs`. Used by the hub's `build.yml` to push to the `gh-pages` branch.

### 10.2 `build.yml` — Main workflow

**Triggers**:
- `schedule`: nightly at 02:00 UTC (safety net)
- `repository_dispatch` with `event_type: docs-updated` (fired by spoke `notify-hub.yml`)
- `workflow_dispatch` (manual)

**Steps**:
```
1. Checkout ph-docs (main)
2. Set up Python 3.11
3. pip install -r requirements.txt  (pyyaml, requests)
4. python scripts/fetch_spokes.py   (sparse-clone each spoke's /docs into src/content/docs/)
5. Set up Node 20 + pnpm
6. pnpm install
7. pnpm build                        (astro build + pagefind index)
8. Deploy dist/ to gh-pages branch   (peaceiris/actions-gh-pages, using ph-docs-pages-deploy)
9. Log build summary (which spokes succeeded / skipped)
```

### 10.3 `validate.yml` — PR check

Runs on PRs to main. Runs `fetch_spokes.py` + `astro build` (no deploy). Confirms the hub builds cleanly before merge.

---

## 11. Deployment

- **GitHub Pages source**: `gh-pages` branch, `/ (root)` directory
- **Custom domain**: `docs.passivehousetools.com` (DNS already updated in DreamHost)
- **CNAME file**: `CNAME` in repo root containing `docs.passivehousetools.com` — copied to `dist/` by Astro at build time via `public/CNAME`
- **HTTPS**: Enforced via GitHub Pages settings (automatic after custom domain is set)

---

## 12. Implementation Phases

Phases are sequential. Each phase produces something verifiable before the next begins.

### Phase 1 — Astro Scaffold + Design System ✅ COMPLETE (2026-04-19)
**Goal**: Working Astro project that renders the hub landing page with correct design, no real content.

1. ✅ Scaffolded Astro manually in existing repo (package.json, astro.config.ts, tsconfig.json)
2. ✅ Install dependencies: js-yaml, gray-matter (pagefind/astro-pagefind deferred to Phase 6)
3. ✅ Port `styles.css` + `screens.css` from mockup → `src/styles/global.css` (all screens ported)
4. ✅ Implement `Header.astro` (logo, 3 library nav links, search button, theme toggle, GitHub)
5. ✅ Implement `Footer.astro`
6. ✅ Implement hub landing `src/pages/index.astro` with 3 static library cards (Reference Docs deferred)
7. ✅ Implement theme toggle (localStorage + `data-theme` on `<html>`, inline script prevents flash)
8. ✅ **Verify**: `pnpm dev` + `pnpm build` both succeed; light + dark mode match mockup

**Notes**: Created `BaseLayout.astro` as shared HTML shell (not in original plan). `LibraryCard.astro` extracted as typed component in this phase (plan had it in Phase 3). `.gitignore` updated for Astro/Node.

### Phase 2 — `libraries.yml` + Content Pipeline ✅ COMPLETE (2026-04-19)
**Goal**: `fetch_spokes.py` runs, spoke docs land in `src/content/docs/`, manifest is written.

1. ✅ Write `libraries.yml` with all three spokes + extended card metadata fields
2. ✅ Write `scripts/fetch_spokes.py` (sparse-clone each spoke's `/docs` → `src/content/docs/<id>/`)
3. ✅ Add `src/content/docs/` to `.gitignore` (done in Phase 1)
4. ✅ Write `src/lib/libraries.ts` — parses `libraries.yml`, exports `LibraryMeta[]`
5. ✅ Write `src/lib/nav.ts` — parses `nav.yml`, exports `NavTree` type + parser + helpers
6. ✅ Write `src/lib/frontmatter.ts` — reads front-matter from MD files using `gray-matter`
7. ✅ **Verify**: `fetch_spokes.py` populates `src/content/docs/` with all 3 spokes; manifest shows 3 succeeded, 0 skipped; `pnpm build` passes

**Notes**: Created `requirements.txt` (pyyaml) and `.venv` for the Python fetch script. `nav.ts` includes `getFirstFilePerGroup()` and `getAllLeafPaths()` helpers for Phases 4-5.

### Phase 3 — Hub Landing with Real Data (Screen 1) ✅ COMPLETE (2026-04-19)
**Goal**: Hub landing page renders real library data from `libraries.yml`.

1. ✅ Update `src/pages/index.astro` to read `LibraryMeta[]` via `getLibraries()`
2. ✅ `LibraryCard.astro` updated to use `LibraryMeta` type directly (created in Phase 1, retyped here)
3. ✅ Library grid renders from real `libraries.yml` data
4. ✅ Card `href` attributes point to `/{lib-id}/` routes
5. ✅ **Verify**: Hub landing shows 3 real library cards with correct metadata, build passes

### Phase 4 — Library Landing Page (Screen 2) ✅ COMPLETE (2026-04-19)
**Goal**: `/{lib-id}/` routes render the library landing with sidebar, header, and feature grid.

1. ✅ Implement `src/pages/[lib]/index.astro` with `getStaticPaths()` over enabled libraries
2. ✅ Read `docs/index.md` front-matter per library → title, subtitle, version, pills (with fallback to `libraries.yml` label when front-matter absent)
3. ✅ Parse `nav.yml` → pass `NavTree` to `Sidebar.astro`
4. ✅ Implement `Sidebar.astro` — collapsible nav tree, numbered items, accent-bar active state, auto-expand group containing current page
5. ✅ Sidebar + content area via `with-sidebar` grid (used `BaseLayout` with `hideFooter` prop instead of separate `LibraryLayout`)
6. ✅ For each top-level nav group: read first-file front-matter → `FeatureCell.astro` cards (falls back to nav group label when card front-matter absent)
7. ✅ Implement `FeatureCell.astro` — feature grid card
8. ✅ Quick links row (pills per nav group + GitHub)
9. ✅ **Verify**: `/phx/` renders with sidebar (Overview, Developer, Reference), feature grid with 2 cards, quick links, correct header highlight; `/honeybee-ph/` renders with sidebar only (no feature grid, no quick links — correct for no nav groups)

**Notes**: Updated `Header.astro` to accept `activeLib` prop and render nav links from `getLibraries()` with active state. `BaseLayout` extended with `activeLib` and `hideFooter` props. Library landing renders its own footer inside the sidebar layout.

### Phase 5 — Content Pages ✅ COMPLETE (2026-04-19)
**Goal**: `/{lib-id}/{slug}` routes render markdown content inside the library layout.

1. ✅ Implement `src/pages/[lib]/[...slug].astro` with `getStaticPaths()` reading nav.yml leaves (skips `index.md` — handled by library landing)
2. ✅ Content layout reuses `with-sidebar` grid + `Sidebar` component (no separate `ContentLayout.astro` needed — same pattern as library landing)
3. ✅ Render markdown via Astro content collections: `src/content.config.ts` defines `docs` collection with glob loader over `src/content/docs/**/*.md`; pages use `getEntry()` + `render()` → `<Content />` component
4. ✅ Article typography styles added to `global.css`: headings (h1–h4), paragraphs, lists, code blocks (Shiki syntax highlighting via Astro default), blockquotes, tables, horizontal rules, images
5. ✅ Implement `FetchCallout.astro` — LLM-ready URL callout with copy-to-clipboard, ported from Screen 3 mockup. Available for future MDX use.
6. ✅ Implement `SchemaTable.astro` — field/type/description table with REQ badges, ported from Screen 3 mockup. Available for future MDX use.
7. ✅ Sidebar active state works: current page highlighted with `is-active`, parent group auto-expanded with `is-open`; breadcrumb shows group label + page label
8. ✅ **Verify**: 9 pages built — `/phx/dev/architecture/` renders with correct sidebar state, breadcrumb, and full markdown content with syntax-highlighted code blocks

**Notes**: Fixed `import.meta.dirname` path resolution bug — during Astro's build phase, `import.meta.dirname` resolves to `dist/chunks/` instead of `src/lib/`. All path resolution in `nav.ts`, `frontmatter.ts`, and `libraries.ts` switched to `process.cwd()`. This bug was latent in Phases 1-4 (frontmatter functions silently returned empty fallback objects) but became blocking in Phase 5 since `getStaticPaths()` depends on `getNavTree()` to discover content pages. `FetchCallout` and `SchemaTable` components are created but not currently used in any pages — all spoke content is plain `.md` without front-matter. They will be used when spokes adopt MDX or when `ph-reference-docs` is created.

### Phase 6 — Search (Screen 4) ✅ COMPLETE (2026-04-19)
**Goal**: `⌘K` opens search modal, search returns grouped results across all libraries.

1. ✅ Install `pagefind` dev dependency; update build script to `astro build && pagefind --site dist`
2. ✅ Add `data-pagefind-body` and `data-pagefind-meta="library:${lib.label}"` to content areas in `[...slug].astro` and `[lib]/index.astro` — hub landing excluded (navigation-only page)
3. ✅ Implement `SearchModal.astro` — modal scrim + search input + grouped results area + keyboard hint footer, ported from Screen 4 mockup
4. ✅ Wire Pagefind JS API via `is:inline` script (Vite cannot resolve Pagefind's post-build JS): lazy-loads `/pagefind/pagefind.js`, debounced search (150ms), results grouped by `library` meta field, rendered with per-library headers and result counts
5. ✅ Keyboard handlers: `⌘K`/`Ctrl+K` toggles modal, `Escape` closes, `↑↓` navigate results with `is-focused` class, `Enter` opens focused result; click-outside-to-close on scrim
6. ✅ `SearchModal` included in `BaseLayout.astro` — available on all pages
7. ✅ **Verify**: `pnpm build` succeeds (9 pages + Pagefind index); Pagefind indexed 8 pages / 2500 words across all libraries

**Notes**: Pagefind's JS is only available after build, so the search script uses `is:inline` to bypass Vite's module resolution. Search results use `<a>` tags (not `<div>`) for native link behavior — added `text-decoration:none; color:inherit` to `.search-result` CSS. The `abbreviate()` function generates short library badges from display names (e.g., "Honeybee-PH" → "HP"). Search does not work in `pnpm dev` mode — only after `pnpm build` + `pnpm preview`.

### Phase 7 — GitHub Actions + Deployment
**Goal**: Pushes to spoke `/docs` auto-rebuild the live site at `docs.passivehousetools.com`.

1. Write `public/CNAME` containing `docs.passivehousetools.com`
2. Write `.github/workflows/build.yml` — triggers: schedule + `repository_dispatch` + `workflow_dispatch`
3. Write `.github/workflows/validate.yml` — PR check
4. Push to `PH-Tools/ph-docs` main branch
5. Enable GitHub Pages on the `gh-pages` branch in repo settings
6. Set custom domain to `docs.passivehousetools.com` in GitHub Pages settings (HTTPS enforce)
7. Manually trigger `workflow_dispatch` run → confirm site builds and deploys
8. **Verify**: `docs.passivehousetools.com` serves the hub landing; push a change to PHX `/docs` → hub rebuilds within ~5 minutes

---

## 13. Deferred / Out of Scope

| Item | Why deferred |
|------|-------------|
| `ph-reference-docs` spoke | Repo not yet created; unclear if needed |
| Auto-generated API docs (mkdocstrings equivalent) | Requires separate tooling; add in a future phase once content conventions are stable |
| MDX adoption across all spoke pages | Spokes currently write plain `.md`; MDX components (`FetchCallout`, `SchemaTable`) are available but not required |
| honeybee_ph and honeybee_revive nav expansion | Those repos only have `Overview: index.md` — feature grids will populate automatically once they add nav groups |

---

## 14. Spoke Repo Contributor Guide (to be written separately)

Once the hub is live, each spoke repo gets a short `DOCS.md` at its root explaining:
- The `docs/` folder structure
- The `index.md` front-matter schema (title, subtitle, version, pills)
- The section card front-matter convention (card_title, card_description in the first file of each nav group)
- How to add a new nav section
- How to use MDX components (FetchCallout, SchemaTable) in `.mdx` files
- How `notify-hub.yml` triggers a hub rebuild on push to `/docs/**`
