# Ns-3-simulations
### Tarefas pendendes:
- [x] Limpar e organizar datasets
- [x]  Refazer arquivos df.py para adcionar.
- [ ]  Implementar o Algoritmo de Batman.
- [ ] Terminar a documentação do batman
- [ ]  Implementar as Entradas da simulação em CSV.


## Cabeçalho
Ns-3 é um simulador de redes de eventos discretos para sistemas de Internet, direcionado principalmente para pesquisa e uso educacional. O ns-3 é um software gratuito e de código aberto, licenciado sob a licença GNU GPLv2 e mantido por uma comunidade mundial.

## mmWave: Módulo do ns-3
- Este é um módulo ns-3 para simulação de redes celulares 5G operando em mmWaves. Uma descrição deste módulo pode ser encontrada neste artigo.
- Principais características:
- Suporte a uma ampla gama de modelos de canais, incluindo o modelo baseado em 3GPP TR 38.901 para frequências entre 0,5 e 100 GHz. Ray tracing e traços medidos também podem ser usados.
- Classes PHY e MAC personalizadas que suportam a estrutura e numerologias de quadros 3GPP NR.
- Agendadores personalizados para suporte a formatos TDD dinâmicos
- Agregação de operadora na camada MAC
- Melhorias na camada RLC com ressegmentação de pacotes para retransmissões
- Conectividade dupla com estações base LTE, com transferência rápida de células secundárias e rastreamento de canal
- Simulação de elementos centrais da rede (também com o MME como nó real)

Para mais informações sobre o módulo ns3 e possivel encontrar em [mmWave-Ns3](https://github.com/nyuwireless-unipd/ns3-mmwave)

## RxPacketTrace
### RxPacketTrace é responsável para fazer o monitoramento dos pacotes que são transmitidos na simulação. Cada coluna do arquivo contém informações específicas sobre os pacotes que foram transmitidos (DL-Downlink) e os pacotes Recebidos (UL-Uplink)

- **DL/UL** - Indica o estado do pacote, se ele se encontra em Downlink ou em Uplink. Downlink é a transmissão do pacote pela estação-base e Uplink é a transmissão do pacote pelo usuário para a estação-base
- **Time**: O timestamp (em segundos) em que o evento (transmissão ou recepção do pacote) ocorreu.
- **Frame**: O número do quadro (frame) em que a transmissão ou recepção ocorreu. Quadros são unidades de tempo na estrutura temporal de LTE/5G.
- **subF**: Subframe em que a transmissão ou recepção ocorreu. Um frame é dividido em subframes.
- **slot:** Slot no subframe em que a transmissão ou recepção ocorreu. Cada subframe é dividido em slots.
- **1stSym:** Primeiro símbolo da transmissão ou recepção no slot.
- **symbol#:** Número de símbolos envolvidos na transmissão ou recepção.
- **cellId:** ID da célula à qual a transmissão ou recepção está associada. Em redes LTE/5G, cada célula tem um identificador único.
- **rnti:** Radio Network Temporary Identifier (RNTI), que é um identificador temporário usado para identificar o equipamento do usuário (UE) na rede.
- **ccId:** Component Carrier ID, usado em sistemas de agregação de portadoras onde múltiplas portadoras de frequência podem ser utilizadas simultaneamente.
- **tbSize:** Transport Block Size, que é o tamanho do bloco de transporte em bits. Este valor indica a quantidade de dados transmitidos ou recebidos.
- **mcs:** Modulation and Coding Scheme, que indica o esquema de modulação e codificação utilizado para a transmissão. MCS é um parâmetro que influencia a taxa de transmissão de dados e a robustez contra erros.
- **rv:** Redundancy Version, que é usada para identificar diferentes versões redundantes do bloco de transporte no HARQ (Hybrid Automatic Repeat Request) para correção de erro.
- **SINR(dB):** Signal to Interference plus Noise Ratio em decibéis. É a medida de qualidade do sinal que foi recebido pelos nós de usuário.
- **corrupt:** Indicador binário (0 ou 1) que mostra se o pacote foi corrompido (1) ou não (0) durante a transmissão.
- **TBler:** Transport Block Error Rate, que é a taxa de erro do bloco de transporte. Indica a proporção de blocos de transporte que foram recebidos com erro.

![image](https://github.com/Hiarleyy/Ns-3-simulations/assets/111695591/2177e459-496d-4d2d-a01d-f03cea067d53)

# DlRLcStats
### O arquivo DlRlcStats serve para analisar o desempenho da camada RLC (Radio Link Control) no enlace descendente (DL - Downlink) em uma simulação de rede realizada com o ns-3. Ele contém métricas detalhadas que permitem avaliar e entender o comportamento da transmissão de dados na rede.

- **% start**: Início do intervalo de tempo (em segundos) para as estatísticas registradas.**end**: Fim do intervalo de tempo (em segundos) para as estatísticas registradas.
- **CellId**: Identificação da célula onde os dados foram registrados.
- **IMSI**: Identidade Internacional de Assinante Móvel (International Mobile Subscriber Identity) do usuário.
- **RNTI**: Identificador Temporário de Rede de Rádio (Radio Network Temporary Identifier) do usuário.
- **LCID**: Identificador de Canal Lógico (Logical Channel Identifier), usado para diferenciar diferentes fluxos de dados.
- **nTxPDUs**: Número de unidades de dados de protocolo (PDUs) transmitidas.
- **TxBytes**: Número de bytes transmitidos.
- **nRxPDUs**: Número de PDUs recebidas.
- **RxBytes**: Número de bytes recebidos.
- **delay**: Atraso médio (em segundos) das PDUs.
- **stdDev**: Desvio padrão do atraso das PDUs.
- **min**: Menor valor de atraso (em segundos) registrado.
- **max**: Maior valor de atraso (em segundos) registrado.
- **PduSize**: Tamanho médio das PDUs (em bytes).
- **stdDev.1**: Desvio padrão do tamanho das PDUs.
- **min.1**: Menor tamanho de PDU registrado (em bytes).
- **max.1**: Maior tamanho de PDU registrado (em bytes).

![image](https://github.com/Hiarleyy/Ns-3-simulations/assets/111695591/cd2436ee-cf0b-4368-8434-176ba3ec8eb5)



#### [Algoritmo Batman](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/Documenta%C3%A7%C3%A3o/bat.md)


# Contato
- Marcos Hiarley <marcoshiarley.silva@gmail.com>
- Robert Gabriel <robertgabriel@disroot.org>


