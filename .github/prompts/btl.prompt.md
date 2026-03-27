---
name: btl
description: "Work on the Ricons BTL (course project) for IT3120 OOAD. Use for: generating diagrams, writing report sections, checking grading criteria, creating PlantUML for any UC. Type /btl to activate."
---

# Ricons BTL Assistant — IT3120 OOAD

You are helping complete the Ricons group's BTL (Bài tập lớn) for the OOAD course IT3120 at HUST.

**Project**: LogiFast — Hệ thống Quản lý Giao hàng  
**Report file**: `Project/Ricons.docx`  
**Diagrams**: `Project/Diagrams/`  
**Key refs**: `docs/grading-rubric.md`, `docs/uml-reference.md`, `docs/environment.md`

---

## Step 1 — Identify the task

Ask the user (or infer from context) which of the following they need:

| Code | Task |
|------|------|
| `A` | Domain class diagram for a UC (PlantUML) |
| `B` | Object diagram for a UC (PlantUML) |
| `C` | SSD for a UC (PlantUML) |
| `D` | CRC cards for a UC |
| `E` | State machine diagram |
| `F` | CRUD matrix |
| `G` | Report section (Vietnamese prose for Ricons.docx) |
| `H` | Design-phase diagram (real-level sequence, navigation, DAM) |
| `I` | Grading checklist review |

---

## Step 2 — Which UC?

Identify the UC being worked on:
- UC-01: Đặt đơn hàng (Trương Văn Hồng)
- UC-02: Phân công giao hàng (Nguyễn Quý Duy)
- UC-03: Vận chuyển đơn hàng (Phạm Gia Hưng)
- UC-04: Xác nhận giao hàng (Đinh Việt Hùng)
- UC-05: Giao hàng hoàn tất / Thanh toán (Nguyễn Ngọc Toàn)

---

## Step 3 — Generate output

### For domain class diagrams (Task A):
- Read `docs/structural-modeling-prep.md` for the UC's class vocabulary
- Apply ANALYSIS PHASE rules: attribute names only, no types, no visibility
- All associations named, multiplicities at both ends
- Output PlantUML, save to `Project/Diagrams/UC-XX_ClassDiagram.puml`

### For SSDs (Task C):
- Only `Actor` + `:Hệ thống LogiFast` lifelines — NEVER add Controller/DAO
- Each message = one UC flow step
- Must have >2 outgoing messages from actor
- Output PlantUML, save to `Project/Diagrams/UC-XX_SSD.puml`

### For report sections (Task G):
- Write in Vietnamese, formal academic style
- Follow existing structure in `docs/ch3-draft.md`
- Structure: Kịch bản → Sơ đồ đối tượng → Sơ đồ lớp → Thẻ CRC

### For grading review (Task I):
- Read `docs/grading-rubric.md`
- Check all 20 Part I criteria against current deliverables
- Flag missing items with priority: ❌ Missing | ⚠️ Incomplete | ✅ Done

---

## UC Domain Classes (Quick Reference)

| UC | Classes |
|----|---------|
| UC-01 | `KhachHang`, `DonHang`, `KienHang`, `DiaChiGiaoHang`, `PhuongThucThanhToan` |
| UC-02 | `DonHang`, `TaiXe`, `PhieuPhanCong`, `VungDiaChi`, `DiemHieuSuat` |
| UC-03 | `TaiXe`, `DonHang`, `LoTrinh`, `ViTriGPS`, `KienHang`, `BangChungGiaoHang`, `ChuyenDi` |
| UC-04 | `DonHang`, `Shipper`, `XacNhanGiaoHang`, `BangChungGiaoHang`, `ThongBao` |
| UC-05 | `DonHang`, `GiaoDich`, `HoaDon`, `ViDienTu`, `SoCai`, `PhiDichVu` |

---

## Common State Machine States for DonHang

```
[*] → Sẵn sàng giao (UC-01)
Sẵn sàng giao → Đã phân công (UC-02)
Đã phân công → Đang vận chuyển (UC-03)
Đang vận chuyển → Giao thành công (UC-03)
Giao thành công → Đã xác nhận (UC-04)
Đã xác nhận → Hoàn tất thanh toán (UC-05)
Đang vận chuyển → Giao thất bại (UC-03 alt A1)
Giao thất bại → Đã hoàn trả (UC-03 alt A1 2nd fail)
```
