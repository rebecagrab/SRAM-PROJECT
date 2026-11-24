import sys
import pya

PDK = "/home/rebeca/projetos/PDK/IHP-Open-PDK/ihp-sg13g2/libs.tech/klayout/python"
sys.path.insert(0, PDK + "/pycell4klayout-api/source/python")
sys.path.insert(0, PDK)

import cni
import sg13g2_pycell_lib

print("\n=== BIBLIOTECAS REGISTRADAS NO KLAYOUT ===")
for name in pya.Library.library_names():
    print(name)

print("\n=== TECNOLOGIA ===")
for name in pya.Technology.technology_names():
    print(name)

print("\n=== TESTE DE REGISTRO ===")
for name in ("SG13_dev", "sg13_native_pcell_lib"):
    print(name, "=>", pya.Library.library_by_name(name))
