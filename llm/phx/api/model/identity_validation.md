# identity_validation

Read-only validation for identities and references consumed by exporters.

**Source**: `PHX/identity_validation.py`

---

## IdentityValidationTarget

Export contracts with identity-bearing project references.

**Inherits from**: `str`, `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `WUFI` | `'wufi'` | — |
| `METR` | `'metr'` | — |
| `PHPP` | `'phpp'` | — |

---

## IdentityIssueKind

Stable categories emitted by identity validation.

**Inherits from**: `str`, `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `DUPLICATE` | `'duplicate'` | — |
| `DANGLING_REFERENCE` | `'dangling-reference'` | — |

---

## IdentityIssue

One duplicate identity or dangling reference in the project graph.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `sort_key` | — | — |

---

## IdentityValidationError

Aggregate error raised before an exporter consumes an invalid graph.

**Inherits from**: `ValueError`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `target` | — | — |
| `issues` | `tuple` | — |

---
