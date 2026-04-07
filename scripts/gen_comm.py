import xml.etree.ElementTree as ET
import sys, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(__file__))

def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')

def diagram_wrap(name, did, model_xml):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<mxfile host="app.diagrams.net" version="29.6.6">\n'
            f'  <diagram name="{name}" id="{did}">\n'
            f'    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" '
            f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
            f'pageWidth="1169" pageHeight="827" math="0" shadow="0">\n'
            f'      <root>\n'
            f'        <mxCell id="0"/>\n'
            f'        <mxCell id="1" parent="0"/>\n'
            f'{model_xml}\n'
            f'      </root>\n'
            f'    </mxGraphModel>\n'
            f'  </diagram>\n'
            f'</mxfile>\n')

def cell(cid, val, style, x, y, w, h, parent='1', extra=''):
    return (f'        <mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'vertex="1" parent="{parent}" {extra}>'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')

def edgecell(cid, val, style, src, tgt, parent='1'):
    geom = '<mxGeometry relative="1" as="geometry"/>'
    return (f'        <mxCell id="{cid}" value="{esc(val)}" style="{style}" '
            f'edge="1" source="{src}" target="{tgt}" parent="{parent}">{geom}</mxCell>')


cells = []

# Title
cells.append(cell('title', '<b>Sơ đồ giao tiếp mức nghiệp vụ — UC-03: Vận chuyển đơn hàng</b><br>Hệ thống Quản lý Giao hàng LogiFast',
                  'text;html=1;align=center;verticalAlign=middle;resizable=0;fontSize=14;', 100, 20, 800, 40))

# Frame
cells.append(cell('frame', 'Vận chuyển đơn hàng', 
                  'shape=umlFrame;whiteSpace=wrap;html=1;width=160;height=30;boundedLbl=1;verticalAlign=middle;align=left;spacingLeft=5;fontSize=12;',
                  40, 80, 1000, 600))


# Actors and Objects
cells.append(cell('a_taixe', ':Tài xế giao hàng', 'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fontSize=12;', 120, 300, 40, 80))

cells.append(cell('o_chuyendi', ':ChuyenDi', 'html=1;whiteSpace=wrap;fontSize=12;', 400, 150, 120, 40))
cells.append(cell('o_donhang', ':DonHang', 'html=1;whiteSpace=wrap;fontSize=12;', 400, 450, 120, 40))
cells.append(cell('o_kienhang', ':KienHang', 'html=1;whiteSpace=wrap;fontSize=12;', 700, 450, 120, 40))
cells.append(cell('o_lotrinh', ':LoTrinh', 'html=1;whiteSpace=wrap;fontSize=12;', 400, 300, 120, 40))
cells.append(cell('o_vitri', ':ViTriGPS', 'html=1;whiteSpace=wrap;fontSize=12;', 700, 300, 120, 40))
cells.append(cell('o_suco', ':SuCoGiaoThong', 'html=1;whiteSpace=wrap;fontSize=12;', 700, 150, 120, 40))

# Connections (solid lines)
EDGE_ST = 'edgeStyle=none;html=1;endArrow=none;endFill=0;strokeColor=#333333;strokeWidth=1;'
cells.append(edgecell('e1', '', EDGE_ST, 'a_taixe', 'o_chuyendi'))
cells.append(edgecell('e2', '', EDGE_ST, 'a_taixe', 'o_lotrinh'))
cells.append(edgecell('e3', '', EDGE_ST, 'a_taixe', 'o_donhang'))

cells.append(edgecell('e4', '', EDGE_ST, 'o_donhang', 'o_kienhang'))
cells.append(edgecell('e5', '', EDGE_ST, 'o_lotrinh', 'o_vitri'))
cells.append(edgecell('e6', '', EDGE_ST, 'o_lotrinh', 'o_suco'))


# Messages (directional arrows above lines)
# To create the message arrow, we use a shape element with text label
MSG_ST = 'html=1;align=center;verticalAlign=bottom;labelBackgroundColor=none;fontSize=11;strokeColor=none;fillColor=none;fontStyle=0;'
DIR_ST = 'shape=flexArrow;endArrow=classic;html=1;fillColor=#000000;strokeColor=none;width=2;endSize=4;endWidth=4;'

# 1: xacNhanBatDauCa -> ChuyenDi
cells.append(cell('m1_l', '1: xacNhanBatDauCa(maTaiXe)', MSG_ST, 180, 180, 200, 20))
cells.append(cell('m1_a', '', DIR_ST, 200, 205, 50, 10))

# 2: quetMaQR -> KienHang (indirect through DonHang maybe?) Let's point to DonHang for now
cells.append(cell('m2_l', '2: quetMaQR(maQR)', MSG_ST, 200, 420, 160, 20))
cells.append(cell('m2_a', '', DIR_ST, 250, 445, 50, 10))

# 3: batDauGiaoHang -> LoTrinh 
cells.append(cell('m3_l', '3: batDauGiaoHang(maDonHang)', MSG_ST, 210, 290, 180, 20))
cells.append(cell('m3_a', '', DIR_ST, 250, 315, 50, 10))

# 4: capNhatViTriGPS -> ViTriGPS 
cells.append(cell('m4_l', '4: capNhatViTriGPS()', MSG_ST, 540, 290, 160, 20))
cells.append(cell('m4_a', '', DIR_ST, 580, 315, 50, 10))


model_xml = '\n'.join(cells)
xml = diagram_wrap('UC03_CommDiagram', 'uc03-comm', model_xml)

path = os.path.join(BASE, 'Project', 'Diagrams', 'UC03_CommDiagram.drawio')
with open(path, 'w', encoding='utf-8') as f:
    f.write(xml)

print("Created Drawio!")
