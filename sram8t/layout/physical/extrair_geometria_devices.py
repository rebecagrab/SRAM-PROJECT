import pya

gds = "SRAM8T_DEVICE_ARRAY.gds"
ly = pya.Layout()
ly.read(gds)

top = ly.top_cell()
print("TOP:", top.name, "BBOX:", top.bbox())

for inst in top.each_inst():
    cell = inst.cell
    print("\nDEVICE:", cell.name)
    print("TRANS:", inst.trans)
    print("BBOX:", inst.bbox())

    for layer_index in ly.layer_indexes():
        layer = ly.get_info(layer_index)
        shapes = cell.shapes(layer_index)
        if shapes.is_empty():
            continue

        boxes = []
        for shape in shapes.each():
            if shape.is_box():
                boxes.append(shape.box)
            elif shape.is_polygon():
                boxes.append(shape.polygon.bbox())
            elif shape.is_path():
                boxes.append(shape.path.bbox())

        if boxes:
            print(" LAYER", layer, "COUNT", len(boxes))
            for box in boxes[:12]:
                print("   ", box)
