# io_solar_dhw

Controller Class for the PHPP "SolarDHW" worksheet.

**Source**: `PHX/io_solar_dhw.py`

---

## SolarDHWData

Convenience class for organizing and cleaning the data.

### Methods

#### *classmethod* from_PHPP_data(_data)

Clean up the data coming in from PHPP

| Arg | Type | Description |
|-----|------|-------------|
| `_data` | — | — |

---

## SolarDHW

IO Controller for the PHPP 'Solar DHW' worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Methods

#### get_phpp_data()

Get the data from the PHPP worksheet.

---
