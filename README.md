# PH-Tools Documentation Hub

Unified documentation site for the [PH-Tools](https://github.com/PH-Tools) ecosystem — Passive House modeling, data exchange, and analysis libraries.

**Live site**: [docs.passivehousetools.com](https://docs.passivehousetools.com)

## Architecture

This repo is the **hub** in a hub-and-spoke model. It contains no library documentation — only the build pipeline, design system, and Astro components that fetch, assemble, and render docs from spoke repos into a single site.

**Spokes** (library repos) own their docs in a standard `/docs` folder:

| Library | Repo | Category |
|---------|------|----------|
| Honeybee-PH | [PH-Tools/honeybee_ph](https://github.com/PH-Tools/honeybee_ph) | Modeling |
| PHX | [PH-Tools/PHX](https://github.com/PH-Tools/PHX) | Exchange |
| Honeybee-REVIVE | [PH-Tools/honeybee_revive](https://github.com/PH-Tools/honeybee_revive) | Analysis |

Adding a new library = one entry in `libraries.yml`. The build pipeline discovers it automatically.

## Build Pipeline

```
python scripts/fetch_spokes.py   # sparse-clone each spoke's /docs into src/content/docs/
pnpm build                        # astro build + pagefind search index → dist/
```

The fetch script never aborts on a single spoke failure — it logs, skips, and continues. Partial builds are valid.

## Local Development

```bash
# Prerequisites: Python 3.11+, Node 20+, pnpm
pip install -r requirements.txt
pnpm install

# Fetch spoke docs and start dev server
python scripts/fetch_spokes.py
pnpm dev

# Full build (includes Pagefind search index)
pnpm build
pnpm preview
```

## Deployment

GitHub Actions (`build.yml`) runs on:
- **Nightly** schedule (02:00 UTC)
- **Spoke dispatch** — when a spoke pushes to `/docs/**` on main, it fires a `repository_dispatch` to this repo
- **Manual** trigger via `workflow_dispatch`

The workflow fetches spokes, builds the site, and deploys `dist/` to the `gh-pages` branch using the built-in `GITHUB_TOKEN`.

## Spoke Convention

Each spoke repo must have:

```
docs/
├── index.md    # Required — front-matter: title, subtitle, version, pills
├── nav.yml     # Required — MkDocs-style navigation structure
└── <sections>/ # Optional — dev/, reference/, etc.
```

See `context/ARCHITECTURE.md` for the full build pipeline reference and `context/PRD.md` for strategy and design decisions.

## Tech Stack

| Component | Tool |
|-----------|------|
| Site generator | Astro 5 |
| Search | Pagefind |
| Design system | bldgtyp tokens (CDN) |
| Fonts | Outfit + JetBrains Mono |
| Content fetch | Python (`fetch_spokes.py`) |
| CI/CD | GitHub Actions |
| Hosting | GitHub Pages |

## License

GPL-2.0 — see [LICENSE](LICENSE).
