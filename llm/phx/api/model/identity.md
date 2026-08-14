# identity

Project-scoped numeric identity allocation for PHX conversions.

**Source**: `PHX/identity.py`

---

## IdentityNamespaceKey

A named namespace carrying explicit project- or variant-ownership metadata.

**Inherits from**: `str`

---

## IdentityNamespaces

Stable namespace keys grouped by target/reference ownership.

### Methods

#### *staticmethod* mechanical_devices(owner)

Return the compatibility namespace for one mechanical leaf type.

| Arg | Type | Description |
|-----|------|-------------|
| `owner` | — | — |

#### *staticmethod* electrical_devices(owner)

Return the compatibility namespace for one electrical leaf type.

| Arg | Type | Description |
|-----|------|-------------|
| `owner` | — | — |

---

## LegacyCounterOwner

Structural type for classes that retain the legacy counter fallback.

**Inherits from**: `Protocol`

---

## IdentityAllocationError

Base error for invalid project identity allocation.

**Inherits from**: `ValueError`

---

## DuplicateIdentityError

Raised when one identity is claimed twice in the same namespace.

**Inherits from**: `IdentityAllocationError`

### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `namespace` | — | — |
| `value` | — | — |
| `existing_source` | — | — |
| `source` | — | — |

---

## IdentityAllocator

Allocate deterministic positive integers within independent namespaces.

### Methods

#### next_id(namespace)

Claim and return the next available positive integer in a namespace.

| Arg | Type | Description |
|-----|------|-------------|
| `namespace` | — | — |

#### claim_id(namespace, value, source)

Claim an explicit positive integer, raising on a namespace conflict.

| Arg | Type | Description |
|-----|------|-------------|
| `namespace` | — | — |
| `value` | — | — |
| `source` | — | — |

#### is_claimed(namespace, value)

Return whether a value is already claimed in a namespace.

| Arg | Type | Description |
|-----|------|-------------|
| `namespace` | — | — |
| `value` | — | — |

#### snapshot()

Return a deterministic diagnostic view of allocated identities.

---

## IdentityOwningProject

Structural contract for projects that retain their construction allocator.

**Inherits from**: `Protocol`

---
