# phx_site

PHX Site (Location and Climate) Dataclasses

**Source**: `PHX/phx_site.py`

---

## PhxGround

Soil and groundwater thermal properties for ground heat loss calculations.

---

## PhxPEFactor

Primary energy (PE) conversion factor for a single fuel type.

---

## PhxCO2Factor

CO2 emission factor for a single fuel type.

---

## PhxSiteEnergyFactors

Collection of primary energy (PE) and CO2 conversion factors for the site.

---

## PhxLocation

Geographic coordinates and site metadata for the building location.

---

## PhxClimatePeakLoad

Climate conditions at a single peak-load design point (heating or cooling).

---

## PhxClimateIterOutput

Single month of climate data yielded by PhxClimate.monthly_values.

---

## PhxClimate

Monthly climate dataset for the building location.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `max_temperature_air` | — | The maximum air temperature in the dataset. |
| `min_temperature_air` | — | The minimum air temperature in the dataset. |
| `max_air_temperature_amplitude` | — | The absolute difference between the maximum and minimum air temperature. |
| `average_temperature_amplitude` | — | The Average between the maximum and minimum air temperature. |
| `monthly_hours` | — | The a ordered (Jan-Dec) list of tuples containing the month-name and the number of hours in that month. |
| `monthly_values` | — | A generator that yields the monthly values one at a time for the climate data. |

---

## PhxPHPPCodes

PHPP climate dataset selection codes for country, region, and dataset.

---

## PhxSite

Top-level container for a building's site location, climate, and energy factors.

---
