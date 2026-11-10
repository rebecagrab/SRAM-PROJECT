## Resultados da Simulação da SRAM 8T

### Configuração da simulação

A célula SRAM 8T foi simulada utilizando o **ngspice** com o PDK **IHP SG13G2** e modelos MOS do corner típico (`mos_tt`).

A alimentação utilizada foi:

- **VDD:** 1,2 V
- **GND:** 0 V
- **Análise:** Transiente (`.tran`)
- **Tempo total de simulação:** 20 ns
- **Passo de simulação:** 10 ps
- **Temperatura:** 27 °C

### Operação de escrita

A operação de escrita foi realizada através da ativação da **WWL (Write Word Line)** e das bitlines correspondentes.

O tempo de escrita foi medido utilizando:

```spice
.measure tran t_write TRIG v(net3) VAL=0.6 RISE=1 TARG v(x1.q) VAL=0.6 FALL=1
```

Resultado obtido:

| Parâmetro | Resultado |
|---|---:|
| Tempo de escrita (`t_write`) | 1,748468e-11 s |
| Tempo de escrita convertido | **17,48 ps** |

### Operação de leitura

A operação de leitura foi implementada utilizando uma porta de leitura isolada da célula de armazenamento.

O caminho de leitura é composto por dois transistores NMOS:

```text
RBL → XM7 → nó interno → XM8 → GND
```

Onde:

- **XM7** é controlado pela **RWL (Read Word Line)**;
- **XM8** é controlado pelo nó interno **Q**;
- quando **RWL = 1** e **Q = 1**, existe um caminho condutivo entre a Read Bit Line (RBL) e o GND;
- consequentemente, a RBL pré-carregada descarrega, indicando a leitura do dado armazenado.

A medição do tempo de leitura foi realizada utilizando:

```spice
.measure tran t_read TRIG v(net4) VAL=0.6 RISE=1 TARG v(net6) VAL=0.6 FALL=1
```

Resultado obtido:

| Parâmetro | Resultado |
|---|---:|
| Tempo de leitura (`t_read`) | 5,688625e-10 s |
| Tempo de leitura convertido | **568,86 ps** |
| Tempo de leitura convertido | **0,569 ns** |

### Resumo dos resultados

| Operação | Tempo |
|---|---:|
| Escrita | **17,48 ps** |
| Leitura | **568,86 ps (0,569 ns)** |

### Conclusão da simulação

Os resultados obtidos confirmam o funcionamento das operações básicas da célula SRAM 8T desenvolvida.

A simulação demonstrou:

- funcionamento da operação de escrita;
- alteração do estado armazenado nos nós internos da célula;
- funcionamento da porta de leitura isolada;
- pré-carga da Read Bit Line (RBL);
- descarga da RBL durante a operação de leitura para o estado lógico correspondente;
- medição automática dos tempos de escrita e leitura utilizando comandos `.measure` do ngspice.

Os resultados atuais obtidos para esta implementação são **17,48 ps para a operação de escrita** e **568,86 ps para a operação de leitura**.

## 3. Medição de Consumo de Potência

Após a validação das operações de escrita e leitura da SRAM 8T, foi realizada uma primeira medição do consumo de potência durante a simulação transiente.

A potência média foi calculada utilizando a corrente fornecida pela fonte de alimentação `V1`, conforme a expressão:

```spice
.measure tran p_avg AVG par('-v(VDD)*i(V1)') FROM=0n TO=20n
```

A simulação foi realizada durante o intervalo de **0 ns a 20 ns**, abrangendo as operações avaliadas no testbench.

### Resultado

| Parâmetro | Resultado |
|---|---:|
| Tempo de escrita (`t_write`) | 17,48 ps |
| Tempo de leitura (`t_read`) | 568,86 ps |
| Potência média (`p_avg`) | 13,64 µW |

O valor obtido para a potência média foi:

```text
p_avg = 1.364417e-05 W
```

Portanto:

**Potência média = 13,64 µW**

### Observação

Este valor representa a potência média calculada durante toda a janela de simulação, entre **0 ns e 20 ns**. Dessa forma, a medição inclui o comportamento do circuito durante os diferentes estados presentes na simulação.

Como próxima etapa, serão realizadas medições específicas de consumo durante as operações de **escrita** e **leitura**, permitindo uma análise mais detalhada do desempenho energético da SRAM 8T.

## 4. Medição de Potência Durante as Operações

Para realizar uma análise mais detalhada do consumo da SRAM 8T, foram calculadas as potências médias em diferentes janelas temporais da simulação transiente.

A potência foi calculada a partir da tensão de alimentação e da corrente fornecida pela fonte `V1`, utilizando a expressão:

```spice
AVG par('-v(VDD)*i(V1)')
```

### 4.1 Potência média total

A potência média durante toda a simulação, entre **0 ns e 20 ns**, foi:

| Medição | Resultado |
|---|---:|
| Potência média total | **13,64 µW** |

### 4.2 Potência durante a operação de escrita

A operação de escrita foi analisada na janela entre **12 ns e 17 ns**.

```spice
.measure tran p_write AVG par('-v(VDD)*i(V1)') FROM=12n TO=17n
```

Resultado:

**p_write = 2.930375e-07 W**

Portanto:

**Potência média durante a escrita = 0,293 µW**

### 4.3 Potência durante a operação de leitura

A operação de leitura foi analisada na janela entre **5 ns e 10 ns**.

```spice
.measure tran p_read AVG par('-v(VDD)*i(V1)') FROM=5n TO=10n
```

Resultado:

**p_read = 4.932231e-05 W**

Portanto:

**Potência média durante a leitura = 49,32 µW**

### 4.4 Resumo dos resultados

| Parâmetro | Resultado |
|---|---:|
| Tempo de escrita | **17,48 ps** |
| Tempo de leitura | **568,86 ps** |
| Potência média total | **13,64 µW** |
| Potência média durante a escrita | **0,293 µW** |
| Potência média durante a leitura | **49,32 µW** |

### Observação

Os valores apresentados correspondem à potência média fornecida pela fonte de alimentação `V1` durante as respectivas janelas temporais. Os resultados serão posteriormente utilizados para comparação com a implementação da SRAM 10T.

# Resultados Consolidados — SRAM 8T

## 1. Condições da Simulação

A célula SRAM 8T foi simulada nas seguintes condições:

| Parâmetro | Valor |
|---|---|
| Tecnologia | IHP SG13G2 |
| Corner dos transistores MOS | `mos_tt` |
| Tensão de alimentação | 1,2 V |
| Temperatura | 27 °C |
| Tipo de análise | Transiente |
| Tempo total de simulação | 20 ns |
| Passo máximo de simulação | 10 ps |
| Arquitetura | SRAM 8T |

As simulações foram realizadas utilizando os modelos de transistores MOS de baixa tensão da tecnologia IHP SG13G2.

---

## 2. Operação de Escrita

A operação de escrita foi ativada por meio da **Write Word Line (`WWL`)**.

O atraso de escrita medido foi:

```text
t_write = 1.748468e-11 s
```

Convertendo para picossegundos:

```text
t_write ≈ 17,48 ps
```

Durante a operação de escrita, os nós internos de armazenamento mudaram corretamente de estado:

- `Q`: aproximadamente **1,2 V → 0 V**
- `QB`: aproximadamente **0 V → 1,2 V**

### Resultado

A célula SRAM 8T conseguiu alterar e armazenar corretamente o novo estado lógico.

**Operação de escrita: APROVADA ✅**

---

## 3. Operação de Leitura

A operação de leitura foi ativada por meio da **Read Word Line (`RWL`)**.

O atraso de leitura medido foi:

```text
t_read = 5.686825e-10 s
```

Convertendo para picossegundos:

```text
t_read ≈ 568,68 ps
```

Durante a operação de leitura, os nós internos de armazenamento permaneceram estáveis.

### Resultado

A informação armazenada foi preservada durante a operação de leitura.

**Operação de leitura não destrutiva: APROVADA ✅**

---

## 4. Consumo Médio de Potência

O consumo médio de potência foi medido considerando todo o intervalo de simulação, de **0 ns a 20 ns**.

Comando utilizado:

```spice
.measure tran p_avg AVG par('-v(VDD)*i(V1)') FROM=0n TO=20n
```

Resultado:

```text
P_avg = 1.364417e-05 W
```

Convertendo para microwatts:

```text
P_avg ≈ 13,64 µW
```

---

## 5. Consumo de Potência Durante a Escrita

O consumo de potência durante a operação de escrita foi medido no intervalo de **12 ns a 17 ns**.

Comando utilizado:

```spice
.measure tran p_write AVG par('-v(VDD)*i(V1)') FROM=12n TO=17n
```

Resultado:

```text
P_write = 2.930375e-07 W
```

Convertendo para microwatts:

```text
P_write ≈ 0,293 µW
```

---

## 6. Consumo de Potência Durante a Leitura

O consumo de potência durante a operação de leitura foi medido no intervalo de **5 ns a 10 ns**.

Comando utilizado:

```spice
.measure tran p_read AVG par('-v(VDD)*i(V1)') FROM=5n TO=10n
```

Resultado:

```text
P_read = 4.932231e-05 W
```

Convertendo para microwatts:

```text
P_read ≈ 49,32 µW
```

---

## 7. Análise de Estabilidade Funcional

A simulação transiente também foi utilizada para verificar a estabilidade funcional da célula SRAM 8T.

### Estado Inicial

A célula foi inicializada com:

```text
Q = 1,2 V
QB = 0 V
```

Os nós complementares de armazenamento representaram corretamente o estado lógico armazenado.

### Estabilidade Durante a Leitura

Durante a operação de leitura:

- A **Read Word Line (`RWL`)** foi ativada.
- A leitura ocorreu pelo caminho de leitura dedicado.
- Os nós internos `Q` e `QB` mantiveram seus valores armazenados.

Isso confirma que a operação de leitura não alterou o dado armazenado durante o intervalo analisado.

**Leitura não destrutiva: CONFIRMADA ✅**

### Estabilidade Durante a Escrita

Durante a operação de escrita:

- A **Write Word Line (`WWL`)** foi ativada.
- O estado anteriormente armazenado foi alterado corretamente.
- Os nós `Q` e `QB` inverteram seus estados.
- O novo estado permaneceu armazenado após a operação.

**Escrita e retenção do novo estado: CONFIRMADAS ✅**

### Resultado

A célula SRAM 8T demonstrou:

- Armazenamento correto de dados.
- Operação de escrita funcional.
- Operação de leitura não destrutiva.
- Retenção do novo estado após a escrita.

**Estabilidade funcional: APROVADA ✅**

> **Observação:** Esta análise representa uma verificação funcional de estabilidade por meio de simulação transiente. Uma caracterização mais completa da estabilidade de uma SRAM pode incluir análises como **Static Noise Margin (SNM)**, curva borboleta, margem de escrita e variações de Processo, Tensão e Temperatura (PVT).

---

# 8. Resumo Consolidado dos Resultados

| Métrica | Resultado |
|---|---:|
| **Tempo de escrita** | **17,48 ps** |
| **Tempo de leitura** | **568,68 ps** |
| **Potência média** | **13,64 µW** |
| **Potência durante a escrita** | **0,293 µW** |
| **Potência durante a leitura** | **49,32 µW** |
| **Operação de escrita** | **APROVADA ✅** |
| **Leitura não destrutiva** | **APROVADA ✅** |
| **Retenção de dados** | **APROVADA ✅** |
| **Estabilidade funcional** | **APROVADA ✅** |

---

# Conclusão

A célula **SRAM 8T** foi implementada e simulada com sucesso em nível esquemático utilizando a tecnologia **IHP SG13G2**.

As simulações confirmaram o funcionamento correto das operações de escrita e leitura, a preservação do dado armazenado durante a leitura e o armazenamento correto do novo estado após a operação de escrita.

Os principais resultados obtidos foram:

- **Tempo de escrita:** 17,48 ps
- **Tempo de leitura:** 568,68 ps
- **Potência média:** 13,64 µW
- **Potência durante a escrita:** 0,293 µW
- **Potência durante a leitura:** 49,32 µW

Esses resultados serão utilizados como **linha de base** para as próximas etapas do projeto, incluindo o desenvolvimento do layout físico da SRAM 8T, as simulações pós-layout e a futura comparação com uma arquitetura SRAM 10T.
