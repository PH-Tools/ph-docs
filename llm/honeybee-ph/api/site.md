# site

Passive-House Style Monthly Climate Data

**Source**: `honeybee_ph/site.py`

---

## Climate_MonthlyValueSet

A set of 12 monthly values (temp, radiation, etc).

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `values` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `values` | `List[float]` | — |

---

## Climate_MonthlyTempCollection

Collection class to organize monthly temperature values

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `air_temps` | — | — |
| `dewpoints` | — | — |
| `sky_temps` | — | — |
| `ground_temps` | — | — |

---

## Climate_MonthlyRadiationCollection

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `north` | — | — |
| `east` | — | — |
| `south` | — | — |
| `west` | — | — |
| `glob` | — | — |

---

## Climate_PeakLoadValueSet

A set of Peak Load data.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `temp` | — | — |
| `rad_north` | — | — |
| `rad_east` | — | — |
| `rad_south` | — | — |
| `rad_west` | — | — |
| `rad_global` | — | — |
| `dewpoint` | — | — |
| `sky_temp` | — | — |
| `ground_temp` | — | — |

---

## Climate_PeakLoadCollection

A Collection of Peak Loads (Heating and Cooling).

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heat_load_1` | — | — |
| `heat_load_2` | — | — |
| `cooling_load_1` | — | — |
| `cooling_load_2` | — | — |

---

## Climate_Ground

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ground_thermal_conductivity` | `int` | — |
| `ground_heat_capacity` | `int` | — |
| `ground_density` | `int` | — |
| `depth_groundwater` | `int` | — |
| `flow_rate_groundwater` | `float` | — |

---

## Climate

No description available.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | — | — |
| `station_elevation` | — | — |
| `summer_daily_temperature_swing` | — | — |
| `average_wind_speed` | — | — |
| `ground` | `Climate_Ground` | — |
| `monthly_temps` | — | — |
| `monthly_radiation` | — | — |
| `peak_loads` | — | — |

---

## Location

Geographic Location Information.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `latitude` | — | — |
| `longitude` | — | — |
| `site_elevation` | — | — |
| `climate_zone` | — | — |
| `hours_from_UTC` | — | — |

---

## PHPPCodes

Settings / names if using Pre-loaded PHPP Library Data

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `country_code` | — | — |
| `region_code` | — | — |
| `dataset_name` | — | — |

---

## Site

Location and Climate data for the building site.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `location` | — | — |
| `climate` | — | — |
| `phpp_library_codes` | — | — |

---
