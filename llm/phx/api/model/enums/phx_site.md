# phx_site

Valid 'types' for Site Settings.

**Source**: `PHX/phx_site.py`

---

## SiteSelection

Selection source for site location data.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `WUFI_DATABASE` | `1` | Site data from the WUFI climate database. |
| `USER_DEFINED` | `2` | Site data entered manually by the user. |
| `STANDARD` | `3` | Standard default site data. |

---

## SiteClimateSelection

Selection source for climate data.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD` | `1` | Standard climate data set. |
| `WUFI_DATABASE` | `2` | Climate data from the WUFI climate database. |
| `USER_DEFINED` | `6` | Climate data entered manually by the user. |

---

## SiteEnergyFactorSelection

Selection source for primary energy and CO2 conversion factors.

**Inherits from**: `Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `STANDARD_USA` | `1` | Standard US energy factors. |
| `STANDARD_GERMANY` | `2` | Standard German energy factors. |
| `STANDARD_ITALY` | `2` | Standard Italian energy factors. |
| `STANDARD_CANADA` | `4` | Standard Canadian energy factors. |
| `USER_DEFINED` | `6` | User-specified energy factors. |

---
