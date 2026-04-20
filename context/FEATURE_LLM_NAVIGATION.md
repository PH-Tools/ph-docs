# Feature: LLM-Optimized Navigation Layer

**Status**: Proposal  
**Date**: 2026-04-19  
**Context**: The primary consumers of docs.passivehousetools.com are LLM agents (via Claude skills, Claude Code sessions, and WebFetch), not humans browsing in a browser. The site's current build pipeline and URL structure are sound, but everything it serves is HTML — optimized for human rendering, not machine consumption. This feature adds a parallel set of static, machine-readable outputs that make the site trivially navigable by LLMs.

---

## Problem

Today, when a Claude skill or agent needs content from this site, it must:

1. Know the exact URL in advance (hardcoded in the skill)
2. Fetch an HTML page (header, sidebar, footer, CSS, JS — ~80% layout noise)
3. Parse the content out of the HTML

This creates three problems:

- **Discoverability**: No way for an agent to ask "what pages exist?" without navigating HTML
- **Token waste**: Fetching HTML burns 5-10x more context window than the actual content
- **Brittleness**: Skills hardcode URLs; if a page moves, the skill breaks silently

The strategy doc (Section 11) already envisions skills as thin pointers to stable URLs. This feature builds the infrastructure to make that pattern work.

---

## Proposed Additions

Six additions, all static files generated at build time. No runtime services, no API, no deployment changes. Ordered by priority.

---

### 1. `llms.txt` — Site Index for LLMs

**What**: A plain-text file at `/llms.txt` following the emerging [llmstxt.org](https://llmstxt.org) convention. Claude's `WebFetch` and other LLM tooling already know to look for this file at a site's root.

**Generated from**: `libraries.yml` + each spoke's `nav.yml`

**Example output**:

```
# PH-Tools Documentation

> Unified documentation for PH-Tools open-source libraries: Passive House
> modeling, data exchange, and analysis tools for building energy performance.

## Honeybee-PH
Grasshopper-native Passive House modeling.
- [Overview](https://docs.passivehousetools.com/honeybee-ph/)

## PHX
Passive House Exchange data model & file I/O.
- [Overview](https://docs.passivehousetools.com/phx/)
- [Architecture](https://docs.passivehousetools.com/phx/dev/architecture/)
- [Exporter & Importer Patterns](https://docs.passivehousetools.com/phx/dev/exporter-patterns/)
- [PHX Model Reference](https://docs.passivehousetools.com/phx/reference/phx-model-reference/)
- [WUFI XML Schema](https://docs.passivehousetools.com/phx/reference/wufi-xml-schema/)

## Honeybee-REVIVE
Carbon & energy analysis for building design.
- [Overview](https://docs.passivehousetools.com/honeybee-revive/)
```

**Implementation**: Post-build script or Astro endpoint that walks `libraries.yml` + assembled `nav.yml` files and writes `dist/llms.txt`.

**Optional companion**: `/llms-full.txt` — concatenates all raw markdown content into a single file. One fetch = entire corpus in context. Useful for smaller doc sites; may be too large once spoke content grows significantly.

---

### 2. Raw Markdown Routes

**What**: For every HTML page at `/{lib}/{slug}/`, also emit the raw markdown source at `/{lib}/{slug}.md`.

**Why**: When an LLM fetches the HTML version of a reference page, the actual content might be 2,000 tokens but the full HTML response is 10,000-15,000 tokens (header, nav, sidebar, footer, inline styles, scripts). The `.md` route serves just the content — front-matter stripped, pure markdown body.

**Example**:

| HTML route (for humans) | Raw route (for LLMs) |
|-------------------------|----------------------|
| `/phx/reference/wufi-xml-schema/` | `/phx/reference/wufi-xml-schema.md` |
| `/phx/dev/architecture/` | `/phx/dev/architecture.md` |
| `/honeybee-ph/` | `/honeybee-ph.md` |

**Implementation**: Astro can generate these as additional static endpoints. For each content page, read the markdown source, strip front-matter, and write it to `dist/` as a `.md` file alongside the HTML directory.

**Interaction with `FetchCallout`**: The `FetchCallout` component (already built, Screen 3) should show the `.md` URL by default, since its primary audience is LLM users copying the URL into a skill.

---

### 3. LLM-Oriented Front-Matter in Spoke Content

**What**: Extend the spoke `docs/` front-matter convention with optional fields that help LLMs decide whether a page is relevant to their current task — without fetching and reading the full content.

**New optional fields**:

```yaml
---
title: WUFI XML Schema
# Existing fields (unchanged):
card_title: Reference
card_description: "..."

# New LLM fields (optional):
llm_purpose: "Authoritative field mapping for all WUFI-Passive XML elements and attributes"
llm_use_when: "Before parsing, generating, validating, or modifying any WUFI XML file"
llm_related:
  - "reference/phx-model-reference.md"
  - "dev/exporter-patterns.md"
---
```

| Field | What it tells the LLM |
|-------|----------------------|
| `llm_purpose` | One-line description of what this page authoritatively covers |
| `llm_use_when` | When to fetch this page (task trigger) |
| `llm_related` | Other pages that are commonly needed alongside this one |

**These fields are optional.** Pages without them still work fine — they just don't appear in structured indexes with rich metadata.

**These fields feed into**: `site-index.json` (item 4) and `llms.txt` generation.

---

### 4. `site-index.json` — Structured Page Catalog

**What**: A build-time-generated JSON manifest at `/site-index.json` listing every page with structured metadata. This is the machine-readable equivalent of the site's navigation — an LLM agent can fetch this single file and programmatically find the right page for any task.

**Example output**:

```json
{
  "generated": "2026-04-19T14:30:00Z",
  "base_url": "https://docs.passivehousetools.com",
  "libraries": [
    {
      "id": "phx",
      "label": "PHX",
      "description": "Passive House Exchange data model & file I/O.",
      "pages": [
        {
          "title": "Overview",
          "path": "/phx/",
          "raw_path": "/phx.md",
          "section": null
        },
        {
          "title": "WUFI XML Schema",
          "path": "/phx/reference/wufi-xml-schema/",
          "raw_path": "/phx/reference/wufi-xml-schema.md",
          "section": "Reference",
          "llm_purpose": "Authoritative field mapping for all WUFI-Passive XML elements",
          "llm_use_when": "Before parsing, generating, or modifying any WUFI XML file",
          "llm_related": ["/phx/reference/phx-model-reference.md"]
        }
      ]
    }
  ]
}
```

**Implementation**: Post-build script that walks each library's `nav.yml` + page front-matter and writes `dist/site-index.json`.

**Usage pattern**: An LLM agent fetches `site-index.json`, scans the `llm_purpose` / `llm_use_when` fields to find relevant pages, then fetches just those pages via `raw_path`.

---

### 5. `/llm-instructions.md` — Agent Onboarding File

**What**: A static markdown file at a stable URL that tells any LLM agent how to navigate and use the site. This is the file that Claude skills point to as their entry point.

**Example content**:

```markdown
# PH-Tools Documentation — LLM Navigation Guide

## How to find content
1. Fetch /site-index.json for a structured catalog of all pages
2. Match your task against `llm_use_when` fields to find relevant pages
3. Fetch the `raw_path` URL (.md) for each relevant page — not the HTML version

## Direct access (common tasks)
- Parsing/generating WUFI XML → /phx/reference/wufi-xml-schema.md
- Understanding PHX data model → /phx/reference/phx-model-reference.md
- PHX exporter/importer patterns → /phx/dev/exporter-patterns.md

## URL conventions
- HTML (for humans): /phx/reference/wufi-xml-schema/
- Raw markdown (for LLMs): /phx/reference/wufi-xml-schema.md
- Site index: /site-index.json
- This file: /llm-instructions.md

## Content freshness
All content is sourced from library repos and rebuilt automatically on every push.
```

**Why a separate file instead of embedding in `llms.txt`**: `llms.txt` is a catalog (what exists). This file is procedural (how to use it). Skills that don't need the full catalog can fetch just the instructions.

**Implementation**: Could be a static file in `public/`, or generated at build time with the "Direct access" section populated from front-matter.

---

### 6. MCP Server (Deferred)

**What**: A local MCP server that provides tool-based access to the docs content. Installed in each team member's Claude Code MCP config.

**Tools it would expose**:

| Tool | What it does |
|------|-------------|
| `list_libraries` | Returns all libraries with descriptions |
| `list_pages` | Returns pages for a library (or all), with LLM metadata |
| `get_page` | Returns raw markdown for a specific page |
| `search` | Full-text search across all content, returns page URLs + snippets |

**Why this is valuable**: Eliminates the fetch-parse-filter loop. An agent calls `search("ventilation WUFI XML")` and gets back exactly the right page content — no HTML parsing, no token waste, no multi-step URL discovery.

**Why deferred**: Items 1-5 solve 80% of the problem with static files and zero infrastructure. The MCP server adds value once:
- Spoke repos have substantial content (not just stubs)
- The `llms.txt` + raw markdown pattern has been validated in real skill workflows
- Search becomes a bottleneck (Pagefind is client-side JS — unusable by LLMs)

**Implementation when ready**: A small Python server in `ph-docs/mcp/` that reads from the local content tree (post-fetch) or proxies to the live site. Added to `.claude/settings.json` for each team member.

---

## How These Compose

The end-to-end flow for an LLM agent:

```
Skill says: "Fetch https://docs.passivehousetools.com/llm-instructions.md"
    ↓
Agent learns: URL conventions, direct-access shortcuts, how to use site-index.json
    ↓
Agent fetches: /site-index.json  (if it needs to discover pages)
    ↓
Agent fetches: /phx/reference/wufi-xml-schema.md  (raw markdown, minimal tokens)
    ↓
Agent has authoritative, current content in context
```

A skill like `wufi-xml` goes from 200+ lines of embedded schema to:

```markdown
Before working with any WUFI XML file, fetch the current schema reference:
  https://docs.passivehousetools.com/phx/reference/wufi-xml-schema.md
Use it as the authoritative field mapping guide for this session.
```

---

## What Changes in Existing Code

| File / Component | Change |
|-----------------|--------|
| Build script (`package.json`) | Add post-build step to generate `llms.txt`, `site-index.json`, raw `.md` files |
| `FetchCallout.astro` | Default to showing `.md` URL instead of HTML URL |
| Spoke `docs/` convention | Add optional `llm_*` front-matter fields to spec |
| `IMPLEMENTATION_PLAN.md` | Add Phase 8 for LLM navigation layer |
| `PH-Tools_Doc_Strategy_v1.0.md` | Update Section 11 with concrete implementation details |

No changes to: `libraries.yml` format, `fetch_spokes.py`, `nav.yml` format, Astro routing, design system, GitHub Actions triggers.

---

## Implementation Estimate

Items 1-5 are all build-time static file generation. They share the same infrastructure: walk the assembled content tree, read front-matter, write files to `dist/`. A single post-build script handles all of them.

| Item | Depends on |
|------|-----------|
| 1. `llms.txt` | `libraries.yml` + `nav.yml` (both exist) |
| 2. Raw `.md` routes | Assembled markdown files (exist after `fetch_spokes.py`) |
| 3. LLM front-matter | Spoke content updates (separate PRs per spoke) |
| 4. `site-index.json` | Items 1 + 3 (same data, different format) |
| 5. `llm-instructions.md` | Items 2 + 4 (references their URLs) |
| 6. MCP server | All of the above + substantial spoke content |

Items 1, 2, and 4 can be built together as a single post-build script. Item 3 is a spoke-side convention change. Item 5 is a static file. Item 6 is deferred.

---

*End of proposal*
