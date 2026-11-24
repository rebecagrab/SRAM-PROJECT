import klayout.db as db

layout = db.Layout()
layout.dbu = 0.001
top = layout.create_cell("SRAM8T_PCELLS_TEST")

print("KLayout DB carregado.")
print("Versão da API:", db.__version__ if hasattr(db, "__version__") else "disponível")

layout.write("/home/rebeca/projetos/sram/SRAM-PROJECT/sram8t/layout/physical/SRAM8T_PCELLS_TEST.gds")
print("GDS de teste criado.")
