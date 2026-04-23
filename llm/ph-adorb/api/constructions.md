# constructions

Assembly (wall, floor, etc..) Constructions, and Collection classes.

**Source**: `ph_adorb/constructions.py`

---

## PhAdorbConstruction

A single building envelope construction assembly (wall, floor, roof, or window).

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `quantity_ft2` | — | Total area converted to square feet. |
| `cost` | — | Total Cost (quantity * cost_per_m2). |
| `CO2_kg` | — | Total CO2 (quantity * CO2_kg_per_m2). |
| `material_fraction` | — | Fraction of cost attributable to materials (1 - labor_fraction). |

### Methods

#### set_quantity_ft2(_value)

Set the total area from a value in square feet.

| Arg | Type | Description |
|-----|------|-------------|
| `_value` | — | — |

---

## PhAdorbConstructionCollection

A dict-backed, iterable collection of construction assemblies.

**Inherits from**: `BaseModel`

### Methods

#### add_construction(_construction)

Add a construction to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_construction` | — | — |

#### get_construction(key)

Return a construction by display name.

| Arg | Type | Description |
|-----|------|-------------|
| `key` | — | — |

#### keys()

Return construction names sorted alphabetically.

#### values()

Return constructions sorted alphabetically by display name.

#### set_constructions_ft2_quantities(_construction_quantities_ft2)

Set the quantity (ft2) of each Construction.

| Arg | Type | Description |
|-----|------|-------------|
| `_construction_quantities_ft2` | — | — |

---
