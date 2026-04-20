# What This Repo Is

**PH-Tools/ph-docs** is the hub-and-spoke documentation aggregator for the PH-Tools ecosystem. It fetches docs from spoke repos (honeybee-ph, PHX, honeybee-revive), builds a unified Astro site with a custom bldgtyp-branded design system, and deploys to GitHub Pages.

**Live site**: [docs.passivehousetools.com](https://docs.passivehousetools.com)  
**Status**: All 7 implementation phases complete. Site is live and auto-rebuilds on spoke doc changes.

## Architecture

Refer to `context/ARCHITECTURE.md` for the full build pipeline reference.  
Refer to `context/PRD.Dmd` for strategy and design decisions.  

### Hub-and-Spoke Model

- **Hub** (this repo): Reads `libraries.yml`, sparse-clones each spoke's `/docs` folder into `src/content/docs/`, builds with Astro, deploys to GitHub Pages.
- **Spokes**: Library repos (honeybee_ph, PHX, honeybee_revive) that own their docs in a standard `/docs` folder with `index.md` + `nav.yml`.
- **Build sequence**: `python scripts/fetch_spokes.py` → `pnpm build` (Astro + Pagefind) → deploy `dist/` to gh-pages.



### Key Technical Details

- **Single layout**: `BaseLayout.astro` is the only layout — all pages (hub landing, library landing, content) use it with props (`activeLib`, `hideFooter`).
- **Content rendering**: Markdown is rendered via Astro content collections (`src/content.config.ts` defines a `docs` collection with glob loader). Content pages use `getEntry()` + `render()` from `astro:content`.
- **Path resolution**: All `src/lib/*.ts` modules use `process.cwd()` (not `import.meta.dirname`) because Astro's build phase runs from `dist/chunks/`.
- **Search**: Pagefind runs post-build (`pagefind --site dist`). The `SearchModal.astro` script uses `is:inline` to bypass Vite (Pagefind JS only exists after build). Results are grouped by library via `data-pagefind-meta="library:..."`.
- **Deploy**: `build.yml` uses the built-in `GITHUB_TOKEN` (not a PAT) to push to `gh-pages`. Spoke dispatch uses `HUB_DISPATCH_TOKEN` org secret.

### Spoke `/docs` Convention

Every spoke repo must have:

```
docs/
├── index.md    # Required — front-matter: title, subtitle, version, pills
├── nav.yml     # Required — MkDocs-style nav (read by Astro at build time)
└── dev/        # Optional — architecture.md is first file → card front-matter
    ├── architecture.md    ← put card_title + card_description here
    └── ...
```

See spoke `docs/.instructions.md` files for the full convention reference.

## Critical Design Principles

1. **Graceful degradation**: `fetch_spokes.py` never aborts on a single spoke failure. Log, skip, continue. Always exit 0.
2. **Hub assembles, spokes author**: This repo contains no library documentation. All library docs live in spoke repos.
3. **One source of truth**: No duplicated content across repos.
4. **Adding a library = one entry**: New spoke = new entry in `libraries.yml`. Nothing else changes.
5. **Card metadata split**: Hub landing card data (description, tag_line, category) lives in `libraries.yml`. Library section card data (card_title, card_description) lives in front-matter of the first file per nav group in each spoke.