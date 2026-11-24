import pya

print("=== CONSTRUTOR SRAM8T ===")

lib = pya.Library.library_by_name("SG13_dev")

if lib is None:
    print("ERRO: biblioteca SG13_dev não encontrada")
else:
    print("Biblioteca SG13_dev encontrada")

    for name in ["nmos", "pmos"]:
        try:
            params = lib.get_pcell_parameters(name)
            print(f"\nPCell: {name}")
            for p in params:
                print(p.name, "=", p.default)
        except Exception as e:
            print(f"Erro consultando {name}: {e}")
