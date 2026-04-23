# ppp_sections

Core data structures for PPP file format sections.

**Source**: `PHX/ppp_sections.py`

---

## PppSection

A single PPP section block with header and values.

### Methods

#### to_lines()

Return the section as a list of lines (header + values).

---

## PppFile

An ordered collection of PppSections that serializes to a complete PPP file.

### Methods

#### to_lines()

Return all lines for the complete PPP file.

---
