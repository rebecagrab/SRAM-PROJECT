import sys
import pya

PDK = "/home/rebeca/projetos/PDK/IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python"
sys.path.insert(0, PDK + "/pycell4klayout-api/source/python")
sys.path.insert(0, PDK)

import cni
import sg13g2_pycell_lib

# Biblioteca oficial
lib = sg13g2_pycell_lib.PyCellLib()
lib_layout = lib.layout()

n_decl = lib_layout.pcell_declaration("nmos")
p_decl = lib_layout.pcell_declaration("pmos")

# Layout de destino
layout = pya.Layout()
layout.dbu = 0.001
top = layout.create_cell("SRAM8T_DEVICE_ARRAY")

def make_device(decl, name, x, y):
    params = [p.default for p in decl.get_parameters()]
    idx = layout.add_pcell_variant(lib, decl.id(), params)
    cell = layout.cell(idx)
    top.insert(pya.CellInstArray(idx, pya.Trans(x, y)))
    print(f"{name}: cell={cell.name}, bbox={cell.bbox()}")
    return cell

# NMOS e PMOS conforme netlist original
devices = [
    ("M1_NMOS_PULLDOWN", n_decl,    0,    0),
    ("M2_NMOS_PULLDOWN", n_decl, 2500,    0),
    ("M3_PMOS_PULLUP",   p_decl,    0, 4000),
    ("M4_PMOS_PULLUP",   p_decl, 2500, 4000),
    ("M5_WRITE_ACCESS",  n_decl, 5000,    0),
    ("M6_WRITE_ACCESS",  n_decl, 7500,    0),
    ("M7_READ_ACCESS",   n_decl,10000,    0),
    ("M8_READ_ACCESS",   n_decl,12500,    0),
]

for name, decl, x, y in devices:
    make_device(decl, name, x, y)

out = "SRAM8T_DEVICE_ARRAY.gds"
layout.write(out)

print("\n================================")
print("ARRAY FÍSICO GERADO:", out)
print("Total de dispositivos:", len(devices))
print("BBox TOP:", top.bbox())
print("================================")
