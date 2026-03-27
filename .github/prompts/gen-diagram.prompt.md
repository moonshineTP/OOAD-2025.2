---
name: gen-diagram
description: "Generate any OOAD diagram as PlantUML for the LogiFast project. Use when asked to generate, create, or draw a class diagram, object diagram, SSD, state machine, activity diagram, or sequence diagram for any UC."
---

# Diagram Generation — LogiFast OOAD

Generate PlantUML diagrams for the LogiFast delivery management system.

## Usage

Specify:
1. **Diagram type**: class / object / ssd / state-machine / activity / sequence
2. **UC number**: UC-01 through UC-05 (or "all" for CRUD matrix)
3. **Phase**: analysis (Part I) or design (Part II)

---

## Template Library

### Class Diagram — Analysis (Part I)
```plantuml
@startuml UC-XX Domain Class Diagram
skinparam classAttributeIconSize 0
hide empty members
skinparam style strictuml

class [ClassName1] {
  attr1
  attr2
  attr3
}

class [ClassName2] {
  attr1
  attr2
}

[ClassName1] "1" -- "0..*" [ClassName2] : "associationName >"
@enduml
```

### Object Diagram
```plantuml
@startuml UC-XX Object Diagram — [Scenario Name]
object "[instance1 : ClassName1]" as obj1 {
  attr1 = "value1"
  attr2 = "value2"
}
object "[instance2 : ClassName2]" as obj2 {
  attr1 = "value"
}
obj1 -- obj2 : "associationName"
@enduml
```

### SSD
```plantuml
@startuml UC-XX System Sequence Diagram
actor "[Actor name]" as A
participant ":Hệ thống LogiFast" as S

A -> S : message1(params)
S --> A : response1(data)

A -> S : message2(params)
S --> A : response2(data)

A -> S : message3(params)
S --> A : response3(data)
@enduml
```

### State Machine (DonHang lifecycle)
```plantuml
@startuml State Machine — DonHang
[*] --> SanSangGiao : UC-01 hoàn tất\n/ OrderCreated phát

SanSangGiao --> DaPhanCong : UC-02 / taiXe chấp nhận
DaPhanCong --> DangVanChuyen : UC-03 step 1 / taiXe bắt đầu ca
DangVanChuyen --> GiaoThanhCong : UC-03 step 13 / bangChungGiaoHang lưu
DangVanChuyen --> GiaoThatBai : UC-03 alt A1\n[lần 2] / tạo lệnh hoàn trả
GiaoThatBai --> DaHoanTra : UC-03 / returnTrip phân công
GiaoThanhCong --> DaXacNhan : UC-04 / xacNhanGiaoHang()
DaXacNhan --> HoanTatThanhToan : UC-05 / giaoDich tạo
HoanTatThanhToan --> [*]
@enduml
```

### Real-level Sequence (Part II Design)
```plantuml
@startuml UC-XX Real-level Sequence
actor "[Actor]" as A
participant "[ScreenName]\n<<UI>>" as UI
participant "[ControllerName]\n<<Controller>>" as CTRL
participant "[DomainClassName]\n<<Domain>>" as DOM
participant "[DAMClassName]\n<<DAM>>" as DAM
database "Database\n<<DB>>" as DB

A -> UI : userAction()
UI -> CTRL : processRequest(params)
CTRL -> DOM : businessMethod(params)
DOM -> DAM : save(entity)
DAM -> DB : INSERT INTO table VALUES(...)
DB --> DAM : rowsAffected
DAM --> DOM : entity
DOM --> CTRL : result
CTRL --> UI : viewData
UI --> A : displayResult
@enduml
```

---

## Output Instructions

1. Generate the PlantUML code block
2. State the file save path: `Project/Diagrams/UC-XX_[Type].puml`
3. List any grading rules applied (from `docs/grading-rubric.md`)
4. Flag any assumptions made about the UC flow
