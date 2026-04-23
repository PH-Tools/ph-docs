# building

Valid 'types' for Building Elements.

**Source**: `PHX/building.py`

---

## ComponentFaceType

Classification of building component face orientations.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `0` | Unclassified face type. |
| `WALL` | `1` | Vertical wall surface. |
| `FLOOR` | `2` | Horizontal floor surface. |
| `ROOF_CEILING` | `3` | Roof or ceiling surface. |
| `WINDOW` | `4` | Glazed window surface. |
| `ADIABATIC` | `5` | Adiabatic boundary (no heat flow). |
| `CUSTOM` | `6` | User-defined face type. |
| `AIR_BOUNDARY` | `7` | Air boundary between zones. |

---

## ComponentExposureExterior

Exterior exposure condition for a building component.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `0` | No exposure assigned. |
| `EXTERIOR` | `-1` | Exposed to outdoor air. |
| `GROUND` | `-2` | In contact with ground. |
| `SURFACE` | `-3` | Exposed to another surface (interior boundary). |

---

## ComponentFaceOpacity

Opacity classification of a building component face.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `OPAQUE` | `1` | Solid, non-transparent surface (walls, roofs, floors). |
| `TRANSPARENT` | `2` | Glazed or translucent surface (windows, curtain walls). |
| `AIRBOUNDARY` | `3` | Virtual air boundary between zones. |

---

## ComponentColor

Display color assignment for building components in WUFI visualization.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `EXT_WALL_INNER` | `1` | Interior side of an exterior wall. |
| `EXT_WALL_OUTER` | `2` | Exterior side of an exterior wall. |
| `INNER_WALL` | `3` | Interior partition wall. |
| `WINDOW` | `4` | Window or glazed component. |
| `FLOOR` | `5` | Floor surface. |
| `CEILING` | `6` | Ceiling surface. |
| `SLOPED_ROOF_OUTER` | `7` | Exterior side of a sloped roof. |
| `SLOPED_ROOF_INNER` | `8` | Interior side of a sloped roof. |
| `SLOPED_ROOF_THATCH` | `9` | Thatch-style sloped roof. |
| `FLAT_ROOF_OUTER` | `10` | Exterior side of a flat roof. |
| `FLAT_ROOF_INNER` | `11` | Interior side of a flat roof. |
| `SURFACE_GROUND_CONTACT` | `12` | Surface in contact with ground. |
| `GROUND_ABOVE` | `13` | Ground surface above the component. |
| `GROUND_BENEATH` | `14` | Ground surface beneath the component. |

---

## ThermalBridgeType

Classification of thermal bridge boundary conditions.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `AMBIENT` | `15` | Thermal bridge exposed to outdoor ambient air. |
| `PERIMETER` | `16` | Thermal bridge at the building perimeter (e.g. slab edge). |
| `UNDERGROUND` | `17` | Thermal bridge in contact with ground. |

---

## SpecificHeatCapacityType

Thermal mass classification for a building zone.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `LIGHTWEIGHT` | `1` | Light construction (e.g. wood frame). |
| `MIXED` | `2` | Mixed construction weight. |
| `MASSIVE` | `3` | Heavy construction (e.g. concrete, masonry). |
| `USER_DEFINED` | `6` | User-specified heat capacity value. |

---

## SpecificHeatCapacityValueWhM2K

Specific heat capacity values in Wh/m2K for standard construction types.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `LIGHTWEIGHT` | `60` | 60 Wh/m2K for lightweight construction. |
| `MIXED` | `132` | 132 Wh/m2K for mixed construction. |
| `MASSIVE` | `204` | 204 Wh/m2K for massive construction. |

---

## WufiVolumeGrossMode

Method for determining gross building volume in WUFI.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `USER_DEFINED` | `6` | Gross volume entered manually by the user. |
| `FROM_VISUALIZED_COMPONENTS` | `7` | Gross volume calculated from modeled component geometry. |

---

## WufiVolumeNetMode

Method for determining net interior volume in WUFI.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `ESTIMATED_FROM_GROSS` | `4` | Net volume estimated as a fraction of gross volume. |
| `FROM_GROSS_AND_COMPONETS` | `5` | Net volume derived from gross volume minus component thicknesses. |
| `USER_DEFINED` | `6` | Net volume entered manually by the user. |
| `FROM_VISUALIZED_COMPONENTS` | `7` | Net volume calculated from modeled component geometry. |

---

## WufiWeightedFloorAreaMode

Method for determining weighted floor area (TFA/iCFA) in WUFI.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `FROM_VISUALIZED_GEOMETRY` | `2` | Floor area calculated from modeled floor geometry. |
| `ESTIMATED_FROM_GROSS_VOLUME` | `4` | Floor area estimated from the gross volume. |
| `USER_DEFINED` | `6` | Floor area entered manually by the user. |

---

## ZoneType

Classification of thermal zones in the energy model.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `SIMULATED` | `1` | Zone included in the active energy balance simulation. |
| `ATTACHED` | `2` | Adjacent unconditioned zone not directly simulated. |

---

## AttachedZoneType

Specific type of an attached (non-simulated) thermal zone.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `NONE` | `0` | No attached zone type assigned. |
| `UNHEATED_SPACE` | `1` | Generic unheated adjacent space. |
| `UNHEATED_CELLAR` | `2` | Unheated basement or cellar. |
| `UNHEATED_CRAWLSPACE` | `3` | Unheated crawlspace below the building. |
| `UNHEATED_WINTER_GARDEN` | `4` | Unheated sunroom or winter garden. |
| `UNHEATED_ATTIC` | `5` | Unheated attic space. |
| `CONDITIONED` | `6` | Attached zone that is conditioned. |

---

## WindExposureType

Wind exposure classification for infiltration calculations.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `SEVERAL_SIDES_EXPOSED_NO_SCREENING` | `1` | Multiple facades exposed, no wind screening. |
| `SEVERAL_SIDES_EXPOSED_MODERATE_SCREENING` | `2` | Multiple facades exposed, moderate wind screening. |
| `SEVERAL_SIDES_EXPOSED_HIGH_SCREENING` | `3` | Multiple facades exposed, high wind screening. |
| `ONE_SIDE_EXPOSED_NO_SCREENING` | `4` | Single facade exposed, no wind screening. |
| `ONE_SIDE_EXPOSED_MODERATE_SCREENING` | `5` | Single facade exposed, moderate wind screening. |
| `ONE_SIDE_EXPOSED_HIGH_SCREENING` | `7` | Single facade exposed, high wind screening. |
| `USER_DEFINED` | `6` | User-specified wind exposure coefficient. |

---
