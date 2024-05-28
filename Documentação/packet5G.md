# Packet_5G
## Execução do programa

para realizar a execução do programa e fazer as simulações desejadas é necessário instalar as dependências do programa:
1. [ Network Simulator (Ns3)](https://www.nsnam.org/)
2. [Mmwave Module](https://github.com/nyuwireless-unipd/ns3-mmwave)
é possivel instalar o simulador e o respectivo modulo separadamente, ou então acessar por meio de um docker https://hub.docker.com/r/fedeit/ns3-mmwave, a qual o simulador já se encontra configurado e pronto para uso.

#### Instalando o Simulador Ns3 com o Módulo mmWave:
No repositório oficial do módulo [mmWave](https://github.com/nyuwireless-unipd/ns3-mmwave) para o Network Simulator se encontra o manual detalhado para instalar o simulador juntamente com o mmwave. Para realizar a instalação é necessário executar os seguintes passos:


~~~~bash
git clone https://github.com/nyuwireless-unipd/ns3-mmwave.git
cd ns3-mmwave
./ns3 configure --disable-python --enable-examples && ./ns3 build
~~~~

Para verificar se todos os módulos foram instalados corretamente, com o seguinte comando e possível rodar a seguinte simulação de exemplo:

~~~~bash
./ns3 run mmwave-simple-epc
~~~~
---
## Código da simulação (Packet5G.cc)

O network simulator utiliza como linguagem principal o C++, onde para compilar a simulação é necessário que o arquivo seja construído antes de ser executado, para isso e necessário rodar o seguinte código no prompt:

~~~bash
./ns3 build Packet5G.cc
~~~

- Includes Utilizados no Projeto
```cpp
  #include "ns3/core-module.h"
  #include "ns3/network-module.h"
  #include "ns3/internet-module.h"
  #include "ns3/applications-module.h"
  #include "ns3/mobility-module.h"
  #include <ns3/buildings-helper.h>
  #include "ns3/config-store.h"
  #include "ns3/mmwave-helper.h"
  #include "ns3/ipv4-global-routing-helper.h"
  #include "ns3/applications-module.h"
  #include "ns3/log.h"
  #include "ns3/isotropic-antenna-model.h"
  #include <map>
  #include "ns3/netanim-module.h"
  #include "ns3/flow-monitor.h"
  #include "ns3/flow-monitor-helper.h"
  #include "ns3/mmwave-point-to-point-epc-helper.h"
  #include "ns3/point-to-point-helper.h"
  #include "ns3/global-route-manager.h"

  using namespace ns3;
  using namespace mmwave;
```


- Funções responsáveis pelo monitoramento dos pacotes transmitidos 
~~~~cpp
void
TxMacPacketTraceUe (Ptr<OutputStreamWrapper> stream, uint16_t rnti, uint8_t ccId, uint32_t size)
{
  *stream->GetStream () << Simulator::Now ().GetSeconds () << "\t" << (uint32_t)ccId << '\t' << size << std::endl;

}
void
Traces (std::string filePath)
{
  std::string path = "/NodeList/*/DeviceList/*/ComponentCarrierMapUe/*/MmWaveUeMac/TxMacPacketTraceUe";

  filePath = filePath + "TxMacPacketTraceUe.txt";

  AsciiTraceHelper asciiTraceHelper;

  Ptr<OutputStreamWrapper> stream1 = asciiTraceHelper.CreateFileStream (filePath);

  *stream1->GetStream () << "Time" << "\t" << "CC" << '\t' << "Packet size" << std::endl;

  Config::ConnectWithoutContextFailSafe (path, MakeBoundCallback (&TxMacPacketTraceUe, stream1));
}
~~~~

- Definição dos parâmetros de simulação, criação dos objetos e valores padrões
~~~~cpp
//Função principal
int
main (int argc, char *argv[])
{
  bool blockage = false;
  bool useEpc = true;
  double totalBandwidth = 200e6;
  double frequency = 26.0e9; //Definição da frequencia do cenário
  double simTime = 60; // tempo de simulação
  std::string condition = "l";
  
  // Valores padrão da simulação -- Podem ser alterados indicando a variavel desejada no argumento do inicio da simulação

  CommandLine cmd;
  cmd.AddValue ("blockage", "If enabled blockage = true", blockage);
  cmd.AddValue ("frequency", "CC central frequency", frequency);
  cmd.AddValue ("totalBandwidth", "System bandwidth in Hz", totalBandwidth);
  cmd.AddValue ("simTime", "Simulation time", simTime);
  cmd.AddValue ("useEpc", "If enabled use EPC, else use RLC saturation mode", useEpc);

  cmd.AddValue ("condition", "Channel condition, l = LOS, n = NLOS, otherwise the condition is randomly determined", condition);

  cmd.Parse (argc, argv);

  Time::SetResolution (Time::NS);

  //Criação de Objetos

  Ptr<MmWavePhyMacCommon> phyMacConfig0 = CreateObject<MmWavePhyMacCommon> ();
  phyMacConfig0->SetBandwidth (totalBandwidth);
  phyMacConfig0->SetCentreFrequency (frequency);
  Ptr<MmWaveComponentCarrier> cc0 = CreateObject<MmWaveComponentCarrier> ();
  cc0->SetConfigurationParameters (phyMacConfig0);
  cc0->SetAsPrimary (true);
  std::map<uint8_t, MmWaveComponentCarrier> ccMap;
  ccMap [0] = *cc0;

  //criação e definição padrão dos Helpers
  Config::SetDefault ("ns3::MmWaveHelper::ChannelModel",StringValue ("ns3::ThreeGppSpectrumPropagationLossModel"));//channel model utilizado

  Config::SetDefault ("ns3::ThreeGppChannelModel::Scenario", StringValue ("UMa")); //Definição do cenário de aplicação

  Config::SetDefault ("ns3::ThreeGppChannelModel::Blockage", BooleanValue (blockage)); //Habilitar/Desabilitar para modelo de Blockage

  Config::SetDefault ("ns3::MmWaveHelper::PathlossModel",StringValue ("ns3::ThreeGppUmaPropagationLossModel"));
   // por padrão, antenas isotrópicas são usadas. Para usar o padrão de radiação 3GPP, use o <ThreeGppAntennaArrayModel>.É necessária a configuração adequada dos ângulos de rolamento e inclinação
  Config::SetDefault ("ns3::PhasedArrayModel::AntennaElement", PointerValue (CreateObject<IsotropicAntennaModel> ()));
~~~~


- Criação do EPC para a simulação. O EPC é uma parte crucial da infraestrutura de rede em simulações LTE/5G, permitindo que as simulações no ns-3 reflitam mais fielmente o comportamento de uma rede real. Ele proporciona funções essenciais de gerenciamento de sessões, roteamento de dados, políticas de QoS, autenticação e mobilidade, garantindo uma comunicação eficiente e contínua para os usuários móveis.
~~~~cpp
  Ptr<MmWaveHelper> helper = CreateObject<MmWaveHelper> ();
  helper->SetCcPhyParams (ccMap);
  if (condition == "l")
  {
    helper->SetChannelConditionModelType ("ns3::AlwaysLosChannelConditionModel");
  }
  else if (condition == "n")
  {
    helper->SetChannelConditionModelType("ns3::NeverLosChannelConditionModel");

  }

  // Criação do EPC
  Ipv4Address remoteHostAddr;
  Ptr<Node> remoteHost;
  InternetStackHelper internet;
  Ptr<MmWavePointToPointEpcHelper> epcHelper;
  Ipv4StaticRoutingHelper ipv4RoutingHelper;

  if (useEpc)

    {
      epcHelper = CreateObject<MmWavePointToPointEpcHelper> ();
      helper->SetEpcHelper (epcHelper);
      //cria a Internet conectando o Host remoto ao pgw e Configura a  ferramenta de roteamento
      Ptr<Node> pgw = epcHelper->GetPgwNode ();
      
      // Criação do Host Remoto
      NodeContainer remoteHostContainer;
      remoteHostContainer.Create (1);
      internet.Install (remoteHostContainer);
      Ipv4StaticRoutingHelper ipv4RoutingHelper;
      Ipv4InterfaceContainer internetIpIfaces;
      remoteHost = remoteHostContainer.Get (0);
      
      // Criação da internet
      PointToPointHelper p2ph;
      p2ph.SetDeviceAttribute ("DataRate", DataRateValue (DataRate("10Gb/s")));
      p2ph.SetDeviceAttribute ("Mtu", UintegerValue (1500));
      p2ph.SetChannelAttribute ("Delay", TimeValue (Seconds (0.001)));
      NetDeviceContainer internetDevices = p2ph.Install (pgw, remoteHost);
      Ipv4AddressHelper ipv4h;
      ipv4h.SetBase ("1.0.0.0", "255.255.0.0");
      internetIpIfaces = ipv4h.Assign (internetDevices);
      // interface 0 é localhost, 1 é p2p device

      remoteHostAddr = internetIpIfaces.GetAddress (1);
      Ptr<Ipv4StaticRouting> remoteHostStaticRouting = ipv4RoutingHelper.GetStaticRouting (remoteHost->GetObject<Ipv4> ());
      remoteHostStaticRouting->AddNetworkRouteTo (Ipv4Address ("7.0.0.0"), Ipv4Mask ("255.255.0.0"), 1);

    }
~~~~

- Instalação do Nó de Estação Base e definição de mobilidade. a Estação base é responsável pela transmissão do sinal para os nós de Usuários. 
~~~~cpp
// Criação do EnbNode (Estação-base)
  NodeContainer enbNodes;
  enbNodes.Create (1);


  // Definindo a Mobilidade do EnbNode
  Ptr<ListPositionAllocator> enbPositionAlloc = CreateObject<ListPositionAllocator> ();
  enbPositionAlloc->Add (Vector (10.0, 10.0, 15.0));
  
  MobilityHelper enbmobility;
  enbmobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  enbmobility.SetPositionAllocator (enbPositionAlloc);
  enbmobility.Install (enbNodes);
  BuildingsHelper::Install (enbNodes);
  
  // Instalando o Enb
  NetDeviceContainer enbNetDevices = helper->InstallEnbDevice (enbNodes);
  std::cout << "eNB device installed" << std::endl;
~~~~

- Criação dos Uenodes , a qual representam os usuários da rede 5G. Para essa simulação foram definidos 10 usuários com mobilidade constante, com as coordenadas sendo determinadas pelo algoritmo de Batman. 
~~~~cpp
  // Criação dos Uenodes (Users)
  NodeContainer ueNodes;
  ueNodes.Create (10);  // Criando 10 UeNodes

  // Definindo a mobilidade dos UeNodes (Posição constante)
  MobilityHelper uemobility;
  uemobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  // Definição de coordenadas para cada nó -- (coordenadas do algoritmo BATMAN)
  Ptr<ListPositionAllocator> uePositionAlloc = CreateObject<ListPositionAllocator> ();

  uePositionAlloc->Add (Vector (50.0, 50.0, 1.6)); // Position for UE 1
  uePositionAlloc->Add (Vector (100.0, 100.0, 1.6)); // Position for UE 2
  uePositionAlloc->Add (Vector (30.0, 80.0, 1.6)); // Position for UE 3
  uePositionAlloc->Add (Vector (32.0, 10.0, 1.6)); // Position for UE 4
  uePositionAlloc->Add (Vector (90.0, 44.0, 1.6)); // Position for UE 5

  uePositionAlloc->Add (Vector (12.0, 34.0, 1.6)); // Position for UE 6
  uePositionAlloc->Add (Vector (9.0, 13.0, 1.6)); // Position for UE 7
  uePositionAlloc->Add (Vector (34.0, 34.0, 1.6)); // Position for UE 8
  uePositionAlloc->Add (Vector (27.0, 67.0, 1.6)); // Position for UE 9
  uePositionAlloc->Add (Vector (72.0, 78.0, 1.6)); // Position for UE 10

  uemobility.SetPositionAllocator (uePositionAlloc);
  uemobility.Install (ueNodes);
  BuildingsHelper::Install (ueNodes);

  // Imprime as coordenadas dos Uenodes
  std::cout << "UE1 position: " << ueNodes.Get (0)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE2 position: " << ueNodes.Get (1)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE3 position: " << ueNodes.Get (2)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE4 position: " << ueNodes.Get (3)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE5 position: " << ueNodes.Get (4)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE6 position: " << ueNodes.Get (5)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE7 position: " << ueNodes.Get (6)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE8 position: " << ueNodes.Get (7)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE9 position: " << ueNodes.Get (8)->GetObject<MobilityModel> ()->GetPosition () << std::endl;
  std::cout << "UE10 position: " << ueNodes.Get (9)->GetObject<MobilityModel> ()->GetPosition () << std::endl;

  // Instalando os UeDevices
  NetDeviceContainer ueNetDevices = helper->InstallUeDevice (ueNodes);
  std::cout << "UE devices installed" << std::endl;
~~~~


- Instalação do Protocolo Ip e definição do Gateway Padrão para cada um dos Nós de Usuário.
~~~~cpp
if (useEpc)

    {
      //Instalando o protocolo IP nos Uenodes
      internet.Install (ueNodes);
      Ipv4InterfaceContainer ueIpIface;
      ueIpIface = epcHelper->AssignUeIpv4Address (ueNetDevices);
      // Atribui os endereços IP e Instala as aplicações nos Uenodes

      // Definindo o Gateway padrão para os Uenodes --- Estrutura similar para os outros Uenodes
      Ptr<Ipv4StaticRouting> ueStaticRouting1 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (0)->GetObject<Ipv4> ());
      ueStaticRouting1->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//1
      Ptr<Ipv4StaticRouting> ueStaticRouting2 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (1)->GetObject<Ipv4> ());
      ueStaticRouting2->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//2
      Ptr<Ipv4StaticRouting> ueStaticRouting3 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (2)->GetObject<Ipv4> ());
      ueStaticRouting3->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//3
      /*
      .
      .
      .
      */

      ueStaticRouting5->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//10
      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);
~~~~
- Definição das aplicações dos Uenodes e Host remoto. A estrutura se repete para os demais Uenodes.
~~~~cpp
// Instala e inicia as aplicações nos Uenodes e Host remoto -- Estrutura Similar para os demais Uenodes

      uint16_t dlPort = 1234;
      uint16_t ulPort = 2000;
      ApplicationContainer clientApps;
      ApplicationContainer serverApps;
      uint16_t interPacketInterval = 10;


      PacketSinkHelper dlPacketSinkHelper ("ns3::UdpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), dlPort));
      PacketSinkHelper ulPacketSinkHelper ("ns3::UdpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), ulPort));
      serverApps.Add (dlPacketSinkHelper.Install (ueNodes.Get (0)));
      serverApps.Add (ulPacketSinkHelper.Install (remoteHost));
      
      UdpClientHelper dlClient (ueIpIface.GetAddress (0), dlPort);
    dlClient.SetAttribute("Interval",TimeValue(MilliSeconds(interPacketInterval)));
      dlClient.SetAttribute ("MaxPackets", UintegerValue (1000000));
      UdpClientHelper ulClient (remoteHostAddr, ulPort);

      ulClient.SetAttribute ("Interval", TimeValue (MilliSeconds (interPacketInterval)));
      ulClient.SetAttribute ("MaxPackets", UintegerValue (1000000));
      clientApps.Add (dlClient.Install (remoteHost));
      clientApps.Add (ulClient.Install (ueNodes.Get (0)));
      /*
      .
      .
      .
      */
      PacketSinkHelper dlPacketSinkHelper10("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 9));
      PacketSinkHelper ulPacketSinkHelper10("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 9));
      serverApps.Add(dlPacketSinkHelper10.Install(ueNodes.Get(9)));
      serverApps.Add(ulPacketSinkHelper10.Install(remoteHost));
      UdpClientHelper dlClient10(ueIpIface.GetAddress(9), dlPort + 9);
      dlClient10.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient10.SetAttribute("MaxPackets", UintegerValue(1000000));
      UdpClientHelper ulClient10(remoteHostAddr, ulPort + 9);
      ulClient10.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient10.SetAttribute("MaxPackets", UintegerValue(1000000));
      
      clientApps.Add(dlClient10.Install(remoteHost));
      clientApps.Add(ulClient10.Install(ueNodes.Get(9)));
      
      serverApps.Start (Seconds (0.01));
      clientApps.Start (Seconds (0.01));
      
    }
~~~~

- Definição do data radio bearer, chamada da função Tracer e encerramento da simulação, definido pela variável SimTime.
~~~~cpp
else
    {
      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);
      // ativando o data radio bearer
      enum EpsBearer::Qci q = EpsBearer::GBR_CONV_VOICE;
      EpsBearer bearer (q);
      helper->ActivateDataRadioBearer (ueNetDevices, bearer);
    }
  helper->EnableTraces ();
  Traces ("./"); // habilitando o uplink tracer
  Simulator::Stop (Seconds (simTime));
  Simulator::Run ();
  Simulator::Destroy ();
  //flowMonitor->SerializeToXmlFile("flow5g.xml", true, true);    
  return 0; //Fim da simulação
  }
~~~~
## References

