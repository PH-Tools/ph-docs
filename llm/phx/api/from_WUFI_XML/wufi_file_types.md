# wufi_file_types

Pydantic Model Unit-Types for WUFI-XML file format.

**Source**: `PHX/wufi_file_types.py`

---

## BaseConverter

Base Class for any types which return a value, converted to the right unit.

### Methods

#### *classmethod* validate(v)

Since WUFI XMl files come in several shapes and the XML tag may, or

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## BaseCaster

Base Class for any types which return a value, cast to the right type.

### Methods

#### *classmethod* validate(v)

_input: Dict[str, Any] | None | float

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## Watts

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Watts_per_M2K

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Watts_per_MK

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Watts_per_M2

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Watts_per_DegreeK

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## KiloWatt

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Watt_per_Watt

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## kWh

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## kWh_per_M2

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## kWh_per_kWh

No description available.

**Inherits from**: `float`

### Methods

#### *classmethod* validate(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## Wh_per_M3

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Wh_per_M2K

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## M

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## MM

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## M3

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## M2

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Liter

No description available.

**Inherits from**: `float`

### Methods

#### *classmethod* validate(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## DegreeC

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## DegreeDeltaK

No description available.

**Inherits from**: `float`

### Methods

#### *classmethod* validate(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---

## M_per_Second

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## M_per_Day

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## KG_per_M3

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## MG_per_M3

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## Joule_per_KGK

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## PartsPerMillionByVolume

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## Hour

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## Days_per_Year

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## Hours_per_Year

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## KiloHours_per_Year

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## Lux

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## M3_per_Hour

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## M3_per_Hour_per_M2

No description available.

**Inherits from**: `float`, `BaseConverter`

---

## ACH

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## AngleDegree

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## CardinalDegrees

No description available.

**Inherits from**: `float`, `BaseCaster`

---

## WUFI_Vapor_Resistance_Factor

No description available.

**Inherits from**: `float`

### Methods

#### *classmethod* validate(v)

| Arg | Type | Description |
|-----|------|-------------|
| `v` | — | — |

---
