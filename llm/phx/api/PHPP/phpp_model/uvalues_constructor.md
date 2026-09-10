# uvalues_constructor

Data-entry constructor for the U-Values Worksheet.

**Source**: `PHX/uvalues_constructor.py`

---

## ConstructorBlock

A single U-Value/Constructor entry block.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `r_si_selector` | — | Return the PHPP orientation-selector string (Rsi) for the block's face-type. |
| `r_se_selector` | — | Return the PHPP adjacency-selector string (Rse) for the block's exterior exposure. |

### Methods

#### is_mass_material(_layer)

Return True if the Layer is an SD 'Mass' Layer.

| Arg | Type | Description |
|-----|------|-------------|
| `_layer` | — | — |

#### create_xl_items(_sheet_name, _start_row)

Convert the PHX-Construction into a list of XLItems for writing to the PHPP.

| Arg | Type | Description |
|-----|------|-------------|
| `_sheet_name` | — | — |
| `_start_row` | — | — |

---
