"""
scripts/fix_mismatches.py
Fixes all 5 mismatches between Section 3 (brainstorming) and UC sections:

  Fix 1: ChuyenDi.thoiGianBatDau timestamp — step 3 says "09:30", should be "09:28"
  Fix 2: Generic 'id' in UC-03 tables → domain-specific attribute names (maTaiXe, etc.)
  Fix 3: UC-01 uses ChiTietDonHang/ctd1 but Section 3 says ChiTietKienHang/ctkh1
  Fix 4: Section 3 Table 3.3 has 'vdc1' but UC-02 & ch4-draft use 'vda1'
  Fix 5: '3.2. Phân loại danh từ' styled NormalWeb → Heading2
"""

from docx import Document
from docx.oxml.ns import qn
import re

DOC_PATH = r"Project/Ch4_MoHinhHoaCauTruc.docx"
NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

doc = Document(DOC_PATH)
body = doc.element.body
fixes = []

# ── helpers ──────────────────────────────────────────────────────────────

def gettxt(elem):
    return "".join(t.text or "" for t in elem.findall(f".//{{{NS}}}t"))

def replace_in_runs(elem, old, new):
    """Replace text across runs in an element. Returns True if replaced."""
    # Try simple per-run replacement first
    for t_el in elem.findall(f".//{{{NS}}}t"):
        if t_el.text and old in t_el.text:
            t_el.text = t_el.text.replace(old, new)
            return True
    # If not found in single runs, try concatenated replacement across runs
    runs = elem.findall(f".//{{{NS}}}r")
    full_text = ""
    run_map = []  # (run_element, t_element, start_idx, end_idx)
    for r in runs:
        t_el = r.find(f"{{{NS}}}t")
        if t_el is not None and t_el.text:
            start = len(full_text)
            full_text += t_el.text
            run_map.append((r, t_el, start, len(full_text)))
    if old in full_text:
        idx = full_text.index(old)
        end_idx = idx + len(old)
        # Find which runs are affected
        for r, t_el, rs, re_ in run_map:
            if re_ <= idx or rs >= end_idx:
                continue  # not affected
            # Compute the local slice that falls in [idx, end_idx)
            local_start = max(0, idx - rs)
            local_end = min(len(t_el.text), end_idx - rs)
            before = t_el.text[:local_start]
            after = t_el.text[local_end:]
            if rs <= idx:
                # This run contains the start of the match
                t_el.text = before + new + after
            else:
                # Continuation run — remove the matched part
                t_el.text = before + after
        return True
    return False

def set_cell_text(tbl_elem, row_idx, col_idx, new_text):
    """Set text of a specific cell, clearing all existing runs."""
    rows = tbl_elem.findall(f".//{{{NS}}}tr")
    cells = rows[row_idx].findall(f".//{{{NS}}}tc")
    cell = cells[col_idx]
    # Clear all paragraphs and add fresh one
    for p in cell.findall(f"{{{NS}}}p"):
        cell.remove(p)
    from docx.oxml import OxmlElement
    new_p = OxmlElement("w:p")
    new_r = OxmlElement("w:r")
    new_t = OxmlElement("w:t")
    new_t.set(qn("xml:space"), "preserve")
    new_t.text = new_text
    new_r.append(new_t)
    new_p.append(new_r)
    cell.append(new_p)

def get_cell_text(tbl_elem, row_idx, col_idx):
    rows = tbl_elem.findall(f".//{{{NS}}}tr")
    cells = rows[row_idx].findall(f".//{{{NS}}}tc")
    return "".join(t.text or "" for t in cells[col_idx].findall(f".//{{{NS}}}t"))


# ═══════════════════════════════════════════════════════════════════════
# FIX 1: ChuyenDi.thoiGianBatDau — step 3 says "09:30", should be "09:28"
# ═══════════════════════════════════════════════════════════════════════

children = list(body)
for child in children:
    txt = gettxt(child)
    if 'ChuyenDi.thoiGianBatDau = "09:30"' in txt:
        if replace_in_runs(child, 'ChuyenDi.thoiGianBatDau = "09:30"',
                                   'ChuyenDi.thoiGianBatDau = "09:28"'):
            fixes.append("Fix 1: step 3 thoiGianBatDau 09:30 → 09:28")
        break

# ═══════════════════════════════════════════════════════════════════════
# FIX 2: UC-03 object table and class diagram table — generic 'id' → domain names
# ═══════════════════════════════════════════════════════════════════════

# Mapping: class name → (generic prefix to replace, domain-specific name)
id_map = {
    "TaiXe":              ("id=TX-001",           "maTaiXe=TX-001"),
    "DonHang":            ("id=ORD-2026-001",     "maDonHang=ORD-2026-001"),
    "KienHang":           ("id=KH-PKG-001",       "maKienHang=KH-PKG-001"),
    "LoTrinh":            ("id=LT-2026-001",      "maLoTrinh=LT-2026-001"),
    "ViTriGPS":           ("id=GPS-TX001-1006",   "maViTri=GPS-TX001-1006"),
    "ChuyenDi":           ("id=CD-2026-0326-T1",  "maChuyenDi=CD-2026-0326-T1"),
    "BangChungGiaoHang":  ("id=BC-2026-001",      "maBangChung=BC-2026-001"),
}

# Class diagram attribute map
attr_map = {
    "TaiXe":              ("id, ten,",             "maTaiXe, ten,"),
    "DonHang":            ("id, trangThai,",       "maDonHang, trangThai,"),
    "KienHang":           ("id, maQR,",            "maKienHang, maQR,"),
    "LoTrinh":            ("id, diemXuatPhat,",    "maLoTrinh, diemXuatPhat,"),
    "ViTriGPS":           ("id, viDo,",            "maViTri, viDo,"),
    "ChuyenDi":           ("id, thoiGianBatDau,",  "maChuyenDi, thoiGianBatDau,"),
    "BangChungGiaoHang":  ("id, tenNguoiNhan,",    "maBangChung, tenNguoiNhan,"),
}

# Find UC-03 object table (contains "Thuộc tính chính (giá trị kịch bản)")
# and class diagram table (contains "Thuộc tính (phân tích — chỉ tên)")
for child in children:
    tag = child.tag.split("}")[-1]
    if tag != "tbl":
        continue
    header_txt = gettxt(child)

    # Object table (Fix 2a)
    if "Thuộc tính chính (giá trị kịch bản)" in header_txt:
        rows = child.findall(f".//{{{NS}}}tr")
        for ri in range(1, len(rows)):
            cells = rows[ri].findall(f".//{{{NS}}}tc")
            cls_name = "".join(t.text or "" for t in cells[0].findall(f".//{{{NS}}}t")).strip()
            if cls_name in id_map:
                old_id, new_id = id_map[cls_name]
                cell_txt = get_cell_text(child, ri, 2)
                if old_id in cell_txt:
                    new_txt = cell_txt.replace(old_id, new_id)
                    set_cell_text(child, ri, 2, new_txt)
                    fixes.append(f"Fix 2a: obj table {cls_name}: {old_id} → {new_id}")

    # Class diagram table (Fix 2b)
    if "Thuộc tính (phân tích" in header_txt:
        rows = child.findall(f".//{{{NS}}}tr")
        for ri in range(1, len(rows)):
            cells = rows[ri].findall(f".//{{{NS}}}tc")
            cls_name = "".join(t.text or "" for t in cells[0].findall(f".//{{{NS}}}t")).strip()
            if cls_name in attr_map:
                old_attr, new_attr = attr_map[cls_name]
                cell_txt = get_cell_text(child, ri, 1)
                if old_attr in cell_txt:
                    new_txt = cell_txt.replace(old_attr, new_attr)
                    set_cell_text(child, ri, 1, new_txt)
                    fixes.append(f"Fix 2b: class table {cls_name}: {old_attr} → {new_attr}")


# ═══════════════════════════════════════════════════════════════════════
# FIX 3: UC-01 uses ChiTietDonHang/ctd1 → align to Section 3's ChiTietKienHang/ctkh1
# ═══════════════════════════════════════════════════════════════════════

# 3a: UC-01 object table — row with ChiTietDonHang
for child in children:
    tag = child.tag.split("}")[-1]
    if tag != "tbl":
        continue
    txt = gettxt(child)
    # UC-01 object table has "Giá trị thuộc tính chính" and contains "ChiTietDonHang"
    if "ChiTietDonHang" in txt and "Giá trị thuộc tính chính" in txt:
        rows = child.findall(f".//{{{NS}}}tr")
        for ri in range(1, len(rows)):
            c0 = get_cell_text(child, ri, 0).strip()
            if c0 == "ChiTietDonHang":
                set_cell_text(child, ri, 0, "ChiTietKienHang")
                c1 = get_cell_text(child, ri, 1)
                new_c1 = c1.replace("ctd1", "ctkh1").replace("ChiTietDonHang", "ChiTietKienHang")
                set_cell_text(child, ri, 1, new_c1)
                c2 = get_cell_text(child, ri, 2)
                new_c2 = c2.replace("CTD-001-01", "CTKH-01")
                set_cell_text(child, ri, 2, new_c2)
                fixes.append("Fix 3a: UC-01 obj table: ChiTietDonHang→ChiTietKienHang, ctd1→ctkh1")

# 3b: UC-01 relation text paragraphs
for child in children:
    txt = gettxt(child)
    if "dh1 gồm ctd1" in txt:
        replace_in_runs(child, "ctd1", "ctkh1")
        replace_in_runs(child, "ChiTietDonHang", "ChiTietKienHang")
        fixes.append("Fix 3b: UC-01 relation 'dh1 gồm ctd1' → ctkh1/ChiTietKienHang")
    if "ctd1 tham chiếu sp1" in txt:
        replace_in_runs(child, "ctd1", "ctkh1")
        replace_in_runs(child, "ChiTietDonHang", "ChiTietKienHang")
        fixes.append("Fix 3c: UC-01 relation 'ctd1→ctkh1 tham chiếu sp1'")


# ═══════════════════════════════════════════════════════════════════════
# FIX 4: Section 3 Table 3.3 instance 'vdc1' → 'vda1'
# ═══════════════════════════════════════════════════════════════════════

for child in children:
    tag = child.tag.split("}")[-1]
    if tag != "tbl":
        continue
    txt = gettxt(child)
    if "UC xuất hiện" in txt and "vdc1" in txt:
        rows = child.findall(f".//{{{NS}}}tr")
        for ri in range(1, len(rows)):
            c0 = get_cell_text(child, ri, 0).strip()
            if c0 == "vdc1":
                set_cell_text(child, ri, 0, "vda1")
                fixes.append("Fix 4: Section 3 Table 3.3: vdc1 → vda1")
                break


# ═══════════════════════════════════════════════════════════════════════
# FIX 5: Heading style for '3.2. Phân loại danh từ' — NormalWeb → Heading2
# ═══════════════════════════════════════════════════════════════════════

for child in children:
    tag = child.tag.split("}")[-1]
    if tag != "p":
        continue
    txt = gettxt(child)
    if "3.2. Phân loại danh từ" in txt.strip():
        pPr = child.find(f"{{{NS}}}pPr")
        if pPr is None:
            from docx.oxml import OxmlElement
            pPr = OxmlElement("w:pPr")
            child.insert(0, pPr)
        pStyle = pPr.find(f"{{{NS}}}pStyle")
        if pStyle is None:
            from docx.oxml import OxmlElement
            pStyle = OxmlElement("w:pStyle")
            pPr.insert(0, pStyle)
        pStyle.set(qn("w:val"), "Heading2")
        fixes.append("Fix 5: '3.2. Phân loại danh từ' NormalWeb → Heading2")
        break


# ── save & report ────────────────────────────────────────────────────
doc.save(DOC_PATH)
print(f"Applied {len(fixes)} fixes:")
for f in fixes:
    print(f"  ✓ {f}")
print("Saved to", DOC_PATH)
