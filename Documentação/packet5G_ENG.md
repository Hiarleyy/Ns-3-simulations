# Packet_5G

**Language / Idioma:** [🇺🇸 English](packet5G_ENG.md) | [🇧🇷 Português](packet5G.md)

## Program Execution

To execute the program and perform the desired simulations, it is necessary to install the program dependencies:
1. [Network Simulator (Ns3)](https://www.nsnam.org/)
2. [Mmwave Module](https://github.com/nyuwireless-unipd/ns3-mmwave)

You can install the simulator and the respective module separately, or access it through a docker https://hub.docker.com/r/fedeit/ns3-mmwave, where the simulator is already configured and ready to use.

#### Installing the Ns3 Simulator with mmWave Module:
In the official repository of the [mmWave](https://github.com/nyuwireless-unipd/ns3-mmwave) module for the Network Simulator, you can find the detailed manual to install the simulator along with mmwave. To perform the installation, you need to execute the following steps:


~~~~bash
git clone https://github.com/nyuwireless-unipd/ns3-mmwave.git
cd ns3-mmwave
./ns3 configure --disable-python --enable-examples && ./ns3 build
~~~~

To verify that all modules were installed correctly, with the following command you can run the following example simulation:

~~~~bash
./ns3 run mmwave-simple-epc
~~~~
---
## Simulation Code (Packet5G.cc)

The network simulator uses C++ as its main language, where to compile the simulation it is necessary that the file is built before being executed. For this, it is necessary to run the following code in the prompt:

~~~bash
./ns3 build Packet5G.cc
~~~

- Includes Used in the Project
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


- Functions responsible for monitoring transmitted packets
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

- Definition of simulation parameters, object creation and default values
~~~~cpp
//Main function
int
main (int argc, char *argv[])
{
  bool blockage = false;
  bool useEpc = true;
  double totalBandwidth = 200e6;
  double frequency = 26.0e9; //Scenario frequency definition
  double simTime = 60; // simulation time
  std::string condition = "l";
  
  // Default simulation values -- Can be changed by indicating the desired variable in the simulation start argument

  CommandLine cmd;
  cmd.AddValue ("blockage", "If enabled blockage = true", blockage);
  cmd.AddValue ("frequency", "CC central frequency", frequency);
  cmd.AddValue ("totalBandwidth", "System bandwidth in Hz", totalBandwidth);
  cmd.AddValue ("simTime", "Simulation time", simTime);
  cmd.AddValue ("useEpc", "If enabled use EPC, else use RLC saturation mode", useEpc);

  cmd.AddValue ("condition", "Channel condition, l = LOS, n = NLOS, otherwise the condition is randomly determined", condition);

  cmd.Parse (argc, argv);

  Time::SetResolution (Time::NS);

  //Object Creation

  Ptr<MmWavePhyMacCommon> phyMacConfig0 = CreateObject<MmWavePhyMacCommon> ();
  phyMacConfig0->SetBandwidth (totalBandwidth);
  phyMacConfig0->SetCentreFrequency (frequency);
  Ptr<MmWaveComponentCarrier> cc0 = CreateObject<MmWaveComponentCarrier> ();
  cc0->SetConfigurationParameters (phyMacConfig0);
  cc0->SetAsPrimary (true);
  std::map<uint8_t, MmWaveComponentCarrier> ccMap;
  ccMap [0] = *cc0;

  //creation and default definition of Helpers
  Config::SetDefault ("ns3::MmWaveHelper::ChannelModel",StringValue ("ns3::ThreeGppSpectrumPropagationLossModel"));//channel model used

  Config::SetDefault ("ns3::ThreeGppChannelModel::Scenario", StringValue ("UMa")); //Application scenario definition

  Config::SetDefault ("ns3::ThreeGppChannelModel::Blockage", BooleanValue (blockage)); //Enable/Disable Blockage model

  Config::SetDefault ("ns3::MmWaveHelper::PathlossModel",StringValue ("ns3::ThreeGppUmaPropagationLossModel"));
   // by default, isotropic antennas are used. To use the 3GPP radiation pattern, use <ThreeGppAntennaArrayModel>. Proper configuration of roll and tilt angles is required
  Config::SetDefault ("ns3::PhasedArrayModel::AntennaElement", PointerValue (CreateObject<IsotropicAntennaModel> ()));
~~~~


- EPC creation for simulation. The EPC is a crucial part of the network infrastructure in LTE/5G simulations, allowing ns-3 simulations to more faithfully reflect the behavior of a real network. It provides essential functions for session management, data routing, QoS policies, authentication and mobility, ensuring efficient and continuous communication for mobile users.
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

  // EPC Creation
  Ipv4Address remoteHostAddr;
  Ptr<Node> remoteHost;
  InternetStackHelper internet;
  Ptr<MmWavePointToPointEpcHelper> epcHelper;
  Ipv4StaticRoutingHelper ipv4RoutingHelper;

  if (useEpc)

    {
      epcHelper = CreateObject<MmWavePointToPointEpcHelper> ();
      helper->SetEpcHelper (epcHelper);
      //creates the Internet connecting the remote Host to the pgw and configures the routing tool
      Ptr<Node> pgw = epcHelper->GetPgwNode ();
      
      // Remote Host Creation
      NodeContainer remoteHostContainer;
      remoteHostContainer.Create (1);
      internet.Install (remoteHostContainer);
      Ipv4StaticRoutingHelper ipv4RoutingHelper;
      Ipv4InterfaceContainer internetIpIfaces;
      remoteHost = remoteHostContainer.Get (0);
      
      // Internet creation
      PointToPointHelper p2ph;
      p2ph.SetDeviceAttribute ("DataRate", DataRateValue (DataRate("10Gb/s")));
      p2ph.SetDeviceAttribute ("Mtu", UintegerValue (1500));
      p2ph.SetChannelAttribute ("Delay", TimeValue (Seconds (0.001)));
      NetDeviceContainer internetDevices = p2ph.Install (pgw, remoteHost);
      Ipv4AddressHelper ipv4h;
      ipv4h.SetBase ("1.0.0.0", "255.255.0.0");
      internetIpIfaces = ipv4h.Assign (internetDevices);
      // interface 0 is localhost, 1 is p2p device

      remoteHostAddr = internetIpIfaces.GetAddress (1);
      Ptr<Ipv4StaticRouting> remoteHostStaticRouting = ipv4RoutingHelper.GetStaticRouting (remoteHost->GetObject<Ipv4> ());
      remoteHostStaticRouting->AddNetworkRouteTo (Ipv4Address ("7.0.0.0"), Ipv4Mask ("255.255.0.0"), 1);

    }
~~~~

- Base Station Node installation and mobility definition. The base station is responsible for signal transmission to User nodes.
~~~~cpp
// EnbNode (Base Station) Creation
  NodeContainer enbNodes;
  enbNodes.Create (1);


  // Defining EnbNode Mobility
  Ptr<ListPositionAllocator> enbPositionAlloc = CreateObject<ListPositionAllocator> ();
  enbPositionAlloc->Add (Vector (10.0, 10.0, 15.0));
  
  MobilityHelper enbmobility;
  enbmobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  enbmobility.SetPositionAllocator (enbPositionAlloc);
  enbmobility.Install (enbNodes);
  BuildingsHelper::Install (enbNodes);
  
  // Installing the Enb
  NetDeviceContainer enbNetDevices = helper->InstallEnbDevice (enbNodes);
  std::cout << "eNB device installed" << std::endl;
~~~~

- Creation of Uenodes, which represent the 5G network users. For this simulation, 10 users with constant mobility were defined, with coordinates being determined by the Batman algorithm.
~~~~cpp
  // Uenodes (Users) Creation
  NodeContainer ueNodes;
  ueNodes.Create (10);  // Creating 10 UeNodes

  // Defining UeNodes mobility (Constant position)
  MobilityHelper uemobility;
  uemobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  // Coordinate definition for each node -- (BATMAN algorithm coordinates)
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

  // Prints Uenodes coordinates
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

  // Installing UeDevices
  NetDeviceContainer ueNetDevices = helper->InstallUeDevice (ueNodes);
  std::cout << "UE devices installed" << std::endl;
~~~~


- IP Protocol installation and Default Gateway definition for each User Node.
~~~~cpp
if (useEpc)

    {
      //Installing IP protocol on Uenodes
      internet.Install (ueNodes);
      Ipv4InterfaceContainer ueIpIface;
      ueIpIface = epcHelper->AssignUeIpv4Address (ueNetDevices);
      // Assigns IP addresses and Installs applications on Uenodes

      // Defining the default Gateway for Uenodes --- Similar structure for other Uenodes
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
- Definition of Uenodes and remote Host applications. The structure repeats for other Uenodes.
~~~~cpp
// Installs and starts applications on Uenodes and remote Host -- Similar Structure for other Uenodes

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

- Data radio bearer definition, Tracer function call and simulation termination, defined by the SimTime variable.
~~~~cpp
else
    {
      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);
      // activating the data radio bearer
      enum EpsBearer::Qci q = EpsBearer::GBR_CONV_VOICE;
      EpsBearer bearer (q);
      helper->ActivateDataRadioBearer (ueNetDevices, bearer);
    }
  helper->EnableTraces ();
  Traces ("./"); // enabling the uplink tracer
  Simulator::Stop (Seconds (simTime));
  Simulator::Run ();
  Simulator::Destroy ();
  //flowMonitor->SerializeToXmlFile("flow5g.xml", true, true);    
  return 0; //End of simulation
  }
~~~~
## References