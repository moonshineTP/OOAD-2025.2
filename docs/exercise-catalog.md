# Exercise Catalog — IT3120 OOAD

Full problem statements for all in-class exercises.

---

## File: bai-tap-mo-hinh-hoa-du-lieu.docx

### Bài 1 — Vẽ sơ đồ lớp (Auto-Service System)

**Domain**: Company T provides car care services.

**Class specifications**:
- `Owner`: name, address
- `Vehicle`: vin, model, year (abstract parent)
  - `Car` extends Vehicle: door_num, segment
  - `Truck` extends Vehicle: load
- `Manufacturer`: name, location
- `Dealer` (service branch): name, address
- `Service` (**association class** linking Vehicle and Dealer): date, odo
  - `Warranty` extends Service: eligibility
- `ServiceType`: description, cost
- `Part`: description, unit_cost

**Relationships**:
- Owner ↔ Vehicle: M:N (owner has many vehicles; vehicle has many owners)
- Vehicle → Manufacturer: M:1 (vehicle has exactly 1 manufacturer; manufacturer has many vehicles)
- Vehicle ↔ Dealer: M:N via **Service** (vehicle serviced at many branches; branch serves many vehicles)
- Service → ServiceType: M:1 (each service belongs to 1 service type)
- ServiceType ↔ Part: M:N (service type uses 0..*  parts; part used in 1..* service types)

**Business rule**: Owner and vehicle only enter the system on first service visit at any branch.
**Cost rule**: Service cost = sum of part costs; if no parts → free service.

**Goal**: Test class diagram notation, relationships, multiplicities.

---

### Bài 2 — Vẽ sơ đồ đối tượng (Instance Data)

**Use the model from Bài 1.** Create objects for this scenario:

On 1/4/2025, teacher Nguyễn Bá Ngọc (address: Thanh Sơn–Phú Thọ) had an oil change for his car at Gara Sơn Thủy (128 Trần Đại Nghĩa).
- Car brand: Volga (Russian manufacturer)
- Model: GAS-3155, year 2020, VIN: *3155*5889999*, 4 doors, economy segment
- Service: oil change, 60,000 km odometer, date 1/4/2025
- Cost: 2,000,000 VND total:
  - 1,800,000 VND for 10L Genesis premium oil (Part)
  - 200,000 VND labor (Part)
- This is a voluntary service (not warranty)

**Goal**: Test object diagram notation and constraint satisfaction.

---

## File: BaiTap-PhanTich-ThietKe.docx

### Bài 1 — Sơ đồ hoạt động (Activity Diagram — Order Processing)

**Domain**: Company shipping department manages order fulfillment.

**Process**: When an order arrives, staff sends copies of a packing slip to:
1. **Sales dept** → update order status
2. **Accounting dept** → handle payment procedures
3. **Customer** → confirm on receipt

Accounting notifies Sales after payment. Customer sends confirmation after receipt. Sales updates order to "Paid" and "Received" after both notifications.

**Requirement**: Draw an activity diagram with **swimlanes** for each party. May add information.

---

### Bài 2 — Phân tích hệ thống giám sát vi phạm giao thông

**Domain**: Traffic violation monitoring system with 4 subsystems:
1. **Violation records subsystem**: logs violations, tracks fines, sends to court if unpaid
2. **Accident records subsystem**: logs accident info + insurance parties
3. **Insurance summary subsystem**: combines violation + accident data → sends to insurers
4. **License management subsystem**: issues, restores, or revokes driver licenses

**Process details**:
- Traffic officer creates violation record → owner/officer/court relations established in DB
- If driver admits guilt → pre-filled envelope sent with violation code
- If driver contests: marked X on return envelope → system records hearing request + sends detail report to court + sends scheduling survey to driver
- Court schedules hearing → notifies driver
- After hearing: court sends verdict → if innocent, violation cancelled for insurer; if guilty, another envelope sent for fine payment
- Non-payment within 2 weeks → warning to court → court may revoke license

**Requirements**:
1. List all events the system must respond to. Classify each event. Identify corresponding UC. (Consider: does the officer directly enter data or does office staff enter it?)
2. Draw overall UC diagram
3. Brief UC specifications

---

### Bài 3 — Mô hình hóa cấu trúc hệ thống quản lý dịch vụ ô tô

**Same domain as Bài 1 data modeling** (Company T car services), with added `id` fields for ServiceType and Part.

**Requirements**:
1. Draw class diagram with relationship names and multiplicities
2. Create objects and object diagram for the oil change scenario (1/4/2024, teacher Ngọc, Gara Sơn Thủy)
3. Identify state chains for a vehicle from the company's perspective. Draw a state machine.

---

### Bài 4 — Đặc tả chi tiết ca sử dụng (Insurance Policy)

**UC**: Add vehicle to existing insurance policy

**Scenario**: Customer calls insurance company staff, provides policy code. Staff enters code → system shows policy info → staff verifies coverage is paid and policy is active. Customer provides vehicle make/model/year/VIN. Staff enters → system validates. Customer selects coverage types and amounts per coverage. Staff enters → system validates amounts within policy limits. After all coverages entered, system checks total (including other vehicles in policy) against thresholds. Customer must confirm all drivers and their driving time percentages. If new driver added → invoke "Add driver" UC. System updates policy, calculates new premium, prints updated policy, sends to policyholder.

**Requirements**:
a. Detailed UC specification (may add information)
b. Activity diagram for main flow

---

### Bài 5 — SSD (for Bài 4)

Draw a **System Sequence Diagram** for the main flow described in Bài 4.

---

### Bài 6 — Mô hình hóa tổng hợp (Havelt Used Books)

**Domain**: Havelt — internet company connecting used book sellers and buyers.

**Seller side**: Must register (address, phone, email). Login via secure portal. Lists books via form (category, condition, price). Unlimited listings. System maintains search index.

**Buyer side**: Browses and searches (by title, author, category, keyword). Decides to buy → opens account with credit card. After payment: Havelt emails all selected sellers + marks books sold. Order stays "open" until shipment confirmed. Seller must notify buyer within 48h. Must ship within 24h after notification. Seller notifies buyer + Havelt after shipping.

**Monthly reconciliation**: After 30 days in "shipping" status → list sent to sellers for verification (allows dispute if buyer didn't receive or book condition different). Buyer can optionally rate seller.

**Requirements**:
- Domain class diagram (domain model)
- UC list + UC diagram
- Detailed spec for 2 UCs: "Register Seller" + "Create Book Purchase Order"
- SSDs for both specified UCs
- Business-level sequence diagrams for both

---

### Bài 7 — UC diagram: Hệ thống quản lý đào tạo

Refer to the university education management system students currently use. Draw an overall UC diagram. Based on personal experience, specify the "Đăng ký học phần" (course registration) UC.

---

### Bài 8 — UC diagram: Phòng khám riêng

**Domain**: Private doctor's clinic system.

New patient fills form (name, address, phone, brief medical info) → stored in patient record. When patient calls to make/change appointment → receptionist checks schedule → if slot found, appointment created → if new patient, temporary record created (some fields blank, filled when they arrive). Appointments often made far in advance → receptionist sends email reminder 1 week before.

**Requirement**: Draw overall UC diagram.

---

### Bài 9 — UC diagram: Công ty bất động sản R

**Domain**: Real estate company R.

- Home seller signs contract + provides property info → stored in R's DB + distributed to city real estate network
- Two buyer types:
  1. Interested in specific house → R exports info from DB → agent uses to show property (out of scope)
  2. Needs help finding a house → buyer fills preference form → data entered to buyer DB → agent searches R's DB for matches → results exported to help agent present options

**Requirement**: Draw UC diagram.

---

### Bài 10 — Xác định đối tượng từ phiếu xuất kho

Given a warehouse issue slip (hình in document).

**Requirements**:
a. Identify objects representing data in the slip → draw object diagram
b. Draw class diagram

---

### Bài 11 — Thiết kế lớp (Coupling Analysis)

Given a problematic class design (diagram in document).

**Requirements**: Analyze coupling problems. Sketch a solution achieving loose coupling between components. Draw class diagram + sequence diagram.

---

### Bài 12 — Thiết kế lưu trữ cố định (Persistent Storage)

Given a domain model (diagram in document).

**Requirements**: Identify information to persist. Map to relational DB. Design DB + sketch DAM classes.

**Reference mapping table from solution**:
| Lớp lĩnh vực | Lớp DAM | Bảng CSDL |
|---|---|---|
| TaiKhoan | TaiKhoanDAM | TaiKhoan(id, so_du) |
| DanhMuc | DanhMucDAM | DanhMuc(id, gd_id, tk_id, gia_tri) |
| GiaoDich | GiaoDichDAM | GiaoDich(id, mo_ta, kh_id) |
| KhachHang | KhachHangDAM | KhachHang(id, ten, type) |
| CaNhan | CaNhanDAM | CaNhan(kh_id, CMT) |
| ToChuc | ToChucDAM | ToChuc(kh_id, DK) |

---

### Bài 13 — Hệ thống chăm sóc khách hàng CRM

**User stories**:
- Salesperson: manage contact list (name, email, phone)
- Salesperson: record actions/interactions (call/email, timestamp, notes) per contact
- Salesperson: manage company list (name)
- Salesperson: associate contacts with companies
- Salesperson: manage own contact info (name, email) visible to team
- *Extra*: maintain industry list; associate companies with industries (1 or more)

**Requirements**:
a. Identify domain classes → draw domain class diagram
b. Detailed class design + DB design

---

### Bài 14 — Tacostagram (Social Network Class Diagram)

**User stories** (all features):
- Create timestamped taco posts → shared on timeline
- Like other users' posts (only once per post)
- View like count on posts
- Comment on posts (and view others' comments)
- Follow other users
- Timeline shows only posts from followed users
- Register with: username (display name), real name, location

**Requirement**: Identify domain classes → draw class diagram with attributes, associations, labels, multiplicities.

---

### Bài 15 — SSD (Customer Management UC)

**UC flow** (given):
- Main flow: Employee selects customer management → chooses Add/Find/List
  - S-1 (Add): system asks → employee fills form → submits → system validates + saves → notifies success
  - S-2 (Find): system asks → employee enters search → system finds → if 1 result: show details; else: run S-3
  - S-3 (List): show list → employee selects → show details → back to list

**Requirement**: Draw SSD showing user↔system interactions.

---

### Bài 16 — Phân tích sự kiện hệ thống bán hàng trực tuyến

**User journey of Nguyễn Văn A (NVA)**:
1. Receives birthday money from grandmother
2. Wants a new tablet
3. Browses tablets on e-commerce website
4. Browses computer components on same site
5. Reads product reviews
6. Places order for a tablet
7. Pays online
8. Receives package from delivery person
9. Transfers remaining money to savings

**Requirements**:
a. Identify which events the analyst needs to study for the online sales system. Explain why (which involve the system boundary).
b. Sketch functional model: define actors + UC list with brief descriptions
c. Draw overall UC diagram consistent with (b)

**Hint**: Events 1, 9 are outside system scope. Events 4 (component browsing) may or may not be in scope depending on whether the site sells components. Focus on events 3, 5, 6, 7, 8 as primary system events.
