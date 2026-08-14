# site

Passive-House Style Monthly Climate Data

**Source**: `honeybee_ph/site.py`

---

## Climate_MonthlyValueSet

A set of 12 monthly climate values (temperature, radiation, etc.).

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

Collection of monthly temperature data sets.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `air_temps` | — | Monthly air temperatures in degrees C. |
| `dewpoints` | — | Monthly dewpoint temperatures in degrees C. |
| `sky_temps` | — | Monthly sky temperatures in degrees C. |
| `ground_temps` | — | Monthly ground temperatures in degrees C. |

---

## Climate_MonthlyRadiationCollection

Collection of monthly solar radiation data by orientation.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `north` | — | Monthly north-facing radiation in kWh/m2. |
| `east` | — | Monthly east-facing radiation in kWh/m2. |
| `south` | — | Monthly south-facing radiation in kWh/m2. |
| `west` | — | Monthly west-facing radiation in kWh/m2. |
| `glob` | — | Monthly global horizontal radiation in kWh/m2. |

---

## Climate_PeakLoadValueSet

A set of peak load climate data for a single design condition.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `temp` | — | Design temperature in degrees C. |
| `rad_north` | — | North-facing radiation in W/m2. |
| `rad_east` | — | East-facing radiation in W/m2. |
| `rad_south` | — | South-facing radiation in W/m2. |
| `rad_west` | — | West-facing radiation in W/m2. |
| `rad_global` | — | Global horizontal radiation in W/m2. |
| `dewpoint` | — | Dewpoint temperature in degrees C. |
| `sky_temp` | — | Sky temperature in degrees C. |
| `ground_temp` | — | Ground temperature in degrees C. |

---

## Climate_PeakLoadCollection

Collection of peak heating and cooling load design conditions.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `heat_load_1` | — | Primary heating design condition. |
| `heat_load_2` | — | Secondary heating design condition. |
| `cooling_load_1` | — | Primary cooling design condition. |
| `cooling_load_2` | — | Secondary cooling design condition. |

---

## Climate_Ground

Ground thermal properties for foundation heat loss calculations.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `ground_thermal_conductivity` | `int` | Thermal conductivity in W/(mK). Default: 2. |
| `ground_heat_capacity` | `int` | Specific heat capacity in J/(kgK). Default: 1000. |
| `ground_density` | `int` | Density in kg/m3. Default: 2000. |
| `depth_groundwater` | `int` | Depth to groundwater table in meters. Default: 3. |
| `flow_rate_groundwater` | `float` | Groundwater flow rate in m/day. Default: 0.05. |

---

## ClimateProvenance

Source identity, conversion method, and availability for climate data.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `source_type` | — | Source category. One of ``legacy_unknown``, ``phi_approved``, ``phius_approved``, ``epw_derived``, or ``user_defined``. |
| `source_name` | — | Human-readable source name. |
| `source_uri` | — | Source file path or URI. |
| `source_version` | — | Version of the source data. |
| `source_checksum` | — | SHA-256 checksum for a file source. |
| `conversion_method` | — | Algorithm used to convert the source. |
| `conversion_method_version` | — | Version of the conversion method. |
| `is_certification_approved` | — | Whether the source is approved for certification; ``None`` means unknown. |
| `monthly_data_available` | — | Whether monthly-demand data is available. |
| `peak_load_data_available` | — | Whether peak-load data is available. |
| `assumptions` | — | JSON-safe conversion assumptions. |

---

## Climate

Complete climate dataset for PH energy modeling.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `display_name` | — | — |
| `station_elevation` | — | Weather station elevation in meters. |
| `summer_daily_temperature_swing` | — | Daily temperature swing in K. Default: 8.0. |
| `average_wind_speed` | — | Average wind speed in m/s. Default: 4.0. |
| `ground` | `Climate_Ground` | Ground thermal properties. |
| `monthly_temps` | — | Monthly temperature data. |
| `monthly_radiation` | — | Monthly radiation data. |
| `provenance` | — | Source and availability metadata. |
| `peak_loads` | — | Peak load design conditions. |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `is_monthly_demand_ready` | `bool` | Whether all explicitly available monthly-demand fields are finite. |
| `is_peak_load_ready` | `bool` | Whether all explicitly available peak-load fields are finite. |

### Methods

#### monthly_demand_readiness_issues()

Return deterministic issues preventing monthly-demand use.

**Returns**: `List[str]`

#### peak_load_readiness_issues()

Return deterministic issues preventing peak-load use.

**Returns**: `List[str]`

---

## Location

Geographic location data for the building site.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `latitude` | — | Site latitude in decimal degrees. Default: 40.6. |
| `longitude` | — | Site longitude in decimal degrees. Default: -73.8. |
| `site_elevation` | — | Site elevation in meters above sea level. |
| `climate_zone` | — | ASHRAE climate zone number, or None when the source does not supply one. Default: 1. |
| `hours_from_UTC` | — | Time zone offset from UTC in hours. Default: -4. |

---

## PHPPCodes

PHPP climate library reference codes.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `country_code` | — | PHPP country code string. Default: "US-United States of America". |
| `region_code` | — | PHPP region code string. Default: "New York". |
| `dataset_name` | — | PHPP dataset identifier. Default: "US0055c-New York". |

### Methods

#### *classmethod* blank()

Create a record with no PHPP climate-library identity.

**Returns**: `PHPPCodes`

---

## Site

Complete site data combining location, climate, and PHPP library codes.

**Inherits from**: `_base._Base`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `location` | — | Geographic location data. |
| `climate` | — | Climate dataset for energy modeling. |
| `phpp_library_codes` | — | PHPP climate library reference codes. |

### Methods

#### *classmethod* from_epw(file_path, ground_temperature_depth, ground_reflectance, diffuse_model)

Create a preliminary monthly-demand Site from a caller-supplied EPW.

| Arg | Type | Description |
|-----|------|-------------|
| `file_path` | `str` | Path to a local annual EPW file. |
| `ground_temperature_depth` | `Optional[float]` | EPW ground-series depth in meters. May be omitted only when exactly one series is available. |
| `ground_reflectance` | `float` | Finite directional-radiation ground reflectance from 0 through 1. Default: 0.2. |
| `diffuse_model` | `str` | ``"isotropic"`` or ``"anisotropic"``. |

**Returns**: `Site`

---
