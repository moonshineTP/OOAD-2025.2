# UML Notation Reference — IT3120 OOAD

Quick cheat sheet for all diagram types used in this course.

---

## Class Diagram (Sơ đồ lớp)

```
┌─────────────────┐
│   ClassName     │  ← Class name (bold, centered)
├─────────────────┤
│ - attr: Type    │  ← Attributes (- private, + public, # protected)
│ + attr: Type    │
├─────────────────┤
│ + method(): R   │  ← Methods (omit in domain model)
└─────────────────┘
```

### Relationships
| Symbol | Name | Meaning |
|--------|------|---------|
| `—————` | Association | "related to", "uses" |
| `————>` | Directed association | knows about, unidirectional |
| `◇————` | Aggregation | "has-a" (part exists independently) |
| `◆————` | Composition | "contains" (part cannot exist without whole) |
| `——|>` or `◁——` | Inheritance/Generalization | "is-a" |
| `- - ->` | Dependency | "uses temporarily" |
| `- - -|>` | Realization | implements interface |

### Association Class (Lớp liên kết)
```
Vehicle ———————————————— Dealer
            |
        ┌───┴────────┐
        │  Service   │   ← Drawn as class connected to the line
        │  date      │
        │  odo       │
        └────────────┘
```

### Multiplicities (Cơ số)
| Notation | Meaning |
|---------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one (optional) |
| `*` or `0..*` | Zero or many |
| `1..*` | One or many |
| `m..n` | Between m and n |

**Placement**: Multiplicities go at the TARGET end of the association.

### Visibility
- `+` public
- `-` private
- `#` protected
- `~` package

---

## Object Diagram (Sơ đồ đối tượng)

```
┌──────────────────────────┐
│ objectName : ClassName   │  ← underlined name:class
├──────────────────────────┤
│ attr1 = "value"          │  ← concrete attribute values
│ attr2 = 42               │
└──────────────────────────┘
```
- Anonymous objects: `: ClassName`
- Links (not associations) connect objects
- Must satisfy all class diagram constraints

---

## Use Case Diagram (Sơ đồ ca sử dụng)

```
┌─────────────────────────────────────────┐
│         SystemName                      │
│                                         │
│    (  UC Name  )      (  UC Name  )    │
│         │                  │            │
│    <<include>>        <<extend>>       │
│         │                  │            │
│    (  Sub UC   )     (  Base UC  )    │
│                                         │
└─────────────────────────────────────────┘
    O             O
   /|\           /|\
   / \           / \
  Actor1        Actor2
```

### Actor Types
| Type | Notation | Example |
|------|----------|---------|
| Human | Stick figure | Khách hàng, Tài xế |
| External system | Rectangle with `<<actor>>` or `<<system>>` | Hệ thống thanh toán |
| Time | `<<actor>>` labeled "Timer" | Scheduled events |

### Relationships
| Relationship | Direction | Meaning |
|-------------|-----------|---------|
| `<<include>>` | base → included | Included UC always runs as part of base |
| `<<extend>>` | extension → base | Extension runs conditionally |
| Generalization | child → parent | Actor or UC inheritance |

---

## Activity Diagram (Sơ đồ hoạt động)

```
       Actor1             Actor2           Actor3
         │                  │                │
    ●    │                  │                │    ← Initial node
    │    │                  │                │
  [Action]                  │                │
    │    │                  │                │
    ├────────────────>[Action2]              │    ← Parallel fork (thick bar)
    │    │                  │                │
    │    │            [Action3]              │
    │    │                  │                │
  <Decision>                │                │    ← Decision diamond
  /        \                │                │
[Alt1]   [Alt2]             │                │
    \        /              │                │
   [Merge]                  │                │
    │    │                  │                │
    ⊙    │                  │                │    ← Final node
```

### Key Nodes
| Node | Symbol | Purpose |
|------|--------|---------|
| Initial | `●` (filled circle) | Start point |
| Action | Rounded rectangle | An activity |
| Decision | `◇` | Branching on condition |
| Merge | `◇` | Joining alternative paths |
| Fork | Thick bar (multiple out) | Start parallel flows |
| Join | Thick bar (multiple in) | Synchronize parallel flows |
| Object/Document | Rectangle (sharp corners) | Artifact flowing between swimlanes |
| Final | `⊙` (circle+dot) | End point |

---

## System Sequence Diagram — SSD (Sơ đồ tuần tự mức hệ thống)

```
       Actor                  :System
         │                       │
         │──── systemOp1() ──────>│
         │                       │  (internal processing)
         │<════ return value ═════│
         │                       │
    loop │──── systemOp2(x) ────>│
         │<════ response ═════════│
    end  │                       │
         │                       │
   alt   │──── systemOp3() ──────>│
   [condition A] │               │
         │<════ result A ═════════│
   [condition B] │               │
         │<════ result B ═════════│
   end   │                       │
```

### Rules
- **Only 2 lifelines**: actor + :System (or :SystemName)
- Shows only the **system boundary** — no internal objects
- Each system operation becomes a **message contract** later
- Solid arrows = calls; dashed arrows = returns
- Interaction fragments: `loop`, `alt`, `opt`, `ref`

---

## Business-Level Sequence Diagram (Sơ đồ tuần tự mức nghiệp vụ)

```
  Actor    :Controller    :DomainObj    :OtherObj    :DAM
    │            │              │             │         │
    │─message()─>│              │             │         │
    │            │──method()───>│             │         │
    │            │              │──method()──>│         │
    │            │              │<════════════│         │
    │            │              │──save()───────────────>│
    │            │              │<════════════════════════│
    │            │<═════════════│             │         │
    │<═══════════│              │             │         │
```

- Multiple lifelines: UI/Controller + all domain objects
- Shows MVC pattern: UI → Controller → Domain → DAM
- Object creation: lifeline starts at creation message (dashed box)

---

## State Machine Diagram (Sơ đồ máy trạng thái)

```
        ●
        │ (initial)
        ▼
  ┌──────────┐  event1 [guard] / action   ┌──────────┐
  │  State1  │ ────────────────────────> │  State2  │
  └──────────┘                           └──────────┘
        │                                      │
        │ event2                         event3│
        ▼                                      ▼
  ┌──────────┐                           ┌──────────┐
  │  State3  │                           │  State4  │
  └──────────┘                           └──────────┘
                                               │
                                               ▼
                                               ⊙  (final)
```

### Transition Syntax
```
trigger [guard] / action
```
- `trigger`: event that causes transition (can be omitted → automatic)
- `[guard]`: boolean condition (optional)
- `/ action`: action performed during transition (optional)

### State Activities
```
┌─────────────────────────────┐
│       StateName             │
├─────────────────────────────┤
│ entry / action              │  ← on entering state
│ do / activity               │  ← while in state
│ exit / action               │  ← on leaving state
└─────────────────────────────┘
```

---

## Communication Diagram (Sơ đồ giao tiếp)

```
    Actor
      │
      │ 1: message()
      ▼
  :Object1  ──── 1.1: method() ────>  :Object2
      │
      │ 1.2: method2()
      ▼
  :Object3
```
- Same information as sequence diagram but shown as network
- Messages numbered hierarchically: 1, 1.1, 1.2, 2, 2.1...
- Useful for showing object relationships more clearly

---

## Component Diagram (Sơ đồ thành phần)

```
┌──────────────┐    ─○─    ┌──────────────┐
│  Component1  │ ──────── │  Component2  │
│              │  requires │              │
└──────────────┘  interface└──────────────┘
```
- `─○─` = provided interface (lollipop)
- `─(─` = required interface (socket)

---

## Deployment Diagram (Sơ đồ triển khai)

```
┌─────────────────────────────────────────────────┐
│  <<device>> Client Machine                      │
│  ┌────────────────────────────────────┐         │
│  │ <<execution environment>> Browser  │         │
│  │  ┌─────────────┐                  │         │
│  │  │  Web App    │                  │         │
│  │  └─────────────┘                  │         │
│  └────────────────────────────────────┘         │
└─────────────────────────────────────────────────┘
                    │  <<HTTP>>
                    ▼
┌─────────────────────────────────────────────────┐
│  <<device>> App Server                          │
│  ┌──────────────────────────────┐               │
│  │  <<artifact>> app.jar        │               │
│  └──────────────────────────────┘               │
└─────────────────────────────────────────────────┘
```

---

## IFML — Interface Flow Notation (UI Design)

```
┌──────────────────┐  button click  ┌──────────────────┐
│  <<ViewComponent>>│ ─────────────>│  <<ViewComponent>>│
│   HomeScreen      │               │   DetailScreen    │
│  [DataBinding]    │               │  [DataBinding]    │
└──────────────────┘               └──────────────────┘
```
- `<<ViewComponent>>` = screen/page
- `<<ViewContainer>>` = container (tab, list)
- `<<Event>>` = user interaction trigger
- Navigation flow shown as labeled arrows

---

## Common UML Stereotypes Used in Course

| Stereotype | Meaning |
|-----------|---------|
| `<<actor>>` | External entity in UC diagram |
| `<<include>>` | Mandatory UC inclusion |
| `<<extend>>` | Optional UC extension |
| `<<interface>>` | Interface (no implementation) |
| `<<abstract>>` | Abstract class |
| `<<device>>` | Hardware node in deployment |
| `<<artifact>>` | Deployable file (jar, war, exe) |
| `<<execution environment>>` | Runtime environment (JVM, Browser) |
| `<<boundary>>` | UI/boundary class |
| `<<control>>` | Controller class |
| `<<entity>>` | Domain/entity class |
