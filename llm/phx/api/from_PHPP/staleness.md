# staleness

Stale-cache signals: can the cached values in a closed PHPP be trusted?

**Source**: `PHX/staleness.py`

---

## FreshnessVerdict

The reader's verdict on the cached values.

**Inherits from**: `enum.Enum`

### Values

| Member | Value | Meaning |
|--------|-------|---------|
| `FRESH` | `'fresh'` | Last saved by Excel, automatic calculation, no recalc-on-load flag, results cached. |
| `SUSPECT` | `'suspect'` | Something observable says the cache may be behind (manual calc, recalc flag, non-Excel writer). |
| `EMPTY` | `'empty'` | The results cells carry formulas but no cached values at all — nothing to read. |

---

## Freshness

Verdict plus the evidence it rests on.

---
