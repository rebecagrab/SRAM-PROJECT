# DOCUMENTAÇÃO DOS AVANÇOS — PROJETO SRAM 8T

## 1. Objetivo do projeto

Este projeto tem como objetivo o desenvolvimento e a simulação de uma célula de memória SRAM 8T utilizando ferramentas de projeto de circuitos integrados.

O desenvolvimento está sendo realizado utilizando:

- Xschem para criação dos esquemáticos;
- ngspice para simulações elétricas;
- Docker;
- ambiente UNIC-CASS;
- PDK IHP SG13G2.

A alimentação utilizada nos testes é:

- VDD = 1,2 V
- GND = 0 V

---

## 2. Estrutura do projeto

A estrutura atual do projeto é organizada da seguinte forma:

```text
SRAM-PROJECT/
├── documentation
├── layout/
├── results/
├── simulations/
├── sram8t/
│   └── schematic/
├── README.md
└── .git/
```

A principal célula desenvolvida até o momento é a SRAM 8T.

---

## 3. Desenvolvimento da célula SRAM 8T

A célula SRAM foi implementada utilizando oito transistores MOS.

### 3.1 Núcleo de armazenamento

O núcleo da memória é formado por dois inversores CMOS cruzados.

Os transistores utilizados são:

- 2 NMOS para os inversores;
- 2 PMOS para os inversores.

Os nós internos de armazenamento são:

- Q
- QB

Esses nós armazenam valores complementares:

- Q = 1,2 V e QB = 0 V;
ou
- Q = 0 V e QB = 1,2 V.

---

## 4. Circuito de escrita

A operação de escrita utiliza transistores de acesso controlados pela linha:

- WWL — Write Word Line.

As linhas de dados utilizadas são:

- BL;
- BLB.

Durante a ativação da WWL, os valores presentes nas linhas BL e BLB podem alterar o estado armazenado nos nós Q e QB.

---

## 5. Circuito de leitura

A SRAM 8T possui uma porta de leitura separada do circuito de armazenamento.

Os principais sinais utilizados são:

- RWL — Read Word Line;
- RBL — Read Bit Line.

A estrutura de leitura foi implementada com dois transistores NMOS em série.

A operação ocorre da seguinte forma:

Quando:

- RWL = 1;
- Q = 1;

é criado um caminho condutivo entre RBL e GND.

Assim, a linha RBL pode descarregar.

Quando:

- RWL = 1;
- Q = 0;

o caminho de descarga permanece desligado e a RBL deve permanecer carregada.

---

## 6. Testbench desenvolvido

Foi criado o arquivo:

```text
sram8t/schematic/sram8t_tb.sch
```

O testbench possui:

- fonte de alimentação VDD;
- fontes para as linhas BL e BLB;
- pulsos para WWL;
- pulsos para RWL;
- circuito de pré-carga da RBL;
- capacitor de carga na RBL;
- condições iniciais para os nós internos Q e QB.

---

## 7. Modelo tecnológico

O modelo de transistores utilizado pertence ao PDK IHP SG13G2.

A biblioteca é carregada através do comando:

```spice
.lib /opt/pdks/ihp-sg13g2/libs.tech/ngspice/models/cornerMOSlv.lib mos_tt
```

Os transistores utilizados incluem:

```text
sg13_lv_nmos
sg13_lv_pmos
```

Com dimensões utilizadas nos testes:

```text
W = 0,15 µm
L = 0,13 µm
```

---

## 8. Configuração da simulação

A análise transitória utilizada inicialmente foi:

```spice
.tran 10p 20n uic
```

Foram utilizados diferentes estados iniciais para verificar o comportamento da memória.

### Estado armazenado 1

```spice
.ic v(x1.q)=1.2
.ic v(x1.qb)=0
```

### Estado armazenado 0

```spice
.ic v(x1.q)=0
.ic v(x1.qb)=1.2
```

---

## 9. Pré-carga da Read Bit Line

Foi implementado um circuito de pré-carga utilizando um transistor PMOS.

A função desse circuito é carregar a linha RBL para aproximadamente:

```text
1,2 V
```

antes da operação de leitura.

O circuito utiliza:

- um transistor PMOS conectado entre VDD e RBL;
- um sinal PRE para controlar o transistor;
- um capacitor conectado à RBL para representar a carga da linha.

A configuração conceitual é:

```text
VDD
 │
PMOS
 │
RBL
 │
Capacitor
 │
GND
```

Durante a pré-carga:

```text
RBL → aproximadamente 1,2 V
```

Durante a leitura, o PMOS deve permanecer desligado para permitir a descarga da RBL quando necessário.

---

## 10. Problemas encontrados e correções realizadas

Durante o desenvolvimento foram encontrados alguns problemas importantes.

### 10.1 Caminhos incorretos

Inicialmente houve tentativas de acessar o projeto utilizando caminhos incorretos.

O caminho correto dentro do container Docker é:

```text
/home/designer/shared/SRAM-PROJECT
```

O projeto no ambiente WSL é montado no container através do Docker.

---

### 10.2 Nós flutuantes

Durante a implementação da pré-carga ocorreram erros de matriz singular:

```text
Warning: singular matrix: check node
```

Esses erros estavam relacionados a conexões incorretas e nós sem uma conexão elétrica válida.

As conexões foram revisadas e corrigidas até que a simulação transitória pudesse ser executada corretamente.

---

### 10.3 Erros de vetores no ngspice

Também ocorreram erros como:

```text
Error: no such vector
```

Isso aconteceu quando foram utilizados nomes de nós que não correspondiam ao netlist atual.

Após verificar o netlist gerado pelo Xschem, os comandos de plotagem foram ajustados.

---

## 11. Resultados obtidos

A simulação transitória está funcionando corretamente.

Foram obtidas curvas para:

- Q;
- QB;
- RWL;
- RBL;
- sinais relacionados à pré-carga.

Os resultados mostraram:

1. a inicialização dos nós internos Q e QB;
2. a ativação da RWL;
3. a pré-carga da RBL;
4. a possibilidade de observar o comportamento da linha de leitura durante a janela de leitura.

---

## 12. Estado atual do projeto

Neste momento, o projeto possui:

- célula SRAM 8T criada;
- esquemático funcional;
- testbench criado;
- modelos do PDK carregados corretamente;
- alimentação de 1,2 V configurada;
- sinais de escrita e leitura implementados;
- circuito de pré-carga da RBL implementado;
- simulações transitórias funcionando;
- condições iniciais de Q e QB sendo testadas;
- resultados gráficos gerados.

---

## 13. Próximos passos

Os próximos passos do desenvolvimento são:

### 13.1 Finalizar a validação da leitura

Realizar e comparar os dois casos:

**Caso A:**

```text
Q = 1
QB = 0
```

Resultado esperado:

```text
RWL ativa → RBL descarrega
```

**Caso B:**

```text
Q = 0
QB = 1
```

Resultado esperado:

```text
RWL ativa → RBL permanece carregada
```

---

### 13.2 Organizar os sinais temporais

Ajustar os tempos dos sinais:

- PRE;
- RWL;
- WWL.

O objetivo é garantir uma sequência clara:

```text
1. Pré-carga da RBL
2. Desativação da pré-carga
3. Ativação da RWL
4. Leitura do estado armazenado
```

---

### 13.3 Registrar os resultados

Salvar os gráficos mais importantes na pasta:

```text
results/
```

Os resultados devem incluir:

- leitura de Q = 1;
- leitura de Q = 0;
- comportamento da RBL;
- comportamento das linhas de controle.

---

## 14. Conclusão parcial

O projeto avançou da configuração inicial do ambiente até a criação e simulação de uma célula SRAM 8T com circuito de leitura e pré-carga.

A infraestrutura de simulação está funcionando corretamente e o próximo objetivo é finalizar a validação experimental da operação de leitura através da comparação dos dois estados armazenados.

O projeto continuará com ajustes no timing dos sinais, validação da leitura e organização dos resultados para documentação técnica e futuras etapas de projeto físico.
