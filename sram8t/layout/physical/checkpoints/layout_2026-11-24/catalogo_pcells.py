import sys
import pya

PDK = "/home/rebeca/projetos/PDK/IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python"
sys.path.insert(0, PDK + "/pycell4klayout-api/source/python")
sys.path.insert(0, PDK)

import cni
import sg13g2_pycell_lib

print("Instanciando biblioteca oficial...")
dev = sg13g2_pycell_lib.PyCellLib()
native = sg13g2_pycell_lib.SG13G2_NativePCellLib()

for lib in (dev, native):
    print("\n============================")
    print("Biblioteca:", lib.description)
    layout = lib.layout()
    print("PCell names:", layout.pcell_names())

    for name in sorted(layout.pcell_names()):
        decl = layout.pcell_declaration(name)
        print("\nPCell:", name)
        if decl:
            for p in decl.parameters():
                print("  ", p.name, "=", p.default)

print("\nFIM")
