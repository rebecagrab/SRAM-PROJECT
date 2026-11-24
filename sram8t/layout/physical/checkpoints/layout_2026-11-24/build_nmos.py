import pya

ly = pya.Layout()
ly.dbu = 0.001
cell = ly.create_cell("NMOS_TEST")

# Camadas reais SG13G2 (GDS)
ACT = ly.layer(1, 0)
POLY = ly.layer(5, 0)
CONT = ly.layer(6, 0)
M1 = ly.layer(8, 0)

def u(v):
    return int(round(v / ly.dbu))

def box(layer, x1, y1, x2, y2):
    cell.shapes(layer).insert(pya.Box(u(x1), u(y1), u(x2), u(y2)))

# Active region
box(ACT, 0.00, 0.00, 1.00, 0.60)

# Gate crossing Active
box(POLY, 0.435, -0.20, 0.565, 0.80)

# Contacts (0.16 x 0.16 um)
box(CONT, 0.15, 0.22, 0.31, 0.38)
box(CONT, 0.69, 0.22, 0.85, 0.38)

# Metal1 source/drain pads
box(M1, 0.05, 0.15, 0.40, 0.45)
box(M1, 0.60, 0.15, 0.95, 0.45)

# Gate Metal1 connection
box(M1, 0.435, -0.45, 0.565, -0.25)

out = "sram8t/layout/physical/nmos_test_stage2.gds"
ly.write(out)
print("NMOS TESTE GERADO:", out)
print("Active 1/0 | GatePoly 5/0 | Contact 6/0 | Metal1 8/0")
