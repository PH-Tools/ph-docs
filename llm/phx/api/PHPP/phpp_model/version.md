# version

Class for managing PHPP Version data.

**Source**: `PHX/version.py`

---

## PHPPVersion

Manage the PHPP Version number and language information.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `number_major` | `clean_input` | — |
| `number_minor` | `clean_input` | — |
| `language` | `clean_input` | — |

### Methods

#### clean_input(_input)

Upper, strip, replace spaces.

| Arg | Type | Description |
|-----|------|-------------|
| `_input` | — | — |

#### number()

Return the full version number (ie: "9.6", "10.4", etc..)

---
