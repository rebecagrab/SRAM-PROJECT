import pya

ly = pya.Layout()
ly.dbu = 0.001
top = ly.create_cell("SRAM8T")

# Layers temporárias de construção/organização
active = ly.layer(pya.LayerInfo(100, 0, "ACTIVE_PLAN"))
poly   = ly.layer(pya.LayerInfo(101, 0, "GATE_PLAN"))
metal  = ly.layer(pya.LayerInfo(102, 0, "ROUTE_PLAN"))
labels = ly.layer(pya.LayerInfo(103, 0, "LABELS"))
frame  = ly.layer(pya.LayerInfo(104, 0, "BOUNDARY"))

def um(v):
    return round(v / ly.dbu)

def rect(layer, x1, y1, x2, y2):
    top.shapes(layer).insert(pya.Box(um(x1), um(y1), um(x2), um(y2)))

def label(txt, x, y):
    top.shapes(labels).insert(pya.Text(txt, pya.Trans(um(x), um(y))))

# Cell boundary
rect(frame, 0, 0, 24, 18)
label("SRAM 8T - CELL", 1, 17)

# Latch inverter 1
rect(active, 3, 12, 7, 15)
rect(poly, 4.8, 11.5, 5.2, 15.5)
label("P1", 3, 15.2)

rect(active, 3, 7, 7, 10)
rect(poly, 4.8, 6.5, 5.2, 10.5)
label("N1", 3, 10.2)

# Latch inverter 2
rect(active, 17, 12, 21, 15)
rect(poly, 18.8, 11.5, 19.2, 15.5)
label("P2", 17, 15.2)

rect(active, 17, 7, 21, 10)
rect(poly, 18.8, 6.5, 19.2, 10.5)
label("N2", 17, 10.2)

# Write access devices
rect(active, 8, 12, 11, 15)
rect(poly, 9.3, 11.5, 9.7, 15.5)
label("AX1", 8, 15.2)

rect(active, 13, 12, 16, 15)
rect(poly, 14.3, 11.5, 14.7, 15.5)
label("AX2", 13, 15.2)

# Read port devices
rect(active, 8, 4, 11, 7)
rect(poly, 9.3, 3.5, 9.7, 7.5)
label("R1", 8, 7.2)

rect(active, 13, 4, 16, 7)
rect(poly, 14.3, 3.5, 14.7, 7.5)
label("R2", 13, 7.2)

# Signal routing planning
rect(metal, 1, 16, 23, 16.3)
label("VDD", 1, 16.5)

rect(metal, 1, 1, 23, 1.3)
label("GND", 1, 1.5)

rect(metal, 1, 10.8, 1.3, 14)
label("BL", 1, 14.2)

rect(metal, 22.7, 10.8, 23, 14)
label("BLB", 21.5, 14.2)

rect(metal, 1, 8, 23, 8.3)
label("WL", 1, 8.5)

rect(metal, 1, 3, 23, 3.3)
label("RWL", 1, 3.5)

rect(metal, 22.7, 3.3, 23, 7)
label("RBL", 21.5, 7.2)

# Cross-coupled node markers
label("Q", 11.2, 10.8)
label("QB", 12.3, 10.8)

out = "sram8t/layout/physical/sram8t_layout_stage1.gds"
ly.write(out)
print("LAYOUT GERADO:", out)
