# foundations

Valid 'types' for Foundation Options and Types

**Source**: `PHX/foundations.py`

---

## CalculationSetting

Foundation heat loss calculation setting.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `USER_DEFINED` | `6` | User-specified foundation calculation parameters. |

---

## FoundationType

Classification of foundation types for ground heat loss calculations.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `HEATED_BASEMENT` | `1` | Fully conditioned basement within the thermal envelope. |
| `UNHEATED_BASEMENT` | `2` | Unconditioned basement below the thermal envelope. |
| `SLAB_ON_GRADE` | `3` | Foundation slab directly on soil. |
| `VENTED_CRAWLSPACE` | `4` | Ventilated crawlspace below the building. |
| `NONE` | `5` | No foundation type assigned. |

---

## PerimeterInsulationPosition

Orientation of perimeter insulation at the foundation edge.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `UNDEFINED` | `1` | Insulation position not specified. |
| `HORIZONTAL` | `2` | Insulation placed horizontally (e.g. wing insulation). |
| `VERTICAL` | `3` | Insulation placed vertically along the foundation wall. |

---
