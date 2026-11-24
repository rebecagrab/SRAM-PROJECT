import sys
import pya

PDK = "/home/rebeca/projetos/PDK/IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python"
sys.path.insert(0, PDK + "/pycell4klayout-api/source/python")
sys.path.insert(0, PDK)

import cni
import sg13g2_pycell_lib

# Instanciar biblioteca PCell oficial
lib = sg13g2_pycell_lib.PyCellLib()
lib_layout = lib.layout()

# Declarações reais
n_decl = lib_layout.pcell_declaration("nmos")
p_decl = lib_layout.pcell_declaration("pmos")

if n_decl is None or p_decl is None:
    raise RuntimeError("Declarações NMOS/PMOS não encontradas.")

print("=== PARÂMETROS NMOS ===")
for p in n_decl.get_parameters():
    print(p.name, "default =", p.default)

print("\n=== PARÂMETROS PMOS ===")
for p in p_decl.get_parameters():
    print(p.name, "default =", p.default)

# Layout de destino
layout = pya.Layout()
layout.dbu = 0.001
top = layout.create_cell("SRAM8T_PCELLS_TEST")

# Usar defaults oficiais para validar a geração
n_params = [p.default for p in n_decl.get_parameters()]
p_params = [p.default for p in p_decl.get_parameters()]

n_idx = layout.add_pcell_variant(lib, n_decl.id(), n_params)
p_idx = layout.add_pcell_variant(lib, p_decl.id(), p_params)

nmos = layout.cell(n_idx)
pmos = layout.cell(p_idx)

top.insert(pya.CellInstArray(n_idx, pya.Trans(0, 0)))
top.insert(pya.CellInstArray(p_idx, pya.Trans(5000, 0)))

out = "teste_pcell_sg13_real.gds"
layout.write(out)

print("\n=== RESULTADO ===")
print("NMOS cell:", nmos.name, "bbox:", nmos.bbox())
print("PMOS cell:", pmos.name, "bbox:", pmos.bbox())
print("TOP bbox:", top.bbox())
print("GDS gerado:", out)
