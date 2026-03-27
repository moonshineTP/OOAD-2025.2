# OOAD Course Workspace — IT3120 (2025-2)

## Course Context
- **Course**: Phân tích và thiết kế hệ thống (OOAD) — IT3120
- **Instructor**: TS. Nguyễn Bá Ngọc (`ngocnb@soict.hust.edu.vn`)
- **Semester**: 2025-2 | **Class**: 167831
- **Group**: Ricons (5 members)

---

## File Map

```
Project/
├── Ricons.docx                          # Final SRS+SDD report (delivery management system)
├── Exercise/
│   ├── bai-tap-mo-hinh-hoa-du-lieu.docx # Data modeling exercises (class + object diagrams)
│   └── BaiTap-PhanTich-ThietKe.docx     # Analysis & design exercises (16 problems)
└── Requirements/
    ├── Nhiệm vụ BTL 20252.docx           # 2025-2 weekly task schedule (authoritative)
    ├── Bai-tap-lon-2023-2.docx           # Full deliverables spec (2023-2 reference)
    └── Yêu cầu BTL.xlsx                  # Quality thresholds / grading criteria

Material/
├── 20222-Ch01-TongQuan.pptx             # Ch1: Overview of OOAD/SDLC
├── 20222-Ch02-MoHinhHoaChucNang.pptx    # Ch2: Functional modeling (Use Cases)
├── 20222-Ch03-MoHinhHoaCauTruc.pptx     # Ch3: Structural modeling (Class Diagram)
├── 20222-Ch04-MoHinhHoaHanhVi.pptx      # Ch4: Behavioral modeling (State, Sequence)
├── 20222-Ch05-ThietKeLop.pptx           # Ch5: Detailed class design
├── 20222-ChuyenSangThietKe.pptx         # Transition to design
├── 20222-KienTrucHeThong.pptx           # System architecture
├── 20222-SDLC.pptx                      # Software development lifecycle
├── 20222-ThietKeGiaoDien.pptx           # UI design
├── 20222-ThietKeLuuTruCoDinh.pptx       # Persistent storage design
├── 20242-Ch06-MauThietKe.pptx           # Design patterns
├── Chương 6 *.docx                       # UC modeling: writing requirements in context
├── Chương 9 *.docx                       # UC modeling: drawing SSDs
├── Chương 10-12 *.docx                   # Domain modeling (visualization, links, attributes)
├── Chương 14 *.docx                      # Two special use cases (CRUD + search)
├── PattersonSuperstore_vi.docx           # Patterson Superstore case study (Vietnamese)
├── UC - Vì sao *.docx                    # Why UCs are not functions
├── Ước lượng *.docx                      # UCP estimation guide
├── BaiTap/                               # Exercise archive (includes older BTL specs)
└── 20252/                                # Current semester: BTL tasks + OurBoard.pptx

docs/                                     # Agent reference docs (generated)
├── exercise-catalog.md                   # All exercises with problem statements
├── uml-reference.md                      # UML notation cheat sheet
└── ucp-guide.md                          # UCP estimation methodology
```

---

## Custom Commands
| Command | Purpose |
|---------|---------|
| `/exercise` | Solve in-class OOAD exercises (diagrams, specs, analysis) |
| `/btl` | Work on the Ricons course project (BTL deliverables) |

**Key reference docs** (in `docs/`):
- `grading-rubric.md` — full 20+20+5 rubric from Yêu cầu BTL.xlsx + Ricons status tracker
- `exercise-catalog.md` — all 16 exercise problem statements
- `uml-reference.md` — UML notation cheat sheet
- `ucp-guide.md` — UCP estimation with T1–T13 and E1–E8 descriptions

---

## Ricons Project: Hệ thống Quản lý Giao hàng (LogiFast)

**Client**: Công ty Logistics Cần Giờ (LogiFast) — last-mile delivery, southern Vietnam
**Core Problem**: Fragmented tools (Excel + manual notes + separate apps) → no Single Source of Truth
**System**: Centralized delivery management — order placement through payment settlement

### Use Cases (Event-Driven, 5 events → 5 UCs)

| UC | Business Event | Main Actor | Steps | Complexity | Owner |
|----|---------------|------------|-------|------------|-------|
| UC-01 | Đặt đơn hàng | Khách hàng | 4 | Simple | Trương Văn Hồng |
| UC-02 | Phân công giao hàng | Hệ thống phân công | 6 | Medium | Nguyễn Quý Duy |
| UC-03 | Vận chuyển đơn hàng | Tài xế giao hàng | 13 | Complex | Phạm Gia Hưng |
| UC-04 | Xác nhận giao hàng | Shipper | 5 | Medium | Đinh Việt Hùng |
| UC-05 | Giao hàng hoàn tất / Thanh toán | Shipper | 5 | Medium | Nguyễn Ngọc Toàn |

**UCP Estimate**: UUCP=59 → TCF=1.15 → EF=1.01 → **UCP≈68.5** → PHM=28 → **~1919 person-hours → 3–4 months**

---

## Critical Grading Rules (from Yêu cầu BTL.xlsx)

| Rule | Detail |
|------|--------|
| **Analysis attributes** | Name only — NO types, NO `+/-/#` visibility. Types added only in design phase. |
| **Per-UC class diagrams** | Each UC must have its OWN class diagram; diagrams must meaningfully differ. |
| **Per-UC object diagrams** | ≥1 usage scenario + object diagram per UC. |
| **Per-UC SSDs** | ≥1 SSD per UC; each SSD must have >2 outgoing messages. |
| **CRUD matrix** | Required in Part I: rows = all UCs, columns = all domain classes, values traceable to UC flows. |
| **State machine linkage** | Transitions must reference both UC activities AND SSD messages. |
| **Real-level sequence** | Must include full stack: UI → Controller → Domain → DAM → DB. |
| **Navigation diagram** | Must be consistent with real-level sequence diagram. |

## BTL 2025-2 Weekly Schedule

| Week | Deliverable |
|------|-------------|
| 25 | Topic selection + urgency justification (≥5 expected values, 1 page) |
| 26 | UC diagram + detailed UC specs (1 per member) + task division |
| 27 | UCP estimation |
| 29 | Structural modeling: domain class diagram (per UC) + CRC cards |
| Later | State machine (key object) + SSD + sequence + communication diagrams |
| Later | Architecture: deployment + component diagrams |
| Later | Enriched domain model (types, OCL) + DB design + DAM layer |
| Later | UI design: scenario + navigation diagram + wireframes per UC |

---

## Vietnamese ↔ OOAD Glossary

| Vietnamese | English |
|-----------|---------|
| Ca sử dụng / CSD | Use Case (UC) |
| Sơ đồ ca sử dụng | Use Case Diagram |
| Đặc tả ca sử dụng | Use Case Specification |
| Tác nhân | Actor |
| Sơ đồ lớp | Class Diagram |
| Sơ đồ đối tượng | Object Diagram |
| Sơ đồ hoạt động | Activity Diagram |
| Sơ đồ tuần tự mức hệ thống (SSD) | System Sequence Diagram |
| Sơ đồ tuần tự mức nghiệp vụ | Business-level Sequence Diagram |
| Sơ đồ giao tiếp | Communication Diagram |
| Sơ đồ máy trạng thái | State Machine Diagram |
| Sơ đồ thành phần | Component Diagram |
| Sơ đồ triển khai | Deployment Diagram |
| Mô hình lĩnh vực | Domain Model |
| Thẻ CRC | CRC Card (Class–Responsibility–Collaborator) |
| Hợp đồng thông điệp | Message Contract / System Operation Contract |
| Đường bơi | Swimlane |
| Lớp DAM | Data Access Manager class |
| Cơ số | Multiplicity |
| Lớp liên kết | Association class |
| Sự kiện kích hoạt | Trigger event |
| Luồng sự kiện chính | Main flow / Happy path |
| Luồng thay thế | Alternative flow |
| Luồng ngoại lệ | Exception flow |
| Tiền điều kiện | Precondition |
| Hậu điều kiện | Postcondition |
| Tính cấp thiết | Urgency / Business case |
| Ước lượng UCP | Use Case Point estimation |
| Hệ số phức tạp kỹ thuật | Technical Complexity Factor (TCF) |
| Hệ số môi trường | Environment Factor (EF) |
| Giờ công / Giờ nhân lực | Person-hours |
