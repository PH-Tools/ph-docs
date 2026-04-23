# io_hot_water

Controller Class for the PHPP "DHW+Distribution" worksheet.

**Source**: `PHX/io_hot_water.py`

---

## RecircPiping

The Recirculation Piping Section Group

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | — |

### Methods

#### find_header_row(_row_start, _rows)

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_rows` | — | — |

---

## BranchPiping

The Branch Piping Section Group

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | — |

### Methods

#### find_header_row(_row_start, _rows)

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_rows` | — | — |

---

## DHWPiping

The DHW Piping Section Group

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `recirc_piping` | `RecircPiping` | — |
| `branch_piping` | `BranchPiping` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | — |

### Methods

#### find_header_row(_row_start, _row_end)

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### find_recirc_piping_start_row()

#### find_branch_piping_start_row()

---

## TankData

Convenience Wrapper for Tank Data read in from the PHPP.

### Methods

#### *classmethod* from_phpp_data(_d)

| Arg | Type | Description |
|-----|------|-------------|
| `_d` | — | — |

---

## Tank

An individual tank entry item.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `entry_row_start` | — | The row where the tank entry starts. |

### Methods

#### find_entry_row_start()

Find the row where the tank entry starts.

#### get_phpp_data(_tank_num)

Get the PHPP data for the specified tank number.

| Arg | Type | Description |
|-----|------|-------------|
| `_tank_num` | — | — |

---

## Tanks

The Tanks (Storage Heat Loss) Section Group

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `tank_1` | `Tank` | — |
| `tank_2` | `Tank` | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `header_row` | — | The row where the tank header starts. |

### Methods

#### find_header_row(_row_start, _row_end)

Find the row where the tank header starts.

| Arg | Type | Description |
|-----|------|-------------|
| `_row_start` | — | — |
| `_row_end` | — | — |

#### get_all_tank_device_data()

Get all the tank data from the spreadsheet.

---

## HotWater

IO Controller for the PHPP 'DHW+Distribution' PHPP worksheet.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `xl` | — | — |
| `shape` | — | — |
| `tanks` | `Tanks` | — |
| `dhw_piping` | `DHWPiping` | — |

### Methods

#### write_tanks(_phpp_hw_tanks)

Write the tank data to the spreadsheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_hw_tanks` | — | — |

#### write_branch_piping(_phpp_branch_piping)

Write the branch piping data to the spreadsheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_branch_piping` | — | — |

#### write_recirc_piping(_phpp_recirc_piping)

Write the recirc piping data to the spreadsheet.

| Arg | Type | Description |
|-----|------|-------------|
| `_phpp_recirc_piping` | — | — |

#### get_all_tank_device_data()

Get all the tank data from the PHPP worksheet.

---
