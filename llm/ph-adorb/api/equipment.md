# equipment

Equipment (mechanical, lighting, etc..), and Collection classes.

**Source**: `ph_adorb/equipment.py`

---

## PhAdorbEquipmentType

Classification of building equipment types.

**Inherits from**: `str`, `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `MECHANICAL` | `'Mechanical'` | HVAC mechanical equipment (heat pumps, ERVs, etc.). |
| `HOT_WATER` | `'Hot Water'` | Domestic hot water equipment. |
| `APPLIANCE` | `'Appliance'` | Plug-load appliances (refrigerators, stoves, etc.). |
| `LIGHTS` | `'Lights'` | Lighting systems. |
| `PV_ARRAY` | `'PV Array'` | Photovoltaic solar panels. |
| `BATTERY` | `'Battery'` | Battery energy storage systems. |

---

## PhAdorbEquipment

A single piece of building equipment with cost and lifetime data.

**Inherits from**: `BaseModel`

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `material_fraction` | — | Fraction of cost attributable to materials (1 - labor_fraction). |

---

## PhAdorbEquipmentCollection

A dict-backed, iterable collection of equipment items.

**Inherits from**: `BaseModel`

### Methods

#### add_equipment(_ph_adorb_equipment)

Add an equipment item to the collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_ph_adorb_equipment` | — | — |

#### get_equipment(key)

Return an equipment item by name.

| Arg | Type | Description |
|-----|------|-------------|
| `key` | — | — |

#### keys()

Return equipment names sorted alphabetically.

#### values()

Return equipment items sorted alphabetically by name.

---
