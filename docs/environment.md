# Môi trường ứng dụng — LogiFast (Hệ thống Quản lý Giao hàng Timely)

> **Phạm vi**: Tài liệu này đáp ứng ba tiêu chí đầu của rubric chấm điểm (I.1 – I.3) và đặt nền từ vựng lĩnh vực cho toàn bộ sơ đồ lớp và sơ đồ đối tượng (5 UC).

---

## 1. Bối cảnh doanh nghiệp (Tiêu chí I.1)

### 1.1 Giới thiệu doanh nghiệp

**Công ty Logistics Cần Giờ (LogiFast)** hiện đang vận hành trong một hệ sinh thái giao nhận đầy biến động tại khu vực miền Nam. Môi trường kinh doanh của công ty mang tính chất lưỡng cực, nhiều nguồn và có nhiều cạnh tranh.

- **Phân khúc B2C**: LogiFast cung cấp dịch vụ vận chuyển cho mạng lưới các đại lý bán lẻ và cửa hàng tiện lợi, chủ yếu tập trung vào các mặt hàng tiêu dùng nhanh và hàng hóa có hạn sử dụng cao.
- **Phân khúc B2B**: Công ty đóng vai trò là mắt xích "chặng cuối" (last-mile delivery) thiết yếu cho các sàn thương mại điện tử lớn khi các đơn vị này chưa tự xây dựng được hạ tầng vận hành tại địa phương.

Sự đan xen này tạo ra áp lực vận hành khổng lồ khi số lượng đơn hàng trong khu vực ngày càng tăng.

### 1.2 Hệ thống công cụ hiện tại và điểm yếu

Đội ngũ điều phối đang vật lộn với "mớ bòng bong" các công cụ rời rạc:

| Nhóm vấn đề | Biểu hiện cụ thể |
|---|---|
| Tiếp nhận đơn hàng | API từ đối tác B2B xen lẫn file Excel thủ công từ đại lý nhỏ và ghi chú tay |
| Vận hành thực địa | Tài xế dùng ứng dụng bản đồ cá nhân, ứng dụng theo dõi không đồng bộ, sổ tay riêng |
| Quản lý dữ liệu | Không có Nguồn Sự thật Duy nhất (Single Source of Truth) — dữ liệu phân mảnh |
| Điều phối tuyến đường | Hoàn toàn dựa vào kinh nghiệm cá nhân, không có thuật toán tối ưu |
| Bằng chứng giao hàng | Quản lý ảnh/GPS rời rạc, khó đối soát khi khiếu nại |

### 1.3 Tầm nhìn chiến lược

Ban lãnh đạo LogiFast đã xác định mục tiêu chuyển mình sang mảng giao đồ ăn (food delivery) và các dịch vụ yêu cầu tính thời gian cực kỳ khắt khe. Điều này đòi hỏi hệ thống phải có khả năng:

- Điều phối nhân sự theo ca làm việc
- Hỗ trợ hoạt động xuyên đêm và ngày lễ
- Lập kế hoạch lộ trình linh hoạt theo từng phút

---

## 2. Cơ cấu tổ chức (Tiêu chí I.2)

### 2.1 Sơ đồ phân cấp tổ chức

```
LogiFast — Công ty Logistics Cần Giờ
│
├── Ban lãnh đạo
│   └── Giám đốc (Director / CEO)
│
├── Phòng Vận hành (Operations Department)
│   ├── Quản lý Vận hành (Operations Manager)
│   └── Điều phối viên (Coordinator / Dispatcher)
│
├── Đội Tài xế (Driver Team)
│   └── Nhân viên Giao hàng (Shipper / Tài xế)
│
├── Phòng Kế toán – Tài chính (Finance & Accounting)
│   ├── Kế toán viên (Accountant)
│   └── Quản trị viên (Admin)
│
└── Phòng Công nghệ Thông tin (IT Department)
    └── Kỹ sư hệ thống / Admin hệ thống
```

### 2.2 Bảng vai trò và trách nhiệm

| Chức vụ (VN) | Title (EN) | Phòng ban | UC liên quan | Vai trò trong hệ thống |
|---|---|---|---|---|
| Giám đốc | Director / CEO | Ban lãnh đạo | — | Phê duyệt chiến lược, không tương tác trực tiếp với hệ thống |
| Quản lý Vận hành | Operations Manager | Phòng Vận hành | UC-02 (actor phụ) | Giám sát điều phối, can thiệp thủ công khi khẩn cấp |
| Điều phối viên | Coordinator / Dispatcher | Phòng Vận hành | UC-02, UC-03 | Theo dõi phân công tự động, xử lý sự cố tuyến đường |
| Nhân viên Giao hàng / Tài xế / Shipper | Driver / Shipper | Đội Tài xế | UC-02, UC-03, UC-04, UC-05 | Nhận đơn, lấy hàng tại kho, giao hàng, xác nhận hoàn tất |
| Kế toán viên | Accountant | Phòng Kế toán–Tài chính | UC-05 (actor phụ) | Đối soát công nợ B2B, kiểm tra doanh thu |
| Quản trị viên (Admin) | Admin | Phòng Kế toán–Tài chính | UC-05 (actor phụ) | Phê duyệt sai lệch COD, kiểm soát sổ cái |
| Kỹ sư / Admin hệ thống | System Engineer / Admin | Phòng CNTT | — | Vận hành hệ thống, xử lý log lỗi |

### 2.3 Tác nhân ngoài hệ thống

| Tác nhân ngoài | Loại | UC liên quan | Mô tả |
|---|---|---|---|
| Khách hàng (B2C) | Con người | UC-01, UC-03, UC-04, UC-05 | Đặt đơn, theo dõi, xác nhận nhận hàng |
| Đối tác B2B | Tổ chức bên ngoài | UC-01 | Gửi đơn hàng qua API |

---

## 3. Tính cấp thiết và Giá trị kỳ vọng (Tiêu chí I.3)

### 3.1 Khó khăn hiện tại → Giải pháp đề xuất

| # | Khó khăn | Giải pháp của hệ thống mới |
|---|---|---|
| 1 | **Đa kênh thiếu tập trung**: Đơn hàng đến từ API B2B, Excel thủ công, ghi chú tay — dữ liệu phân mảnh, dễ sai/trùng | Một cổng tiếp nhận duy nhất, tự động chuẩn hóa và kiểm tra tính hợp lệ đơn hàng từ mọi nguồn |
| 2 | **Chi phí vận hành cao, hiệu suất thấp**: Không có thuật toán tối ưu tuyến đường, lãng phí nhiên liệu và thời gian tài xế | Tích hợp thuật toán VRP, gom đơn theo tuyến, phân công tự động theo vị trí và tải trọng |
| 3 | **Áp lực SLA (thời gian giao hàng)**: Không thể cung cấp ETA chính xác theo điều kiện giao thông thực tế | Cập nhật ETA liên tục từ GPS và dữ liệu giao thông, thông báo chủ động cho khách khi lệch lịch |
| 4 | **Thiếu minh bạch tài xế**: Không có cơ chế xác thực bằng chứng giao hàng (ảnh/GPS), khó xử lý khiếu nại | Lưu trữ bằng chứng giao hàng số hóa (hình ảnh + tọa độ + chữ ký/OTP), truy xuất theo đơn hàng |

### 3.2 Lý do lựa chọn hệ thống thông tin tập trung

1. **Đột phá khả năng mở rộng**: Tự động hóa toàn bộ chu trình từ tạo đơn đến phân công, quản lý khối lượng tăng gấp nhiều lần mà không cần tăng tuyến tính nhân sự.
2. **Thiết lập Nguồn Sự thật Duy nhất**: Loại bỏ hoàn toàn trùng lặp và sai sót dữ liệu, đồng bộ thông tin xuyên suốt từ tiếp nhận đến thanh toán.
3. **Chuẩn bị cho tương lai**: Nền tảng số hóa là điều kiện tiên quyết để mở rộng sang food delivery và các dịch vụ real-time khác.

### 3.3 Giá trị kỳ vọng (≥ 5 giá trị)

| # | Đối tượng thụ hưởng | Giá trị kỳ vọng |
|---|---|---|
| V1 | Doanh nghiệp | **Tối ưu hóa nguồn lực**: Tự động hóa từ tạo đơn đến phân công, giảm nhân sự quản lý trung gian nhưng vẫn đảm bảo năng suất |
| V2 | Doanh nghiệp | **Ra quyết định dựa trên dữ liệu**: Báo cáo thống kê và đánh giá hiệu suất tài xế giúp điều chỉnh chiến lược vận hành minh bạch |
| V3 | Doanh nghiệp | **Khả năng mở rộng**: Lưu trữ hồ sơ vĩnh viễn và chỉ mục tìm kiếm nhanh cho phép quản lý hàng triệu đơn hàng |
| V4 | Tài xế | **Công bằng và hiệu quả**: Phân công tự động theo khoảng cách giúp nhận đơn phù hợp nhất, giảm quãng đường chạy rỗng, tăng thu nhập thực tế |
| V5 | Tài xế | **Hỗ trợ vận hành**: Lập kế hoạch lộ trình và tái điều phối giúp giảm áp lực khi gặp sự cố trên đường |
| V6 | Khách hàng | **Trải nghiệm minh bạch**: Theo dõi hành trình thời gian thực trên bản đồ, biết chính xác vị trí tài xế và ETA |
| V7 | Khách hàng | **Giao tiếp chủ động**: Hệ thống tự động thông báo khi có thay đổi ETA hoặc sự cố, giúp khách hàng chủ động sắp xếp thời gian |

---

## 4. Luồng thông tin tổng quan

### 4.1 Vòng đời đơn hàng và luồng thông tin

```
[Khách hàng / Đối tác B2B]
        │ đặt đơn (UC-01)
        ▼
[Phòng Vận hành — Hệ thống quản lý đơn hàng]
  • Tạo DonHang mới, gán trạng thái "Sẵn sàng giao"
        │ kích hoạt SK-02
        ▼
[Phòng Vận hành — Hệ thống điều phối (UC-02)]
  • Quét TaiXe khả dụng, tính điểm ưu tiên
  • Tạo PhieuPhanCong, đẩy xuống app tài xế
        │ tài xế chấp nhận
        ▼
[Đội Tài xế — UC-03: Vận chuyển]
  • Tài xế lấy hàng tại KhoHang, bắt đầu LoTrinh
  • Hệ thống theo dõi cập nhật GPS → tính ETA liên tục
  • Thông báo "Tài xế đã đến" cho Khách hàng
        │ giao nhận thực địa
        ▼
[Đội Tài xế — UC-04: Xác nhận giao hàng]
  • Shipper tạo BangChungGiaoHang (ảnh + chữ ký/OTP)
  • Cập nhật DonHang → "Đã giao"
        │ kích hoạt SK-05
        ▼
[Phòng Kế toán–Tài chính — UC-05: Thanh toán]
  • Tính HoaDon, trích hoa hồng, cập nhật ViDienTu tài xế
  • Ghi CongNo cho đối tác B2B
  • Lưu chứng từ điện tử
```

### 4.2 Bảng luồng thông tin theo sự kiện

| Sự kiện | Actor gửi thông tin | Thông tin truyền đi | Actor nhận | Hệ thống xử lý |
|---|---|---|---|---|
| SK-01: Đặt đơn | Khách hàng / API B2B | Thông tin đơn hàng, địa chỉ giao | Hệ thống quản lý đơn | Kiểm tra hợp lệ, tạo DonHang |
| SK-02: Phân công | Hệ thống | Danh sách đơn "Sẵn sàng" | Hệ thống điều phối | Tính toán VRP, gán tài xế |
| SK-02 → tài xế | Hệ thống điều phối | "Yêu cầu giao hàng mới" + chi tiết | Tài xế (qua app) | Tài xế chấp nhận/từ chối |
| SK-03: Vận chuyển | Hệ thống theo dõi GPS | Vị trí thực tế, ETA | Khách hàng, Điều phối viên | Cập nhật bản đồ real-time |
| SK-04: Xác nhận | Shipper | Bằng chứng giao hàng | Hệ thống | Cập nhật trạng thái đơn |
| SK-05: Thanh toán | Hệ thống | Dữ liệu tài chính đơn | Phòng Kế toán | Đối soát, lưu sổ cái |

---

## 5. Từ vựng lĩnh vực — Nền tảng cho sơ đồ lớp và sơ đồ đối tượng

> **Quy tắc phân tích (I.12)**: Thuộc tính chỉ ghi **tên**, KHÔNG ghi kiểu dữ liệu, KHÔNG ghi giới hạn truy cập (`+/-/#`).

### 5.1 Bảng lớp lĩnh vực toàn hệ thống

| Lớp (VN) | Class (EN) | Thuộc tính (chỉ tên) | UC liên quan | Tiền tố ID mẫu |
|---|---|---|---|---|
| `KhachHang` | Customer | id, ten, soDienThoai, diaChi, loaiKhach | UC-01, 03, 04, 05 | `KH-` |
| `DonHang` | Order | id, trangThai, diaChiGiao, tongGiaTri, hinhThucThanhToan, thoiGianDat | UC-01 → 05 | `ORD-` |
| `SanPham` | Product | id, ten, moTa, donGia | UC-01 | `SP-` |
| `ChiTietDonHang` | Order Line | id, soLuong, donGia | UC-01 | `CTD-` |
| `TaiXe` | Driver | id, ten, soDienThoai, trangThai, viTriHienTai | UC-02, 03, 04, 05 | `TX-` |
| `PhieuPhanCong` | Assignment Ticket | id, thoiGianPhanCong, trangThai, diemUuTien | UC-02 | `PPC-` |
| `KhoHang` | Warehouse | id, ten, diaChi | UC-02, 03 | `KHO-` |
| `LoTrinh` | Route | id, diemBatDau, diemDen, trangThai | UC-03 | `LT-` |
| `BangChungGiaoHang` | Delivery Proof | id, tenNguoiNhan, thoiGianGiao, hinhAnh, toaDo | UC-03, 04 | `BC-` |
| `LichGiaoLai` | Redelivery Schedule | id, lyDo, soLanThu, thoiGianGiaoLai | UC-03 | `LGL-` |
| `XacNhanGiaoHang` | Delivery Confirmation | id, phuongThucXacNhan, thoiGianXacNhan | UC-04 | `XN-` |
| `HoaDon` | Invoice | id, tongTien, trangThai, thoiGianXuatHoaDon | UC-05 | `HD-` |
| `ThanhToan` | Payment | id, soTien, hinhThucThanhToan, thoiGian | UC-05 | `TT-` |
| `ViDienTu` | Digital Wallet | id, soDu, chuSoHuu | UC-05 | `VI-` |
| `CongNo` | Payable / Debt | id, soTien, trangThai, hanThanhToan | UC-05 | `CN-` |

### 5.2 Trạng thái `DonHang` theo vòng đời

```
[Mới tạo]
    │ UC-01 hoàn tất
    ▼
[Sẵn sàng giao]
    │ UC-02 phân công tài xế
    ▼
[Đã phân công]
    │ Tài xế lấy hàng (UC-03a)
    ▼
[Đang giao hàng]
    │ Giao thành công (UC-03c)          │ Không liên lạc (UC-03f)    │ Khách từ chối (UC-03g)
    ▼                                    ▼                             ▼
[Giao thành công]               [Gặp sự cố – Chậm trễ]        [Khách từ chối nhận]
    │ UC-04 xác nhận                     │ LichGiaoLai tạo
    ▼                                    ▼
[Đã xác nhận giao]              [Giao thất bại lần N]
    │ UC-05 đối soát
    ▼
[Hoàn tất thanh toán]
```

### 5.3 Trạng thái `TaiXe` trong vận hành

| Trạng thái | Khi nào | UC kích hoạt |
|---|---|---|
| `Trống` (Available) | Chưa có đơn nào | — |
| `Đang giao hàng` | Sau khi nhận PhieuPhanCong | UC-02 |
| `Đã đến điểm giao` | Nhấn "Đã đến điểm giao" trên app | UC-03 |
| `Hoàn tất chuyến` | Sau khi tất cả đơn trong chuyến được xử lý | UC-04/05 |

### 5.4 Ví dụ giá trị ID thống nhất giữa các UC

| Lớp | Ví dụ giá trị ID | Dùng trong |
|---|---|---|
| KhachHang | `KH-055` | UC-01, UC-03 object diagram |
| TaiXe | `TX-001` | UC-02, UC-03, UC-04 object diagram |
| DonHang | `ORD-2026-001` | Tất cả UC object diagrams |
| KhoHang | `KHO-SGN-01` | UC-02, UC-03 object diagram |
| PhieuPhanCong | `PPC-2026-0326-001` | UC-02 object diagram |
| BangChungGiaoHang | `BC-2026-001` | UC-03, UC-04 object diagram |
| HoaDon | `HD-2026-001` | UC-05 object diagram |

---

*Tài liệu này là nền tảng tham chiếu — mọi sơ đồ lớp và sơ đồ đối tượng của 5 UC đều phải dùng đúng tên lớp và tiền tố ID trong Mục 5.*
