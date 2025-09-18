tags: #fleeting #5g #ns3 #project 
Created:2024-06-20, Thu Jun 4 - 19:31
Week-number:25

**Language / Idioma:** [🇺🇸 English](Docker-MmWave_ENG.md) | [🇧🇷 Português](Docker-MmWave.md)

## Resumo:

- Foi desenvolvida uma imagem em docker para facilitar a utilização do simulador Ns3, é possível ter acesso a imagem personalizada do projeto em : https://hub.docker.com/r/hiarley/ns3-mmwave/tags
- Versão do Mmwave : (mmwave-8.0)
 -  Versão do Ns-3 : (Ns-3 3.42) 

## Como utilizar a imagem ?
- Após verificar todos os requisitos de utilização do Docker Desktop, você pode utilizar o seguinte comando para acessar essa imagem:

```Bash
docker pull hiarley/ns3-mmwave
```
-  Para iniciar um container utilizando essa imagem é necessário utilizar o comando ``docker run`` da seguinte forma:

```bash
docker run --name ns3-container -it hiarley/ns3-mmwave
```

- Dessa forma você irá criar um container com o nome ns3-container, e para executá-lo, você pode utilizar:
```bash
docker exec -it ns3-container bash
```

## **Compiladores e Ferramentas de Desenvolvimento**:

- **GCC**: GNU Compiler Collection (GCC) versão 4.9 ou superior. A versão recomendada é o GCC 9.3.0 ou superior.
- **G++**: Compilador C++ associado ao GCC.
- **Python**: Python 3.6 ou superior para scripts de configuração e execução.
- **Ranger:** Terminal personalizado para facilitar a visualização e mudança dos arquivos 
- **Fish**: Terminal utilizado para completar comandos do Linux
- **Vim**: Editor de texto para mudanças no código - ( Pode Ser Substituído pelo Nano)

## **Bibliotecas Necessárias**:

- **GNU C Library** (glibc) versão 2.27 ou superior.
- **CMake** versão 3.10 ou superior para construir alguns módulos opcionais.
- **pkg-config** para facilitar a configuração das bibliotecas dependentes.
- **libsqlite3-dev** para suporte a SQLite.
- **libxml2-dev** para suporte ao XML.
- **libgtk-3-dev** e **libgtk2.0-0** para a interface gráfica (opcional).
- **libpcap-dev** para suporte à captura de pacotes.
- **libgsl-dev** para bibliotecas GNU Scientific Library.
- **libbz2-dev** para suporte a compressão bzip2.
- **libboost-all-dev** para várias funcionalidades de suporte (opcional).

## **Ferramentas Opcionais**:

- **Netanim**: Para animação de simulações, requer a biblioteca Qt4 ou Qt5.
- **GNUplot**: Para geração de gráficos.
- **Tcpdump**: Para captura e análise de pacotes.
## Shellscript Para o NS3
- A imagem do projeto também adiciona dois arquivos para facilitar o uso do programa
	reload.sh -- Renova o arquivo Packet.cc para ser buildado novamente
	move-files.sh -- Move os arquivos de output para uma pasta chamada dataframe
## **Módulos de Desenvolvimento**
- Ns3-Mmwave: (https://github.com/nyuwireless-unipd/ns3-mmwave) -- **Versão 8.0** 
- ---
Reference:

https://ieeexplore.ieee.org/document/8344116/
