# Architecture: Hub-and-Spoke Build Pipeline

This document explains exactly how the PH-Tools docs site is built — from source files scattered across multiple GitHub repos to a single deployed website. Read this if you need to debug the build, add a new library, or understand why things are structured the way they are.

---

## The Core Idea

Documentation is **authored in each library's own repo** (the "spokes"), but **published as one unified site** (the "hub"). This repo (`ph-docs`) is the hub. It contains no library documentation — only the build machinery, design system, and Astro components that fetch, assemble, and render the site.

The key benefit: a developer working on PHX writes docs in `PHX/docs/` and never touches this repo. The hub picks up their changes automatically.

---

## What Lives Where

### This repo (`ph-docs`) owns:

- The build script (`scripts/fetch_spokes.py`)
- The library registry (`libraries.yml`)
- The Astro project (`astro.config.ts`, `src/`)
  - Pages: hub landing, library landing, content pages
  - Components: Header, Sidebar, LibraryCard, FeatureCell, SearchModal, etc.
  - Layouts: HubLayout, LibraryLayout, ContentLayout
  - Utilities: `src/lib/nav.ts`, `src/lib/libraries.ts`, `src/lib/frontmatter.ts`
  - Design system: `src/styles/global.css`
- The GitHub Actions workflows (`.github/workflows/`)
- The CNAME file (`public/CNAME` → `docs.passivehousetools.com`)

### Spoke repos own:

- Their own documentation content (`docs/index.md`, tutorials, API docs, etc.)
- Their own navigation structure (`docs/nav.yml`)
- A small dispatch workflow (`.github/workflows/notify-hub.yml`)

### Nobody owns (generated at build time):

- `src/content/docs/` — temporary directory where spoke markdown lands
- `dist/` — final static HTML output from Astro

Both are git-ignored.

---

## The Build Pipeline, Step by Step

Every build — whether local, nightly CI, or dispatch-triggered — runs these two commands in sequence:

```
python scripts/fetch_spokes.py  →  pnpm build  (astro build + pagefind index)
```

Here is exactly what each step does.

### Step 1: `fetch_spokes.py` — Gather Content

**Input**: `libraries.yml` (the registry)

**Output**: `src/content/docs/` directory populated with spoke markdown

For each enabled entry in `libraries.yml`, the script:

1. **Sparse-clones** the repo — downloads only the `/docs` subtree (not the full repo with source code, tests, etc.)
2. **Validates** that `index.md` and `nav.yml` exist
3. **Copies** the docs into `src/content/docs/<lib-id>/`

After fetching honeybee-ph and PHX:

```
src/content/docs/
├── honeybee-ph/          ← sparse-cloned from PH-Tools/honeybee_ph/docs/
│   ├── index.md
│   └── nav.yml
└── phx/                  ← sparse-cloned from PH-Tools/PHX/docs/
    ├── index.md
    ├── nav.yml
    ├── dev/
    │   ├── architecture.md
    │   └── exporter-patterns.md
    └── reference/
        ├── phx-model-reference.md
        └── wufi-xml-schema.md
```

**Graceful degradation**: If a spoke fails (repo not found, branch missing, no docs folder, missing required files), the script logs a warning and skips it. It never aborts. Partial builds are valid — the site just won't include that library's section. The script always exits 0.

**Build manifest**: The script writes `src/content/docs/build_manifest.json` recording which spokes succeeded and which were skipped:

```json
{
  "succeeded": ["honeybee-ph", "phx"],
  "skipped": [
    {"id": "honeybee-revive", "reason": "docs not found in repo"}
  ]
}
```

### Step 2: `pnpm build` — Generate the Site

**Input**: `libraries.yml` + `src/content/docs/` (populated by step 1) + Astro source (`src/`)

**Output**: `dist/` — static HTML + assets + Pagefind search index, ready to deploy

Astro reads the assembled markdown from `src/content/docs/`, passes it through the appropriate layout and components, and outputs static HTML. Navigation is built at compile time by `src/lib/nav.ts`, which parses each spoke's `nav.yml` directly — there is no separate nav-assembly script.

Pagefind runs automatically after Astro's build, crawls the rendered HTML in `dist/`, and writes a search index. The search modal (`SearchModal.astro`) uses this index client-side with results grouped by library.

---

## How Content Flows Through the System

```
PH-Tools/PHX  /docs/  ──────────────→  src/content/docs/phx/
  index.md                               index.md       (library header front-matter)
  nav.yml                                nav.yml        (→ Sidebar + feature grid)
  dev/architecture.md                    dev/architecture.md  (card front-matter)
  dev/exporter-patterns.md               dev/exporter-patterns.md
  reference/phx-model-reference.md       reference/phx-model-reference.md

                        ↓  Astro build
            src/pages/[lib]/index.astro     →  /phx/                (library landing)
            src/pages/[lib]/[...slug].astro →  /phx/dev/architecture/ (content page)

                        ↓  Pagefind
            dist/_pagefind/   (search index, grouped by library)
```

---

## How Spokes Trigger Rebuilds

When a developer pushes changes to `/docs/**` on main in a spoke repo, a small GitHub Actions workflow fires:

```
Spoke repo push to /docs  →  notify-hub.yml  →  POST repository_dispatch to ph-docs  →  build.yml runs
```

The dispatch workflow (`notify-hub.yml`) uses the `ph-docs-hub-dispatch` org-level secret to call the GitHub API. The hub's `build.yml` workflow listens for `repository_dispatch` events with type `docs-updated`.

Spoke doc changes appear on the live site within a few minutes of merging to main, with no manual intervention.

---

## `libraries.yml` — The Registry

This file is the single source of truth for which repos contribute docs and how their hub landing cards appear. Each entry:

```yaml
- id:          phx                    # Subdirectory name in src/content/docs/
  repo:        PH-Tools/PHX           # GitHub org/repo
  label:       PHX                    # Display name in nav and sidebar
  docs_path:   docs/                  # Path inside repo (default: docs/)
  branch:      main                   # Branch to fetch (default: main)
  enabled:     true                   # Set false to skip without removing
  # Hub landing card metadata (Screen 1):
  index:       "02"                   # Display order number
  tag_line:    "PYTHON · DATA MODEL"  # Type tags shown on card
  category:    "Exchange"             # Category label (accent-colored)
  description: "Passive House Exchange data model & file I/O."
```

Adding a new library = adding one entry here. The build pipeline discovers it automatically.

---

## Content Conventions in Spoke Repos

### `docs/index.md` — Library landing header

The spoke's `docs/index.md` provides front-matter for the library landing page header (Screen 2: large title, description, version, and pill tags):

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

If absent, the hub falls back to the `label` from `libraries.yml` with no pills.

### Section card front-matter — feature grid

The library landing page shows a feature grid with one card per top-level nav group. Card metadata lives in the **first file of each nav group**:

```yaml
# docs/dev/architecture.md (first file under "Developer" group)
---
title: Architecture
card_title: Developer Guide
card_description: "Architecture decisions, exporter/importer patterns, and
                   conventions for extending PHX."
card_index: "01"
---
```

If a spoke has no nav groups (only a flat `Overview: index.md`), the feature grid is omitted.

### `docs/nav.yml` — Navigation structure

Standard MkDocs-style nav format. No changes needed from existing spoke repos:

```yaml
nav:
  - Overview: index.md
  - Developer:
    - Architecture: dev/architecture.md
    - Exporter & Importer Patterns: dev/exporter-patterns.md
  - Reference:
    - PHX Model Reference: reference/phx-model-reference.md
    - WUFI XML Schema: reference/wufi-xml-schema.md
```

Parsed by `src/lib/nav.ts` into a typed `NavTree` at build time. Two item types:
- **Leaf**: `{ label: string; path: string }` — links to a specific page
- **Group**: `{ label: string; children: NavItem[] }` — collapsible section

---

## Astro Project Structure

```
src/
├── content/docs/           # Git-ignored — populated by fetch_spokes.py
│
├── layouts/
│   ├── HubLayout.astro     # Hub landing (Screen 1) — no sidebar
│   ├── LibraryLayout.astro # Library landing (Screen 2) — sidebar + feature grid
│   └── ContentLayout.astro # Article page — sidebar + markdown body
│
├── components/
│   ├── Header.astro        # Sticky: logo · primary nav · ⌘K search · theme toggle
│   ├── Footer.astro        # Shared footer
│   ├── Sidebar.astro       # Collapsible nav tree built from NavTree
│   ├── SearchModal.astro   # ⌘K overlay powered by Pagefind
│   ├── LibraryCard.astro   # Hub landing grid card (2-column)
│   ├── FeatureCell.astro   # Library landing section card (2-column grid)
│   ├── FetchCallout.astro  # LLM-ready URL callout (MDX component)
│   └── SchemaTable.astro   # Field/type/description table (MDX component)
│
├── pages/
│   ├── index.astro                 # /           → hub landing
│   ├── [lib]/
│   │   ├── index.astro             # /{lib}/     → library landing
│   │   └── [...slug].astro         # /{lib}/...  → content page
│
├── lib/
│   ├── nav.ts              # Parses nav.yml → NavTree; finds first-file per group
│   ├── libraries.ts        # Parses libraries.yml → LibraryMeta[]
│   └── frontmatter.ts      # Reads front-matter from assembled MD files
│
└── styles/
    └── global.css          # Full design system (bldgtyp tokens CDN + mockup styles)
```

---

## Design System

`src/styles/global.css` imports the bldgtyp CDN tokens and defines the full design system:

```css
@import url('https://bldgtyp.github.io/branding/tokens/tokens.css');  /* CDN */
@import url('https://fonts.googleapis.com/...');                       /* Outfit + JetBrains Mono */
```

Key CSS custom properties (defined in the file, not from CDN):

| Variable | Value | Usage |
|---|---|---|
| `--accent` | `#7a9424` | Active states, links, borders |
| `--accent-light` | `#e8ecd8` | Card hover backgrounds |
| `--accent-dark` | `#4a5916` | Dark text on light accent |
| `--font-sans` | `'Outfit'` | All body text and headings |
| `--font-mono` | `'JetBrains Mono'` | Labels, nav, code, annotations |

Theme switching uses `data-theme="light" | "dark"` on `<html>`. Dark values are defined in `[data-theme="dark"]` blocks. Graph-paper backgrounds (`.graph-paper`, `.graph-paper-subtle`) use accent-colored `linear-gradient` patterns.

---

## GitHub Actions

### Secrets (already configured in PH-Tools org)

| Secret | Scope | Used By |
|---|---|---|
| `ph-docs-hub-dispatch` | `workflow` on PH-Tools/ph-docs | Spoke `notify-hub.yml` — triggers hub rebuild |
| `ph-docs-pages-deploy` | `contents: write` on PH-Tools/ph-docs | Hub `build.yml` — pushes to gh-pages branch |

### `build.yml` — Main workflow

Triggers: `schedule` (nightly 02:00 UTC) · `repository_dispatch` (from spokes) · `workflow_dispatch` (manual)

```
1. Checkout ph-docs main
2. Python 3.11 → pip install pyyaml requests
3. python scripts/fetch_spokes.py    ← lands content in src/content/docs/
4. Node 20 + pnpm → pnpm install
5. pnpm build                        ← astro build + pagefind index → dist/
6. Deploy dist/ → gh-pages branch    ← using ph-docs-pages-deploy token
7. Log build summary
```

### `validate.yml` — PR check

Runs `fetch_spokes.py` + `pnpm build` on PRs to main. No deploy. Confirms clean build before merge.

---

## Common Tasks

### "I added a new library but it doesn't appear"

1. Check `libraries.yml` — is the entry present and `enabled: true`?
2. Check the spoke repo — does `/docs/index.md` and `/docs/nav.yml` exist on the configured branch?
3. Re-run `python scripts/fetch_spokes.py` and check the output for `[SKIP]` messages.
4. Check `src/content/docs/build_manifest.json` — is the library in `succeeded` or `skipped`?

### "I changed CSS but it's not updating in dev"

CSS lives in `src/styles/global.css`. Changes are picked up immediately by `pnpm dev` — no extra steps needed (unlike the old MkDocs setup).

### "The sidebar shows the wrong structure"

Check the spoke's `docs/nav.yml`. The paths in `nav.yml` are relative to the spoke's `/docs` folder. `src/lib/nav.ts` reads this at Astro build time. Re-run `pnpm dev` after editing.

### "Feature grid cards are missing or have wrong titles"

Card metadata comes from front-matter in the **first file of each top-level nav group**. For a group `Developer` whose first file is `dev/architecture.md`, open that file and confirm it has `card_title` and `card_description` in its YAML front-matter.

### "Library landing shows no version or pills"

Add front-matter to the spoke's `docs/index.md`:
```yaml
---
title: PHX
subtitle: "..."
version: "1.4.0"
pills:
  - "v1.4.0 — latest"
---
```
Then push to main — the hub will rebuild automatically via `notify-hub.yml`.

### "The search index is stale"

Pagefind runs at `pnpm build` time. In development (`pnpm dev`), search uses the last built index. Run `pnpm build` locally if you need to test search against fresh content.

### "I want to test the full build locally without deploying"

```bash
python scripts/fetch_spokes.py   # fetch all spoke docs
pnpm build                        # build + pagefind index
pnpm preview                      # serve dist/ locally
```
