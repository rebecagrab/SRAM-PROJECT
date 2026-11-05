# SETUP — Ambiente de Desenvolvimento SRAM 8T

Este documento descreve a configuração do ambiente utilizado para o desenvolvimento e simulação do projeto SRAM 8T.

## 1. Sistema operacional

- Windows 10
- WSL2
- Ubuntu 22.04

## 2. Controle de versão

O projeto utiliza Git e GitHub para controle de versão e backup.

Repositório:

`SRAM-PROJECT`

Estrutura principal do projeto:

```text
SRAM-PROJECT/
├── sram8t/
│   ├── schematic/
│   ├── simulations/
│   └── layout/
├── results/
├── documentation/
├── README.md
└── SETUP.md
```

## 3. Docker

O ambiente de ferramentas de projeto integrado é executado utilizando Docker.

Imagem utilizada:

```text
isaiassh/unic-cass-tools:1.1.0
```

Para verificar a instalação do Docker:

```bash
docker --version
```

Para baixar a imagem:

```bash
docker pull isaiassh/unic-cass-tools:1.1.0
```

## 4. Ferramentas utilizadas

O ambiente inclui ferramentas para projeto e simulação de circuitos integrados, incluindo:

- Xschem — criação de esquemáticos
- NGSpice — simulação elétrica
- Xyce — simulação alternativa
- KLayout — desenvolvimento e visualização de layout
- Magic — edição de layout
- OpenROAD — ferramentas de projeto físico

## 5. PDK

O projeto utiliza o processo:

```text
IHP SG13G2
```

PDK utilizado:

```text
ihp-sg13g2
```

## 6. Executando o ambiente

Entre na pasta do projeto:

```bash
cd /home/rebeca/projetos/sram/SRAM-PROJECT
```

O projeto é compartilhado com o container Docker para permitir que os arquivos sejam acessados pelas ferramentas de projeto.

Ao iniciar o container, o diretório compartilhado é acessível em:

```text
/home/designer/shared/SRAM-PROJECT
```

## 7. Salvando o progresso

Após realizar alterações importantes:

```bash
git status
git add .
git commit -m "Descrição das alterações"
git push
```

Isso envia uma cópia atualizada do projeto para o GitHub.

## 8. Estrutura da SRAM

O projeto consiste no desenvolvimento de uma célula SRAM 8T.

A estrutura inclui:

- 4 transistores formando dois inversores CMOS cruzados;
- 2 transistores de acesso para escrita;
- 2 transistores para uma porta de leitura independente.

Sinais principais:

```text
VDD  - Alimentação
GND  - Referência de terra

Q    - Nó interno da célula
QB   - Nó interno complementar

BL   - Bit Line
BLB  - Bit Line complementar

WWL  - Write Word Line

RBL  - Read Bit Line
RWL  - Read Word Line
```

## 9. Fluxo do projeto

O desenvolvimento seguirá as seguintes etapas:

1. Esquemático da célula SRAM 8T;
2. Criação do testbench;
3. Simulação de escrita;
4. Simulação de retenção;
5. Simulação de leitura;
6. Desenvolvimento do layout;
7. Extração pós-layout;
8. Simulações pós-layout;
9. Análise dos resultados;
10. Preparação do artigo para o congresso.
