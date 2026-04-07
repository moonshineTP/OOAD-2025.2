## 0.6. Thiết kế Sơ đồ tuần tự mức Nghiệp Vụ (Business-Level Sequence Diagram) - Đặc tả cho UC-03

Ghi chú quan trọng: Theo nghiên cứu, SSD mức hệ thống chỉ coi hệ thống là "Hộp đen". Tuy nhiên, theo yêu cầu của môn học, chúng ta sẽ thiết kế luồng thông điệp xuyên suốt mức nghiệp vụ (Business-Level SD / "Mở hộp đen") cho riêng **UC-03: Vận chuyển đơn hàng**.

Việc mô hình hóa này dựa vững chắc trên **Thẻ CRC UC-03**, **Sơ đồ lớp lĩnh vực**, và **Sơ đồ đối tượng UC-03** đã lấy từ dữ liệu được cung cấp.

### 1. Thành phần tham gia (Lifelines mức thiết kế)
Khác với mức Hệ thống, Sơ đồ tuần tự mức nghiệp vụ (SD) bắt buộc phải bao gồm ĐẦY ĐỦ các lớp chức năng (Boundary - Control - Entity):

- **Actors (Từ UCD)**: Tài xế (Human), Khách hàng (Human), Hệ thống theo dõi (API), Hệ thống điều phối (API).
- **Boundary/UI Classes**: :GiaoDienTaiXe (hoặc UI_App).
- **Control Classes**: :VanChuyenController (Lớp điều khiển trung tâm UC-03).
- **Entity Classes (Từ thẻ CRC)**: :ChuyenDi, :LoTrinh, :KienHang, :DonHang, :ViTriGPS, :BangChungGiaoHang, :SuCoGiaoThong.
- **System/DB (Tùy chọn hiển thị đầy đủ)**: LogiFast DB / DAM.

### 2. Mô tả luồng thông điệp (Flow of messages) mapping với Kịch bản (Scenario)

*Lưu ý: Tên thông điệp mức nghiệp vụ / thiết kế lúc này PHẢI mang dạng ngôn ngữ tự nhiên Tiếng Việt không tham số, chính xác như yêu cầu môn học, nhằm đặc tả hành vi một cách dễ hiểu.*

**Giai đoạn 1: Bắt đầu ca và quét kiện hàng (Tương ứng bước 1, 2, 3)**
- **1.1.** Tài xế gửi thông điệp 1. Nhấn nút bắt đầu hành trình() tới :GiaoDienTaiXe.
- **1.2.** :GiaoDienTaiXe gửi thông điệp 2. Yêu cầu bắt đầu ca() tới :VanChuyenController.
- **1.3.** :VanChuyenController gửi thông điệp 3. Tạo chuyến đi() để tạo :ChuyenDi.
- **1.4.** :ChuyenDi gửi thông điệp 4. Khởi tạo lộ trình() cho :LoTrinh.
- **1.5.** Tài xế thao tác bằng thông điệp 5. Quét mã kiện hàng() trên :GiaoDienTaiXe.
- **1.6.** Controller truy vấn bằng thông điệp 6. Truy xuất thông tin kiện hàng() tới :KienHang, sau đó lấy đơn bằng thông điệp 7. Báo cáo thông tin đơn khởi tạo() tới :DonHang.
- **1.7.** Controller gọi thông điệp 8. Yêu cầu tính toán lộ trình tối ưu() tới Hệ thống điều phối và cập nhật bằng thông điệp 10. Cập nhật dữ liệu lộ trình() tới :LoTrinh.

**Giai đoạn 2: Tracking GPS và Điều hướng di chuyển (Tương ứng bước 4)**
*(Vòng lặp loop [Mỗi 30s])*
- **2.1.** Cảm biến module GPS của Hệ thống theo dõi gửi thông điệp 11. Báo cáo Tọa độ() tới Controller.
- **2.2.** Controller gửi thông điệp 12. Lưu vết định vị GPS() tạo :ViTriGPS.
- **2.3.** Controller gửi thông điệp 13. Bổ sung tọa độ vào lộ trình() tới :LoTrinh.
- **2.4.** Nếu khoảng cách < 200m, Controller gửi thông điệp 14. Gửi thông báo sắp đến nơi() tới Khách hàng.

**Giai đoạn 3: Luồng thay thế - Rẽ nhánh khi có Sự cố giao thông (Alternates)**
*(Trong khung lt [co su co] | [khong co]  )*
- **3.1.** Nếu kẹt xe, Hệ thống theo dõi gửi thông điệp 15. Báo động phát hiện tắc đường() tới Controller.
- **3.2.** Controller gửi thông điệp 16. Ghi nhận sự cố() để tạo :SuCoGiaoThong.
- **3.3.** Gửi thông điệp 17. Thay đổi trạng thái Đang tái tối ưu() tới :LoTrinh.
- **3.4.** Gọi 18. Yêu cầu tính lại lộ trình mới() tới Hệ thống điều phối. Controller gửi tiếp 20. Cảnh báo đổi hướng di chuyển() tới :GiaoDienTaiXe.

**Giai đoạn 4: Hoàn tất bàn giao (Tương ứng bước 5, 6)**
- **4.1.** Tài xế gửi thông điệp 21. Nhấn nút đã đến nơi() tới :GiaoDienTaiXe.
- **4.2.** Tài xế gửi thông điệp *21a. Trao đổi vật lý()* với Khách hàng.
- **4.3.** Tài xế kết thúc bằng việc gửi 22. Gửi bằng chứng xác nhận giao thành công() cho :GiaoDienTaiXe.
- **4.4.** Controller gửi thông điệp 23. Lưu hình ảnh bằng chứng giao hàng() để tạo :BangChungGiaoHang.
- **4.5.** Controller cập nhật các class: gọi 24. Đánh dấu trạng thái Giao thành công() tới :DonHang, gọi 25. Đánh dấu Đã giao hiện tại() tới :KienHang, và 26. Khép lại tiến trình hiện tại() tới :LoTrinh.
- **4.6.** Cuối cùng, Controller gửi thông điệp 27. Lưu trữ biến động vào cơ sở dữ liệu() xuống LogiFast DB / DAM.

### 3. Description for Diagram Agent 
Vẽ hệ thống tuần tự mức nghiệp vụ (Business-Level SD) với đầy đủ class: Actor, Boundary (:GiaoDienTaiXe), Controller (:VanChuyenController), Entities. Tham chiếu nội dung bảng trên: 100% messages là tiếng việt, tuần tự từ 1 đến 27. Messages đều phải không có tham số theo đúng yêu cầu môn học.
