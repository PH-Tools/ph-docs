# io_solar_pv

Controller Class for the PHPP "SolarPV" worksheet.

**Source**: `PHX/io_solar_pv.py`

---

## SolarPVData

Convenience class for organizing and cleaning the data.

### Methods

#### *classmethod* from_PHPP_data(_data)

Clean up the data coming in from PHPP

| Arg | Type | Description |
|-----|------|-------------|
| `_data` | — | — |

---

## SolarPV

IO Controller for the PHPP 'Solar PV' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

Get the data from the PHPP worksheet.

---
