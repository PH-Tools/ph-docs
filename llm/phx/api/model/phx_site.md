# phx_site

PHX Site (Location and Climate) Dataclasses

**Source**: `PHX/phx_site.py`

---

## PhxGround

No description available.

---

## PhxPEFactor

Conversion Factors for Site-Energy->Primary-Energy

---

## PhxCO2Factor

Conversion Factors for Site->CO2

---

## PhxSiteEnergyFactors

No description available.

---

## PhxLocation

The physical location of the building.

---

## PhxClimatePeakLoad

No description available.

---

## PhxClimateIterOutput

Wrapper class for organizing output of the 'PhxClimate.monthly_values' property.

---

## PhxClimate

Monthly Climate Date for the building location.

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

No description available.

---

## PhxSite

The climate and location date for the building's site.

---
