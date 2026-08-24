# sniff

Is this file a PHPP? Which version, which language, project or blank template?

**Source**: `PHX/sniff.py`

---

## Flavour

What kind of PHPP-shaped file this is.

**Inherits from**: `enum.Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `PROJECT` | `'project'` | A PHPP with project content (TFA > 0, or a building name, dwelling units, or a chosen climate). |
| `BLANK_TEMPLATE` | `'blank_template'` | A PHPP with none of those (PHI's empty template, or a never-filled copy). |

---

## PhppIdentity

The identity of a PHPP workbook as read from its header cells.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `version_key` | — | The PHX shape-file key for this version, ie: 'EN_10_6' (language_major_minor). |
| `version_label` | — | Human label, ie: 'PHPP 10.6 EN' or 'PHPP 10.6 EN (easyPHv3)'. |

---

## SniffResult

Outcome of sniffing one path: an identity or a refusal, plus the evidence either way.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `ok` | — | True when an identity was established. |

---
