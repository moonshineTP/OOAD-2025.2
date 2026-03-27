---
applyTo: "docs/**,Project/**"
description: "OOAD analysis phase rules for LogiFast/Ricons BTL. Use when editing domain models, class diagrams, object diagrams, SSDs, CRC cards, or CRUD matrix in any format."
---

# OOAD Analysis Phase — Enforcement Rules

## ⚠️ Attribute Rules (Part I — Domain Model)
- Write attribute **names ONLY** — NO `:Type`, NO `:String`, NO `:int`, NO `:Date`
- NO visibility markers (`+`, `-`, `#`) on any attribute
- These are added ONLY in Part II (design phase / enriched class diagram)

**Wrong (Part I):** `- maDonHang: String`, `+ ngayTao: Date`
**Correct (Part I):** `maDonHang`, `ngayTao`

## Association Rules
- Every association MUST have a **name** (label on the line)
- Every association MUST have **multiplicities at BOTH ends** — never just one end
- Multiplicity format: `1`, `0..1`, `*`, `1..*`
- Direction of multiplicity: placed at the TARGET end of the arrow

## Per-UC Diagram Rules
- Each UC must have its OWN separate class diagram — no shared global diagram
- Class diagrams across UCs MUST meaningfully differ (different classes or different relationships)
- Each UC must have ≥1 object diagram showing a concrete usage scenario

## SSD Rules (System Sequence Diagram)
- Lifelines: ONLY `Actor` (stick figure) + `:System` (box) — NO Controller, DAO, Service, etc.
- Every SSD must have >2 outgoing messages from the actor to :System
- All SSD messages must be traceable to a step in the UC main flow

## CRC Card Format
```
| Lớp        | [ClassName]                     |
|-------------|----------------------------------|
| Trách nhiệm | [Responsibility 1]               |
|             | [Responsibility 2]               |
| Đối tác     | [Collaborating class names]      |
```
- In Part I: attributes section contains names only (no types)
- In Part II: add types to CRC attribute section

## CRUD Matrix Requirements
- Rows = ALL use cases (UC-01 through UC-05)
- Columns = ALL domain classes from all UC class diagrams
- Cell values: C (Create), R (Read), U (Update), D (Delete), blank (no interaction)
- Each CRUD value must be traceable to a specific UC step number

## State Machine Rules
- Every transition label must reference EITHER a UC activity step OR an SSD message
- Format: `trigger [guard] / action`

## Checklist Before Submitting Any Diagram
- [ ] No `:Type` on attributes (Part I only)
- [ ] No `+/-/#` visibility markers (Part I only)
- [ ] All associations named
- [ ] Multiplicities at both ends of every association
- [ ] Per-UC class diagram (not one global diagram)
- [ ] ≥1 object diagram per UC
- [ ] ≥1 SSD per UC with >2 messages
- [ ] SSD has only Actor + :System lifelines
- [ ] CRUD matrix present with all UCs and classes
