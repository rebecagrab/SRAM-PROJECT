import pya

ly = pya.Layout()
ly.dbu = 0.001
cell = ly.create_cell("NMOS_STAGE3")

ACT  = ly.layer(1, 0)
POLY = ly.layer(5, 0)
CONT = ly.layer(6, 0)
M1   = ly.layer(8, 0)

def u(v):
    return int(round(v / ly.dbu))

def box(layer, x1, y1, x2, y2):
    cell.shapes(layer).insert(pya.Box(u(x1), u(y1), u(x2), u(y2)))

# Active
box(ACT, 0.00, 0.00, 1.00, 0.60)

# Gate: cruza Active e prolonga para baixo
box(POLY, 0.435, -0.50, 0.565, 0.80)

# Source e Drain - contatos
box(CONT, 0.15, 0.22, 0.31, 0.38)
box(CONT, 0.69, 0.22, 0.85, 0.38)

# Metal1 source e drain
box(M1, 0.05, 0.15, 0.40, 0.45)
box(M1, 0.60, 0.15, 0.95, 0.45)

# Contato de Gate na extensão de Poly
box(CONT, 0.42, -0.38, 0.58, -0.22)

# Metal1 para Gate
box(M1, 0.30, -0.45, 0.70, -0.15)

ly.write("sram8t/layout/physical/nmos_stage3.gds")
print("NMOS STAGE 3 criado: nmos_stage3.gds")
