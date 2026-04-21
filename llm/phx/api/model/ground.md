# ground

PHX Foundation Classes for below-grade and ground-contact thermal boundary conditions.

**Source**: `PHX/ground.py`

---

## PhxFoundation

Base class for all PHX foundation / ground-contact boundary conditions.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `foundation_type_num` | — | The FoundationType enum for this foundation element. |

---

## PhxHeatedBasement

A heated (conditioned) basement foundation within the thermal envelope.

**Inherits from**: `PhxFoundation`

---

## PhxUnHeatedBasement

An unheated (unconditioned) basement below the thermal envelope.

**Inherits from**: `PhxFoundation`

---

## PhxSlabOnGrade

A slab-on-grade foundation in direct contact with the soil.

**Inherits from**: `PhxFoundation`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `perim_insulation_position` | — | The PerimeterInsulationPosition enum (horizontal or vertical). |

---

## PhxVentedCrawlspace

A vented crawlspace foundation beneath the thermal envelope.

**Inherits from**: `PhxFoundation`

---
