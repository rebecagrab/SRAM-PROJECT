## Atualização – Desenvolvimento do Layout da SRAM 8T

### Etapa realizada: Exploração e validação do layout do transistor NMOS

Nesta etapa foi realizada a exploração do ambiente de layout físico utilizando a ferramenta Magic, configurada com a tecnologia IHP SG13G2.

Inicialmente, foram realizados testes para abertura e manipulação da célula de layout da SRAM (`sram8t_layout`). Durante o processo, foi identificado que a criação de uma nova célula vazia não era necessária para o desenvolvimento do transistor, pois o PDK já disponibiliza dispositivos parametrizados prontos para utilização.

Foi então utilizado um transistor NMOS do PDK, identificado como:

`sg13_lv_nmos_BTVQUG`

O dispositivo foi inserido e analisado dentro do ambiente Magic.

### Verificação das conexões

Através da seleção das regiões do dispositivo e da utilização do comando `what`, foram identificadas as principais conexões do transistor:

- Gate (G): conectado à camada `polycont`;
- Drain (D): conectado à região `ndiffc`;
- Source (S): conectado à região `ndiffc`.

Também foram identificadas as seguintes camadas presentes no dispositivo:

- nmos;
- ndiff;
- ndiffc;
- poly;
- polycont;
- metal1;
- via1;
- metal2.

A análise confirmou que o dispositivo utilizado possui a estrutura física necessária para representar um transistor NMOS no processo tecnológico IHP SG13G2.

### Problemas identificados durante a prática

Durante os testes, foram encontrados alguns problemas relacionados à hierarquia de células no Magic. Em especial, ocorreu uma tentativa de criação de uma estrutura circular, gerando a mensagem:

"The edit cell is already a descendant of 'sram8t_layout', which means that you're trying to create a circular structure. This isn't legal."

Esse problema ocorreu devido à tentativa de manipular a célula principal da SRAM enquanto uma célula descendente já estava presente na hierarquia.

Também foi observado que comandos como `edit` não são adequados para carregar uma célula inexistente ou retornar diretamente para outra célula, sendo necessário compreender a diferença entre os comandos de carregamento, edição e hierarquia.

### Estado atual do projeto

Ao final desta etapa:

- O ambiente Magic está funcionando corretamente;
- A tecnologia IHP SG13G2 está carregada;
- O transistor NMOS parametrizado foi inserido e visualizado;
- As conexões de Gate, Drain e Source foram identificadas;
- As camadas físicas utilizadas pelo transistor foram verificadas;
- O layout principal da SRAM 8T continua sendo utilizado como célula de desenvolvimento;
- A próxima etapa será organizar corretamente a hierarquia da célula SRAM e inserir os transistores necessários para a implementação da arquitetura SRAM 8T.

### Próxima etapa

A próxima atividade será estruturar a célula `sram8t_layout` utilizando instâncias dos transistores NMOS e PMOS fornecidos pelo PDK, evitando a criação de estruturas hierárquicas circulares.

Após isso, será iniciado o posicionamento dos transistores que formarão os inversores cruzados e os demais elementos da arquitetura SRAM 8T.
