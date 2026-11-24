import pya

layout = pya.Layout()
layout.dbu = 0.001

top = layout.create_cell("SRAM8T_TOP")

# Camadas temporárias de organização do floorplan
DEV = layout.layer(100, 0)
TEXT = layout.layer(101, 0)
RAIL = layout.layer(102, 0)

def box(x1, y1, x2, y2):
    return pya.Box(
        int(x1 / layout.dbu), int(y1 / layout.dbu),
        int(x2 / layout.dbu), int(y2 / layout.dbu)
    )

def device(name, x, y, w=2.0, h=2.0):
    top.shapes(DEV).insert(box(x, y, x+w, y+h))
    top.shapes(TEXT).insert(pya.Text(name, pya.Trans(int((x+0.25)/layout.dbu), int((y+0.25)/layout.dbu))))

# Núcleo de armazenamento: M1-M4
device("M1 NMOS PD", 5, 5)
device("M3 PMOS PU", 5, 9)
device("M2 NMOS PD", 13, 5)
device("M4 PMOS PU", 13, 9)

# Acesso de escrita: M5-M6
device("M5 WRITE", 5, 17)
device("M6 WRITE", 13, 17)

# Caminho de leitura: M7-M8
device("M7 READ", 23, 5)
device("M8 READ", 23, 9)

# Rails ilustrativas
top.shapes(RAIL).insert(box(3, 12, 19, 12.5))
top.shapes(RAIL).insert(box(3, 4, 19, 4.5))

layout.write("sram8t/layout/physical/SRAM8T_TOP.gds")
print("SRAM8T FLOORPLAN GERADO")
