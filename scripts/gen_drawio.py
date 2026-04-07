"""Generate clean draw.io XML for UC-03 diagrams (no XML comments, html=1 everywhere)."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.join(os.path.dirname(__file__), '..', 'Project', 'Diagrams')

# ── helpers ─────────────────────────────────────────────────────────────────

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

def mxfile_wrap(diagram_xml):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<mxfile host="app.diagrams.net" version="29.6.6">\n'
            + diagram_xml +
            '\n</mxfile>\n')

def diagram_wrap(name, did, model_xml):
    return (f'  <diagram name="{name}" id="{did}">\n'
            f'{model_xml}\n'
            f'  </diagram>')

def model_wrap(cells, pw=1654, ph=1169):
    inner = '\n'.join(f'        {c}' for c in cells)
    return (f'    <mxGraphModel dx="1600" dy="900" grid="1" gridSize="10" guides="1" '
            f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            f'pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">\n'
            f'      <root>\n'
            f'        <mxCell id="0"/>\n'
            f'        <mxCell id="1" parent="0"/>\n'
            f'{inner}\n'
            f'      </root>\n'
            f'    </mxGraphModel>')

def cell(cid, val, style, x, y, w, h, parent='1', extra=''):
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'vertex="1" parent="{parent}" {extra}>'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
            f'</mxCell>')

def edgecell(cid, val, style, src, tgt, parent='1', pts=None):
    if pts:
        pts_xml = (''.join(f'<mxPoint x="{p[0]}" y="{p[1]}"/>' for p in pts))
        geo = f'<mxGeometry relative="1" as="geometry"><Array as="points">{pts_xml}</Array></mxGeometry>'
    else:
        geo = '<mxGeometry relative="1" as="geometry"/>'
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'edge="1" source="{src}" target="{tgt}" parent="{parent}">'
            f'{geo}</mxCell>')

def arrow(cid, val, style, x1, y1, x2, y2, parent='1'):
    geo = (f'<mxGeometry relative="1" as="geometry">'
           f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
           f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/>'
           f'</mxGeometry>')
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'edge="1" parent="{parent}">'
            f'{geo}</mxCell>')

# ── Styles ────────────────────────────────────────────────────────────────────
OBJ_SW   = 'swimlane;html=1;startSize=28;fontStyle=4;fontSize=12;fillColor=#D5E8D4;strokeColor=#82B366;'
OBJ_TXT  = 'text;html=1;align=left;verticalAlign=top;spacingLeft=4;fontSize=10;strokeColor=none;fillColor=none;'
CLS_SW   = 'swimlane;html=1;startSize=28;fontStyle=1;fontSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;'
CLS_ABS  = 'swimlane;html=1;startSize=28;fontStyle=3;fontSize=12;fillColor=#DAE8FC;strokeColor=#6C8EBF;'
CLS_TXT  = 'text;html=1;align=left;verticalAlign=top;spacingLeft=4;fontSize=10;strokeColor=none;fillColor=none;'
NOTE_ST  = ('shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;'
            'fillColor=#FFF9C4;strokeColor=#D6B656;align=left;verticalAlign=top;size=14;')
WARN_ST  = ('shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;fontSize=10;fontStyle=1;'
            'fillColor=#FFE6CC;strokeColor=#D79B00;align=left;verticalAlign=top;size=14;')
ASSOC    = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#333333;fontSize=10;'
COMP     = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;startArrow=diamondThin;startFill=1;strokeColor=#333333;fontSize=10;'
INH      = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=block;endFill=0;strokeColor=#6C8EBF;fontSize=10;'
OBJ_E    = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=none;strokeColor=#82B366;fontSize=10;'
MSG_OUT  = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=open;endFill=1;strokeColor=#333333;fontSize=11;'
MSG_RET  = 'edgeStyle=orthogonalEdgeStyle;html=1;endArrow=open;endFill=0;dashed=1;strokeColor=#333333;fontSize=11;'
LIFE_ST  = 'endArrow=none;dashed=1;html=1;strokeColor=#333333;'
ACT_BOX  = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontStyle=1;fontSize=12;'
PHASE_ST = 'text;html=1;align=left;verticalAlign=middle;fontSize=11;fontStyle=1;strokeColor=#CCCCCC;fillColor=#F5F5F5;'
TITLE_ST = 'text;html=1;align=center;verticalAlign=middle;fontSize=12;fontStyle=1;strokeColor=none;fillColor=none;'

def obj_box(cid, inst, cls_, attrs, x, y, w):
    rows = len(attrs)
    hbody = max(rows * 16 + 6, 30)
    htot = 28 + hbody
    hdr = cell(cid, f'{inst} : {cls_}', OBJ_SW, x, y, w, htot)
    body_val = '\n'.join(f'{k} = "{v}"' for k, v in attrs)
    bdy = cell(f'{cid}_b', body_val, OBJ_TXT, 0, 28, w, hbody, parent=cid)
    return [hdr, bdy], htot

def cls_box(cid, name, attrs, x, y, w, abstract=False):
    rows = len(attrs)
    hbody = max(rows * 16 + 6, 22)
    htot = 28 + hbody
    st = CLS_ABS if abstract else CLS_SW
    lbl = f'<i>{name}</i>' if abstract else name
    hdr = cell(cid, lbl, st, x, y, w, htot)
    body_val = '\n'.join(attrs) if attrs else '(kế thừa ThongBao)'
    bdy = cell(f'{cid}_b', body_val, CLS_TXT, 0, 28, w, hbody, parent=cid)
    return [hdr, bdy], htot


# ═══════════════════════════════════════════════════════════════════════════
# OBJECT DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════
c = []
c.append(cell('ttl',
    '<b>Sơ đồ đối tượng — UC-03: Vận chuyển đơn hàng</b><br>'
    '<b>Kịch bản:</b> TX-001 Trần Minh Khoa giao ORD-2026-001 — tái định tuyến giữa hành trình<br>'
    '26/03/2026 — Luồng sự kiện chính (UC-03 kết thúc tại điểm giao → kích hoạt UC-04)',
    TITLE_ST, 160, 20, 1300, 60))

# Row 1
r1,H1 = obj_box('cd1','cd1','ChuyenDi',[
    ('maChuyenDi','CD-2026-0326-T1'),
    ('thoiGianBatDau','2026-03-26T09:28:00'),
    ('thoiGianKetThuc','2026-03-26T10:10:00')], 60, 110, 290)
r2,H2 = obj_box('tx1','tx1','TaiXe',[
    ('maTaiXe','TX-001'),
    ('ten','Trần Minh Khoa'),
    ('soDienThoai','0912345678'),
    ('trangThai','Đang giao hàng'),
    ('viTriHienTai','10.7525, 106.6624')], 410, 110, 310)
r3,H3 = obj_box('lt1','lt1','LoTrinh',[
    ('maLoTrinh','LT-2026-001'),
    ('diemXuatPhat','KHO-SGN-01'),
    ('diemDen','123 Nguyễn Văn Cừ, Q.5'),
    ('khoangCach','9.2 km'),
    ('/thoiGianDuKien','35 phút'),
    ('trangThai','Hoàn tất')], 790, 110, 320)
Y2 = 110 + max(H1,H2,H3) + 50

r4,H4 = obj_box('dh1','dh1','DonHang',[
    ('maDonHang','ORD-2026-001'),
    ('trangThai','Chờ xác nhận'),
    ('diaChiGiao','123 Nguyễn Văn Cừ, Q.5'),
    ('tongGiaTri','8.500.000 VND'),
    ('hinhThucThanhToan','COD')], 60, Y2, 320)
r5,H5 = obj_box('kp1','kh_pkg1','KienHang',[
    ('maKienHang','KH-PKG-001'),
    ('maQR','QR-ORD-2026-001'),
    ('khoiLuong','0.35 kg'),
    ('trangThai','Đang xác nhận')], 450, Y2, 300)
r6,H6 = obj_box('gps1','gps1','ViTriGPS',[
    ('maViTri','GPS-TX001-1006'),
    ('viDo','10.7525'),
    ('kinhDo','106.6624'),
    ('thoiGian','2026-03-26T10:06:00')], 820, Y2, 300)
Y3 = Y2 + max(H4,H5,H6) + 50

r7,H7 = obj_box('sc1','sc1','SuCoGiaoThong',[
    ('maSuCo','SC-2026-001'),
    ('loaiSuCo','Ùn tắc giao thông'),
    ('thoiGianPhatHien','2026-03-26T09:45:00'),
    ('toaDo','Vành đai 2, Q.8')], 60, Y3, 330)
r8,H8 = obj_box('tb1','tb1','ThongBaoSuCoGiaoThong',[
    ('maThongBao','TB-UC03-001'),
    ('noiDung','Shipper đang đến, ETA 2 phút'),
    ('thoiGianGui','2026-03-26T10:04:00'),
    ('kenhGui','App + SMS')], 470, Y3, 380)

for row in [r1,r2,r3,r4,r5,r6,r7,r8]:
    c.extend(row)

# Scenario note
c.append(cell('note_sc',
    '<b>Diễn biến kịch bản:</b><br>'
    '09:28 — TX-001 bắt đầu ca, ChuyenDi cd1 được tạo<br>'
    '09:30 — Quét QR "QR-ORD-2026-001", xác nhận KienHang<br>'
    '09:31 — batDauGiaoHang → tạo LoTrinh lt1 (9.2 km, ETA 35 phút)<br>'
    '09:31–10:04 — GPS ghi nhận mỗi 30 giây → nhiều ViTriGPS<br>'
    '09:45 — Hệ thống phát hiện SuCoGiaoThong sc1; điều phối tái định tuyến<br>'
    '10:04 — DonHang gần đến → ThongBaoSuCoGiaoThong tb1 gửi cho khách<br>'
    '10:06 — xacNhanDaDenDiemGiao → UC-03 kết thúc<br>'
    '→ DonHang.trangThai = "Chờ xác nhận" → kích hoạt UC-04',
    NOTE_ST, 875, Y3, 420, 168))

# Links
for eid, lbl, src, tgt in [
    ('e1','bao gồm','cd1','lt1'),
    ('e2','thực hiện','tx1','lt1'),
    ('e3','giao','lt1','dh1'),
    ('e4','ghi nhận','lt1','gps1'),
    ('e5','chứa','dh1','kp1'),
    ('e6','gặp sự cố','lt1','sc1'),
    ('e7','kích hoạt thông báo','dh1','tb1'),
]:
    c.append(edgecell(eid, lbl, OBJ_E, src, tgt))

xml_obj = mxfile_wrap(diagram_wrap('UC03 Object Diagram','uc03-obj',
                                    model_wrap(c)))
path = os.path.join(BASE, 'UC03_ObjectDiagram.drawio')
with open(path, 'w', encoding='utf-8') as f:
    f.write(xml_obj)
print(f'Object diagram: {len(xml_obj)} chars → {path}')


# ═══════════════════════════════════════════════════════════════════════════
# CLASS DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════
c = []
c.append(cell('ttl',
    '<b>Sơ đồ lớp lĩnh vực — UC-03: Vận chuyển đơn hàng</b><br>'
    'Hệ thống Quản lý Giao hàng LogiFast<br>'
    '<i>Giai đoạn phân tích — thuộc tính chỉ ghi tên, không kiểu dữ liệu, không ký hiệu truy cập</i>',
    TITLE_ST, 160, 20, 1000, 60))

# Row 1
r1,C1 = cls_box('ChuyenDi','ChuyenDi',
    ['maChuyenDi','thoiGianBatDau','thoiGianKetThuc'], 60, 110, 230)
r2,C2 = cls_box('TaiXe','TaiXe',
    ['maTaiXe','ten','soDienThoai','trangThai','viTriHienTai'], 340, 110, 220)
r3,C3 = cls_box('LoTrinh','LoTrinh',
    ['maLoTrinh','diemXuatPhat','diemDen','khoangCach','/thoiGianDuKien','trangThai'],
    620, 110, 240)

CY2 = 110 + max(C1,C2,C3) + 60
r4,C4 = cls_box('DonHang','DonHang',
    ['maDonHang','trangThai','diaChiGiao','tongGiaTri','hinhThucThanhToan','thoiGianDat'],
    60, CY2, 250)
r5,C5 = cls_box('KienHang','KienHang',
    ['maKienHang','maQR','khoiLuong','trangThai'], 370, CY2, 220)
r6,C6 = cls_box('ViTriGPS','ViTriGPS',
    ['maViTri','viDo','kinhDo','thoiGian'], 650, CY2, 220)

CY3 = CY2 + max(C4,C5,C6) + 60
r7,C7 = cls_box('SuCoGiaoThong','SuCoGiaoThong',
    ['maSuCo','loaiSuCo','thoiGianPhatHien','toaDo'], 60, CY3, 250)
r8,C8 = cls_box('ThongBao','ThongBao',
    ['maThongBao','noiDung','thoiGianGui','kenhGui'], 380, CY3, 230, abstract=True)
r9,C9 = cls_box('ThongBaoSCGT','ThongBaoSuCoGiaoThong',
    [], 680, CY3, 270)

for row in [r1,r2,r3,r4,r5,r6,r7,r8,r9]:
    c.extend(row)

# Notes
for nid, txt, x, y, w, h in [
    ('n1','trangThai trong UC-03:<br>"Đang giao hàng"', 950, 115, 200, 40),
    ('n3','/thoiGianDuKien: thuộc tính suy diễn<br>Tái định tuyến khi gặp SuCoGiaoThong', 950, 160, 230, 44),
    ('n4','trangThai → "Chờ xác nhận"<br>(kết thúc UC-03)', -220, CY2+5, 220, 40),
    ('n5','trangThai: "Đang vận chuyển"<br>→ "Đang xác nhận"', 950, CY2+5, 220, 40),
    ('n6','Ghi nhận mỗi 30 giây<br>bởi Hệ thống theo dõi GPS', 950, CY2+C5//2, 200, 40),
    ('n7','Phát hiện bởi Hệ thống theo dõi<br>Kích hoạt điều phối tái định tuyến', -240, CY3+5, 230, 44),
    ('n9','Gửi cho khách khi ETA ≤ 2 phút', 960, CY3+5, 200, 36),
]:
    c.append(cell(nid, txt, NOTE_ST, x, y, w, h))

# Associations (multiplicity embedded in label)
for aid, src, tgt, lbl, st in [
    ('a1','ChuyenDi','LoTrinh','1 ─── bao gồm ─── 1..*', ASSOC),
    ('a2','TaiXe','LoTrinh','1 ─── thực hiện ─── 0..*', ASSOC),
    ('a3','LoTrinh','DonHang','1..* ─── giao ─── 1', ASSOC),
    ('a4','LoTrinh','ViTriGPS','1 ◆─── ghi nhận ─── 1..*', COMP),
    ('a5','DonHang','KienHang','1 ◆─── chứa ─── 1..*', COMP),
    ('a6','LoTrinh','SuCoGiaoThong','1 ─── gặp sự cố ─── 0..*', ASSOC),
    ('a7','DonHang','ThongBaoSCGT','1 ─── kích hoạt thông báo ─── 0..*', ASSOC),
]:
    c.append(edgecell(aid, lbl, st, src, tgt))

# Inheritance
c.append(edgecell('inh1','', INH, 'ThongBaoSCGT', 'ThongBao'))

xml_cls = mxfile_wrap(diagram_wrap('UC03 Class Diagram','uc03-cls',
                                    model_wrap(c)))
path = os.path.join(BASE, 'UC03_ClassDiagram.drawio')
with open(path, 'w', encoding='utf-8') as f:
    f.write(xml_cls)
print(f'Class diagram: {len(xml_cls)} chars → {path}')


# ═══════════════════════════════════════════════════════════════════════════
# SSD
# ═══════════════════════════════════════════════════════════════════════════
c = []
c.append(cell('ttl',
    '<b>Sơ đồ tuần tự mức hệ thống (SSD) — UC-03: Vận chuyển đơn hàng</b><br>'
    'Hệ thống Quản lý Giao hàng LogiFast<br>'
    '<i>Chỉ 2 lifeline: Tác nhân + :Hệ thống — UC-03 kết thúc tại điểm giao, không tạo bằng chứng</i>',
    TITLE_ST, 80, 20, 1000, 60))

AX, SX = 200, 780

# Lifeline headers
c.append(cell('actor_h','Tài xế<br>giao hàng',
    'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;',
    AX-25, 95, 50, 80))
c.append(cell('sys_h',':Hệ Thống LogiFast', ACT_BOX, SX-110, 105, 220, 50))

# Lifeline lines
c.append(arrow('al','', LIFE_ST, AX, 175, AX, 1520))
c.append(arrow('sl','', LIFE_ST + 'strokeColor=#6C8EBF;', SX, 155, SX, 1520))

def phase_bar(pid, txt, y):
    return cell(pid, txt, PHASE_ST, 100, y, 900, 26)

def msg_arrow(mid, lbl, y, ret=False):
    if ret:
        return arrow(mid, lbl, MSG_RET, SX, y, AX, y)
    else:
        return arrow(mid, lbl, MSG_OUT, AX, y, SX, y)

def side_note(nid, txt, y, h=40):
    return cell(nid, txt, NOTE_ST, SX+15, y, 235, h)

# ── Bước 1
c.append(phase_bar('p1','Bước 1: Bắt đầu ca làm việc', 200))
c.append(msg_arrow('m1','xacNhanBatDauCa(maTaiXe)', 236))
c.append(side_note('n1','Tạo ChuyenDi mới', 223, 28))
c.append(msg_arrow('m1r','xacNhanChuyenDi(maChuyenDi, danhSachDon)', 296, ret=True))
c.append(side_note('n1r','Trả danh sách đơn cần giao trong ca', 283, 28))

# ── Bước 2
c.append(phase_bar('p2','Bước 2: Xác nhận lấy hàng tại kho', 360))
c.append(msg_arrow('m2','quetMaQR(maQR)', 396))
c.append(side_note('n2','Quét mã QR trên kiện hàng', 383, 28))
c.append(msg_arrow('m2r','xacNhanKienHang(tenSanPham, diaChiGiao)', 456, ret=True))
c.append(side_note('n2r','Xác định KienHang hợp lệ', 443, 28))

# ── Bước 3
c.append(phase_bar('p3','Bước 3: Bắt đầu giao hàng', 520))
c.append(msg_arrow('m3','batDauGiaoHang(maDonHang)', 556))
c.append(side_note('n3','DonHang.trangThai → "Đang giao hàng"', 543, 28))
c.append(msg_arrow('m3r','hienThiLoTrinh(maLoTrinh, khoangCach, thoiGianDuKien)', 616, ret=True))
c.append(side_note('n3r','Tính LoTrinh tối ưu, trả ETA', 603, 28))

# ── Bước 4
c.append(phase_bar('p4','Bước 4: Tracking hành trình (loop mỗi 30 giây)', 680))
# Loop frame
c.append(cell('loop_f','loop [mỗi 30 giây]',
    'swimlane;html=1;startSize=20;fontStyle=1;fontSize=10;fillColor=none;strokeColor=#666666;align=left;spacingLeft=6;',
    100, 706, 760, 130))
# Inside loop — coordinates relative to loop_f
c.append(arrow('m4','capNhatViTriGPS(viDo, kinhDo)', MSG_OUT,
               100, 50, 680, 50, parent='loop_f'))
c.append(cell('n4','Ghi ViTriGPS mỗi 30 giây', NOTE_ST, 690, 38, 220, 28, parent='loop_f'))
c.append(arrow('m4r','ghiNhanThanhCong()', MSG_RET,
               680, 95, 100, 95, parent='loop_f'))
c.append(cell('n4r','ETA hiệu chỉnh liên tục', NOTE_ST, 690, 83, 220, 28, parent='loop_f'))

# Rerouting note
c.append(cell('re_n',
    '[Luồng phụ — tái định tuyến]<br>'
    'SuCoGiaoThong phát hiện bởi Hệ thống theo dõi →<br>'
    'Hệ thống điều phối tính lại LoTrinh nội bộ<br>'
    '(không có thông điệp mới ra actor)',
    NOTE_ST, 120, 858, 390, 68))

# ── Bước 5
c.append(phase_bar('p5','Bước 5: Xác nhận đến điểm giao — kết thúc UC-03', 944))
c.append(msg_arrow('m5','xacNhanDaDenDiemGiao(maDonHang)', 980))
c.append(side_note('n5','Tài xế đến điểm đến<br>DonHang.trangThai → "Chờ xác nhận"', 967, 40))
c.append(msg_arrow('m5r','xacNhanCoMat(maThongBao)', 1046, ret=True))
c.append(side_note('n5r',
    'ThongBaoSuCoGiaoThong gửi cho khách<br>HandoverStarted → kích hoạt UC-04',
    1033, 44))

c.append(cell('end_n',
    'UC-03 KẾT THÚC Ở ĐÂY<br>'
    'Việc chụp ảnh biên nhận và OTP<br>'
    'xử lý tại UC-04 (Xác nhận giao hàng)',
    WARN_ST, 500, 1120, 320, 66))

xml_ssd = mxfile_wrap(diagram_wrap('UC03 SSD','uc03-ssd',
                                    model_wrap(c, pw=1169, ph=1654)))
path = os.path.join(BASE, 'UC03_SSD.drawio')
with open(path, 'w', encoding='utf-8') as f:
    f.write(xml_ssd)
print(f'SSD: {len(xml_ssd)} chars → {path}')

print('All done.')
