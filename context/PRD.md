# PH-Tools Documentation Strategy

**Unified Hub-and-Spoke Architecture for Libraries, Reference Docs, and LLM Workflows**

bldgtyp, LLC · v1.0 · April 2026

> This document supersedes Draft v0.3 (April 2026). The core hub-and-spoke architecture and content strategy are unchanged. The primary revision is the **replacement of MkDocs with Astro** as the site renderer, driven by the need for full UI control to match the bespoke Claude Design mockup. All pipeline, spoke convention, and LLM-integration decisions from v0.3 are carried forward.

---

## 1. Current State

The PH-Tools documentation ecosystem has grown organically across repositories, hosting platforms, and local machine paths.

| Location | Contents / Role |
|----------|----------------|
| passivehousetools.com | Top-level splash page. DreamHost DNS. Thin redirect only — no real content. |
| ph-tools.github.io/honeybee_grasshopper_ph/ | Primary public user docs for Honeybee-PH. GitHub Pages, auto-deployed via Actions. |
| ph-tools.github.io/honeybee_ph/ | Experimental Sphinx developer docs (honeybee_ph only). Not yet extended to other libraries. |
| PHX/PHPP/phpp_localization/EN_10_6.json | PHPP field mappings buried in repo. Useful data, not surfaced as readable docs. |
| ~/Dropbox/…/PHX/docs/context/ | PHX context docs. Local only. Not in version control. Inaccessible to teammates. |
| ~/.claude/skills/phius-certification/ ~/.claude/skills/wufi-xml/ ~/.claude/skills/phx-model/ | LLM skill files. Local only. Embed schema knowledge inline — duplicating content that exists (less cleanly) elsewhere. |

### 1.1 Core Problems

| Problem | Symptom | Risk |
|---------|---------|------|
| Duplication | WUFI XML knowledge in code, a skill, and a Dropbox doc | Silent drift — copies go out of sync |
| Local-only content | Context docs and skills on ~/.claude/ only | John can't use them; community can't benefit |
| No stable URLs | Schema docs have no fetchable address | LLM fetch instructions break when paths change |
| Audience mismatch | One site tries to serve users, devs, and LLMs | Every group gets a poor experience |
| Platform scatter | DreamHost + GitHub Pages + Dropbox + local paths | No clear answer to "where should this live?" |

---

## 2. Audiences & Their Needs

| Audience | What They Need | Entry Point |
|----------|---------------|-------------|
| New Honeybee-PH users | Install guide, tutorials, component reference, worked examples | passivehousetools.com or search |
| PH consultants using LLMs | Fetchable schema docs at stable URLs; skills/plugins for Claude | Plugin marketplace or GitHub |
| bldgtyp developers | API docs, architecture notes, CLAUDE.md context, schema maps | Repo README or dev docs |
| External contributors | Contribution guide, module map, test setup, design decisions | GitHub repo + dev docs |
| LLM agents (Claude Code / Claude) | Machine-readable schema maps at stable URLs; SKILL.md pointers | URL fetch at task start |

---

## 3. Proposed Architecture

Core principle: **One source of truth per piece of knowledge.** Docs are authored in the repo where the code lives, aggregated automatically into a single user-facing hub, and consumed by humans and LLMs alike — with no local-only or duplicated copies.

### 3.1 Three Layers

| Layer | Content | Authored In | Published At |
|-------|---------|-------------|--------------|
| Layer 1 — User Docs | Tutorials, install guides, component reference, worked examples | Each library repo (`/docs/`) | docs.passivehousetools.com (hub) |
| Layer 2 — Reference Docs | Schema maps, file-format specs, PHPP/WUFI field guides. Human + LLM dual-purpose. | ph-reference-docs repo (standalone, **deferred**) | Deferred |
| Layer 3 — Developer Docs | Architecture notes, CLAUDE.md context, export patterns | Each library repo (`/docs/dev/`) | docs.passivehousetools.com/\<lib\>/... (hub) |

### 3.2 The Hub-and-Spoke Model

The hub is a dedicated GitHub repository — **PH-Tools/ph-docs** — whose only job is to aggregate, assemble, and publish the unified docs site. It contains no original content. It is a build system and design system, not a content store.

Each library repo (spoke) owns and authors its own docs in a standard `/docs` folder. A GitHub Action in the hub periodically fetches each spoke's `/docs` content, and Astro builds a single unified static site deployed to GitHub Pages under `docs.passivehousetools.com`.

Key properties of this model:

- **Developers stay in their own repo.** A PHX developer writing docs never touches the hub. They write Markdown in `PHX/docs/` and the hub picks it up automatically.
- **Users see one site.** A single URL, single search index, single navigation covering all libraries.
- **The hub is resilient.** If a spoke has missing or malformed docs, the hub logs a warning and skips it — it never fails the build because of a child repo problem.
- **Adding a new library requires one entry** in `libraries.yml`. Nothing else changes.
- **OpenPH is a future sibling.** Once ready, it gets its own identical hub. We copy this setup; we don't extend this one.

### 3.3 Why Astro, Not MkDocs

The v0.3 strategy specified MkDocs Material as the site generator. After designing a detailed bespoke mockup (Claude Design, April 2026), we determined that matching the mockup's UI with MkDocs would require overriding ~70% of Material's Jinja2 templates and fighting its CSS specificity — fragile and maintenance-intensive.

**Astro** is selected instead. It is a static site generator designed for content/Markdown sites that gives full UI control via components. Key reasons:

| Criterion | MkDocs Material | Astro |
|-----------|----------------|-------|
| Markdown rendering | Built-in | Built-in |
| UI control | Limited (template overrides) | Full (component-based) |
| Design system integration | Requires CSS adapter layer | Direct (CSS custom properties) |
| Search | Built-in (opinionated UI) | Pagefind (zero-config, customizable) |
| nav.yml parsing | Built-in | Custom (`src/lib/nav.ts`) — simple |
| API doc generation | mkdocstrings plugin | Deferred (separate tooling) |
| Build output | `site/` (static HTML) | `dist/` (static HTML) |
| GitHub Pages deploy | Standard | Standard |

**What does NOT change** when switching to Astro:
- Hub-and-spoke content model and principles
- `libraries.yml` registry format (extended, not replaced)
- `fetch_spokes.py` logic (destination path changes from `assembled/` to `src/content/docs/`)
- `notify-hub.yml` spoke trigger pattern (already deployed in all spoke repos)
- GitHub Actions build/deploy structure
- bldgtyp design tokens consumed from CDN

---

## 4. Hub Repository Specification

### 4.1 Repository Identity

| Property | Value |
|----------|-------|
| GitHub repo | PH-Tools/ph-docs |
| Visibility | Public |
| Primary branch | main |
| GitHub Pages source | gh-pages branch (deployed by Action) |
| Custom domain | docs.passivehousetools.com |
| DNS | CNAME record in DreamHost → ph-tools.github.io (already configured) |
| Site generator | Astro 5 with TypeScript |
| Package manager | pnpm |
| Node version | 20+ |
| Python version | 3.11+ (for fetch_spokes.py) |

### 4.2 Repository File Structure

```
ph-docs/
├── astro.config.ts             # Astro config: static output, Pagefind integration
├── tsconfig.json
├── package.json
├── requirements.txt            # Python deps: pyyaml
├── libraries.yml               # Registry of all spoke repos
├── public/
│   └── CNAME                   # docs.passivehousetools.com
├── .github/workflows/
│   ├── build.yml               # Scheduled + dispatch-triggered build & deploy
│   └── validate.yml            # PR check: does hub build cleanly?
├── scripts/
│   └── fetch_spokes.py         # Core fetch + assemble logic
└── src/
    ├── content/docs/           # Git-ignored. Populated at build time.
    ├── layouts/                # BaseLayout (single shared layout)
    ├── components/             # Header, Sidebar, LibraryCard, FeatureCell, etc.
    ├── pages/                  # index.astro, [lib]/index.astro, [lib]/[...slug].astro
    ├── lib/                    # nav.ts, libraries.ts, frontmatter.ts
    └── styles/
        └── global.css          # Full design system
```

### 4.3 `libraries.yml` — The Registry

This file controls which repos contribute to the hub and provides metadata for the hub landing library cards. Adding or removing a library requires only editing this file.

```yaml
libraries:
  - id:          honeybee-ph          # Subdirectory name in src/content/docs/
    repo:        PH-Tools/honeybee_ph # GitHub org/repo
    label:       Honeybee-PH          # Display name in nav and sidebar
    docs_path:   docs/                # Path inside repo (default: docs/)
    branch:      main                 # Branch to fetch (default: main)
    enabled:     true                 # Set false to skip without removing entry
    # Hub landing card metadata (managed here, not in spoke):
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

### 4.4 Spoke `/docs` Folder Convention

Each spoke repo must follow this structure inside its `/docs` folder:

```
docs/
├── index.md      # REQUIRED. Library landing header (front-matter: title, subtitle, version, pills).
├── nav.yml       # REQUIRED. Navigation structure (MkDocs-style list format).
├── dev/          # Optional. Developer docs, architecture, export patterns.
│   ├── architecture.md        ← first file under "Developer" group → card front-matter here
│   └── exporter-patterns.md
└── reference/    # Optional. Schema maps, field guides.
    ├── phx-model-reference.md ← first file under "Reference" group → card front-matter here
    └── wufi-xml-schema.md
```

**`docs/index.md` front-matter** (feeds library landing header):

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

**Section card front-matter** (feeds library landing feature grid):

Card metadata lives in the **first file of each top-level nav group**. The hub's `nav.ts` reads nav.yml, identifies top-level groups, then reads front-matter from each group's first file to populate the feature grid cards.

```yaml
# docs/dev/architecture.md — first file under "Developer" group
---
title: Architecture
card_title: Developer Guide
card_description: "Architecture decisions and patterns for extending PHX."
card_index: "01"
---
```

**`docs/nav.yml` format** (MkDocs-style, unchanged from existing spoke repos):

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

---

## 5. GitHub Actions Specification

### 5.1 Build Workflow (`.github/workflows/build.yml`)

**Triggers:**
- **Schedule:** nightly at 02:00 UTC (safety net)
- **repository_dispatch:** event type `docs-updated` — fired by spoke repos after push to `/docs/**` on main
- **workflow_dispatch:** manual trigger for testing and emergency rebuilds

**Steps — in order:**

1. Checkout hub repo (main branch)
2. Set up Python 3.11 and install `requirements.txt` (pyyaml)
3. Run `fetch_spokes.py` — sparse-clone each spoke's `/docs` into `src/content/docs/`
4. Set up Node 20 + pnpm; run `pnpm install --frozen-lockfile`
5. Run `pnpm build` — Astro builds static site into `dist/`, Pagefind indexes it
6. Deploy `dist/` to gh-pages branch using `peaceiris/actions-gh-pages` with built-in `GITHUB_TOKEN`

**Secrets required (configured at org level):**
- `HUB_DISPATCH_TOKEN` — Fine-grained PAT with `contents: read+write` on PH-Tools/ph-docs. Stored as org secret, shared with spoke repos. Used by spoke `notify-hub.yml` to trigger hub rebuilds via `repository_dispatch`.
- `GITHUB_TOKEN` — Built-in (no setup needed). Workflow sets `permissions: contents: write`. Used by hub `build.yml` to push to gh-pages.

### 5.2 `fetch_spokes.py` — Logic Specification

Reads `libraries.yml`, fetches each spoke's docs, and assembles them into `src/content/docs/` for Astro to consume. Critical requirement: **graceful degradation** — any failure in a single spoke must be caught, logged, and skipped.

```python
load libraries = parse('libraries.yml')
results = {succeeded: [], skipped: []}

for lib in libraries:
  if not lib.enabled:
    results.skipped.append(lib.id, reason='disabled')
    continue

  try:
    url = f'https://github.com/{lib.repo}'
    sparse_clone(url, lib.branch, lib.docs_path,
                 dest=f'src/content/docs/{lib.id}/')

    validate_required(['index.md', 'nav.yml'],
                      in=f'src/content/docs/{lib.id}/')

    results.succeeded.append(lib.id)

  except Exception as e:
    log_warning(f'[SKIP] {lib.id}: {e}')
    results.skipped.append(lib.id, reason=str(e))

write_build_manifest(results, 'src/content/docs/build_manifest.json')
exit(0)  # Always exit 0 — partial builds are valid
```

**Sparse clone implementation:**

```bash
git clone --filter=blob:none --sparse --depth 1 --branch {branch} {url} {dest}
cd {dest}
git sparse-checkout set {docs_path}
```

### 5.3 Spoke-Side Trigger Workflow

Already deployed in all spoke repos as `.github/workflows/notify-hub.yml`. Fires a `repository_dispatch` to the hub when `/docs/**` changes on main. Uses `HUB_DISPATCH_TOKEN` org-level secret.

---

## 6. Design System

### 6.1 Overview

The site uses the **bldgtyp design system** — a fully tokenized system already published at CDN and used across bldgtyp.com, PH-Navigator, and Design-Phase Reports. The hub consumes it directly; no clone or adapter layer is needed.

`src/styles/global.css` imports the CDN token file and defines the full site design system, ported directly from the Claude Design mockup (April 2026):

```css
@import url('https://bldgtyp.github.io/branding/tokens/tokens.css');
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;600&family=JetBrains+Mono:wght@300;400&display=swap');
```

### 6.2 Key Design Tokens

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--accent` | `#7a9424` | `#7a9424` | Active nav, links, borders — invariant |
| `--accent-light` | `#e8ecd8` | `rgba(122,148,36,0.12)` | Hover backgrounds |
| `--accent-dark` | `#4a5916` | — | Dark text contexts |
| `--bg` | `#ffffff` | `#111111` | Page background |
| `--bg-elev` | `#fafaf7` | `#181818` | Elevated surfaces |
| `--fg` | `#111111` | `#ffffff` | Primary text |
| `--fg-muted` | `#555555` | `#b3b3ad` | Secondary text |
| `--font-sans` | `'Outfit'` | — | Body + headings |
| `--font-mono` | `'JetBrains Mono'` | — | Labels, nav, code |

Theme switching: `data-theme="light" | "dark"` on `<html>`. Persisted to `localStorage`. No flash-of-wrong-theme because the theme attribute is set inline via a small script in `<head>` before first paint.

### 6.3 Key UI Patterns

- **Graph paper background** — `linear-gradient` pattern in accent color at 6% / 12% opacity. Used on hero (Screen 1) and library card hover states.
- **Numbered indices** — `font-mono` counters (01, 02, …) in nav items and library cards. Accent-colored.
- **Accent bar** — 2px left border in `--accent` on active nav items.
- **Dashed tree line** — `border-left: 1px dashed var(--border-strong)` on expanded nav group children.
- **Pill buttons** — rounded, `border: 1px solid var(--border-strong)`, hover to accent.

### 6.4 Screen Inventory (from Claude Design mockup)

| Screen | Route | Key Components |
|--------|-------|----------------|
| Screen 1 — Hub Landing | `/` | Hero + SVG linework, LibraryCard grid (2-col), quick strip |
| Screen 2 — Library Landing | `/{lib}/` | Sidebar, lib header + pills, quick links, FeatureCell grid |
| Screen 3 — Content / Reference | `/{lib}/{slug}` | Sidebar, article typography, FetchCallout, SchemaTable |
| Screen 4 — Search Modal | overlay | Grouped results by library, keyboard nav (↑↓ / ↵ / Esc) |

---

## 7. Search

Pagefind is used for site-wide search. It runs at build time (`pnpm build`), crawls `dist/`, and outputs a client-side search bundle alongside the static HTML.

Key properties:
- **Zero runtime dependency** — no external search service, no API keys
- **Grouped results** — pages are tagged with `data-pagefind-meta="library:..."` attributes; the search script groups results by this metadata, matching the mockup's grouped search UI
- **Keyboard-driven** — `⌘K` / `Ctrl+K` to open, `↑↓` to navigate, `↵` to open, `Esc` to close
- **Markdown-indexed** — all rendered HTML in `dist/` is indexed, including API docs and reference pages

`SearchModal.astro` wraps the Pagefind JS API with the mockup's search modal styles. Results are rendered in the hub's grouped format, not Pagefind's default UI.

---

## 8. Toolchain Summary

| Component | Tool | Why |
|-----------|------|-----|
| Site generator | Astro 5 | Full UI control, Markdown-native, static output, content-first |
| Language | TypeScript (strict) | Type safety for nav/frontmatter parsing |
| Package manager | pnpm | Fast, deterministic |
| Search | Pagefind | Build-time, zero-config, grouped results |
| CI/CD | GitHub Actions | Native to GitHub; no external services |
| Hosting | GitHub Pages | Free, reliable, custom domain support |
| Branding | bldgtyp/branding CDN | Already published; imported via URL |
| Content fetch | Python (fetch_spokes.py) | Simple, maintainable, language-agnostic |
| API doc gen | — (deferred) | Out of scope for v1 |

---

## 9. Implementation Phases

See `context/IMPLEMENTATION_PLAN.md` for the full phase-by-phase implementation spec with verification criteria.

All phases are complete. See `context/IMPLEMENTATION_PLAN.md` for detailed per-phase notes.

| Phase | Goal | Status |
|-------|------|--------|
| 1 | Astro scaffold + design system | ✅ Complete |
| 2 | `libraries.yml` + fetch pipeline | ✅ Complete |
| 3 | Hub landing with real data | ✅ Complete |
| 4 | Library landing page | ✅ Complete |
| 5 | Content pages | ✅ Complete |
| 6 | Search | ✅ Complete |
| 7 | GitHub Actions + deploy | ✅ Complete |

---

## 10. Deferred Items

| Item | Status | Notes |
|------|--------|-------|
| `ph-reference-docs` spoke | Deferred | Repo not yet created; value unclear until hub is live |
| Auto-generated API docs | Deferred | Requires separate tooling; add after content conventions are stable |
| MDX in spoke pages | Optional | Hub supports MDX components (FetchCallout, SchemaTable) but spokes can use plain `.md` |
| honeybee_ph / honeybee_revive nav expansion | Organic | Both repos have `Overview: index.md` only; feature grids populate automatically as nav grows |
| OpenPH docs hub | Future | Identical pattern, separate hub repo, separate domain |

---

## 11. LLM Skill Integration

Once reference docs are at stable URLs, LLM skills become thin pointers. This is the long-term goal for the `ph-reference-docs` spoke (currently deferred):

```
# Before (embedded — requires skill update to fix a schema error):
The WUFI XML BuildingSegment element contains the following fields:
  - AirTemp_Exterior: float, units °C, maps to...
  ... (200 more lines) ...

# After (pointer — schema errors fixed by editing one Markdown file):
Before analyzing any WUFI XML file, fetch the current schema reference:
  https://docs.passivehousetools.com/reference/wufi-xml-schema
Use it as the authoritative field mapping guide for this session.
```

This pattern applies to: WUFI XML schema, PHX model reference, PHPP field mapping, Phius Excel mapping, METr JSON schema.

The hub makes this possible by providing **stable, publicly accessible URLs** for all documentation content. The `FetchCallout` component (Screen 3) surfaces the fetch URL prominently on each reference page.

---

## Appendix: As-Built Deviations from v1.0 Plan

The following deviations from the original plan were made during implementation (April 2026). Sections above have been updated inline where possible; this appendix captures the broader architectural changes.

| Planned | As-Built | Why |
|---------|----------|-----|
| Three layouts: `HubLayout`, `LibraryLayout`, `ContentLayout` | Single `BaseLayout.astro` with `activeLib` and `hideFooter` props | All pages share the same HTML shell (head, Header, slot, Footer). Sidebar is placed inside page templates via the `with-sidebar` CSS grid, not in a separate layout. |
| Markdown rendered via Astro's built-in pipeline | Content collections with glob loader (`src/content.config.ts`) + `getEntry()` / `render()` | Content collections give typed access to front-matter and native Shiki syntax highlighting. The glob loader pattern `**/*.md` over `src/content/docs/` cleanly maps to the fetched spoke content. |
| `import.meta.dirname` for path resolution in `src/lib/` | `process.cwd()` for all file reads | During Astro's build phase, compiled modules run from `dist/chunks/`, causing `import.meta.dirname` to resolve to the wrong directory. `process.cwd()` always returns the project root. |
| Two PATs: `ph-docs-hub-dispatch` + `ph-docs-pages-deploy` | One PAT (`HUB_DISPATCH_TOKEN`) + built-in `GITHUB_TOKEN` | The deploy step runs in the same repo it pushes to, so the built-in token works. Only the cross-repo dispatch needs a PAT. |
| `requirements.txt`: pyyaml + requests | `requirements.txt`: pyyaml only | `fetch_spokes.py` uses `subprocess` for git operations, not the GitHub API via requests. |
| `FetchCallout` and `SchemaTable` as MDX components | Created as Astro components, not yet used | All spoke content is plain `.md` without front-matter-driven fetch URLs. Components are ready for future MDX adoption or `ph-reference-docs` spoke. |
| Pagefind grouping via `data-pagefind-section` | Grouping via `data-pagefind-meta="library:..."` | `data-pagefind-meta` attaches metadata to each result, allowing client-side grouping in the search script. Simpler than section-based filtering. |
| Search script as Vite-processed `<script>` | `<script is:inline>` bypassing Vite | Pagefind's JS bundle (`/pagefind/pagefind.js`) only exists after build. Vite rejects the import during compilation. `is:inline` lets the browser handle the dynamic import at runtime. |

---

*End of v1.0 (updated with as-built deviations, April 2026)*
*bldgtyp, LLC · Supersedes PH-Tools_Doc_Strategy_v0.3.md*
