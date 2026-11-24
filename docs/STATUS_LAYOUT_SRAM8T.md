# SRAM8T — Status do Layout Físico

## 1. Objetivo

Desenvolver o layout físico da célula SRAM8T utilizando o PDK IHP SG13G2, com dispositivos MOS reais gerados por meio das PCells oficiais do processo.

O projeto está na etapa de implementação física, evoluindo da validação dos dispositivos para posicionamento topológico, interconexões e validação final.

## 2. Ambiente de desenvolvimento

- **PDK:** IHP Open PDK — SG13G2
- **Ferramenta de layout:** KLayout
- **Ambiente:** WSL / Ubuntu
- **Geração de dispositivos:** PCells oficiais SG13G2
- **Interface de geração:** Python / KLayout API / CNI

## 3. Topologia da SRAM8T

A célula possui oito transistores:

| Dispositivo | Tipo | Função |
|---|---|---|
| M1 | NMOS | Pull-down |
| M2 | NMOS | Pull-down |
| M3 | PMOS | Pull-up |
| M4 | PMOS | Pull-up |
| M5 | NMOS | Write access |
| M6 | NMOS | Write access |
| M7 | NMOS | Read port |
| M8 | NMOS | Read port |

Parâmetros utilizados na netlist de referência:

- Width (W): 0,15 µm
- Length (L): 0,13 µm
- Multiplicidade (m): 1
- Número de gates (ng): 1

## 4. Avanços realizados

### 4.1 Validação das PCells

Foi realizada a configuração do ambiente para acesso às bibliotecas de dispositivos do PDK SG13G2.

Foi confirmada a instanciação dos PCells oficiais:

- NMOS — `sg13_lv_nmos`
- PMOS — `sg13_lv_pmos`

A geração dos dispositivos físicos foi testada e os arquivos GDS resultantes foram produzidos.

### 4.2 Geração dos dispositivos

Foi desenvolvido um fluxo em Python/KLayout para instanciação dos transistores e geração de arquivos GDS.

### 4.3 Array de dispositivos

Foi criado um array inicial contendo os oito dispositivos necessários para a SRAM8T, permitindo verificar a geração e organização das geometrias físicas.

### 4.4 Extração geométrica

Foram analisadas as geometrias geradas pelas PCells, incluindo as camadas relacionadas a:

- Active / Diffusion
- Gate Poly
- Contacts
- Metal 1
- Well e camadas específicas dos dispositivos

### 4.5 Placement preliminar

Foi gerada uma disposição preliminar dos dispositivos.

Esse placement ainda não representa a organização física otimizada da bitcell, nem possui todas as conexões elétricas implementadas.

## 5. Arquivos de desenvolvimento relevantes

Entre os arquivos gerados e utilizados nesta etapa estão:

- `SRAM8T_DEVICE_ARRAY.gds`
- `SRAM8T_COMPACT_PLACEMENT.gds`
- `teste_pcell_sg13_real.gds`
- `build_sram8t_device_array.py`
- `build_sram8t_compact.py`
- `catalogo_pcells.py`
- `extrair_geometria_devices.py`
- `teste_pcell_real.py`

Os arquivos são utilizados como artefatos de desenvolvimento e referência para a próxima etapa.

## 6. Próximas etapas

1. Definir placement baseado na topologia elétrica da SRAM8T.
2. Organizar os transistores para reduzir área e facilitar as conexões.
3. Implementar as interconexões internas Q e QB.
4. Implementar BL e BLB.
5. Implementar WWL.
6. Implementar o circuito de leitura RBL e RWL.
7. Planejar e conectar VDD e GND.
8. Executar o routing.
9. Realizar DRC.
10. Realizar LVS.
11. Gerar e validar o GDS final.

## 7. Estado atual

**Etapa atual:** Layout físico — geração de dispositivos e placement preliminar.

Os dispositivos reais do PDK já foram instanciados e exportados para GDS. A implementação ainda necessita de posicionamento baseado na topologia, roteamento e validações físicas.

Os arquivos atuais não devem ser considerados layout final, DRC-clean ou LVS-clean.

## 8. Ponto de retomada

A próxima atividade será a construção do placement topológico da SRAM8T, utilizando os oito dispositivos da netlist como referência, seguida pelo planejamento e execução das interconexões.

**Última atualização:** 23/11/2026.
