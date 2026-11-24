## Atualização – Desenvolvimento do Layout da SRAM 8T

### Etapa realizada: Exploração inicial do layout do transistor NMOS

Inicialmente, foi realizada a exploração do ambiente de layout físico utilizando a ferramenta Magic, com a tecnologia IHP SG13G2.

Durante os testes, foram encontrados problemas relacionados à manipulação de células, hierarquia e execução de comandos. Após essa etapa, optou-se pela migração do desenvolvimento físico para o **KLayout**, visando dar continuidade à construção do layout.

### Transição para o KLayout

O ambiente de desenvolvimento passou a utilizar:

- **KLayout 0.30.13**
- **PDK IHP SG13G2**
- Scripts Python para geração automatizada de geometrias
- Arquivos GDSII para armazenamento e evolução do layout

Foram identificadas as camadas físicas utilizadas no processo, incluindo:

- Active (`Activ`) — 1/0
- GatePoly (`GatPoly`) — 5/0
- Contact (`Cont`) — 6/0
- Metal1 — 8/0

### Etapa 1 — Floorplan inicial da SRAM8T

Foi criado o primeiro floorplan da SRAM8T, com organização inicial da área de layout, regiões destinadas aos blocos e indicação das áreas de leitura e escrita.

Arquivo gerado:

` sram8t_layout_stage1.gds `

O floorplan serve como base visual e organizacional para o desenvolvimento da estrutura física da célula.

### Etapa 2 — Geometria de teste NMOS

Foi desenvolvida uma primeira geometria experimental de NMOS utilizando as camadas físicas identificadas no PDK.

Arquivo:

`nmos_test_stage2.gds`

Essa etapa teve como objetivo iniciar a construção física do transistor e observar a sobreposição e organização das camadas no KLayout.

### Etapa 3 — Evolução da geometria NMOS

Foi criada uma segunda versão da geometria NMOS, avançando na organização das regiões Active, GatePoly e Metal1.

Arquivo gerado:

`nmos_stage3.gds`

Também foi criado o script de geração:

`build_nmos_stage3.py`

A geometria permanece experimental e ainda precisa passar por validações de regras de projeto, dimensões, contatos e conectividade.

### Scripts desenvolvidos

Os scripts utilizados para geração e construção das geometrias foram preservados no diretório:

` sram8t/layout/physical/ `

Arquivos principais:

- `build_layout.py`
- `build_nmos.py`
- `build_nmos_stage3.py`

A utilização de scripts permite reproduzir e modificar as geometrias sem depender exclusivamente de desenho manual.

### Arquivos gerados

| Arquivo | Descrição |
|---|---|
| `SRAM8T_TOP.gds` | Layout inicial/floorplan |
| `sram8t_layout_stage1.gds` | Floorplan da SRAM8T |
| `nmos_test_stage2.gds` | Geometria NMOS experimental — estágio 2 |
| `nmos_stage3.gds` | Geometria NMOS experimental — estágio 3 |

### Backup e versionamento

Em 22/11/2026, os arquivos gerados, scripts e backup foram adicionados ao repositório Git.

Backup:

`backups/sram8t_2026-11-22.tar.gz`

Commit:

`28fb86a` — Add SRAM8T physical layout stages and backup

As alterações foram integradas aos commits existentes no repositório remoto e enviadas com sucesso para o GitHub, sincronizando a branch `main`.

### Estado atual do projeto

- KLayout 0.30.13 configurado para desenvolvimento de layout.
- Tecnologia IHP SG13G2 carregada.
- Floorplan inicial SRAM8T gerado.
- Geometrias experimentais de NMOS nos estágios 2 e 3 geradas.
- Scripts Python preservados para reprodução.
- Arquivos GDS salvos no repositório.
- Backup criado.
- GitHub sincronizado.

**Status:** desenvolvimento do layout físico em andamento. As geometrias atuais são experimentais, não estando ainda validadas por DRC ou LVS.

### Próxima etapa

Continuar o desenvolvimento da geometria NMOS no KLayout, ajustando dimensões e estrutura física para uma representação mais consistente com as regras do PDK IHP SG13G2.

Após validar a geometria do transistor, avançar para a construção e integração dos dispositivos que compõem a célula SRAM8T, incluindo inversores cruzados, transistores de acesso e estrutura de leitura.
