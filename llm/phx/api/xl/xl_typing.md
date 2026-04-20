# xl_typing

XL-App Protocol Classes.

**Source**: `PHX/xl_typing.py`

---

## xl_Range_Font

No description available.

---

## xl_RangeColumns_Protocol

No description available.

---

## xl_CellRange_Protocol

No description available.

---

## xl_Range_Protocol

No description available.

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

No description available.

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

No description available.

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

No description available.

### Methods

#### add(name, before, after)

| Arg | Type | Description |
|-----|------|-------------|
| `name` | — | — |
| `before` | — | — |
| `after` | — | — |

---

## xl_Book_Protocol

No description available.

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `app` | `xl_app_Protocol` | — |
| `sheets` | `xl_Sheets_Protocol` | — |

---

## xl_Books_Protocol

No description available.

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

No description available.

### Methods

#### calculate()

---

## xl_apps_Protocol

No description available.

### Methods

#### add()

---

## xl_Framework_Protocol

No description available.

### Methods

#### Range(*args, **kwargs)

| Arg | Type | Description |
|-----|------|-------------|
| `*args` | — | — |
| `**kwargs` | — | — |

---
