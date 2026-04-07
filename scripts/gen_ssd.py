"""Generate System Sequence Diagram (SSD) for UC-03 with 5 lifelines and 16 messages."""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

OUT = os.path.join(os.path.dirname(__file__), '..', 'Project', 'Diagrams', 'UC03_SSD_system.drawio')

# ── Helpers ─────────────────────────────────────────────────────────────────

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

def wrap(diagram_xml):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36">\n'
            + diagram_xml +
            '\n</mxfile>\n')

def diagram(name, did, model_xml):
    return (f'  <diagram name="{name}" id="{did}">\n'
            f'{model_xml}\n'
            f'  </diagram>')

def model(cells, pw=1654, ph=2000):
    inner = '\n'.join(f'        {c}' for c in cells)
    return (f'    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" '
            f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            f'pageWidth="{pw}" pageHeight="{ph}" math="0" shadow="0">\n'
            f'      <root>\n'
            f'        <mxCell id="0"/>\n'
            f'        <mxCell id="1" parent="0"/>\n'
            f'{inner}\n'
            f'      </root>\n'
            f'    </mxGraphModel>')

def cell(cid, val, style, x, y, w, h, parent='1'):
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'vertex="1" parent="{parent}">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
            f'</mxCell>')

def edge(cid, val, style, x1, y1, x2, y2, parent='1', label_y=0):
    geo = (f'<mxGeometry relative="1" as="geometry">'
           f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
           f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/>')
    if label_y != 0:
        geo += f'<mxPoint y="{label_y}" as="offset"/>'
    geo += '</mxGeometry>'
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'edge="1" parent="{parent}">'
            f'{geo}</mxCell>')

def swimlane(cid, val, x, y, w, h, parent='1'):
    """Create a swimlane (loop/alt box)."""
    style = 'swimlane;html=1;startSize=20;fillColor=#F5F5F5;strokeColor=#666666;fontSize=11;fontStyle=1;'
    return (f'<mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'vertex="1" parent="{parent}">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
            f'</mxCell>')

# ── Styles ──────────────────────────────────────────────────────────────────
ACTOR_STYLE = 'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=14;'
SYSTEM_STYLE = 'rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontStyle=1;fontSize=16;'
LIFELINE_STYLE = 'endArrow=none;dashed=1;html=1;strokeColor=#333333;'
MSG_STYLE = 'edgeStyle=none;html=1;endArrow=block;endFill=1;strokeColor=#333333;fontSize=12;'
RETURN_STYLE = 'edgeStyle=none;html=1;endArrow=open;endFill=0;dashed=1;strokeColor=#333333;fontSize=12;'
ACTIVATION_STYLE = 'rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;'

# ── Layout Configuration ────────────────────────────────────────────────────
# X positions for each lifeline
X_KHACHHANG = 80
X_TAIXE = 300
X_SYSTEM = 550
X_DIEUPHOI = 850
X_THEODOI = 1100

# Y positions
Y_ACTOR_TOP = 40
Y_LIFELINE_START = 150
Y_MSG_GAP = 60  # vertical spacing between messages
Y_LOOP_START = 580  # where loop box starts (message 7)
Y_LOOP_END = 640   # where loop box ends
Y_ALT_START = 680   # where alt box starts (message 8)
Y_ALT_END = 900     # where alt box ends (message 11)
Y_LIFELINE_END = 1700

# ── Generate Diagram ────────────────────────────────────────────────────────

def generate_ssd():
    cells = []
    cell_id = 100
    
    # === Actors/Lifelines ===
    
    # 1. Khách hàng (leftmost)
    cells.append(cell(f'actor_kh', 'Khách hàng', ACTOR_STYLE, X_KHACHHANG-25, Y_ACTOR_TOP, 50, 95, '1'))
    cells.append(edge(f'll_kh', '', LIFELINE_STYLE, X_KHACHHANG, Y_LIFELINE_START, X_KHACHHANG, Y_LIFELINE_END, '1'))
    
    # 2. Tài xế
    cells.append(cell(f'actor_tx', 'Tài xế', ACTOR_STYLE, X_TAIXE-25, Y_ACTOR_TOP, 50, 95, '1'))
    cells.append(edge(f'll_tx', '', LIFELINE_STYLE, X_TAIXE, Y_LIFELINE_START, X_TAIXE, Y_LIFELINE_END, '1'))
    
    # 3. Hệ thống LogiFast (center, rounded box)
    cells.append(cell(f'sys', 'Hệ thống LogiFast', SYSTEM_STYLE, X_SYSTEM-110, Y_ACTOR_TOP+40, 220, 60, '1'))
    cells.append(edge(f'll_sys', '', 'endArrow=none;dashed=1;html=1;strokeColor=#6C8EBF;strokeWidth=2;', 
                     X_SYSTEM, Y_LIFELINE_START, X_SYSTEM, Y_LIFELINE_END, '1'))
    
    # 4. Hệ thống điều phối
    cells.append(cell(f'actor_dp', '&lt;&lt;actor&gt;&gt;<br/>Hệ thống điều phối', 
                     'rounded=0;whiteSpace=wrap;html=1;fontSize=13;fontStyle=0;', 
                     X_DIEUPHOI-70, Y_ACTOR_TOP+40, 140, 60, '1'))
    cells.append(edge(f'll_dp', '', LIFELINE_STYLE, X_DIEUPHOI, Y_LIFELINE_START, X_DIEUPHOI, Y_LIFELINE_END, '1'))
    
    # 5. Hệ thống theo dõi (rightmost)
    cells.append(cell(f'actor_td', '&lt;&lt;actor&gt;&gt;<br/>Hệ thống theo dõi', 
                     'rounded=0;whiteSpace=wrap;html=1;fontSize=13;fontStyle=0;', 
                     X_THEODOI-70, Y_ACTOR_TOP+40, 140, 60, '1'))
    cells.append(edge(f'll_td', '', LIFELINE_STYLE, X_THEODOI, Y_LIFELINE_START, X_THEODOI, Y_LIFELINE_END, '1'))
    
    # === Messages ===
    y = Y_LIFELINE_START + 60
    
    # Message 1: Tài xế → Hệ thống
    cells.append(edge(f'm1', '1. Bắt đầu ca làm việc()', MSG_STYLE, X_TAIXE, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act1', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 2: Hệ thống → Tài xế (return)
    cells.append(edge(f'm2', '2. Yêu cầu quét mã kiện hàng()', RETURN_STYLE, X_SYSTEM, y, X_TAIXE, y, '1', -10))
    y += Y_MSG_GAP
    
    # Message 3: Tài xế → Hệ thống
    cells.append(edge(f'm3', '3. Quét mã kiện hàng()', MSG_STYLE, X_TAIXE, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act3', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 4: Hệ thống → Hệ thống điều phối
    cells.append(edge(f'm4', '4. Tính toán lộ trình tối ưu()', MSG_STYLE, X_SYSTEM, y, X_DIEUPHOI, y, '1', -10))
    cells.append(cell(f'act4', '', ACTIVATION_STYLE, X_DIEUPHOI-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 5: Hệ thống điều phối → Hệ thống (return)
    cells.append(edge(f'm5', '5. Trả kết quả lộ trình()', RETURN_STYLE, X_DIEUPHOI, y, X_SYSTEM, y, '1', -10))
    y += Y_MSG_GAP
    
    # Message 6: Hệ thống → Tài xế (return)
    cells.append(edge(f'm6', '6. Hiển thị lộ trình và ETA()', RETURN_STYLE, X_SYSTEM, y, X_TAIXE, y, '1', -10))
    y += Y_MSG_GAP + 20
    
    # === LOOP box (message 7) ===
    loop_y_start = y - 10
    loop_height = 80
    loop_width = X_THEODOI - X_SYSTEM + 150
    cells.append(swimlane(f'loop_box', 'loop [mỗi 30 giây]', 
                         X_SYSTEM-50, loop_y_start, loop_width, loop_height, '1'))
    
    # Message 7: Hệ thống theo dõi → Hệ thống (inside loop)
    y += 30
    cells.append(edge(f'm7', '7. Cập nhật vị trí GPS định kỳ()', MSG_STYLE, X_THEODOI, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act7', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP + 20
    
    # === ALT box (messages 8-11) ===
    alt_y_start = y - 10
    alt_height = 280
    alt_width = X_THEODOI - X_TAIXE + 150
    cells.append(swimlane(f'alt_box', 'alt [phát hiện sự cố giao thông]', 
                         X_TAIXE-50, alt_y_start, alt_width, alt_height, '1'))
    
    # Divider line for alt (between conditions)
    alt_divider_y = alt_y_start + 160
    cells.append(edge(f'alt_div', '[else]', 'endArrow=none;dashed=1;html=1;strokeColor=#666666;fontSize=10;', 
                     X_TAIXE-40, alt_divider_y, X_THEODOI+100, alt_divider_y, '1', 15))
    
    # Message 8: Hệ thống theo dõi → Hệ thống (inside alt)
    y += 30
    cells.append(edge(f'm8', '8. Thông báo phát hiện sự cố giao thông()', MSG_STYLE, X_THEODOI, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act8', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 9: Hệ thống → Hệ thống điều phối
    cells.append(edge(f'm9', '9. Yêu cầu tính lại lộ trình()', MSG_STYLE, X_SYSTEM, y, X_DIEUPHOI, y, '1', -10))
    cells.append(cell(f'act9', '', ACTIVATION_STYLE, X_DIEUPHOI-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 10: Hệ thống điều phối → Hệ thống (return)
    cells.append(edge(f'm10', '10. Trả kết quả lộ trình mới()', RETURN_STYLE, X_DIEUPHOI, y, X_SYSTEM, y, '1', -10))
    y += Y_MSG_GAP
    
    # Message 11: Hệ thống → Tài xế (return)
    cells.append(edge(f'm11', '11. Cập nhật lộ trình thay thế()', RETURN_STYLE, X_SYSTEM, y, X_TAIXE, y, '1', -10))
    y += Y_MSG_GAP + 30
    
    # === Continue with remaining messages after alt box ===
    
    # Message 12: Tài xế → Hệ thống
    cells.append(edge(f'm12', '12. Xác nhận đã đến điểm giao()', MSG_STYLE, X_TAIXE, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act12', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 13: Hệ thống → Khách hàng
    cells.append(edge(f'm13', '13. Gửi thông báo Tài xế đã đến()', MSG_STYLE, X_SYSTEM, y, X_KHACHHANG, y, '1', -10))
    cells.append(cell(f'act13', '', ACTIVATION_STYLE, X_KHACHHANG-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 14: Tài xế → Hệ thống
    cells.append(edge(f'm14', '14. Xác nhận bàn giao hàng()', MSG_STYLE, X_TAIXE, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act14', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 15: Khách hàng → Hệ thống
    cells.append(edge(f'm15', '15. Khách hàng đồng ý nhận hàng()', MSG_STYLE, X_KHACHHANG, y, X_SYSTEM, y, '1', -10))
    cells.append(cell(f'act15', '', ACTIVATION_STYLE, X_SYSTEM-5, y, 10, 30, '1'))
    y += Y_MSG_GAP
    
    # Message 16: Hệ thống → Tài xế (return)
    cells.append(edge(f'm16', '16. Thông báo hoàn tất đơn hàng()', RETURN_STYLE, X_SYSTEM, y, X_TAIXE, y, '1', -10))
    
    return cells

# ── Main ────────────────────────────────────────────────────────────────────

def main():
    cells = generate_ssd()
    model_xml = model(cells, pw=1654, ph=2000)
    diagram_xml = diagram('UC03 SSD', 'uc03-ssd', model_xml)
    output = wrap(diagram_xml)
    
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f'✓ Generated: {OUT}')
    print(f'  - 5 lifelines: Khách hàng, Tài xế, Hệ thống LogiFast, Hệ thống điều phối, Hệ thống theo dõi')
    print(f'  - 16 messages with loop and alt boxes')
    print(f'  - File size: {len(output)} bytes')

if __name__ == '__main__':
    main()
