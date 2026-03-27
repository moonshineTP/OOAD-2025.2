# Grading Rubric — Yêu cầu BTL.xlsx

Official quality thresholds for IT3120 BTL. Each item is a pass/fail checkpoint.

---

## Part I — Analysis (20 criteria)

| # | Criterion | Key check |
|---|-----------|-----------|
| 1 | Mô tả được môi trường ứng dụng | Describes the business environment and context |
| 2 | Mô tả cơ cấu tổ chức: phòng ban, chức vụ | Org structure, roles, departments identified |
| 3 | Tính cấp thiết: khó khăn→giải pháp, tiềm năng→lợi ích, giá trị | ≥5 expected values clearly articulated |
| 4 | Tập bảng đặc tả khái quát UC đủ các mục | All fields in brief spec table filled |
| 5 | Sơ đồ UC: tên CSD, tác nhân, đường biên, tên hệ thống | Naming conventions, boundary box, actor notation correct |
| 6 | Luồng sự kiện chi tiết cho TẤT CẢ UC, >2 hoạt động/kịch bản | No UC left without detailed flow; scenarios have >2 steps |
| 7 | Ước lượng UCP | Complete UCP table with final person-hours figure |
| 8 | Phân chia công việc: mỗi thành viên 1 CSD | Assignment table in report |
| 9 | ≥1 kịch bản chi tiết + sơ đồ đối tượng cho MỖI UC | Object diagram per UC matching a concrete scenario |
| 10 | Sơ đồ lớp lĩnh vực cho MỖI UC | Separate class diagram per use case |
| 11 | Sự khác biệt giữa các sơ đồ lớp của các UC khác nhau | Each class diagram has different/appropriate classes |
| 12 | **⚠️ Thuộc tính lớp: chỉ tên, CHƯA có kiểu dữ liệu và giới hạn truy cập** | Analysis phase only — name only, no `String`, no `+/-` |
| 13 | Quan hệ liên kết có tên + cơ số ở 2 đầu | All associations labeled, multiplicities at both ends |
| 14 | Sơ đồ đối tượng tương thích với sơ đồ lớp | Objects satisfy all class diagram constraints |
| 15 | Quy cách SSD: `:ClassName` gạch chân, chỉ tác nhân + hệ thống | Lifeline notation correct, no internal objects in SSD |
| 16 | Luồng thông điệp SSD tương thích với luồng sự kiện UC | Each SSD message traceable to a UC event flow step |
| 17 | ≥1 SSD/UC, SSD có >2 thông điệp gửi đi | Per-UC SSDs required, not trivial |
| 18 | Sơ đồ máy trạng thái: chuyển trạng thái gắn với UC và SSD | Transitions reference UC activities + SSD messages |
| 19 | **Ma trận CRUD: đủ UC và lớp lĩnh vực** | All UCs as rows, all domain classes as columns |
| 20 | **Giá trị CRUD gắn với hoạt động UC và SSD** | Each C/R/U/D traceable to a specific UC step |

---

## Part II — Design (20 mandatory + 5 bonus)

| # | Criterion | Key check |
|---|-----------|-----------|
| 1 | Sơ đồ tuần tự mức nghiệp vụ tương thích với SSD | Business sequence extends SSD with internal objects |
| 2 | Sơ đồ giao tiếp tương thích với sơ đồ tuần tự | Communication diagram shows same interactions |
| 3 | **Sơ đồ tuần tự mức thực tế: đủ giao diện VÀ CSDL** | Full stack: UI → Controller → Domain → DAM → DB |
| 4 | Sơ đồ lớp đã tăng cường: kiểu DL, truy cập, cơ số, ràng buộc | NOW add types, `+/-/#`, OCL notes |
| 5 | Thẻ CRC: Trách nhiệm gắn với thông điệp sơ đồ tuần tự | Each responsibility = a specific method call |
| 6 | Thẻ CRC: Các đối tác (Collaborators) | Other classes this class talks to |
| 7 | Thẻ CRC: Thuộc tính | Attributes with types now included |
| 8 | Ánh xạ CSDL bao quát hết lớp và thuộc tính | No class or attribute left unmapped |
| 9 | Có thể khôi phục cấu trúc đối tượng từ CSDL | Mapping is reversible — no information lost |
| 10 | Ghi nhớ các liên kết (FK) | All associations → FK or junction table |
| 11 | Tập bảng đặc tả CSDL quan hệ | Table spec per table: columns, types, PK, FK, constraints |
| 12 | Các lớp DAM | One DAM class per table with CRUD methods |
| 13 | Quy chuẩn giao diện: màu sắc, biểu tượng, thành phần chung | UI design system documented |
| 14 | Kịch bản sử dụng tương thích với UC spec và sơ đồ tương tác | UI scenario matches UC flow and sequence diagrams |
| 15 | Sơ đồ cấu trúc và điều hướng (IFML / navigation) | Window/screen navigation diagram |
| 16 | Sơ đồ điều hướng tương thích với sơ đồ tuần tự mức thực tế | Navigation flow aligns with real-level sequence diagram |
| 17 | Nguyên mẫu giao diện (wireframe) | Mockup screens per UC |
| 18 | Bảng phân cảnh theo kịch bản sử dụng | Storyboard showing screen transitions |
| 19 | Sơ đồ triển khai thành phẩm | Deployment diagram (hardware + software nodes) |
| 20 | Sử dụng đúng khái niệm trong đầu mục | Correct UML/OOAD terminology throughout |

### Bonus (điểm cộng)
| # | Criterion |
|---|-----------|
| +1 | Sơ đồ gói (package diagram) — modularize the system |
| +2 | Sơ đồ thành phần (component diagram) — architecture |
| +3 | Quan hệ xuất bản (manifest): artifact ↔ component |
| +4 | Ràng buộc OCL trên sơ đồ lớp đã tăng cường |
| +5 | Áp dụng mẫu kiến trúc hệ thống (MVC, Layered, Microservices, etc.) |

---

## Common Failure Modes (checklist before submission)

- [ ] Class attributes at analysis stage still have `:Type` → **remove types from domain model**
- [ ] One global class diagram instead of per-UC diagrams → **split by UC**
- [ ] SSD lifelines include internal objects (Controller, DAO) → **remove, keep actor + :System only**
- [ ] CRUD matrix missing → **add before submission**
- [ ] CRUD values not traceable → **annotate matrix cells with UC step numbers**
- [ ] State machine transitions not labeled with UC activity or SSD message → **add labels**
- [ ] Real-level sequence diagram missing DAM/DB lifelines → **add full stack**
- [ ] Navigation diagram not drawn → **required for all UCs**
- [ ] Object diagrams don't exist per UC → **one per UC minimum**
- [ ] Association multiplicities missing at one end → **both ends required**

---

## Ricons Status Tracker

| # | Criterion | Status |
|---|-----------|--------|
| I.1 | Environment | ✅ Done (Ricons.docx Ch.1) |
| I.2 | Org structure | ✅ Done |
| I.3 | Urgency + values | ✅ Done |
| I.4 | UC brief specs | ✅ Done (5 UCs) |
| I.5 | UC diagram | ✅ Done |
| I.6 | Detailed event flows | ✅ Done (all 5) |
| I.7 | UCP | ✅ Done (UCP≈68.5, ~1919h) |
| I.8 | Task division | ✅ Done |
| I.9 | Per-UC object diagram | 🔄 Scenarios + object tables ready (docs/structural-modeling-prep.md Part C) |
| I.10 | Per-UC class diagram | 🔄 Class sets defined per UC (docs/structural-modeling-prep.md Part D) |
| I.11 | Class diagram differences | 🔄 Verified unique classes per UC (Part D table) |
| I.12 | Attribute names only | ✅ Rule enforced in vocabulary (docs/environment.md Sec 5) |
| I.13 | Named associations + multiplicities | ⬜ Not yet |
| I.14 | Object↔class compatibility | ⬜ Not yet |
| I.15 | SSD conventions | ⬜ Not yet |
| I.16 | SSD↔UC flow compatibility | ⬜ Not yet |
| I.17 | Per-UC SSD | ⬜ Not yet |
| I.18 | State machine (DonHang) | ⬜ Not yet |
| I.19 | CRUD matrix | ⬜ Not yet |
| I.20 | CRUD↔UC/SSD linkage | ⬜ Not yet |
| II.1–20 | Design phase | ⬜ Future |
| II.+1–5 | Bonus | ⬜ Future |
