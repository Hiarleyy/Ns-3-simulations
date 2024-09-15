// Definindo os Includes da Simulação 
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

//Função de monitoramento de pacotes
void
TxMacPacketTraceUe (Ptr<OutputStreamWrapper> stream, uint16_t rnti, uint8_t ccId, uint32_t size)
{
  *stream->GetStream () << Simulator::Now ().GetSeconds () << "\t" << (uint32_t)ccId << '\t' << size << std::endl;
}
//Função de monitoramento de pacotes
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

   // por padrão, antenas isotrópicas são usadas. Para usar o padrão de radiação 3GPP, use o <ThreeGppAntennaArrayModel>
   // cuidado: é necessária a configuração adequada dos ângulos de rolamento e inclinação
  Config::SetDefault ("ns3::PhasedArrayModel::AntennaElement", PointerValue (CreateObject<IsotropicAntennaModel> ())); 

  Ptr<MmWaveHelper> helper = CreateObject<MmWaveHelper> ();
  
  helper->SetCcPhyParams (ccMap);
  if (condition == "l")
  {
    helper->SetChannelConditionModelType ("ns3::AlwaysLosChannelConditionModel");
  }
  else if (condition == "n")
  {
    helper->SetChannelConditionModelType ("ns3::NeverLosChannelConditionModel");
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
    
      //cria a Internet conectando o Host remoto ao pgw e Configura a  ferramenta de roteamento
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
      p2ph.SetDeviceAttribute ("DataRate", DataRateValue (DataRate ("10Gb/s")));
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

  // Criação dos Uenodes (Users)
  NodeContainer ueNodes;
  ueNodes.Create (10);  // Criando 10 UeNodes

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
  
  if (useEpc)
    {
      //Instalando o protocolo IP nos Uenodes
      internet.Install (ueNodes);
      Ipv4InterfaceContainer ueIpIface;
      ueIpIface = epcHelper->AssignUeIpv4Address (ueNetDevices);
      // Atribui os endereços IP e Instala as aplicações nos Uenodes
      // Definindo o Gateway padrão para os Uenodes
      Ptr<Ipv4StaticRouting> ueStaticRouting1 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (0)->GetObject<Ipv4> ());
      ueStaticRouting1->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//1
      
      Ptr<Ipv4StaticRouting> ueStaticRouting2 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (1)->GetObject<Ipv4> ());
      ueStaticRouting2->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//2

      Ptr<Ipv4StaticRouting> ueStaticRouting3 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (2)->GetObject<Ipv4> ());
      ueStaticRouting3->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//3

      Ptr<Ipv4StaticRouting> ueStaticRouting4 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (3)->GetObject<Ipv4> ());
      ueStaticRouting4->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//4

      Ptr<Ipv4StaticRouting> ueStaticRouting5 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (4)->GetObject<Ipv4> ());
      ueStaticRouting5->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//5

      Ptr<Ipv4StaticRouting> ueStaticRouting6 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (5)->GetObject<Ipv4> ());
      ueStaticRouting1->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//6
      
      Ptr<Ipv4StaticRouting> ueStaticRouting7 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (6)->GetObject<Ipv4> ());
      ueStaticRouting2->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//7

      Ptr<Ipv4StaticRouting> ueStaticRouting8 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (7)->GetObject<Ipv4> ());
      ueStaticRouting3->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//8

      Ptr<Ipv4StaticRouting> ueStaticRouting9 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (8)->GetObject<Ipv4> ());
      ueStaticRouting4->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//9

      Ptr<Ipv4StaticRouting> ueStaticRouting10 = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (9)->GetObject<Ipv4> ());
      ueStaticRouting5->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);//10


      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);

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
      dlClient.SetAttribute ("Interval", TimeValue (MilliSeconds (interPacketInterval)));
      dlClient.SetAttribute ("MaxPackets", UintegerValue (1000000));

      UdpClientHelper ulClient (remoteHostAddr, ulPort);
      ulClient.SetAttribute ("Interval", TimeValue (MilliSeconds (interPacketInterval)));
      ulClient.SetAttribute ("MaxPackets", UintegerValue (1000000));

      clientApps.Add (dlClient.Install (remoteHost));
      clientApps.Add (ulClient.Install (ueNodes.Get (0)));

      serverApps.Start (Seconds (0.01));
      clientApps.Start (Seconds (0.01));

      //----Usuario 2----
      PacketSinkHelper dlPacketSinkHelper2 ("ns3::UdpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), dlPort + 1));
      PacketSinkHelper ulPacketSinkHelper2 ("ns3::UdpSocketFactory", InetSocketAddress (Ipv4Address::GetAny (), ulPort + 1));
      serverApps.Add (dlPacketSinkHelper2.Install (ueNodes.Get (1)));
      serverApps.Add (ulPacketSinkHelper2.Install (remoteHost));

      UdpClientHelper dlClient2 (ueIpIface.GetAddress (1), dlPort + 1);
      dlClient2.SetAttribute ("Interval", TimeValue (MilliSeconds (interPacketInterval)));
      dlClient2.SetAttribute ("MaxPackets", UintegerValue (1000000));

      UdpClientHelper ulClient2 (remoteHostAddr, ulPort + 1);
      ulClient2.SetAttribute ("Interval", TimeValue (MilliSeconds (interPacketInterval)));
      ulClient2.SetAttribute ("MaxPackets", UintegerValue (1000000));

      clientApps.Add (dlClient2.Install (remoteHost));
      clientApps.Add (ulClient2.Install (ueNodes.Get (1)));

      serverApps.Start (Seconds (0.01));
      clientApps.Start (Seconds (0.01));
      //----Usuario 3----//
      PacketSinkHelper dlPacketSinkHelper3("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 2));
      PacketSinkHelper ulPacketSinkHelper3("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 2));
      serverApps.Add(dlPacketSinkHelper3.Install(ueNodes.Get(2)));
      serverApps.Add(ulPacketSinkHelper3.Install(remoteHost));

      UdpClientHelper dlClient3(ueIpIface.GetAddress(2), dlPort + 2);
      dlClient3.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient3.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient3(remoteHostAddr, ulPort + 2);
      ulClient3.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient3.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient3.Install(remoteHost));
      clientApps.Add(ulClient3.Install(ueNodes.Get(2)));
      //----Usuario 4----//

      PacketSinkHelper dlPacketSinkHelper4("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 3));
      PacketSinkHelper ulPacketSinkHelper4("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 3));
      serverApps.Add(dlPacketSinkHelper4.Install(ueNodes.Get(3)));
      serverApps.Add(ulPacketSinkHelper4.Install(remoteHost));

      UdpClientHelper dlClient4(ueIpIface.GetAddress(3), dlPort + 3);
      dlClient4.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient4.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient4(remoteHostAddr, ulPort + 3);
      ulClient4.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient4.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient4.Install(remoteHost));
      clientApps.Add(ulClient4.Install(ueNodes.Get(3)));

      //----Usuario 5----//
      PacketSinkHelper dlPacketSinkHelper5("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 4));
      PacketSinkHelper ulPacketSinkHelper5("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 4));
      serverApps.Add(dlPacketSinkHelper5.Install(ueNodes.Get(4)));
      serverApps.Add(ulPacketSinkHelper5.Install(remoteHost));

      UdpClientHelper dlClient5(ueIpIface.GetAddress(4), dlPort + 4);
      dlClient5.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient5.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient5(remoteHostAddr, ulPort + 5);
      ulClient5.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient5.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient5.Install(remoteHost));
      clientApps.Add(ulClient5.Install(ueNodes.Get(4)));

      //----Usuario 6----//
      PacketSinkHelper dlPacketSinkHelper6("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 5));
      PacketSinkHelper ulPacketSinkHelper6("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 5));
      serverApps.Add(dlPacketSinkHelper6.Install(ueNodes.Get(5)));
      serverApps.Add(ulPacketSinkHelper6.Install(remoteHost));

      UdpClientHelper dlClient6(ueIpIface.GetAddress(5), dlPort + 5);
      dlClient6.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient6.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient6(remoteHostAddr, ulPort + 5);
      ulClient6.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient6.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient6.Install(remoteHost));
      clientApps.Add(ulClient6.Install(ueNodes.Get(5)));
      //----Usuario 7----//
      PacketSinkHelper dlPacketSinkHelper7("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 6));
      PacketSinkHelper ulPacketSinkHelper7("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 6));
      serverApps.Add(dlPacketSinkHelper7.Install(ueNodes.Get(6)));
      serverApps.Add(ulPacketSinkHelper7.Install(remoteHost));

      UdpClientHelper dlClient7(ueIpIface.GetAddress(6), dlPort + 6);
      dlClient7.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient7.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient7(remoteHostAddr, ulPort + 6);
      ulClient7.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient7.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient7.Install(remoteHost));
      clientApps.Add(ulClient7.Install(ueNodes.Get(6)));
      //----Usuario 8----//
      PacketSinkHelper dlPacketSinkHelper8("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 7));
      PacketSinkHelper ulPacketSinkHelper8("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 7));
      serverApps.Add(dlPacketSinkHelper8.Install(ueNodes.Get(7)));
      serverApps.Add(ulPacketSinkHelper8.Install(remoteHost));

      UdpClientHelper dlClient8(ueIpIface.GetAddress(7), dlPort + 7);
      dlClient8.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient8.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient8(remoteHostAddr, ulPort + 7);
      ulClient8.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient8.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient8.Install(remoteHost));
      clientApps.Add(ulClient8.Install(ueNodes.Get(7)));
      //----Usuario 9----//
      PacketSinkHelper dlPacketSinkHelper9("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), dlPort + 8));
      PacketSinkHelper ulPacketSinkHelper9("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address::GetAny(), ulPort + 8));
      serverApps.Add(dlPacketSinkHelper9.Install(ueNodes.Get(8)));
      serverApps.Add(ulPacketSinkHelper9.Install(remoteHost));

      UdpClientHelper dlClient9(ueIpIface.GetAddress(8), dlPort + 8);
      dlClient9.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      dlClient9.SetAttribute("MaxPackets", UintegerValue(1000000));

      UdpClientHelper ulClient9(remoteHostAddr, ulPort + 8);
      ulClient9.SetAttribute("Interval", TimeValue(MilliSeconds(interPacketInterval)));
      ulClient9.SetAttribute("MaxPackets", UintegerValue(1000000));

      clientApps.Add(dlClient9.Install(remoteHost));
      clientApps.Add(ulClient9.Install(ueNodes.Get(8)));
      //----Usuario 10----//
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
    }
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