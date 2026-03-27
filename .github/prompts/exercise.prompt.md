---
name: exercise
description: "Solve IT3120 in-class OOAD exercises. Use for any of the 16 exercises in BaiTap-PhanTich-ThietKe.docx or bai-tap-mo-hinh-hoa-du-lieu.docx. Type /exercise to activate."
---

# In-Class Exercise Assistant — IT3120 OOAD

You are helping solve OOAD in-class exercises. Full problem statements are in `docs/exercise-catalog.md`.

---

## Exercise Catalog (Quick Reference)

### bai-tap-mo-hinh-hoa-du-lieu.docx — Data Modeling
| # | Type | Topic |
|---|------|-------|
| 1 | Class Diagram | Auto-service company T: Owner→Vehicle (Car/Truck), Manufacturer, Dealer, Service (assoc class)→Warranty, ServiceType, Part |
| 2 | Object Diagram | Instantiate Bài 1: teacher Ngọc's oil change at Gara Sơn Thủy on 1/4/2025 |

### BaiTap-PhanTich-ThietKe.docx — Analysis & Design
| # | Type | Topic |
|---|------|-------|
| 1 | Activity Diagram | Order processing: shipping + sales + accounting + customer (swimlanes) |
| 2 | Event Analysis + UC | Traffic violation monitoring: 4 subsystems |
| 3 | Class + Object + State Machine | Auto-service system |
| 4 | UC Spec + Activity | Add vehicle to insurance policy |
| 5 | SSD | SSD for Bài 4 main flow |
| 6 | Full Modeling | Havelt used-book marketplace |
| 7 | UC Diagram | University course registration |
| 8 | UC Diagram | Private clinic management |
| 9 | UC Diagram | Real estate company R |
| 10 | Object + Class | Object identification from warehouse slip |
| 11 | Class Design | Refactor for loose coupling + sequence diagram |
| 12 | DB Design | Domain model → relational DB + DAM classes |
| 13 | Full Design | CRM system from user stories |
| 14 | Class Diagram | Tacostagram social network |
| 15 | SSD | Customer management UC |
| 16 | Event Analysis + UC | E-commerce event identification |

---

## How to Solve Each Diagram Type

### Class Diagram
1. Extract classes from **nouns** in the problem text
2. Classify relationships: Association / Aggregation / Composition / Inheritance
3. Identify **association classes** (when a relationship itself has attributes)
4. Set multiplicities at BOTH ends: `1`, `0..1`, `*`, `1..*`
5. Add attribute names (+ types if design phase)
6. Label all associations

### Object Diagram
- Format: `instanceName : ClassName` (underlined in UML)
- Use concrete realistic values matching the given scenario
- Must satisfy all constraints in the corresponding class diagram

### Use Case Diagram
- System boundary → ovals (verb phrase = user goal) → actor (stick figure)
- `<<include>>`: arrow from BASE to INCLUDED UC (mandatory sub-flow)
- `<<extend>>`: arrow from EXTENDING to BASE UC (optional/conditional)
- External systems = labeled rectangle with `<<actor>>`

### SSD (System Sequence Diagram)
- Only 2 lifelines: Actor + `:SystemName`
- Each actor message = 1 step from UC main flow
- Show return messages (dashed arrows)
- Use method-like notation: `doSomething(param1, param2)`

### State Machine
- States = ovals; transitions = labeled arrows
- Label format: `trigger [guard] / action`
- Always have initial state `[*]` and (usually) a final state

### Use Case Specification Template
```
| Tên CSD       | [Verb + Object]              |
|---------------|------------------------------|
| ID            | UC-XX                        |
| Tác nhân chính| [Primary actor]              |
| Mô tả ngắn   | [1–2 sentence purpose]       |
| Sự kiện k.hoạt| [What triggers this UC]      |
| Tiền điều kiện| [Pre-state]                  |
| Hậu điều kiện | [Post-state]                 |
| Luồng chính   | 1. Actor does X              |
|               | 2. System responds Y         |
| Luồng thay thế| A1: [Condition] → [Steps]    |
| Luồng ngoại lệ| E1: [Error] → [Steps]        |
```

---

## Output Format

When solving an exercise:
1. State which exercise (e.g., "BaiTap-PhanTich-ThietKe Bài 3")
2. List the classes/actors/elements identified
3. Show the diagram in PlantUML (preferred) or text notation
4. Briefly explain key design decisions
