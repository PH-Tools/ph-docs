# xl_data

Basic datatypes and data-structures relevant for Excel read/write.

**Source**: `PHX/xl_data.py`

---

## XlItem

A single XLItem which can be written out to a specific XL Range.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `sheet_name` | — | — |
| `xl_range` | — | — |
| `input_unit` | — | — |
| `target_unit` | — | — |
| `xl_range_base` | — | — |
| `range_color` | — | — |
| `font_color` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `xl_anchor_cell` | — | The range's top-left (anchor) cell. ie: 'A1:D10' -> 'A1', 'L41' -> 'L41'. |
| `xl_row_number` | — | — |
| `xl_col_number` | — | — |
| `xl_col_alpha` | — | — |
| `write_value` | — | — |
| `has_color` | — | Return True if the Item has font or background color values. |
| `value_is_iterable` | — | Return True is the item's value is a List or Tuple |

---

## XLItem_List

A list of XLItems which yield a list when 'write_value' is called.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `items` | — | — |
| `write_value` | — | — |
| `sheet_name` | — | — |
| `xl_range` | — | — |
| `xl_row_number` | — | — |
| `xl_col_number` | — | — |
| `xl_col_alpha` | — | — |
| `range_color` | — | — |
| `font_color` | — | — |
| `has_color` | — | Return True if any of the Items has font or background color values. |
| `value_is_iterable` | — | Return True. |

### Methods

#### validate_xl_item_range(_xl_item)

Raise Exception if the XlItem being added has an invalid xl_range.

| Arg | Type | Description |
|-----|------|-------------|
| `_xl_item` | — | — |

#### add_new_xl_item(_xl_item)

| Arg | Type | Description |
|-----|------|-------------|
| `_xl_item` | — | — |

---
