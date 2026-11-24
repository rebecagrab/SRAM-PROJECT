# SRAM8T - Checkpoint Layout Físico

Data: 24/11/2026

## Projeto
SRAM8T - IHP SG13G2

## Ambiente
- KLayout 0.30.13
- PDK IHP SG13G2
- Python API PCells/CNI

## Concluído
- Biblioteca SG13G2 carregada com sucesso.
- PCells oficiais NMOS e PMOS instanciados.
- NMOS: sg13_lv_nmos
- PMOS: sg13_lv_pmos
- W: 0.15 um
- L: 0.13 um
- Geração de dispositivos físicos confirmada.
- Array de 8 dispositivos gerado.
- Geometria dos dispositivos extraída.
- Placement candidato inicial gerado.

## Arquivos importantes
- teste_pcell_sg13_real.gds
- SRAM8T_DEVICE_ARRAY.gds
- SRAM8T_COMPACT_PLACEMENT.gds
- build_sram8t_device_array.py
- build_sram8t_compact.py
- catalogo_pcells.py
- extrair_geometria_devices.py

## Pendências
1. Placement baseado na topologia elétrica.
2. Compactação da bitcell.
3. Interconexões Q e QB.
4. Conexões BL e BLB.
5. Conexão WWL.
6. Porta de leitura RBL e RWL.
7. VDD e GND.
8. Routing.
9. DRC.
10. LVS.
11. GDS final validado.

## Estado atual
Os GDS existentes são candidatos de desenvolvimento.
Nenhum layout foi declarado DRC-clean ou LVS-clean.
O próximo trabalho deve continuar diretamente no layout físico e routing,
sem repetir o carregamento dos PCells ou os testes já concluídos.
