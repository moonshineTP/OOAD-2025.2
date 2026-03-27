# Chuẩn bị Chương 3 — Mô hình hóa cấu trúc (IT3120, 2025-2)

> **Mục đích tài liệu**: Nội dung soạn sẵn để đưa vào Ricons.docx, bao gồm:
> - Phần **Mô tả** và **Mục tiêu** hoàn chỉnh cho từng UC (điền vào bảng đặc tả UC)
> - **Phần mở đầu Chương 3** (phương pháp luận mô hình hóa cấu trúc)
> - **Kịch bản sử dụng + từ vựng đối tượng** theo từng UC (chuẩn bị cho sơ đồ đối tượng)

---

## PHẦN A — Bảng đặc tả UC: điền bổ sung các trường Mô tả & Mục tiêu

> Sao chép các đoạn dưới đây vào đúng ô trong bảng đặc tả UC hiện có của Ricons.docx (Chương 2).

---

### UC-01: Đặt đơn hàng

**Mô tả (field "Mô tả")**:
Ca sử dụng này mô tả quá trình một khách hàng (B2C hoặc đối tác B2B qua API) gửi yêu cầu đặt đơn hàng mới tới hệ thống LogiFast. Hệ thống kiểm tra tính hợp lệ thông tin đơn hàng, tạo mã đơn duy nhất và phát sự kiện "OrderCreated" để kích hoạt quy trình điều phối tiếp theo. Kịch bản điển hình: khách hàng xác nhận giỏ hàng qua ứng dụng, hệ thống phản hồi trang xác nhận có mã đơn và thời gian giao dự kiến.

**Mục tiêu (field "Mục tiêu")**:
Sau khi ca sử dụng hoàn tất, hệ thống tồn tại một `DonHang` mới ở trạng thái *Sẵn sàng giao*, gắn với thông tin khách hàng và danh sách kiện hàng, sẵn sàng để hệ thống phân công xử lý.

---

### UC-02: Phân công giao hàng

**Mô tả (field "Mô tả")**:
Ca sử dụng này mô tả quy trình hệ thống phân công tự động tìm và gán tài xế phù hợp nhất cho các đơn hàng ở trạng thái "Sẵn sàng giao". Hệ thống quét tài xế khả dụng trong bán kính cho phép, xếp hạng theo vị trí thực tế, tải trọng hiện tại và điểm hiệu suất, sau đó gửi thông báo yêu cầu nhận đơn. Kịch bản điển hình: sau khi UC-01 hoàn tất, hệ thống tự động kích hoạt và hoàn thành phân công trong vài giây.

**Mục tiêu (field "Mục tiêu")**:
Sau khi ca sử dụng hoàn tất, tồn tại một `PhieuPhanCong` hợp lệ liên kết `DonHang` với `TaiXe` đã chấp nhận; trạng thái đơn hàng chuyển sang *Đã phân công*, trạng thái tài xe chuyển sang *Đang giao hàng*.

---

### UC-03: Vận chuyển đơn hàng

**Mô tả (field "Mô tả")**:
Ca sử dụng này mô tả toàn bộ hành trình vật lý của đơn hàng từ kho xuất phát đến tay khách hàng. Tài xế bắt đầu ca làm việc, nhận lệnh lấy hàng, quét mã QR tại kho xác nhận đúng kiện hàng, di chuyển theo lộ trình tối ưu được hệ thống bản đồ cung cấp, cập nhật vị trí GPS liên tục, thông báo cho khách khi đến nơi và ghi lại bằng chứng giao hàng. Đây là ca sử dụng phức tạp nhất với 13 bước trong luồng chính và 5 luồng thay thế/ngoại lệ.

**Mục tiêu (field "Mục tiêu")**:
Sau khi ca sử dụng hoàn tất (luồng chính), `DonHang` ở trạng thái *Giao thành công*, một `BangChungGiaoHang` hợp lệ đã được lưu với ảnh + tọa độ + tên người nhận, và sự kiện kích hoạt UC-04 được phát đi.

---

### UC-04: Xác nhận giao hàng

**Mô tả (field "Mô tả")**:
Ca sử dụng này mô tả hành động shipper (hoặc khách hàng) xác nhận chính thức rằng đơn hàng đã được nhận thành công. Hệ thống yêu cầu bằng chứng hợp lệ (chữ ký điện tử, OTP qua SMS, hoặc ảnh chụp) trước khi cập nhật trạng thái cuối cùng. Kịch bản điển hình: shipper nhấn "Xác nhận giao hàng", nhập mã OTP khách hàng đọc, hệ thống ghi nhận thời gian và kích hoạt quy trình thanh toán.

**Mục tiêu (field "Mục tiêu")**:
Sau khi ca sử dụng hoàn tất, `DonHang` ở trạng thái *Đã xác nhận*, một `XacNhanGiaoHang` được tạo với đầy đủ phương thức và thời gian xác nhận; thông báo được gửi đến tất cả các bên liên quan.

---

### UC-05: Giao hàng hoàn tất / Thanh toán

**Mô tả (field "Mô tả")**:
Ca sử dụng này mô tả quy trình đối soát tài chính sau khi giao hàng được xác nhận. Hệ thống xác định hình thức thanh toán (trả trước, tín dụng B2B, tiền mặt, hoặc COD), tính phí dịch vụ và hoa hồng tài xế, cập nhật ví điện tử của tài xế và ghi vào sổ cái doanh nghiệp. Với đơn COD, shipper cần nhập số tiền thu thực tế để hệ thống đối chiếu.

**Mục tiêu (field "Mục tiêu")**:
Sau khi ca sử dụng hoàn tất, một `GiaoDich` (hoặc `HoaDon` cho B2B) được tạo và lưu; `ViDienTu` của tài xế được cộng hoa hồng; đơn hàng chuyển sang *Hoàn tất thanh toán*; sự kiện "PaymentCompleted" được phát đi.

---

## PHẦN B — Phần mở đầu Chương 3: Mô hình hóa cấu trúc

> Dán vào đầu Chương 3 trong Ricons.docx, trước các sơ đồ.

---

### 3.0 Giới thiệu chương và phương pháp luận

#### Mục đích

Chương này xây dựng **mô hình lĩnh vực** (domain model) cho hệ thống LogiFast — lớp trừu tượng nắm bắt các khái niệm nghiệp vụ cốt lõi, các mối quan hệ giữa chúng và các ràng buộc tồn tại trong không gian vấn đề. Đây là nền tảng để chuyển sang thiết kế chi tiết ở Phần II.

#### Phương pháp luận

Nhóm áp dụng phương pháp **phân tích lĩnh vực hướng sự kiện** (event-driven domain analysis), tuân theo quy trình sau:

1. **Nhận diện lớp ứng viên** từ danh từ xuất hiện trong đặc tả luồng sự kiện của 5 UC — loại bỏ danh từ trùng lặp, quá chung chung (ví dụ: "hệ thống"), hoặc nằm ngoài phạm vi.
2. **Gán thuộc tính phân tích** — chỉ ghi tên thuộc tính, chưa gán kiểu dữ liệu hay giới hạn truy cập (quy tắc phân tích I.12).
3. **Xác định quan hệ** giữa các lớp từ động từ và trạng thái trong luồng sự kiện; gán tên quan hệ và cơ số ở cả hai đầu.
4. **Vẽ sơ đồ lớp riêng cho từng UC** — mỗi sơ đồ chỉ hiển thị các lớp tham gia trực tiếp vào luồng sự kiện của UC đó, đảm bảo sự khác biệt có ý nghĩa giữa các UC (tiêu chí I.11).
5. **Xây dựng kịch bản sử dụng cụ thể** cho từng UC và vẽ sơ đồ đối tượng tương ứng — đảm bảo mỗi đối tượng tuân theo ràng buộc của sơ đồ lớp (tiêu chí I.14).

#### Từ vựng lĩnh vực thống nhất

Toàn bộ nhóm sử dụng chung bộ 15 lớp lĩnh vực được định nghĩa trong tài liệu tham chiếu nội bộ (xem `docs/environment.md`, Mục 5). Tên lớp, tên thuộc tính và tiền tố ID mẫu nhất quán xuyên suốt 5 UC để đảm bảo tính truy xuất trong ma trận CRUD.

#### Quy ước vẽ sơ đồ

| Quy ước | Chuẩn áp dụng |
|---------|---------------|
| Tên lớp | UpperCamelCase, tiếng Việt không dấu viết liền (VD: `DonHang`) |
| Tên thuộc tính | lowerCamelCase, tiếng Việt không dấu viết liền (VD: `trangThai`) |
| Tên quan hệ | Động từ tiếng Việt ngắn gọn, chiều mũi tên rõ ràng |
| Cơ số | Ghi ở CẢ HAI đầu quan hệ, dùng ký hiệu UML (`1`, `0..*`, `1..*`) |
| Công cụ | draw.io / PlantUML |

---

## PHẦN C — Kịch bản sử dụng + Từ vựng đối tượng theo UC

> Nội dung này phục vụ hai mục đích:
> (1) Là kịch bản chi tiết để trình bày trong báo cáo (trước sơ đồ đối tượng)
> (2) Là danh sách đối tượng cụ thể (instance) để vẽ sơ đồ đối tượng (tiêu chí I.9)

**⚠️ Quy tắc nhất quán**: Các đối tượng sau đây phải sử dụng ĐÚNG giá trị ID và tên lớp từ `docs/environment.md` Mục 5.4. Cùng một đối tượng (VD: `DonHang ORD-2026-001`) xuất hiện trong nhiều UC phải có cùng giá trị.

---

### UC-01: Kịch bản đặt đơn hàng

**Tên kịch bản**: Khách hàng B2C đặt đơn giao 1 kiện hàng

**Diễn giải**:
Vào 09:15 ngày 26/03/2026, chị Nguyễn Thị Lan (KH-055) đăng nhập ứng dụng LogiFast Mobile, xác nhận giỏ hàng gồm 1 sản phẩm (Điện thoại Samsung A56, SP-0099), nhập địa chỉ giao "123 Nguyễn Văn Cừ, Q.5, TP.HCM", chọn hình thức thanh toán COD. Hệ thống kiểm tra tồn kho → hợp lệ, tạo đơn hàng ORD-2026-001 trạng thái *Sẵn sàng giao*, phát sự kiện "OrderCreated".

**Bảng đối tượng UC-01**:

| Lớp | Tên đối tượng | Giá trị thuộc tính chính |
|-----|--------------|--------------------------|
| `KhachHang` | `kh1 : KhachHang` | id=KH-055, ten="Nguyễn Thị Lan", soDienThoai="0901234567", diaChi="45 Lê Lợi, Q.1", loaiKhach="B2C" |
| `DonHang` | `dh1 : DonHang` | id=ORD-2026-001, trangThai="Sẵn sàng giao", diaChiGiao="123 Nguyễn Văn Cừ, Q.5", tongGiaTri=8500000, hinhThucThanhToan="COD", thoiGianDat="2026-03-26T09:15:00" |
| `SanPham` | `sp1 : SanPham` | id=SP-0099, ten="Samsung Galaxy A56", moTa="Điện thoại thông minh", donGia=8500000 |
| `ChiTietDonHang` | `ctd1 : ChiTietDonHang` | id=CTD-001-01, soLuong=1, donGia=8500000 |

**Quan hệ đối tượng**:
- `kh1` đặt `dh1` (association: *đặt*, KhachHang → DonHang)
- `dh1` gồm `ctd1` (composition: *gồm*, DonHang → ChiTietDonHang)
- `ctd1` tham chiếu `sp1` (association: *thuộc*, ChiTietDonHang → SanPham)

---

### UC-02: Kịch bản phân công giao hàng

**Tên kịch bản**: Hệ thống tự động gán tài xế cho đơn hàng mới

**Diễn giải**:
Ngay sau khi ORD-2026-001 được tạo (09:15), hệ thống phân công quét 3 tài xế khả dụng trong bán kính 5km. Tài xế Trần Minh Khoa (TX-001) gần nhất (2.1km), tải trọng = 0 đơn, điểm hiệu suất = 4.8/5 — được chọn. Hệ thống tạo phiếu phân công PPC-2026-0326-001 và đẩy thông báo tới app. TX-001 nhấn "Chấp nhận" lúc 09:16. Trạng thái DonHang → *Đã phân công*.

**Bảng đối tượng UC-02**:

| Lớp | Tên đối tượng | Giá trị thuộc tính chính |
|-----|--------------|--------------------------|
| `DonHang` | `dh1 : DonHang` | id=ORD-2026-001, trangThai="Đã phân công" *(trạng thái cập nhật từ UC-01)* |
| `TaiXe` | `tx1 : TaiXe` | id=TX-001, ten="Trần Minh Khoa", soDienThoai="0912345678", trangThai="Đang giao hàng", viTriHienTai="10.7626,106.6602" |
| `PhieuPhanCong` | `ppc1 : PhieuPhanCong` | id=PPC-2026-0326-001, thoiGianPhanCong="2026-03-26T09:15:30", trangThai="Đã chấp nhận", diemUuTien=4.8 |
| `KhoHang` | `kho1 : KhoHang` | id=KHO-SGN-01, ten="Kho Bình Chánh", diaChi="Đường số 12, KCN Vĩnh Lộc, Bình Chánh" |

**Quan hệ đối tượng**:
- `ppc1` phân công `dh1` (association: *phân công*, PhieuPhanCong → DonHang)
- `ppc1` gán `tx1` (association: *gán*, PhieuPhanCong → TaiXe)
- `dh1` xuất phát từ `kho1` (association: *xuất phát*, DonHang → KhoHang)

---

### UC-03: Kịch bản vận chuyển đơn hàng

**Tên kịch bản**: Tài xế lấy hàng tại kho và giao thành công tới khách

**Diễn giải**:
09:30 — TX-001 đến KHO-SGN-01, quét QR kiện hàng KH-PKG-001 → hệ thống xác nhận đúng đơn. Hệ thống tính lộ trình LT-2026-001 (9.2km, ETA 35 phút). 09:31 — tài xế xuất phát. GPS cập nhật mỗi 30s. 10:04 — tài xế đến 123 Nguyễn Văn Cừ, thông báo gửi tới KH-055. 10:06 — giao xong, chụp ảnh + ghi tên người nhận "Nguyễn Thị Lan", lưu BC-2026-001. DonHang → *Giao thành công*.

**Bảng đối tượng UC-03**:

| Lớp | Tên đối tượng | Giá trị thuộc tính chính |
|-----|--------------|--------------------------|
| `TaiXe` | `tx1 : TaiXe` | id=TX-001, ten="Trần Minh Khoa", trangThai="Đã đến điểm giao" |
| `DonHang` | `dh1 : DonHang` | id=ORD-2026-001, trangThai="Giao thành công" |
| `KienHang` | `kh_pkg1 : KienHang` | id=KH-PKG-001, maQR="QR-ORD-2026-001", trangThai="Đã giao", khoiLuong=0.35 |
| `LoTrinh` | `lt1 : LoTrinh` | id=LT-2026-001, diemBatDau="KHO-SGN-01", diemDen="123 Nguyễn Văn Cừ, Q.5", trangThai="Hoàn tất" |
| `BangChungGiaoHang` | `bc1 : BangChungGiaoHang` | id=BC-2026-001, tenNguoiNhan="Nguyễn Thị Lan", thoiGianGiao="2026-03-26T10:06:00", hinhAnh="proof_ORD-2026-001.jpg", toaDo="10.7525,106.6624" |

**Quan hệ đối tượng**:
- `tx1` thực hiện `lt1` (association: *thực hiện*, TaiXe → LoTrinh)
- `lt1` giao `dh1` (association: *giao*, LoTrinh → DonHang)
- `dh1` chứa `kh_pkg1` (composition: *chứa*, DonHang → KienHang)
- `dh1` có `bc1` (association: *có bằng chứng*, DonHang → BangChungGiaoHang)

---

### UC-04: Kịch bản xác nhận giao hàng

**Tên kịch bản**: Shipper xác nhận bằng OTP sau khi giao

**Diễn giải**:
10:07 — TX-001 (đóng vai Shipper) chọn ORD-2026-001 trong tab "Chờ xác nhận". Nhấn "Xác nhận giao hàng". Hệ thống gửi OTP 6 số tới 0901234567 (KH-055). Khách đọc OTP "482913". Shipper nhập → hệ thống kiểm tra → hợp lệ. Tạo XN-2026-001 với phương thức "OTP", thời gian 10:07:44. DonHang → *Đã xác nhận*. Gửi thông báo đến KH-055 và Phòng Kế toán.

**Bảng đối tượng UC-04**:

| Lớp | Tên đối tượng | Giá trị thuộc tính chính |
|-----|--------------|--------------------------|
| `TaiXe` | `tx1 : TaiXe` | id=TX-001, ten="Trần Minh Khoa", trangThai="Hoàn tất chuyến" |
| `DonHang` | `dh1 : DonHang` | id=ORD-2026-001, trangThai="Đã xác nhận" |
| `KhachHang` | `kh1 : KhachHang` | id=KH-055, ten="Nguyễn Thị Lan", soDienThoai="0901234567" |
| `BangChungGiaoHang` | `bc1 : BangChungGiaoHang` | id=BC-2026-001 *(tham chiếu từ UC-03)* |
| `XacNhanGiaoHang` | `xn1 : XacNhanGiaoHang` | id=XN-2026-001, phuongThucXacNhan="OTP", thoiGianXacNhan="2026-03-26T10:07:44" |

**Quan hệ đối tượng**:
- `tx1` tạo `xn1` (association: *tạo*, TaiXe → XacNhanGiaoHang)
- `xn1` xác nhận `dh1` (association: *xác nhận*, XacNhanGiaoHang → DonHang)
- `xn1` liên kết `bc1` (association: *đính kèm*, XacNhanGiaoHang → BangChungGiaoHang)
- `kh1` nhận thông báo từ `dh1` (association: *nhận đơn*, KhachHang → DonHang)

---

### UC-05: Kịch bản thanh toán / hoàn tất

**Tên kịch bản**: Hệ thống xử lý COD sau xác nhận giao

**Diễn giải**:
10:08 — hệ thống phát hiện ORD-2026-001 là COD, tự động mở màn hình nhập COD cho TX-001. Shipper nhập số tiền thu thực: 8.500.000đ (khớp với tongGiaTri). Hệ thống tính phí dịch vụ: 42.500đ (0.5%), hoa hồng tài xế: 85.000đ (1%). Tạo GiaoDich TT-2026-001 và HoaDon HD-2026-001. Cộng 85.000đ vào ViDienTu của TX-001 (VI-TX-001). DonHang → *Hoàn tất thanh toán*. Phát "PaymentCompleted".

**Bảng đối tượng UC-05**:

| Lớp | Tên đối tượng | Giá trị thuộc tính chính |
|-----|--------------|--------------------------|
| `TaiXe` | `tx1 : TaiXe` | id=TX-001, ten="Trần Minh Khoa" |
| `DonHang` | `dh1 : DonHang` | id=ORD-2026-001, trangThai="Hoàn tất thanh toán", hinhThucThanhToan="COD" |
| `HoaDon` | `hd1 : HoaDon` | id=HD-2026-001, tongTien=8500000, trangThai="Đã thanh toán", thoiGianXuatHoaDon="2026-03-26T10:08:12" |
| `ThanhToan` | `tt1 : ThanhToan` | id=TT-2026-001, soTien=8500000, hinhThucThanhToan="COD", thoiGian="2026-03-26T10:08:15" |
| `ViDienTu` | `vi1 : ViDienTu` | id=VI-TX-001, soDu=1285000, chuSoHuu="TX-001" |
| `KhachHang` | `kh1 : KhachHang` | id=KH-055, ten="Nguyễn Thị Lan" |

**Quan hệ đối tượng**:
- `dh1` phát sinh `hd1` (association: *phát sinh*, DonHang → HoaDon)
- `hd1` ghi nhận `tt1` (association: *ghi nhận*, HoaDon → ThanhToan)
- `tt1` cập nhật `vi1` (association: *cập nhật*, ThanhToan → ViDienTu)
- `kh1` thanh toán `dh1` (association: *thanh toán*, KhachHang → DonHang)

---

## PHẦN D — Tóm tắt sơ đồ lớp theo UC (không vẽ lại — để tham chiếu)

> Bảng này giúp kiểm tra tiêu chí I.11 (các sơ đồ lớp phải khác nhau có ý nghĩa).

| UC | Lớp chính | Lớp mới xuất hiện lần đầu | Lớp kế thừa từ UC trước |
|----|----------|--------------------------|------------------------|
| UC-01 | KhachHang, DonHang, SanPham, ChiTietDonHang | Tất cả (UC đầu tiên) | — |
| UC-02 | DonHang, TaiXe, PhieuPhanCong, KhoHang | PhieuPhanCong, KhoHang | DonHang |
| UC-03 | TaiXe, DonHang, KienHang, LoTrinh, BangChungGiaoHang | KienHang, LoTrinh, BangChungGiaoHang | TaiXe, DonHang |
| UC-04 | TaiXe, DonHang, KhachHang, BangChungGiaoHang, XacNhanGiaoHang | XacNhanGiaoHang | TaiXe, DonHang, KhachHang, BangChungGiaoHang |
| UC-05 | TaiXe, DonHang, HoaDon, ThanhToan, ViDienTu, KhachHang | HoaDon, ThanhToan, ViDienTu | TaiXe, DonHang, KhachHang |

**Kiểm tra I.11**: Mỗi UC có ít nhất 1–3 lớp mới không xuất hiện ở UC trước → đảm bảo sự khác biệt có ý nghĩa ✅

---

## PHẦN E — Checklist trước khi vẽ sơ đồ

Trước khi bắt đầu vẽ cho từng UC, kiểm tra:

- [ ] Đã có kịch bản cụ thể với giá trị thuộc tính đầy đủ (Phần C ở trên)
- [ ] Tên lớp khớp với `docs/environment.md` Mục 5.1
- [ ] Thuộc tính **chỉ tên**, không có `:Type`, không có `+/-/#`
- [ ] Mọi quan hệ có tên + cơ số ở cả 2 đầu
- [ ] Sơ đồ đối tượng có ít nhất tất cả đối tượng trong bảng Phần C
- [ ] Giá trị ID trong sơ đồ đối tượng khớp với Mục 5.4 của `docs/environment.md`
- [ ] Một lớp nếu xuất hiện ở 2 UC thì thuộc tính phải nhất quán (không được thêm/bỏ thuộc tính tùy tiện)
