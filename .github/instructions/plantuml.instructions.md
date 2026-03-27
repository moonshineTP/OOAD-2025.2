---
applyTo: "**/*.puml,**/*.plantuml,Project/Diagrams/**"
description: "PlantUML syntax rules and OOAD course conventions. Use when writing or editing .puml diagram files for LogiFast UC diagrams."
---

# PlantUML — OOAD Course Conventions

## General Setup
Always start with:
```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam style strictuml
hide empty members
```

## Domain Class Diagram (Part I — Analysis)

```plantuml
@startuml
skinparam classAttributeIconSize 0
hide empty members

class DonHang {
  maDonHang
  trangThai
  ngayTao
  tongGiaTri
}

class KhachHang {
  maKhachHang
  tenKhachHang
  soDienThoai
  email
}

DonHang "1..*" -- "1" KhachHang : "được đặt bởi >"
@enduml
```

**Rules for Part I (domain model):**
- Attribute lines: name ONLY — NO `: Type` suffix
- NO `+`, `-`, `#` prefix on any attribute or method line
- NO method sections
- Use `--` for association (not `-->`)
- Include multiplicity at both ends: `"1..*"` and `"1"`
- Include association label with `>` or `<` for direction

## Design Class Diagram (Part II only)
```plantuml
class DonHang {
  - maDonHang: String
  - trangThai: TrangThaiDonHang
  - ngayTao: Date
  + getMaDonHang(): String
  + setTrangThai(t: TrangThaiDonHang): void
}
```

## Object Diagram
```plantuml
@startuml
object "dh001 : DonHang" as dh001 {
  maDonHang = "DH-2025-001"
  trangThai = "Sẵn sàng giao"
  ngayTao = "2025-03-10"
}

object "kh001 : KhachHang" as kh001 {
  maKhachHang = "KH-001"
  tenKhachHang = "Nguyễn Văn A"
}

dh001 -- kh001
@enduml
```
- Object format: `"instanceName : ClassName"` — underlined automatically
- Use concrete real values (no abstract placeholders)

## System Sequence Diagram (SSD)
```plantuml
@startuml
actor "Khách hàng" as KH
participant ":Hệ thống LogiFast" as SYS

KH -> SYS : xacNhanDonHang(gioHang, diaChiGiao, phuongThucTT)
SYS --> KH : hienThiXacNhan(maDonHang, thoiGianDuKien)

KH -> SYS : xacNhanThanhToan(phuongThucTT)
SYS --> KH : thongBaoThanhCong(maDonHang)

KH -> SYS : xemChiTietDonHang(maDonHang)
SYS --> KH : hienThiChiTiet(donHang)
@enduml
```
- Only TWO participant boxes: the actor + `:Hệ thống LogiFast`
- NO Controller, Service, DAO, Repository participants
- Use Vietnamese method names with camelCase
- Each outgoing message from actor = one UC step
- Must have >2 messages from actor (outgoing arrows)

## State Machine Diagram
```plantuml
@startuml
[*] --> SanSangGiao : UC-01 hoàn tất / OrderCreated
SanSangGiao --> DaPhanCong : UC-02 / phieuPhanCong tạo
DaPhanCong --> DangVanChuyen : UC-03 step 3 / tài xế xác nhận lấy hàng
DangVanChuyen --> GiaoThanhCong : UC-03 step 13 / bangChungGiaoHang lưu
GiaoThanhCong --> DaXacNhan : UC-04 / xacNhanGiaoHang()
DaXacNhan --> HoanTatThanhToan : UC-05 / giaoDich tạo
HoanTatThanhToan --> [*]
@enduml
```
- Transition labels MUST reference UC step (e.g., `UC-03 step 5`) or SSD message name

## Activity Diagram (with swimlanes)
```plantuml
@startuml
|Khách hàng|
start
:Xem giỏ hàng;

|Hệ thống|
:Kiểm tra tính hợp lệ;
if (Hợp lệ?) then (Có)
  :Tạo mã đơn hàng;
else (Không)
  :Hiển thị lỗi;
  stop
endif
:Phát sự kiện OrderCreated;
stop
@enduml
```
