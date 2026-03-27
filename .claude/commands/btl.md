# Course Project Assistant — Ricons BTL (IT3120, 2025-2)

You are helping a student complete their OOAD course project (Bài tập lớn).
**Project**: Hệ thống Quản lý Giao hàng for LogiFast (Công ty Logistics Cần Giờ).

First, identify which **phase** and **deliverable** the user is working on, then provide targeted help.

---

## Project Overview

**Client**: LogiFast — last-mile delivery company in southern Vietnam
**Core problems being solved**:
- Fragmented tools: API feeds from B2B partners + Excel from small agents + manual notes
- No Single Source of Truth → duplicate orders, errors, manual reconciliation overhead
- No route optimization → fuel waste, SLA breaches
- No unified driver tracking → accountability gaps

**System scope**:
- IN: Customer confirms order → driver picks up → delivers → payment settled
- OUT: Warehouse management, supplier management, supply chain

---

## 5 Use Cases (Already Specified in Ricons.docx)

### UC-01: Đặt đơn hàng
- **Actor**: Khách hàng; **Secondary**: Hệ thống quản lý đơn hàng
- **Main flow**: Review cart → Confirm → System validates → Creates unique order ID → Emits "OrderCreated" event → Shows confirmation page
- **Alt A1**: Invalid info → show error → customer corrects
- **Alt A2**: Item out of stock → notify + suggest alternative
- **Exc E1**: System error → log + show error, no order created
- **Complexity**: Simple (UAW weight 5)

### UC-02: Phân công giao hàng (Auto-assignment)
- **Actor**: Hệ thống phân công; **Secondary**: Quản lý, Tài xế
- **Main flow**: Find "Ready" orders → Filter "Available" drivers in radius → Score by position/load/performance → Notify driver → Driver accepts → Status = "Assigned"
- **Alt A1**: Batch nearby orders into one trip
- **Exc E1**: No driver found → expand radius → alert dispatcher
- **Complexity**: Medium

### UC-03: Vận chuyển đơn hàng (13-step main flow)
- **Actor**: Tài xế; **Secondary**: Khách hàng, Đối tác B2B, Hệ thống bản đồ, Điều phối viên
- **Preconditions**: Trip assigned (UC-02), driver logged in, network+GPS active
- **Key steps**: Tap "Start pickup" → GPS activates → Scan QR at warehouse → System validates → Optimal route calculated → GPS updates every 30s + ETA recalculated → Driver arrives → Customer notified → Photo + name confirmation → "Delivered successfully" → SK-04 triggered
- **Alt A1**: Can't reach customer → "Failed attempt 1" → auto-reschedule; 2nd fail → return
- **Alt A2**: Customer refuses → photo evidence → return trip assigned
- **Alt A3**: Traffic jam → reroute + recalculate ETA + SLA warning
- **Exc E1**: Wrong parcel scanned → alert, contact warehouse staff
- **Exc E2**: Emergency → "Paused - Incident" → dispatcher decides
- **Complexity**: Complex (UAW weight 15)

### UC-04: Xác nhận giao hàng
- **Actor**: Shipper; **Secondary**: Khách hàng, Hệ thống thanh toán
- **Main flow**: Login → Select order → View details → Tap "Confirm delivery" → System requests proof (signature/OTP/photo) → Validate → Status = "Delivered" → Record timestamp → Notify parties → Show success
- **Alt A1**: Customer confirms via app/SMS/OTP instead
- **Exc E1**: Invalid OTP / missing info / connection lost → error, no status change
- **Complexity**: Medium

### UC-05: Giao hàng hoàn tất / Thanh toán
- **Actor**: Shipper; **Secondary**: Hệ thống kế toán, Admin
- **Main flow**: Confirm delivery + evidence → Check payment type (prepaid/credit/cash/COD) → Enter COD amount collected → Calculate service fee + commission → Record to driver wallet or ledger → Emit "PaymentCompleted" event → Show reconciliation confirmation
- **Alt A1**: COD amount mismatch → alert → driver submits approval request → Admin approves/rejects
- **Exc E1**: System error → log for Admin manual processing
- **Complexity**: Medium

---

## UCP Estimation (Completed)

| Component | Calculation | Result |
|-----------|-------------|--------|
| UAW | 3 API systems×1 + 2 human actors×3 | **9** |
| UUCW | 1 simple×5 + 3 medium×10 + 1 complex×15 | **50** |
| UUCP | UAW + UUCW | **59** |
| TFactor | Sum of T1–T13 weights | 55 |
| TCF | 0.6 + 0.01×55 | **1.15** |
| EFactor | Sum of E1–E8 weights | 13 |
| EF | 1.4 − 0.03×13 | **1.01** |
| UCP | 59 × 1.15 × 1.01 | **≈68.53** |
| PHM | 4 unfavorable environment factors | **28** |
| Effort | 68.53 × 28 | **≈1919 person-hours** |
| Timeline | 1919 / 5 people / 160h per month | **theoretical 2.4 mo, realistic 3–4 mo** |

---

## Official Grading Rubric (Yêu cầu BTL.xlsx)

### Part I — Analysis (20 mandatory criteria)
| # | Criterion |
|---|-----------|
| 1 | Environment description |
| 2 | Business structure: org units, roles, departments |
| 3 | Urgency: challenges→solutions, potential→benefits, ≥5 expected values |
| 4 | Complete brief UC spec tables with all required fields |
| 5 | UC diagram conventions: verb-noun UC names, actor notation, system boundary, system name |
| 6 | Detailed event flows for ALL UCs, each scenario has >2 activities |
| 7 | UCP estimation (effort in person-hours) |
| 8 | Task division: each member owns exactly 1 UC |
| 9 | **Per UC**: ≥1 detailed usage scenario + object diagram |
| 10 | **Per UC**: domain class diagram |
| 11 | Class diagrams must meaningfully differ between UCs (different classes for different UCs) |
| 12 | **⚠️ Analysis-level attribute rule**: attributes have name only — NO types, NO access modifiers |
| 13 | Associations named, multiplicities at BOTH ends |
| 14 | Object diagrams compatible with their class diagrams |
| 15 | SSD conventions: `:ClassName` with underline, only actor + system lifelines, proper message notation |
| 16 | SSD message flow consistent with corresponding UC event flow |
| 17 | **Per UC**: ≥1 SSD with >2 outgoing messages |
| 18 | State machine for 1 representative object; transitions linked to UC activities AND SSD messages |
| 19 | **CRUD matrix**: rows = all UCs, columns = all domain classes |
| 20 | CRUD matrix values (C/R/U/D) linked to UC event flow activities and SSD messages |

### Part II — Design (20 mandatory + 5 bonus)
| # | Criterion |
|---|-----------|
| 1 | Business-level sequence diagram compatible with SSD |
| 2 | Communication diagram compatible with corresponding sequence diagram |
| 3 | **Real-level sequence diagram** with ALL components: UI → Controller → Domain → DAM → DB |
| 4 | Enriched domain class diagram: data types + access modifiers + multiplicities + association names + constraints |
| 5 | CRC cards: responsibilities tied to messages in business sequence diagram |
| 6 | CRC cards: collaborators |
| 7 | CRC cards: attributes |
| 8 | DB mapping covers all classes and attributes |
| 9 | DB mapping allows object structure reconstruction from DB |
| 10 | DB mapping records associations (FK relationships) |
| 11 | Relational DB table specification sheets |
| 12 | DAM (Data Access Manager) classes |
| 13 | UI standards: color palette, icons, shared components |
| 14 | Usage scenario compatible with UC message flow and interaction diagrams |
| 15 | Navigation structure diagram (IFML / window navigation) |
| 16 | Navigation structure compatible with real-level sequence diagram |
| 17 | UI wireframe prototypes |
| 18 | Storyboard per usage scenario |
| 19 | **Deployment diagram** (final product infrastructure) |
| 20 | Correct use of UML/OOAD concepts in all report headings |
| **+** | **Bonus**: Package diagram with system modularization |
| **+** | **Bonus**: Component diagram for architecture |
| **+** | **Bonus**: Manifest relationships (artifact ↔ component) |
| **+** | **Bonus**: OCL constraints on enriched class diagram |
| **+** | **Bonus**: Architecture pattern (e.g., MVC, Layered, Microservices) applied and named |

---

## CRUD Matrix (Required — Part I items 19–20)

Template for Ricons (fill C/R/U/D per cell):

| UC \ Class | DonHang | KienHang | TaiXe | ChuyenDi | BangChung | GiaoDich | KhachHang |
|-----------|---------|---------|-------|---------|----------|---------|----------|
| UC-01: Đặt đơn hàng | C | C | R | | | | R |
| UC-02: Phân công giao hàng | R,U | R | R,U | C | | | |
| UC-03: Vận chuyển đơn hàng | R,U | R,U | R,U | R,U | C | | |
| UC-04: Xác nhận giao hàng | R,U | R,U | R | R | R,U | | |
| UC-05: Giao hàng hoàn tất | R,U | | R,U | | R | C,R | R |

*Verify: each cell's operation must be traceable to a specific step in the UC event flow or SSD message.*

---

## Per-UC Domain Class Diagrams (Required — Part I items 10–11)

Each UC needs its OWN class diagram showing the classes involved in that UC's scenario. They MUST differ.

**⚠️ Analysis-level rule**: At this stage, class attributes have **name only** — no `:Type`, no `+/-/#` visibility markers. Those are added only in the Design phase (Part II item 4 — enriched class diagram).

| UC | Key classes to include | Unique to this UC |
|----|----------------------|-------------------|
| UC-01 | KhachHang, DonHang, KienHang | KhachHang initiates, DonHang created |
| UC-02 | DonHang, TaiXe, ChuyenDi, HệThốngPhânCông | ChuyenDi created here |
| UC-03 | TaiXe, ChuyenDi, KienHang, DonHang, BangChungGiaoHang | BangChungGiaoHang created here; GPS/route involved |
| UC-04 | Shipper(TaiXe), DonHang, BangChungGiaoHang, KhachHang | Confirmation proof validated |
| UC-05 | Shipper(TaiXe), DonHang, GiaoDich, HệThốngKếToán | GiaoDich created; financial settlement |

---

## BTL 2025-2 Weekly Tasks

### Week 25 — Environment & Urgency ✓
Already in Ricons.docx. Key points:
- LogiFast operates B2C (retail agents) + B2B (e-commerce last-mile)
- Current pain points: fragmented data, no route optimization, SLA pressure, driver accountability gaps
- 5 expected values: scalability, single source of truth, operational efficiency, future-ready (food delivery), transparency

### Week 26 — Functional Modeling ✓
Already in Ricons.docx: UC diagram, 5 UC specifications, UCP. When refining:
- UC diagram should show system boundary, 5 actors, 5 UCs, relationships
- UC specs follow the table format (use template below)
- Activity diagrams: one per UC (draw with swimlanes)

### Week 27 — Structural Modeling (Domain Class Diagram + CRC)
**Candidate domain classes** (identify from UC flows):
- `DonHang` (Order): id, trangThai, ngayTao, diaChiGiao, tongGiaTri, hinhThucThanhToan
- `TaiKhoanKhachHang` / `KhachHang`: id, ten, soDienThoai, diaChi
- `TaiXe`: id, ten, viTriHienTai, trangThai (Trống/Bận), diemHieuSuat
- `ChuyenDi` (Trip): id, trangThai, thoiGianBatDau, loTrinh
- `KienHang` (Parcel): id, maQR, trangThai, khoiLuong
- `BangChungGiaoHang` (DeliveryProof): id, anhChup, tenNguoiNhan, thoiGianGiao
- `GiaoDich` (Transaction): id, soTienThucTe, phi, hoaHong, loaiThanhToan
- `LichGiaoLai` (Rescheduling): id, lyDo, soLanThu
- Key relationships: KhachHang places DonHang; DonHang contains KienHang; TaiXe executes ChuyenDi; ChuyenDi delivers DonHang; DonHang has BangChungGiaoHang; DonHang triggers GiaoDich

**CRC Card format**:
```
┌─────────────────────────────────────────────────────────┐
│ Class: DonHang   ID: 1                                  │
│ Description: Represents a customer order in the system  │
├───────────────────────────────┬─────────────────────────┤
│ Responsibilities              │ Collaborators           │
│ - Store order information     │ KhachHang               │
│ - Track order status          │ KienHang                │
│ - Trigger payment on delivery │ GiaoDich                │
│ - Record delivery proof       │ BangChungGiaoHang       │
└───────────────────────────────┴─────────────────────────┘
```

### Later — Behavioral Modeling
**State machine for DonHang** (Order):
```
● → [Chờ xử lý] → assigned → [Đã phân công]
                             → pickup_started → [Đang lấy hàng]
                                              → picked_up → [Đang vận chuyển]
                                                          → arrived → [Đang giao]
                                                                    → confirmed → [Giao thành công]
                                                                    → failed → [Giao thất bại]
                                                                              → rescheduled → [Lên lịch lại]
                                                                              → returned → [Hoàn hàng]
                                              → cancelled → [Đã hủy]
```

**SSD per UC**: Show actor ↔ :HệThốngQuảnLýGiaoHàng boundary only

### Later — Architecture & Design
- **Architecture pattern**: MVC + DAM layer
- **Package structure**: `GUI` / `Controller` / `Domain` / `DAM`
- **DB**: Recommend PostgreSQL (relational, good for transactional delivery data)
- **Deployment**: Client apps (driver mobile, customer web) → Load balancer → App server → DB server + GPS/Maps API integration

---

## Full Report Structure

### Part I — Analysis
1. **Ch 1**: Môi trường và tính cấp thiết ✓
2. **Ch 2**: Mô hình hóa chức năng ✓ (UC diagram + 5 specs + UCP)
3. **Ch 3**: Mô hình hóa cấu trúc (domain class diagram + CRC cards)
4. **Ch 4**: Mô hình hóa hành vi (state machine + SSD + sequence + communication diagrams)

### Part II — Design
1. **Ch 1**: Thiết kế chi tiết lớp (enriched class diagram + detailed CRC + message contracts)
2. **Ch 2**: Thiết kế tương tác mức nghiệp vụ
3. **Ch 3**: Thiết kế giao diện (standards + IFML + wireframes + storyboard per UC)
4. **Ch 4**: Thiết kế CSDL (tech choice + ORM mapping + DAM layer + table specs)
5. **Ch 5**: Thiết kế tương tác đầy đủ (MVC + DAM sequence diagrams)
6. **Ch 6**: Thiết kế kiến trúc (package + component + deployment diagrams)

---

## UC Specification Template
```
| Use Case ID      | UC-0X                        |
| Tên Use Case     | [Verb phrase]                |
| Actor chính      | [Primary actor]              |
| Actor phụ        | [Secondary actors]           |
| Mô tả            | [Purpose + typical scenario] |
| Mục tiêu         | [What system state is achieved] |
| Điều kiện tiên quyết | [Preconditions]          |
| Điều kiện hậu    | [Postconditions]             |
| Luồng sự kiện chính | 1. Actor does X.          |
|                  | 2. System responds Y.        |
|                  | ...                          |
| Luồng thay thế   | A1 (step N): condition → steps → rejoin |
| Luồng ngoại lệ   | E1 (step N): error → system response    |
```

---

## Message Contract Template (for design phase)
```
| ID          | MC-01                            |
| Ca sử dụng  | UC-01: Đặt đơn hàng              |
| Thông điệp  | confirmOrder(orderId)            |
| Phương thức | Order::confirm                   |
| Tham số     | orderId: int                     |
| Trả về      | OrderConfirmation                |
| Tiền điều kiện | Order exists in PENDING state |
| Hậu điều kiện  | Order.status = CONFIRMED; "OrderCreated" event emitted |
```
