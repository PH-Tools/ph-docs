# io_electricity

Controller Class for the PHPP 'Electricity' worksheet.

**Source**: `PHX/io_electricity.py`

---

## Electricity

IO Controller for PHPP "Electricity" worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `device_map` | `get_device_type_map` | — |

### Methods

#### write_equipment(_equipment_inputs)

Write a list of equipment-input objects to the Worksheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_equipment_inputs` | — | — |

#### build_phx_device_from_phpp(_reader)

Build a PHX Electrical Device object from the PHPP worksheet data.

| Arg | Type | Description |
|-----|------|-------------|
| `_reader` | — | — |

#### get_phx_elec_devices()

Read the Device data from the PHPP worksheet and return a list of PhxElectricalDevice objects.

---
