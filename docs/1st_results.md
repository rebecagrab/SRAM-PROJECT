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
