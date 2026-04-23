# io_exceptions

Exceptions used by the IO classes.

**Source**: `PHX/io_exceptions.py`

---

## FindSectionMarkerException

Raised when a section marker string cannot be found in a worksheet column.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## PerReferenceAreaException

Raised when the PER reference area (TFA or footprint) cannot be found.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## ReadDataException

Raised when a value cannot be read from a PHPP worksheet cell.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---

## PHPPDataMissingException

Raised when a required PHPP field returns None.

**Inherits from**: `Exception`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `msg` | — | — |

---
