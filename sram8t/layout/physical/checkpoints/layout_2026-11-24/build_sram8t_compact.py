import sys
import pya

PDK = "/home/rebeca/projetos/PDK/IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python"
sys.path.insert(0, PDK + "/pycell4klayout-api/source/python")
sys.path.insert(0, PDK)

import cni
import sg13g2_pycell_lib

lib = sg13g2_pycell_lib.PyCellLib()
lib_layout = lib.layout()

n_decl = lib_layout.pcell_declaration("nmos")
p_decl = lib_layout.pcell_declaration("pmos")

layout = pya.Layout()
layout.dbu = 0.001

top = layout.create_cell("SRAM8T_COMPACT_CANDIDATE")

def variant(decl):
    params = [p.default for p in decl.get_parameters()]
    return layout.add_pcell_variant(lib, decl.id(), params)

n_idx = variant(n_decl)
p_idx = variant(p_decl)

n_cell = layout.cell(n_idx)
p_cell = layout.cell(p_idx)

# Coordenadas em DBU (1 DBU = 0,001 um)
# Placement inicial com separação conservadora
# PMOS na parte superior
pmos_positions = [
    (0, 2000),
    (2500, 2000),
]

# NMOS na parte inferior
nmos_positions = [
    (0, 0),       # M1
    (1500, 0),     # M2
    (3000, 0),     # M5
    (4500, 0),     # M6
    (6000, 0),     # M7
    (7500, 0),     # M8
]

for i, (x, y) in enumerate(pmos_positions, 1):
    top.insert(pya.CellInstArray(p_idx, pya.Trans(x, y)))
    print(f"M{i+2} PMOS @ {x},{y}")

for i, (x, y) in enumerate(nmos_positions):
    top.insert(pya.CellInstArray(n_idx, pya.Trans(x, y)))
    print(f"NMOS position {i+1} @ {x},{y}")

# Boundary visual de referência (layer 100/0)
boundary_layer = layout.layer(100, 0)
margin = 500
bbox = top.bbox().enlarged(margin)
top.shapes(boundary_layer).insert(pya.Box(bbox))

out = "SRAM8T_COMPACT_PLACEMENT.gds"
layout.write(out)

print("\nPLACEMENT CANDIDATO GERADO:", out)
print("BBox:", top.bbox())
print("Dispositivos:", len(pmos_positions) + len(nmos_positions))
