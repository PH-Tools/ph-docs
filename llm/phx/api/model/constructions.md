# constructions

PHX Construction, Materials Classes

**Source**: `PHX/constructions.py`

---

## PhxColor

An ARGB color value used for material display in WUFI-Passive.

---

## PhxMaterial

A single building material with thermal, hygric, and display properties.

### Methods

#### equivalent(other)

Check if two materials are equivalent except for their ID-Number.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

---

## PhxLayerDivisionCell

A single cell at a column/row position in a PhxLayerDivisionGrid, holding one material.

---

## PhxLayerDivisionGrid

A grid of PhxLayerDivisionCells to support 'mixed' materials in a single layer.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `column_widths` | — | Return the list of column widths. |
| `column_count` | — | Return the number of columns in the grid. |
| `row_heights` | — | Return the list of row heights. |
| `row_count` | — | Return the number of rows in the grid. |
| `cell_count` | — | Return the total number of cells in the grid. |
| `cells` | — | Return a list of all the PhxLayerDivisionCells in the grid, ordered by row then column |

### Methods

#### set_column_widths(_column_widths)

Set the column widths of the grid.

| Arg | Type | Description |
|-----|------|-------------|
| `_column_widths` | — | — |

#### add_new_column(_column_width)

Add a new COLUMN to the grid with the given width.

| Arg | Type | Description |
|-----|------|-------------|
| `_column_width` | — | — |

#### set_row_heights(_row_heights)

Set the row heights of the grid.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_heights` | — | — |

#### add_new_row(_row_height)

Add a new ROW to the grid with the given height. Will add a default column if none are set.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_height` | — | — |

#### get_cell(_column, _row)

Get the PhxLayerDivisionCell at the given column and row position.

| Arg | Type | Description |
|-----|------|-------------|
| `_column` | — | — |
| `_row` | — | — |

#### set_cell_material(_column_num, _row_num, _phx_material)

Set the PhxMaterial for a specific cell in the grid by its column/row position.

| Arg | Type | Description |
|-----|------|-------------|
| `_column_num` | — | — |
| `_row_num` | — | — |
| `_phx_material` | — | — |

#### get_cell_material(_column_num, _row_num)

Get the PhxMaterial for a specific cell in the grid by its column/row position.

| Arg | Type | Description |
|-----|------|-------------|
| `_column_num` | — | — |
| `_row_num` | — | — |

#### get_cell_area(_column_num, _row_num)

Get the area of the cell (row-height * column-width).

| Arg | Type | Description |
|-----|------|-------------|
| `_column_num` | — | — |
| `_row_num` | — | — |

#### get_base_material()

Get the 'base' material of the grid (the most common material in the layer, by cell-area).

#### populate_defaults()

Populate the grid with default values. Ensure that there is at least one row or column.

---

## PhxLayer

A single layer in a PhxConstructionOpaque assembly.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `materials` | — | Return a list of all the PhxMaterials in the Layer. |
| `material` | — | Return the base PhxMaterial of the Layer. |
| `thickness_mm` | — | Returns the thickness of the layer in MM |
| `layer_resistance` | — | Returns the thermal-resistance of the layer in m2K/W |
| `layer_conductance` | — | Returns the thermal-conductance of the layer in W/m2K |
| `division_materials` | — | Returns a list of all the PhxLayerDivisionCell PhxMaterials ordered by column and then row: |
| `exchange_materials` | — | Returns a list of all the 'Exchange' materials (for mixed layers) in all the Division Cells. |
| `division_material_id_numbers` | — | Returns a list of all the 'Exchange' material id-numbers in all the Division Cells. |

### Methods

#### add_material(_material)

Add a PhxMaterial to the self.materials collection.

| Arg | Type | Description |
|-----|------|-------------|
| `_material` | — | — |

#### set_material(_material)

Set the PhxMaterial for the layer.

| Arg | Type | Description |
|-----|------|-------------|
| `_material` | — | — |

#### *classmethod* from_total_u_value(_total_u_value)

Returns a new PhxLayer with a single material with the given U-Value.

| Arg | Type | Description |
|-----|------|-------------|
| `_total_u_value` | — | — |

#### equivalent(other)

Check if two layers are equivalent.

| Arg | Type | Description |
|-----|------|-------------|
| `other` | — | — |

---

## PhxConstructionOpaque

An opaque assembly construction (wall, roof, or floor) composed of ordered material layers.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `identifier` | — | — |
| `heat_flow_pathways` | — | Return the unique heat-flow pathways through this assembly. |
| `r_value` | — | Total thermal resistance of the assembly in m2K/W, computed from heat-flow pathways. |
| `u_value` | — | Total thermal transmittance (U-value) of the assembly in W/m2K. |
| `exchange_materials` | — | Returns a flat list of all the 'Exchange' materials (for mixed layers) from all the Layers. |

### Methods

#### *classmethod* from_total_u_value(_total_u_value, _display_name)

Returns a new PhxConstructionOpaque with a single layer with the given U-Value.

| Arg | Type | Description |
|-----|------|-------------|
| `_total_u_value` | — | — |
| `_display_name` | — | — |

---

## PhxWindowFrameElement

A single frame edge element (top, bottom, left, or right) of a window construction.

### Methods

#### *classmethod* from_total_u_value(_total_u_value)

Returns a new PhxWindowFrameElement with u-values set to a single value.

| Arg | Type | Description |
|-----|------|-------------|
| `_total_u_value` | — | — |

---

## PhxConstructionWindow

A window construction defining glazing, frame, and overall thermal properties.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `glazing_type_display_name` | — | — |
| `frame_type_display_name` | — | — |
| `identifier` | — | — |
| `id_num_shade` | — | — |
| `frames` | — | Returns a generator of all frame elements in order: Top, Right, Bottom, Left. |

### Methods

#### *classmethod* from_total_u_value(_total_u_value, _g_value, _display_name)

Returns a new PhxConstructionWindow with all u-values set to a single value.

| Arg | Type | Description |
|-----|------|-------------|
| `_total_u_value` | — | — |
| `_g_value` | — | — |
| `_display_name` | — | — |

#### set_all_frames_u_value(_u_value)

Sets the u-value of all frame elements to the given value.

| Arg | Type | Description |
|-----|------|-------------|
| `_u_value` | — | — |

#### set_all_frames_width(_width)

Sets the width of all frame elements to the given value.

| Arg | Type | Description |
|-----|------|-------------|
| `_width` | — | — |

#### set_all_frames_psi_glazing(_psi_glazing)

Sets the psi_glazing of all frame elements to the given value.

| Arg | Type | Description |
|-----|------|-------------|
| `_psi_glazing` | — | — |

#### set_all_frames_psi_install(_psi_install)

Sets the psi_install of all frame elements to the given value.

| Arg | Type | Description |
|-----|------|-------------|
| `_psi_install` | — | — |

---
