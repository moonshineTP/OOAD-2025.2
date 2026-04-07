# Week 30 Plan — Ch5_MoHinhHoaHanhVi.docx

**Date**: 2026-04-07  
**Target file**: `Project/Ch5_MoHinhHoaHanhVi.docx`  
**Source of truth**: `Material/20222-Ch04-MoHinhHoaHanhVi.pptx` (48 slides) + teacher adjustment  
**Grading criteria**: I.15–I.17 (SSD), I.18 (state machine), I.19–I.20 (CRUD matrix)

---

## 0. Critical structural correction

The teacher's adjustment moves **all behavioral diagrams out of Ch4 and into Ch5**.

| Diagram | Was planned in | Correct location |
|---------|---------------|-----------------|
| SSD mức Hệ Thống (per UC) | Ch4 §4.x.4 (placeholder) | **Ch5 §3.x** |
| Thẻ CRC | Ch4 §4.x.5 | Ch4 §4.x.4 (renumbered, stays) |
| Sơ đồ máy trạng thái | Ch5 | Ch5 §2 (unchanged) |
| Sơ đồ giao tiếp mức Hệ Thống / DFD | Not planned | **Ch5 §4** (new) |
| Ma trận CRUD(E) | Ch5 §3 | **Ch5 §5** (renumbered) |

> **Ch4 action required**: Remove or relabel the `[Chèn sơ đồ tuần tự hệ thống (SSD)]` placeholder in each §4.x.4. Replace with `[Chèn thẻ CRC ...]` (renumber accordingly). This is a script fix, not manual.

### Pptx source confirmation

From the **Content slides (slides 4, 15, 31, 42, 45)** — the chapter structure is explicit:
1. Biểu diễn trạng thái → **Sơ đồ máy trạng thái**
2. Các mô hình tương tác phân tích → **Sơ đồ tuần tự mức Hệ Thống** + **Sơ đồ giao tiếp mức Hệ Thống**
3. Kỹ thuật phát hiện quan hệ → **Ma trận CRUD(E)**

From **slide 47** (final report structure): Ch4 = CRC cards + class diagrams. Behavioral diagrams belong to a separate chapter.

From **slides 38–41**: Sơ đồ giao tiếp mức hệ thống (System Communication Diagram) is explicitly compared to the **Sơ đồ luồng dữ liệu (DFD)** mức ngữ cảnh. The pptx shows both as equivalent representations of the same information at the system level (Blackbox). The teacher's reference to "Data Flow Diagram" refers to this comparison section. At this system level, there are NO internal domain classes, only Actor and :System.

---

## 0.5 Actors and their interaction lines (grounded in Ricons.docx)

### Actors (from Table 4, §2 "Phân tích Actor")

| Actor | Type | UCP weight | UCs |
|-------|------|-----------|-----|
| **KhachHang** | Human (complex) | 3 | UC-01 primary, UC-03 secondary, UC-04 secondary |
| **TaiXe** | Human (complex) | 3 | UC-02 secondary, UC-03 primary, UC-04 primary, UC-05 primary |
| Hệ thống điều phối | System/API (simple) | 1 | UC-02, UC-03 |
| Hệ thống theo dõi | System/API (simple) | 1 | UC-03 |
| Hệ thống thanh toán | System/API (simple) | 1 | UC-05 |

> **Note**: "Shipper" in UC-04 and UC-05 = TaiXe (confirmed by noun analysis: "Shipper — Đồng nghĩa, tương đương TaiXe trong phạm vi 5 UC"). All these actors MUST appear exactly as named as lifelines in the System Sequence Diagrams (SSD).

### KhachHang — detailed interaction lines

| UC | Role | What KhachHang does | System Level Message (Parameterless) |
|----|------|---------------------|-----------------|
| UC-01 | **Primary actor** | Xem lại thông tin đơn, bấm xác nhận đặt hàng | `1. Xác nhận đặt hàng()` |
| UC-03 | Secondary actor | Theo dõi vị trí tài xế thời gian thực; nhận thông báo ETA; gặp tài xế, đồng ý bàn giao | `8. Gửi thông báo ETA()` (từ System) |
| UC-04 | Secondary actor | Xác nhận đã nhận hàng qua OTP/app | `2. Cung cấp mã OTP()` |
| UC-05 | Secondary (implied) | Là người mà DonHang.trangThai cuối cùng ảnh hưởng đến | `5. Gửi hóa đơn điện tử()` (từ System) |

**State machine implication for DonHang**: KhachHang triggers the *first* state transition (UC-01 → Sẵn sàng giao) and is the *recipient* of the final state (UC-04 OTP → Đã xác nhận). Every transition in DonHang SMD can be traced to a parameterized message in the SSD.

### TaiXe — detailed interaction lines (System Level)

| UC | Role | What TaiXe does | System Level Message (Parameterless) |
|----|------|-----------------|-----------------|
| UC-02 | Secondary actor | Nhận thông báo "Yêu cầu giao hàng mới", chấp nhận đơn | `3. Phân công giao hàng()` (từ System) |
| UC-03 | **Primary actor** | Bắt đầu ca, quét QR tại kho, xuất phát, GPS tracking, bàn giao vật lý | `1. Bắt đầu ca làm việc()`, `3. Quét mã kiện hàng()` |
| UC-04 | Primary actor (as **Shipper**) | Đăng nhập, chọn đơn, xác nhận giao hàng với OTP/chữ ký | `1. Xác nhận giao hàng()` |
| UC-05 | Primary actor (as **Shipper**) | Thu tiền COD, nhập số tiền, xác nhận đối soát | `1. Yêu cầu nộp tiền COD()` |

**State machine implication for TaiXe**: TaiXe's own state machine (Ngoài ca → Sẵn sàng nhận đơn → Đang giao → Kết thúc ca) is the **guard condition** for UC-02's assignment algorithm — the system only considers TaiXe in state `Sẵn sàng nhận đơn`.

### Hệ thống ngoài (External Systems) — detailed interaction lines (System Level)

Từ flow nghiệp vụ UC-03 (`ricons_full_current.txt`), ta thấy SSD có sự tham gia sâu của các Actor là hệ thống phụ trợ. Điều này cực kỳ quan trọng và phải được thể hiện thành các Lifeline biệt lập trên SSD, song song với `:Module_Vận_chuyển`:

| Actor | UC tham gia | System Level Message (Parameterless) & Flow Mapping |
|-------|------|-------------------------------------------------|
| **Hệ thống theo dõi** | UC-03 | Thực hiện chức năng giám sát thụ động và cung cấp tín hiệu.<br>• `5. Cập nhật vị trí GPS và giao thông()` (Luồng chính)<br>• `6. Thông báo phát hiện sự cố giao thông()` (Kích hoạt Luồng thay thế) |
| **Hệ thống điều phối** | UC-02, UC-03 | Đóng vai trò giải quyết logic tính toán lộ trình và gom đơn.<br>• `1. Yêu cầu phân công()` (Sự kiện gốc ở UC-02)<br>• `2. Tính toán lộ trình đi tối ưu()` (Hệ thống gọi Điều phối ở UC-03)<br>• `7. Tính lại lộ trình và đưa ra gợi ý()` (Luồng thay thế khi có sự cố) |
| **Hệ thống thanh toán** | UC-05 | Xử lý cổng thanh toán COD.<br>• `3. Chuyển tiếp tiến trình thanh toán()` (Từ Hệ thống LogiFast gọi ra) |

> **Critical constraint for SSDs**: Bất kỳ hệ thống ngoài (External System Actor) nào xuất hiện trong Use Case flow specification thì **BẮT BUỘC** phải được vẽ thành một Lifeline độc lập bên cạnh `:Hệ_thống` (hoặc `:Module`). Việc hệ thống chính giao tiếp với các hệ thống ngoài này phải được số hóa và biểu diễn rõ ràng trên SSD.

### Class diagram relations as Business Level grounding (from Ch4 §4.x)

These associations from the per-UC class diagrams ground every interaction in the *subsequent phase* (Business-level sequence diagram), NOT the SSD. At the SSD level, we only care about Actor-System messages.

| Relation (from Ch4) | Business/Design Level implication | UC |
|---------------------|--------------------|----|
| KhachHang `đặt` DonHang | Controller invokes `DonHang.create()` | UC-01 |
| PhieuPhanCong `phân công` DonHang + `gán` TaiXe | Controller links `DonHang` with `TaiXe` via `PhieuPhanCong` | UC-02 |
| TaiXe `thực hiện` LoTrinh | Controller routes to `LoTrinh.start()` | UC-03 |
| LoTrinh `ghi nhận` ViTriGPS | `LoTrinh` appends new `ViTriGPS` object | UC-03 |
| DonHang `kết toán` GiaoDich | Controller calculates COD and passes to `GiaoDich` | UC-05 |

### CRC collaborator chains as behavioral grounding

The CRC cards from Ch4 §4.3.4 directly define which objects each class "knows about" — this dictates message routing in the **Business-Level** Communication Diagram (Phase 2):

| Class | CRC Collaborators | Behavioral implication |
|-------|------------------|----------------------|
| ChuyenDi | TaiXe, LoTrinh | Business Comm: `ChuyenDi` tells `LoTrinh` to calculate route |
| **LoTrinh** | ChuyenDi, TaiXe, DonHang, ViTriGPS, **SuCoGiaoThong** | Business Comm: `SuCoGiaoThong` triggers recaluation in `LoTrinh` |
| ViTriGPS | LoTrinh | GPS snapshots are Composition children of `LoTrinh` |
| KienHang | DonHang | maQR lookup routes to parent `DonHang` |
| ThongBaoSuCoGiaoThong | DonHang | Push notification relies on `DonHang` recipient context |

### SuCoGiaoThong — new class (UC-03 only, not in original 21-class list)

This class was added by Phạm Gia Hưng during UC-03 detailed analysis:

| Field | Value |
|-------|-------|
| Class name | SuCoGiaoThong |
| Columns in CRUD | Add as column 23 (after PhiDichVu); only UC-03 has value: C(Alternative Flow) |
| Impact on state machine | Grounds `LoTrinh: Đang thực hiện → Đang tái tối ưu` transition based on system alert message |

---

## 1. File-level conventions

Same as Ch4_MoHinhHoaCauTruc.docx:
- Styles inherited from `Ricons.docx` via copy-and-clear
- Chapter is **V** (I=Bìa, II=Môi trường, III=Chức năng, IV=Cấu trúc, V=Hành vi)
- `Title` style for chapter heading, `Heading 1` for sections, `Heading 2` for sub-sections, `Heading 3` for per-UC sub-sub-sections
- Tables: manual border injection via `OxmlElement`
- Analysis-phase rule: attribute names only, no types

---

## 2. Chapter title

**Style**: `Title`  
**Text**: `V. Mô hình hóa hành vi`

---

## 3. Section 1 — Giới thiệu

**Style**: `Heading 1` | **Text**: `1. Giới thiệu`

### Natural language (2 paragraphs)

**¶1 — What behavioral modeling answers**:  
Trình bày rằng sau khi mô hình cấu trúc (Chương IV) xác định *những gì* hệ thống ghi nhớ, mô hình hóa hành vi trả lời câu hỏi *như thế nào* các đối tượng đó biến đổi trạng thái và *tương tác ra sao* với nhau trong từng ca sử dụng. Theo bài giảng Ch04 (TS. Nguyễn Bá Ngọc), ba vấn đề cốt lõi cần mô hình hóa là: (1) sự biến đổi trạng thái của đối tượng theo tiến trình nghiệp vụ, (2) tương tác giữa tác nhân và hệ thống, (3) tương tác giữa các đối tượng nội bộ để đáp ứng hoạt động nghiệp vụ.


## 4. Section 2 — Sơ đồ máy trạng thái

**Style**: `Heading 1` | **Text**: `2. Sơ đồ máy trạng thái`

### Natural language intro (1 paragraph)

Nhắc lại tiêu chí từ slide 5: đối tượng được chọn phải (a) xuất hiện trong nhiều UC, (b) có trạng thái liên quan đến công việc nghiệp vụ, (c) có sự thay đổi trạng thái được kích hoạt bởi các sự kiện nghiệp vụ xác định. Trong LogiFast, ba đối tượng thỏa điều kiện: `DonHang` (xuyên suốt 5 UC, **ĐÃ LÀM**), `TaiXe` (điều kiện bảo vệ phân công UC-02), `LoTrinh` (tái tối ưu động bởi OR engine trong UC-03).

### Terminology box (table, 2 cols)

Liệt kê thuật ngữ chuẩn từ slide 6:

| Thuật ngữ | Mô tả |
|-----------|-------|
| Trạng thái | Một giai đoạn trong tiến trình; bộ giá trị thuộc tính thỏa điều kiện nhất định |
| Bước chuyển (Transition) | Từ trạng thái nguồn → trạng thái đích; nhãn: `sự_kiện [điều_kiện] / hành_động` |
| Sự kiện kích hoạt | Nguyên nhân dẫn đến chuyển trạng thái |
| Điều kiện bảo vệ | Chỉ chuyển nếu điều kiện `[...]` được đáp ứng |
| Biểu thức hành vi | Được thực hiện và hoàn thành trước khi chuyển sang trạng thái đích |
| Trạng thái tổng hợp | Chứa máy trạng thái con (có bắt đầu và kết thúc riêng) |
| Trạng thái trực giao | Nhiều vùng song song trong cùng một trạng thái tổng hợp |

---

### 4.1 TaiXe

**Style**: `Heading 2` | **Text**: `2.1. Sơ đồ máy trạng thái — TaiXe`

#### Natural language (1 paragraph)

`TaiXe` có vòng đời theo ca làm việc. Trạng thái của tài xế là điều kiện bảo vệ quan trọng trong UC-02: hệ thống phân công chỉ xét các tài xế đang ở trạng thái `Sẵn sàng nhận đơn`. Ngoài ra, trạng thái `Đang giao hàng` giải thích tại sao cùng một tài xế không thể nhận thêm đơn mới trong UC-02 khi đang trong UC-03.

#### Transition table

| Từ trạng thái | Sự kiện | Điều kiện | Hành động | Đến trạng thái | UC/Bước | Thông điệp SSD |
|--------------|---------|-----------|-----------|----------------|---------|---------------|
| ● | — | — | — | Ngoài ca | — | — |
| Ngoài ca | ShiftStarted | — | tạo ChuyenDi | Sẵn sàng nhận đơn | UC-03 B1 | `xacNhanBatDauCa(maTaiXe)` |
| Sẵn sàng nhận đơn | AssignmentReceived | — | cập nhật trangThai | Đang giao hàng | UC-02 B3 | `phanCongTaiXe(...)` |
| Đang giao hàng | DeliveryCompleted | — | cập nhật trangThai | Sẵn sàng nhận đơn | UC-03 B6 | `xacNhanGiaoHangThanhCong(maBangChung)` |
| Sẵn sàng nhận đơn | ShiftEnded | — | ghi thoiGianKetThuc | Kết thúc ca | UC-03 (end) | `ketThucCa(maTaiXe)` |
| Kết thúc ca | — | — | — | ⊙ | — | — |

#### Diagram spec

| Field | Value |
|-------|-------|
| Source | `Project/Diagrams/TaiXe_StateMachine.puml` |
| States | 4 main |
| Placeholder | `[Chèn sơ đồ máy trạng thái TaiXe — Project/Diagrams/TaiXe_StateMachine.puml]` |

---

### 4.2 LoTrinh

**Style**: `Heading 2` | **Text**: `2.2. Sơ đồ máy trạng thái — LoTrinh`

#### Natural language (2 paragraphs)

**¶1 — Sophistication argument**:  
`LoTrinh` là đối tượng kỹ thuật phức tạp nhất trong UC-03. Không giống các lớp khác, `LoTrinh` không có vòng đời tuyến tính: nó có thể bị **tái tính toán** (recalculated) bởi OR engine khi phát sinh sự kiện bất thường (tắc đường, GPS lệch tuyến >500m). Trạng thái `Đang tái tối ưu` là trạng thái duy nhất trong toàn bộ mô hình LogiFast có hoạt động nội bộ liên tục (`do / OR engine recalculates route`), thể hiện tính chủ động của hệ thống.

**¶2 — Link to SSD loop**:  
Điều kiện bảo vệ `[lệch >500m]` được feed trực tiếp từ thông điệp `capNhatViTriGPS(viDo, kinhDo)` trong vòng lặp `loop [mỗi 30 giây]` của SSD UC-03 (Mục 3.3). Đây là liên kết I.18: chuyển trạng thái `Đang thực hiện → Đang tái tối ưu` có thể truy xuất về cả bước UC-03 Bước 4 lẫn thông điệp SSD `capNhatViTriGPS`. Thuộc tính `/thoiGianDuKien` được tái tính mỗi lần OR hoàn thành, chứng minh `thoiGianDuKien` là thuộc tính suy diễn động, không tĩnh.

#### Transition table

| Từ trạng thái | Sự kiện | Điều kiện | Hành động | Đến trạng thái | UC/Bước | Thông điệp SSD |
|--------------|---------|-----------|-----------|----------------|---------|---------------|
| ● | — | — | OR engine tính tuyến | Đã tính toán | UC-03 B3 | `batDauGiaoHang(maDonHang)` |
| Đã tính toán | DriverDeparted | [tài xế xác nhận] | ghi thoiGianBatDau | Đang thực hiện | UC-03 B3 | `hienThiLoTrinh(maLoTrinh, khoangCach, ETA)` |
| Đang thực hiện | RouteDeviated | [GPS lệch >500m OR tắc đường] | kích hoạt OR engine | Đang tái tối ưu | UC-03 B4 | `capNhatViTriGPS(viDo, kinhDo)` |
| Đang tái tối ưu | OptimizationDone | [tuyến mới tốt hơn ≥10%] | cập nhật khoangCach, /ETA | Đang thực hiện | UC-03 B4 loop | `ghiNhanThanhCong()` |
| Đang tái tối ưu | OptimizationDone | [tuyến cũ vẫn tối ưu] | giữ nguyên | Đang thực hiện | UC-03 B4 loop | `ghiNhanThanhCong()` |
| Đang thực hiện | PackageHandedOver | [GPS ±200m điểm đến] | ghi thoiGianKetThuc | Hoàn tất | UC-03 B6 | `xacNhanBanGiao(...)` |
| Đang thực hiện | OrderCancelled | — | ghi lý do | Bị hủy | UC-03 alt | — |
| Hoàn tất | — | — | — | ⊙ | — | — |
| Bị hủy | — | — | — | ⊙ | — | — |

**Key**: `Đang tái tối ưu` has `do / OR recalculates route` as internal activity (from slide 6: "do activity").

#### Diagram spec

| Field | Value |
|-------|-------|
| Source | `Project/Diagrams/LoTrinh_StateMachine.puml` |
| States | 5 main (including composite `Đang tái tối ưu` with do-activity) |
| Placeholder | `[Chèn sơ đồ máy trạng thái LoTrinh — Project/Diagrams/LoTrinh_StateMachine.puml]` |

---

## 5. Section 3 — Sơ đồ tuần tự mức hệ thống (SSD)

**Style**: `Heading 1` | **Text**: `3. Sơ đồ tuần tự mức hệ thống (SSD)`

### Natural language intro (2 paragraphs)

**¶1 — What SSD is (from slide 24)**:  
Sơ đồ tuần tự mức hệ thống (System Sequence Diagram — SSD) có cấu trúc đơn giản: chỉ gồm tác nhân và hệ thống (`":Hệ thống LogiFast"`). Các thông điệp tương ứng với các hoạt động nghiệp vụ ở mức khái quát cao — mỗi thông điệp đại diện cho một bước trong đặc tả UC. SSD là đầu vào trực tiếp cho bước thiết kế: mỗi thông điệp gửi đến hệ thống sẽ trở thành một hợp đồng thông điệp (system operation contract) ở Phần II.

**¶2 — Notation rules (from slides 17–18, 23)**:  
Quy tắc ký hiệu: tên đối tượng sống viết dạng `tênĐốiTượng:TênLớp`, gạch chân, căn giữa. Với SSD, chỉ có hai đường sống: tác nhân (actor) và `:Hệ thống LogiFast`. Mô tả thông điệp theo cú pháp: `[biểuThứcLôGic] tênThôngĐiệp(danhSáchThamSố)`. Điều kiện bảo vệ trong `[...]` xác định khi nào thông điệp được gửi. Khung kết hợp: `loop` (lặp), `opt` (tùy chọn), `alt` (rẽ nhánh), `break` (dừng vòng lặp).

### Sub-sections: one per UC

**Style for each**: `Heading 2` | **Text**: `3.x. SSD — UC-0x: [Tên UC]`

Each sub-section contains:
1. **Intro paragraph** (1 sentence): Mô tả tác nhân và mục tiêu của UC trong SSD này.
2. **Message table** (columns: #, Hướng, Tên thông điệp (tham số), Bước UC, Ghi chú)
3. **PlantUML code block** (pre-formatted paragraphs, Courier New font)
4. **Placeholder line**: `[Chèn sơ đồ SSD UC-0x — file: Project/Diagrams/UC0x_SSD.puml]`

---

#### 5.1 UC-01 SSD

**Actor**: Khách hàng | **Heading**: `3.1. SSD — UC-01: Đặt đơn hàng`

> **Owner**: Trương Văn Hồng — to fill. Placeholder: `[Chèn SSD UC-01 — Project/Diagrams/UC01_SSD.puml]`

---

#### 5.2 UC-02 SSD

**Actor**: Hệ thống phân công (tự động) | **Heading**: `3.2. SSD — UC-02: Phân công giao hàng`

> **Owner**: Nguyễn Quý Duy — to fill. Placeholder: `[Chèn SSD UC-02 — Project/Diagrams/UC02_SSD.puml]`

---

#### 5.3 UC-03 SSD

**Actor**: Tài xế giao hàng | **Heading**: `3.3. SSD — UC-03: Vận chuyển đơn hàng`

> **Already fully specified** in `scripts/fill_ssd_crc.py` and Ch4 draft. Copy verbatim.

Tại Sơ đồ mức hệ thống này (SSD - System Sequence Diagram), mọi thông điệp phải là **parameterless** và là **Tiếng Việt có dấu** được đánh số thứ tự tuần tự. Không được sử dụng các tham số kỹ thuật hay mã lệnh (camelCase). Các Actor hệ thống phụ trợ buộc phải trở thành Lifelines độc lập.

| # | Hướng | Tên thông điệp (Tiếng Việt, Parameterless) | Bước UC & Luồng tham chiếu từ `ricons_full_current.txt` | Ghi chú |
|---|-------|-------------------------------------------|---------------------------------------------------------|---------|
| 1 | Tài xế → Hệ thống | `1. Bắt đầu ca làm việc()` | B1 (Luồng chính) | Sinh sự kiện tạo lộ trình |
| 2 | Hệ thống → Tài xế | `2. Yêu cầu quét mã kiện hàng()` | B1 (Luồng chính) | Hệ thống yêu cầu xác nhận kiện hàng |
| 3 | Tài xế → Hệ thống | `3. Quét mã kiện hàng()` | B1 (Luồng chính) | Xác thực kiện hàng |
| 4 | Hệ thống → Hệ thống điều phối | `4. Tính toán lộ trình tối ưu()` | B1 (Luồng chính) | Giao tiếp với External System phân luồng |
| 5 | Hệ thống điều phối → Hệ thống | `5. Trả kết quả lộ trình()` | B1 (Luồng chính) | Trả về lộ trình tối ưu để hiển thị |
| 6 | Hệ thống → Tài xế | `6. Hiển thị lộ trình và ETA()` | B2 (Luồng chính) | Tài xế nhận lộ trình |
| 7 *(loop)*| Hệ thống theo dõi → Hệ thống | `7. Cập nhật vị trí GPS định kỳ()` | B2, B3 (Luồng chính) | Ghi nhận Tracking mỗi 30 giây |
| 8 *(alt)* | Hệ thống theo dõi → Hệ thống | `8. Thông báo phát hiện sự cố giao thông()`| B4 (Luồng thay thế d) | Nếu phát hiện tắc đường |
| 9 | Hệ thống → Hệ thống điều phối | `9. Yêu cầu tính lại lộ trình()` | B4 (Luồng thay thế d) | Yêu cầu tái tối ưu |
| 10 | Hệ thống điều phối → Hệ thống | `10. Trả kết quả lộ trình mới()` | B5 (Luồng thay thế d) | Trả về lộ trình thay thế |
| 11 | Hệ thống → Tài xế | `11. Cập nhật lộ trình thay thế()` | B5 (Luồng thay thế d) | Hiển thị lộ trình mới cho xe |
| 12 | Tài xế → Hệ thống | `12. Xác nhận đã đến điểm giao()` | B6 (Luồng chính) | Cập nhật trạng thái "Đã đến điểm giao" |
| 13 | Hệ thống → Khách hàng | `13. Gửi thông báo Tài xế đã đến()` | B6 (Luồng chính) | Thông báo cho Khách hàng chuẩn bị nhận |
| 14 | Tài xế → Hệ thống | `14. Xác nhận bàn giao hàng()` | B7 (Luồng chính) | Tài xế đẩy trạng thái giao xong |
| 15 | Khách hàng → Hệ thống | `15. Khách hàng đồng ý nhận hàng()` | B7 (Luồng chính) | Hoàn tất flow vật lý |
| 16 | Hệ thống → Tài xế | `16. Thông báo hoàn tất đơn hàng()` | B7 (Luồng chính) | Thông báo kết thúc tiến trình |

**Source**: `Project/Diagrams/UC03_SSD_system.puml` | **Owner**: Phạm Gia Hưng (complete)
**Description for Diagram Agent**: Vẽ Sơ đồ mức hệ thống dưới dạng Blackbox. Có 5 Lifelines bao gồm: `Tài xế` (Màu nhạt), `Khách hàng` (Màu nhạt), `Hệ thống theo dõi` (Màu nhạt), `Hệ thống điều phối` (Màu nhạt), và `:Hệ_thống_LogiFast` (Đường sống trung tâm). Dùng 16 message tiếng việt parameter-less ở bảng trên để vẽ. Trình bày rõ ràng các khối `loop` và `alt`.
---

#### 5.4 UC-04 SSD

**Actor**: Shipper | **Heading**: `3.4. SSD — UC-04: Xác nhận giao hàng`

> **Owner**: Đinh Việt Hùng — to fill. Placeholder: `[Chèn SSD UC-04 — Project/Diagrams/UC04_SSD.puml]`

---

#### 5.5 UC-05 SSD

**Actor**: Shipper | **Heading**: `3.5. SSD — UC-05: Giao hàng hoàn tất / Thanh toán`

> **Owner**: Nguyễn Ngọc Toàn — to fill. Placeholder: `[Chèn SSD UC-05 — Project/Diagrams/UC05_SSD.puml]`

---

## 6. Sơ đồ tuần tự mức thiết kế / nghiệp vụ (Business-Level SD / Real-Level SD)
*(Đây là nội dung trả lời yêu cầu bổ sung SSD mức nghiệp vụ)*

Trong phương pháp luận OOAD (theo Hướng dẫn và Checklist chấm điểm):
- **SSD (System Sequence Diagram)** (mức hệ thống) coi toàn bộ hệ thống là một hộp đen (\:System\).
- **Sơ đồ tuần tự mức thiết kế / nghiệp vụ** (Business-Level / Real-Level) sẽ mở hộp đen đó ra, thể hiện rõ các lớp tham gia (Boundary, Controller, Entity) từ *Sơ đồ phân lớp lĩnh vực* (Domain Model) và *Thẻ CRC*.

Dưới đây là kế hoạch (Kịch bản thông điệp) cho **UC-03: Vận chuyển đơn hàng**:

**Các Lifeline tham gia:**
- **Actor:** \Tài xế\, \Khách hàng\, \Hệ thống theo dõi\, \Hệ thống điều phối\.
- **Boundary/UI:** \:GiaoDienTaiXe\.
- **Controller:** \:VanChuyenController\.
- **Entity:** \:ChuyenDi\, \:LoTrinh\, \:KienHang\, \:DonHang\, \:ViTriGPS\, \:BangChungGiaoHang\, \:SuCoGiaoThong\.
- **Database/DAM:** \LogiFast DB / DAM\.

**Kịch bản Thông điệp (100% Tiếng Việt, theo đúng yêu cầu tự nhiên không tham số):**

*Giai đoạn 1: Bắt đầu ca và quét kiện hàng*
1. \Tài xế\ -> \:GiaoDienTaiXe\: Nhấn nút bắt đầu hành trình()
2. \:GiaoDienTaiXe\ -> \:VanChuyenController\: Yêu cầu bắt đầu ca()
3. \:VanChuyenController\ -> \:ChuyenDi\: Tạo chuyến đi()
4. \:ChuyenDi\ -> \:LoTrinh\: Khởi tạo lộ trình()
5. \Tài xế\ -> \:GiaoDienTaiXe\: Quét mã kiện hàng()
6. \:VanChuyenController\ -> \:KienHang\: Truy xuất thông tin kiện hàng()
7. \:VanChuyenController\ -> \:DonHang\: Báo cáo thông tin đơn khởi tạo()
8. \:VanChuyenController\ -> \Hệ thống điều phối\: Yêu cầu tính toán lộ trình tối ưu()
9. \:VanChuyenController\ -> \:LoTrinh\: Cập nhật dữ liệu lộ trình()

*Giai đoạn 2: Tracking và Điều hướng (Vòng lặp mỗi 30s)*
10. \Hệ thống theo dõi\ -> \:VanChuyenController\: Báo cáo Tọa độ()
11. \:VanChuyenController\ -> \:ViTriGPS\: Lưu vết định vị GPS()
12. \:VanChuyenController\ -> \:LoTrinh\: Bổ sung tọa độ vào lộ trình()
13. [Khoảng cách < 200m] \:VanChuyenController\ -> \Khách hàng\: Gửi thông báo sắp đến nơi()

*Giai đoạn 3: Sự cố giao thông (Alternates)*
14. \Hệ thống theo dõi\ -> \:VanChuyenController\: Báo động phát hiện tắc đường()
15. \:VanChuyenController\ -> \:SuCoGiaoThong\: Ghi nhận sự cố()
16. \:VanChuyenController\ -> \:LoTrinh\: Thay đổi trạng thái Đang tái tối ưu()
17. \:VanChuyenController\ -> \Hệ thống điều phối\: Yêu cầu tính lại lộ trình mới()
18. \:VanChuyenController\ -> \:GiaoDienTaiXe\: Cảnh báo đổi hướng di chuyển()

*Giai đoạn 4: Hoàn tất bàn giao*
19. \Tài xế\ -> \:GiaoDienTaiXe\: Nhấn nút đã đến nơi()
20. \Tài xế\ -> \Khách hàng\: Trao đổi vật lý() (Hoạt động ngoại tuyến)
21. \Tài xế\ -> \:GiaoDienTaiXe\: Xác nhận giao thành công()
22. \:VanChuyenController\ -> \:BangChungGiaoHang\: Lưu hình ảnh bằng chứng giao hàng()
23. \:VanChuyenController\ -> \:DonHang\: Đánh dấu trạng thái Giao thành công()
24. \:VanChuyenController\ -> \:KienHang\: Đánh dấu Đã giao hiện tại()
25. \:VanChuyenController\ -> \:LoTrinh\: Khép lại tiến trình hiện tại()
26. \:VanChuyenController\ -> \LogiFast DB / DAM\: Lưu trữ biến động vào cơ sở dữ liệu()

---

## 7. Section 4 — Sơ đồ giao tiếp mức thiết kế / nghiệp vụ (Business-Level CD / Real-Level CD)

Sơ đồ giao tiếp (Communication Diagram) ở mức nghiệp vụ tập trung vào khía cạnh kiên trúc: thay vì bố cục theo thời gian như SSD, nó sắp xếp các đối tượng tự do dạng mạng lưới và hiển thị rõ ràng các liên kết (Links) cấu trúc. Điều này tương ứng chặt chẽ với những gì đã phân tích trong Thẻ CRC: đối tượng nào "biết" đối tượng nào để gửi thông điệp.

**Các móc nối liên kết (Links) dựa trên Thẻ CRC và Sơ đồ lớp:**
- **External -> UI**: `Tài xế` liên kết với `:GiaoDienTaiXe`. `Khách hàng` cũng có tương tác vật lý trực tiếp với `Tài xế` và nhận thông báo từ hệ thống.
- **UI -> Control**: `:GiaoDienTaiXe` gửi yêu cầu vào xử lý trung tâm là `:VanChuyenController`.
- **System -> Control**: Các `Hệ thống theo dõi` và `Hệ thống điều phối` kết nối vào `:VanChuyenController`.
- **Control -> Entity**: `:VanChuyenController` nắm giữ liên kết đến hầu hết các Entity để điều phối: `:ChuyenDi`, `:KienHang`, `:DonHang`, `:ViTriGPS`, `:SuCoGiaoThong`, `:BangChungGiaoHang` và `:LoTrinh`.
- **Entity -> Entity**: Như đã đặc tả ở Thẻ CRC, `:ChuyenDi` có trách nhiệm khởi tạo `:LoTrinh`, nên có link điều khiển trực tiếp tới `:LoTrinh` mà không cần Controller can thiệp.

**Đặc tả chuỗi thông điệp (Flow of messages phân cấp số thập phân, Tiếng Việt):**

*Giai đoạn 1: Bắt đầu ca và quét kiện hàng*
- **1:** Nhấn nút bắt đầu hành trình() [`Tài xế` -> `:GiaoDienTaiXe`]
  - **1.1:** Yêu cầu bắt đầu ca() [`:GiaoDienTaiXe` -> `:VanChuyenController`]
    - **1.1.1:** Tạo chuyến đi() [`:VanChuyenController` -> `:ChuyenDi`]
    - **1.1.2:** Khởi tạo lộ trình() [`:ChuyenDi` -> `:LoTrinh`]
- **2:** Quét mã kiện hàng() [`Tài xế` -> `:GiaoDienTaiXe`]
  - **2.1:** Khởi tạo quá trình xử lý kiện hàng() [`:GiaoDienTaiXe` -> `:VanChuyenController`]
    - **2.1.1:** Truy xuất thông tin kiện hàng() [`:VanChuyenController` -> `:KienHang`]
    - **2.1.2:** Báo cáo thông tin đơn khởi tạo() [`:VanChuyenController` -> `:DonHang`]
    - **2.1.3:** Yêu cầu tính toán lộ trình tối ưu() [`:VanChuyenController` -> `Hệ thống điều phối`]
    - **2.1.4:** Cập nhật dữ liệu lộ trình() [`:VanChuyenController` -> `:LoTrinh`]

*Giai đoạn 2: Tracking và Điều hướng*
- **3:** Báo cáo Tọa độ() [`Hệ thống theo dõi` -> `:VanChuyenController`]
  - **3.1:** Lưu vết định vị GPS() [`:VanChuyenController` -> `:ViTriGPS`]
  - **3.2:** Bổ sung tọa độ vào lộ trình() [`:VanChuyenController` -> `:LoTrinh`]
  - **3.3:** [Khoảng cách < 200m] Gửi thông báo sắp đến nơi() [`:VanChuyenController` -> `Khách hàng`]

*Giai đoạn 3: Sự cố giao thông (Alternates)*
- **4:** Báo động phát hiện tắc đường() [`Hệ thống theo dõi` -> `:VanChuyenController`]
  - **4.1:** Ghi nhận sự cố() [`:VanChuyenController` -> `:SuCoGiaoThong`]
  - **4.2:** Thay đổi trạng thái Đang tái tối ưu() [`:VanChuyenController` -> `:LoTrinh`]
  - **4.3:** Yêu cầu tính lại lộ trình mới() [`:VanChuyenController` -> `Hệ thống điều phối`]
  - **4.4:** Cảnh báo đổi hướng di chuyển() [`:VanChuyenController` -> `:GiaoDienTaiXe`]

*Giai đoạn 4: Hoàn tất bàn giao*
- **5:** Nhấn nút đã đến nơi() [`Tài xế` -> `:GiaoDienTaiXe`]
- **6:** Trao đổi vật lý() [`Tài xế` -> `Khách hàng`]
- **7:** Xác nhận giao thành công() [`Tài xế` -> `:GiaoDienTaiXe`]
  - **7.1:** Thông báo giao hàng thành công() [`:GiaoDienTaiXe` -> `:VanChuyenController`]
    - **7.1.1:** Lưu hình ảnh bằng chứng giao hàng() [`:VanChuyenController` -> `:BangChungGiaoHang`]
    - **7.1.2:** Đánh dấu trạng thái Giao thành công() [`:VanChuyenController` -> `:DonHang`]
    - **7.1.3:** Đánh dấu Đã giao hiện tại() [`:VanChuyenController` -> `:KienHang`]
    - **7.1.4:** Khép lại tiến trình hiện tại() [`:VanChuyenController` -> `:LoTrinh`]
    - **7.1.5:** Lưu trữ biến động vào cơ sở dữ liệu() [`:VanChuyenController` -> `LogiFast DB / DAM`]

### Description for Diagram Agent 
Vẽ hệ thống Sơ đồ giao tiếp mức nghiệp vụ (Business-Level Communication Diagram) dạng mạng lưới đối tượng. Actor ngoài cùng -> Boundary (:GiaoDienTaiXe) -> Controller (:VanChuyenController) -> Entities. Các messages phải đánh số thập phân theo dạng (1.1, 2.1.3,...) và truyền dọc theo nét liên kết. 100% messages là tiếng viết theo nguyên mẫu bảng kế hoạch. Không có tham số. Móc nối giữa Controller, ChuyenDi và LoTrinh phải chính xác như thẻ CRC.

---

## 8. Section 5 — Ma trận CRUD(E)

**Style**: `Heading 1` | **Text**: `5. Ma trận CRUD(E)`

> Note: The pptx (slide 43) explicitly calls this **CRUD(E)** where **E = Execute** (yêu cầu đối tượng thực hiện hành động). Include E in the matrix.

### 8.1 Phương pháp

**Style**: `Heading 2` | **Text**: `5.1. Phương pháp xây dựng`

#### Natural language (2 paragraphs)

**¶1 — CRUD(E) definition (from slide 43)**:  
Ma trận CRUD(E) hỗ trợ xác định các mối quan hệ giữa ca sử dụng và lớp lĩnh vực bằng cách gán nhãn các trường hợp tương tác: **C** (Create — tạo đối tượng mới), **R** (Read — tra cứu thông tin được lưu trong đối tượng), **U** (Update — cập nhật giá trị thuộc tính), **D** (Delete — xóa đối tượng), **E** (Execute — yêu cầu đối tượng thực hiện hành động nghiệp vụ). Ô trống nghĩa là UC không tương tác với lớp đó.

**¶2 — Traceability (rubric I.20)**:  
Mỗi giá trị trong ô được chú thích bằng số bước UC: `C(3)` = tạo mới tại Bước 3 luồng chính; `U(5-alt)` = cập nhật tại Bước 5 luồng thay thế. Nguồn: đặc tả UC chi tiết (Chương III) và bảng thông điệp SSD (Mục 3 chương này).

---

### 8.2 Ma trận

**Style**: `Heading 2` | **Text**: `5.2. Ma trận CRUD(E) — LogiFast`

#### Table spec

Dimensions: **6 rows** (header + 5 UC) × **22 columns** (label + 21 classes)  
Format: 8pt font, narrow columns (~0.7cm each), gray header row, manual borders

**Pre-filled CRUD(E) values**:

| UC | KhachHang | DonHang | SanPham | KienHang | ChiTietKienHang | PhuongThucThanhToan | TaiXe | PhieuPhanCong | VungDiaChi | DiemHieuSuat | LoTrinh | ViTriGPS | ChuyenDi | BangChungGiaoHang | SuCoGiaoThong | XacNhanGiaoHang | ThongBao | GiaoDich | HoaDon | ViDienTu | SoCai | PhiDichVu |
|----|-----------|---------|---------|----------|-----------------|---------------------|-------|---------------|------------|--------------|---------|----------|----------|-------------------|---------------|-----------------|----------|----------|--------|----------|-------|-----------|
| UC-01 | R(1) | C(3) | R(2) | C(3) | C(3) | R(2) | | | | | | | | | | | | | | | | |
| UC-02 | | R(1),U(5) | | | | | R(2) | C(3) | R(2) | R(2),U(5) | | | | | | | | | | | | |
| UC-03 | | U(3),U(6) | | U(2),U(6) | | | R(1) | R(1) | | | C(3),E(4) | C(4) | C(1) | C(6) | C(4-alt) | | | | | | | |
| UC-04 | R(3) | U(4) | | | | | R(1) | | | | | | | R(1) | | C(2) | C(4) | | | | | |
| UC-05 | | U(4) | | | | R(1) | R(1),U(4) | | | | | | | | | R(1) | | C(3) | C(3) | U(4) | U(4) | R(1) |

> Note: `E(4)` on `LoTrinh` at UC-03 = OR engine is **executed** (not just updated) during GPS tracking loop — this is the "Execute" case from slide 43.

---

### 8.3 Giải thích

**Style**: `Heading 2` | **Text**: `5.3. Giải thích các ô trọng tâm`

#### Natural language (1 paragraph with 5 observations)

Năm quan sát chính từ ma trận:
1. `DonHang` có mặt ở cả 5 UC — cột đầy nhất — khớp với vai trò trung tâm đã xác nhận qua sơ đồ máy trạng thái Mục 2.1.
2. `ViTriGPS` chỉ có C(4) ở UC-03, phản ánh đúng: chỉ quy trình vận chuyển mới ghi vết GPS thời gian thực.
3. `GiaoDich, HoaDon, SoCai` chỉ xuất hiện ở UC-05 — nhất quán với UC-05 là điểm kết toán cuối cùng của toàn bộ chu trình.
4. Không UC nào có D (Delete) — hệ thống giao hàng yêu cầu lưu trữ lịch sử toàn bộ để đối soát tài chính và xử lý khiếu nại.
5. `LoTrinh` có cả U và E ở UC-03: U khi cập nhật tuyến sau tái tối ưu, E khi OR engine được kích hoạt thực thi — đây là ô duy nhất trong ma trận có giá trị E, thể hiện tính chủ động của hệ thống.

---

## 9. Complete Chapter Outline

```
[Title]  V. Mô hình hóa hành vi

[H1]  1. Giới thiệu
      ¶ Behavioral modeling answers "how" not "what"
      ¶ Scope: state machine + SSD + communication/DFD + CRUD(E)

[H1]  2. Sơ đồ máy trạng thái
      ¶ Object selection criteria (slide 5)
      [TABLE] Terminology (slide 6)

[H2]  2.1. TaiXe
      ¶ Ca làm việc + UC-02 guard condition
      [TABLE] Transition table (5 rows)
      [INSERT] TaiXe_StateMachine.puml

[H2]  2.2. LoTrinh
      ¶ OR-engine + dynamic recalculation argument
      ¶ Link to SSD loop + /thoiGianDuKien derived attr
      [TABLE] Transition table (8 rows)
      [INSERT] LoTrinh_StateMachine.puml

[H1]  3. Sơ đồ tuần tự mức hệ thống (SSD)
      ¶ SSD definition (slide 24)
      ¶ Notation rules (slides 17-18, 23)

[H2]  3.1. SSD — UC-01: Đặt đơn hàng        (Trương Văn Hồng — placeholder)
      [INSERT placeholder] UC01_SSD.puml

[H2]  3.2. SSD — UC-02: Phân công giao hàng  (Nguyễn Quý Duy — placeholder)
      [INSERT placeholder] UC02_SSD.puml

[H2]  3.3. SSD — UC-03: Vận chuyển đơn hàng  (Phạm Gia Hưng — complete)
      ¶ System-level SSD, 16 messages, all in Vietnamese, parameterless, numbered
      [TABLE] Message table
      [INSERT] UC03_SSD_system.drawio

[H2]  3.4. SSD — UC-04: Xác nhận giao hàng   (Đinh Việt Hùng — placeholder)
      [INSERT placeholder] UC04_SSD.puml

[H2]  3.5. SSD — UC-05: Thanh toán           (Nguyễn Ngọc Toàn — placeholder)
      [INSERT placeholder] UC05_SSD.puml

[H1]  4. Sơ đồ tuần tự mức thiết kế / nghiệp vụ (Business-Level SD / Real-Level SD)
      ¶ Business-level SSD for UC-03: 26 messages, with classes from Domain Model and CRC
      [TABLE] Message flow mapped to Object relations
      [INSERT] UC03_SSD_business.drawio

[H1]  5. Sơ đồ giao tiếp mức thiết kế / nghiệp vụ
      ¶ Communication diagram definition (Business-Level CD)
      [TABLE] Message flow network mapping
      [INSERT] UC03_CommDiagram_business.drawio

[H1]  6. Ma trận CRUD(E)
      
[H2]  6.1. Phương pháp xây dựng
      ¶ CRUD+E definitions (slide 43)
      ¶ Traceability rule (step annotation)

[H2]  6.2. Ma trận CRUD(E) — LogiFast
      [TABLE] 6×23, gray header, 8pt font, narrow cols (includes SuCoGiaoThong)

[H2]  6.3. Giải thích các ô trọng tâm
      ¶ 5 observations
```

---

## 10. Diagrams Summary

| # | Diagram | Type | Tệp lưu trữ (`Project/Diagrams/`) | Trạng thái / Người phụ trách |
|---|---------|------|--------------------------------|-----------------------------|
| 1 | Sơ đồ máy trạng thái - Xe | UML State Máy | `TaiXe_StateMachine.puml` | Hoàn thành |
| 2 | Sơ đồ máy trạng thái - Lộ Trình | UML State Máy (w/ do-activity) | `LoTrinh_StateMachine.puml` | Hoàn thành |
| 3 | UC-03 SSD (hệ thống) | UML Sequence Diagram | `UC03_SSD_system.drawio` | Hoàn thành |
| 4 | UC-03 SSD (nghiệp vụ) | UML Sequence Diagram | `UC03_SSD_business.drawio` | Hoàn thành (cần vẽ thêm từ plan) |
| 5 | UC-03 Sơ đồ giao tiếp (nghiệp vụ) | UML Comm Diagram | `UC03_CommDiagram_business.drawio` & `UC03_CommDiagram.puml` | Hoàn thành |
| 6 | Phần I: Sơ đồ hoạt động UC-03 | UML Activity Diagram | `UC03_ActivityDiagram.drawio` & `.puml` | Hoàn thành |
| 7 | Phần I: Sơ đồ lớp lĩnh vực UC-03 | UML Class Diagram | `UC03_ClassDiagram.drawio` & `.puml` | Hoàn thành |
| 8 | Phần I: Sơ đồ đối tượng UC-03 | UML Object Diagram | `UC03_ObjectDiagram.drawio` | Hoàn thành |
| 9 | Phần I: Sơ đồ tuần tự Domain (thay thế) | UML Sequence Diagram | `UC03_DomainSequence.drawio` | Hoàn thành |

*(Lưu ý: Bảng trạng thái cập nhật ánh xạ chuẩn xác với các file hiện hữu trong thư mục `Project/Diagrams/`.)*

## 11. Rubric Checklist

| Criterion | Where | Check |
|-----------|-------|-------|
| I.15 SSD notation: `:ClassName` underlined, actor + system only | Ch5 §3.x | Each SSD |
| I.16 SSD messages traceable to UC step | Ch5 §3.x message tables | Step column filled |
| I.17 ≥1 SSD per UC, >2 outgoing messages | Ch5 §3.1–3.5 | 5 SSDs, each ≥3 outgoing |
| I.18 State machine: transitions reference UC step + SSD message | Ch5 §2.x transition tables | Last 2 columns of each table |
| I.19 CRUD(E) matrix: all 5 UCs × all 22 classes | Ch5 §6.2 | 6×23 table, no missing column |
| I.20 CRUD values traceable to UC step number | Ch5 §6.2 cells | e.g., `C(3)` not just `C` |

