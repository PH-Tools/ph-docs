# PH-Tools Documentation — LLM Navigation Guide

This site hosts documentation for the PH-Tools open-source libraries.
All content is sourced from library repos and rebuilt automatically on every push.

## How to find content

1. Fetch `/site-index.json` for a structured catalog of all pages with metadata
2. Match your task against `llm_use_when` fields to find relevant pages
3. Fetch the `raw_path` URL (`.md`) for each relevant page — not the HTML version

## URL conventions

| Type | Pattern | Example |
|------|---------|---------|
| HTML (for humans) | `/{lib}/{slug}/` | `https://docs.passivehousetools.com/phx/reference/wufi-xml-schema/` |
| Raw markdown (for LLMs) | `/llm/{lib}/{path}.md` | `https://docs.passivehousetools.com/llm/phx/reference/wufi-xml-schema.md` |
| Site index | `/site-index.json` | `https://docs.passivehousetools.com/site-index.json` |
| This file | `/llm-instructions.md` | `https://docs.passivehousetools.com/llm-instructions.md` |
| LLM site index | `/llms.txt` | `https://docs.passivehousetools.com/llms.txt` |

## Direct access — common tasks

No pages have `llm_use_when` metadata yet.

## Available libraries

- **Honeybee-PH** — Grasshopper-native Passive House modeling. Build PH-compliant models inside Rhino using familiar Honeybee components. (19 pages)
- **Honeybee-REVIVE** — Carbon & energy analysis for building design. Resilience & embodied-carbon workflows for Phius REVIVE. (7 pages)
