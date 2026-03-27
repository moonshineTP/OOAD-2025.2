# GitHub Copilot — Workspace Instructions
# Project: IT3120 OOAD — Ricons Group, Semester 2025-2

## Context

You are assisting a Vietnamese university student group (Ricons, 5 members) completing an OOAD
course project (Bài tập lớn / BTL) for IT3120 at HUST, taught by TS. Nguyễn Bá Ngọc.

- **System being designed**: LogiFast — Hệ thống Quản lý Giao hàng (delivery management for last-mile logistics)
- **Client**: Công ty Logistics Cần Giờ (LogiFast), southern Vietnam
- **Language**: Responses should match the user's language (Vietnamese or English). Diagram labels in Vietnamese.

---

## 5 Use Cases (Core Scope)

| UC   | Name                              | Actor chính           | Complexity | Member        |
|------|-----------------------------------|-----------------------|------------|---------------|
| UC-01 | Đặt đơn hàng                    | Khách hàng            | Simple     | Trương Văn Hồng |
| UC-02 | Phân công giao hàng              | Hệ thống phân công    | Medium     | Nguyễn Quý Duy |
| UC-03 | Vận chuyển đơn hàng              | Tài xế giao hàng      | Complex    | Phạm Gia Hưng |
| UC-04 | Xác nhận giao hàng               | Shipper               | Medium     | Đinh Việt Hùng |
| UC-05 | Giao hàng hoàn tất / Thanh toán  | Shipper               | Medium     | Nguyễn Ngọc Toàn |

---

## Critical Grading Rules (ALWAYS enforce)

### Analysis Phase (Part I)
- **Attributes**: name ONLY — NO `:Type`, NO `+/-/#` visibility markers in domain model
- **Per-UC diagrams**: Each UC must have its OWN class diagram (diagrams must meaningfully differ)
- **Per-UC object diagrams**: ≥1 usage scenario + object diagram per UC
- **Per-UC SSDs**: ≥1 SSD per UC; each SSD must have >2 outgoing messages
- **SSD lifelines**: ONLY `Actor` + `:System` — NO internal objects (Controller, DAO, etc.)
- **CRUD matrix**: Required — rows = all UCs, columns = all domain classes
- **Multiplicities**: Must appear at BOTH ends of every association
- **Association names**: All associations must be labeled

### Design Phase (Part II)
- NOW add `:Type`, `+/-/#`, OCL constraints
- Real-level sequence: full stack UI → Controller → Domain → DAM → DB
- Navigation diagram must be consistent with real-level sequence

---

## Key Reference Files

| File | Content |
|------|---------|
| `docs/grading-rubric.md` | Full 20+20+5 rubric with pass/fail criteria |
| `docs/uml-reference.md` | UML notation cheat sheet for all diagram types |
| `docs/ucp-guide.md` | UCP estimation with T1–T13 and E1–E8 |
| `docs/exercise-catalog.md` | All 16 in-class exercise problem statements |
| `docs/environment.md` | LogiFast business context, org structure, use cases |
| `docs/structural-modeling-prep.md` | UC descriptions and object vocabulary per UC |
| `docs/ch3-draft.md` | Chapter 3 draft content for Ricons.docx |
| `Project/Diagrams/` | Existing PlantUML and draw.io diagrams |

---

## Domain Classes (Per UC — Quick Reference)

### UC-01 Classes
`KhachHang`, `DonHang`, `KienHang`, `DiaChiGiaoHang`, `PhuongThucThanhToan`

### UC-02 Classes
`DonHang`, `TaiXe`, `PhieuPhanCong`, `VungDiaChi`, `DiemHieuSuat`

### UC-03 Classes
`TaiXe`, `DonHang`, `LoTrinh`, `ViTriGPS`, `KienHang`, `BangChungGiaoHang`, `ChuyenDi`

### UC-04 Classes
`DonHang`, `Shipper`, `XacNhanGiaoHang`, `BangChungGiaoHang`, `ThongBao`

### UC-05 Classes
`DonHang`, `GiaoDich`, `HoaDon`, `ViDienTu`, `SoCai`, `PhiDichVu`

---

## Vietnamese ↔ OOAD Glossary (Use Consistently)

| Vietnamese | English |
|-----------|---------|
| Ca sử dụng / CSD | Use Case (UC) |
| Sơ đồ lớp lĩnh vực | Domain Class Diagram |
| Sơ đồ đối tượng | Object Diagram |
| Sơ đồ tuần tự mức hệ thống | System Sequence Diagram (SSD) |
| Sơ đồ tuần tự mức thực tế | Real-level Sequence Diagram |
| Sơ đồ giao tiếp | Communication Diagram |
| Sơ đồ máy trạng thái | State Machine Diagram |
| Thẻ CRC | CRC Card (Class–Responsibility–Collaborator) |
| Ma trận CRUD | CRUD Matrix |
| Lớp DAM | Data Access Manager class |
| Cơ số | Multiplicity |
| Lớp liên kết | Association class |
| Luồng sự kiện chính | Main flow / Happy path |
| Luồng thay thế | Alternative flow |
| Luồng ngoại lệ | Exception flow |
| Tiền điều kiện | Precondition |
| Hậu điều kiện | Postcondition |
| Sơ đồ điều hướng | Navigation Diagram |
| Nguyên mẫu giao diện | Wireframe / UI Prototype |
