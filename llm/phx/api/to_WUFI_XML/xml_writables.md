# xml_writables

Classes used to build XML Node Objects which are used during XML Output

**Source**: `PHX/xml_writables.py`

---

## XML_Node

A single node text/numeric item. Optional Attribute data

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `node_name` | — | — |
| `node_value` | — | — |
| `attr_name` | — | — |
| `attr_value` | — | — |

---

## XML_List

A List of XML Writable objects. Used to add 'count' info to the list parent node

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `node_name` | — | — |
| `node_items` | — | — |
| `attr_name` | — | — |

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `attr_value` | — | — |

---

## XML_Object

XML Writable Object. Object fields will be written out as child nodes

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `node_name` | — | — |
| `node_object` | — | — |
| `attr_name` | — | — |
| `attr_value` | — | — |
| `schema_name` | — | — |

---
