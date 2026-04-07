# Week 30 Research — Mô hình hóa hành vi (Behavioral Modeling)

**Date**: 2026-04-07 | **Sources**: Bai-tap-lon-2023-2.docx, grading rubric, Ch04 pptx (Mô hình hóa hành vi), current project state

---

## 1. Week 30 Mission

Based on the lecture sequence (Ch04 pptx = behavioral modeling) and rubric criteria I.15–I.20, cùng với các đính chính quan trọng:

| # | Deliverable | Rubric | Where |
|---|------------|--------|-------|
| A | Sơ đồ máy trạng thái (DonHang, TaiXe, LoTrinh) | I.18 | Ch V §2 |
| B | SSD mức Hệ thống (5 UCs) | I.15–I.17 | Ch V §3 |
| C | Sơ đồ giao tiếp (Mức hệ thống) + so sánh DFD | — | Ch V §4 |
| D | Ma trận CRUD(E) (5 UC × 21 classes) | I.19, I.20 | Ch V §5 |

> **Correction**: SSDs are NOT in Ch IV. Teacher's adjustment moves all behavioral diagrams to Ch V. CRC stays in Ch IV.

### Chapter content (from pptx slides 4/15/31/42):
- Sơ đồ máy trạng thái (slides 5–14)
- Các mô hình tương tác (Sơ đồ tuần tự và Sơ đồ giao tiếp)
- Kỹ thuật phát hiện quan hệ (Ma trận CRUD)

---

## 2. Terminology & Core Rules — Ch04 Standard 

### 2.1 Định dạng Thông điệp (Message Formatting)
- **Tham số (Parameters)**: KHÔNG CẦN THIẾT (Parameterless). Ở pha phân tích, chúng ta chỉ quan tâm đến *tương tác* giữa các đối tượng thay vì cấu trúc dữ liệu của thông điệp.
- **Ngôn ngữ**: Sử dụng tiếng Việt tự nhiên có dấu.
- **Thứ tự**: BẮT BUỘC đánh số thứ tự tuần tự.
- **Ví dụ Đúng**: 1. Yêu cầu lấy hàng(), 3. Gửi thông báo()
- **Ví dụ Sai**: yeuCauLayHang(maDon), guiThongBao()

### 2.2 Liên kết Hành vi - Cấu trúc (Behavioral - Structural Linkage)
Tồn tại một sự gắn kết chặt chẽ bắt buộc giữa sơ đồ Use Case, thẻ CRC và biểu đồ hành vi:
- Các **Tác nhân (Actors)** và **Hệ thống/Module tương tác** xuất hiện trong Use Case Diagram (như *Khách hàng, Tài xế, Hệ thống theo dõi, Hệ thống điều phối, v.v.*) PHẢI là các đường sống (lifelines) tương ứng trong sơ đồ tuần tự/giao tiếp.
- Các **Lớp (Classes)** đã định nghĩa trong thẻ CRC (Domain classes) PHẢI là các lớp nhận/gửi thông điệp trong biểu đồ mức nghiệp vụ kế tiếp.

### 2.3 Phân biệt Mức Hệ Thống (System Level) và Mức Nghiệp Vụ (Business/Design Level)
Đây là sai lầm dễ mắc phải nhất. Phải rạch ròi 2 mức:

**A. Mức Hệ Thống (System Level)** - *Trọng tâm của pha Phân tích (Ch V)*
- **SSD (System Sequence Diagram)**: Coi hệ thống (hoặc Module chính) là một "Hộp đen" (Black box). Đường sống chỉ bao gồm: **Actor** và **:System** (hoặc cụ thể hơn là :Module_Vận_chuyển, :Hệ_thống_điều_phối như trong biểu đồ Use Case).
- **Communication Diagram mức hệ thống**: Chỉ vẽ tương tác tổng quan giữa Actor và Hệ thống, có thể dùng để so sánh/ánh xạ trực tiếp với DFD (Data Flow Diagram) mức ngữ cảnh theo yêu cầu của GV. KHÔNG có các lớp bên trong.

**B. Mức Nghiệp Vụ / Thực Tế (Business/Real Level)** - *Trọng tâm của pha Thiết kế (Ch sau)*
- **Sequence Diagram mức nghiệp vụ**: Mở hộp đen ra. Đường sống sẽ bao gồm toàn bộ stack: Actor -> UI (Boundary) -> Controller (Control) -> Các lớp Domain (Từ thẻ CRC) -> DAM -> DB.
- **Communication Diagram mức nghiệp vụ**: Thể hiện các đối tượng (như DonHang, TaiXe...) giao tiếp với nhau như thế nào.

---

## 3. Sơ đồ máy trạng thái (State Machine Diagram)

| Vietnamese | UML term | Notation |
|-----------|----------|----------|
| Trạng thái | State | Rounded rectangle |
| Chuyển trạng thái | Transition | sự_kiện [điều_kiện] / hành_động |

**Rule I.18**: Các Action/Trigger trên bước chuyển trạng thái phải map 1-1 với dòng thông điệp đánh số trên SSD (VD: trigger của trạng thái phải tương ứng với thông điệp 3. Gửi thông báo()).

---

## 4. Trọng tâm Ma trận CRUD

| Value | Meaning |
|-------|---------|
| C | Tạo mới (Create/Add) |
| R | Đọc/Truy vấn (Read/View) |
| U | Cập nhật (Update/Modify) |
| D | Xóa (Delete/Remove) |
| E | Thực thi (Execute - VD: Thanh toán, Thuật toán) |

**Rules I.19 + I.20**: Rows = 5 UCs; Columns = all classes từ CRC; Từng ô phải map về Step cụ thể của CSD.
