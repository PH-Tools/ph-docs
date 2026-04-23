# xl_typing

XL-App Protocol Classes.

**Source**: `PHX/xl_typing.py`

---

## xl_Range_Font

Protocol defining the interface for an Excel range font object.

---

## xl_RangeColumns_Protocol

Protocol defining the interface for an Excel range columns collection.

---

## xl_CellRange_Protocol

Protocol defining the interface for a single Excel cell range.

---

## xl_Range_Protocol

Protocol defining the interface for an Excel range object.

### Methods

#### end(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

#### options(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

#### offset(row_offset, column_offset)

| Arg | Type | Description |
|-----|------|-------------|
| `row_offset` | — | — |
| `column_offset` | — | — |

---

## xl_API_Protocol

Protocol defining the interface for an Excel sheet's native API object.

### Methods

#### Rows(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

#### unprotect()

#### Unprotect()

---

## xl_Sheet_Protocol

Protocol defining the interface for an Excel worksheet object.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `api` | `xl_API_Protocol` | — |
| `protected` | `bool` | — |

### Methods

#### range(cell1, cell2)

| Arg | Type | Description |
|-----|------|-------------|
| `cell1` | — | — |
| `cell2` | — | — |

#### clear_contents()

#### clear_formats()

#### clear()

#### activate()

#### autofit(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

#### delete()

---

## xl_Sheets_Protocol

Protocol defining the interface for a collection of Excel worksheets.

### Methods

#### add(name, before, after)

| Arg | Type | Description |
|-----|------|-------------|
| `name` | — | — |
| `before` | — | — |
| `after` | — | — |

---

## xl_Book_Protocol

Protocol defining the interface for an Excel workbook object.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `app` | `xl_app_Protocol` | — |
| `sheets` | `xl_Sheets_Protocol` | — |

---

## xl_Books_Protocol

Protocol defining the interface for a collection of Excel workbooks.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `active` | `xl_Book_Protocol` | — |

### Methods

#### add()

#### open(_p)

| Arg | Type | Description |
|-----|------|-------------|
| `_p` | — | — |

---

## xl_app_Protocol

Protocol defining the interface for an Excel application instance.

### Methods

#### calculate()

---

## xl_apps_Protocol

Protocol defining the interface for a collection of Excel application instances.

### Methods

#### add()

---

## xl_Framework_Protocol

Protocol defining the interface for the Excel interop framework (e.g., xlwings).

### Methods

#### Range(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

---
