/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */
#define NS_LOG_COMPONENT_DEFINE
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
#include "ns3/config-store.h"
#include "ns3/netanim-module.h"
#include "ns3/flow-monitor.h"
#include "ns3/flow-monitor-helper.h"
#include "ns3/mmwave-point-to-point-epc-helper.h"
#include "ns3/point-to-point-helper.h"
#include "ns3/global-route-manager.h"
#include "ns3/trace-helper.h"
#include "ns3/ipv4-flow-probe.h"
#include "ns3/flow-monitor-helper.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/flow-monitor.h"
#include "ns3/ipv4-flow-probe.h"
#include "ns3/gnuplot.h"
#include "ns3/flow-classifier.h"


using namespace ns3;
using namespace mmwave;


double throughput = 0.0;
GnuplotDataset dataset;

def calculate_throughput(monitor, classifier):
    stats = monitor.GetFlowStats()

    for flow_id, flow_stats in stats:
        flow_key = classifier.GetFlowKeyFromFlowId(flow_id)

        # Extract relevant information from the flow tuple
        source_address = flow_key.sourceAddress
        destination_address = flow_key.destinationAddress
        source_port = flow_key.sourcePort
        destination_port = flow_key.destinationPort
        protocol = flow_key.protocol

        received_bytes = flow_stats.rxBytes
        end_time = flow_stats.timeLastRxPacket.GetSeconds()
        start_time = flow_stats.timeFirstTxPacket.GetSeconds()

        flow_throughput = received_bytes * 8 / (end_time - start_time) / 1e6
        throughput += flow_throughput
    return throughput

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

int
main (int argc, char *argv[])
{
  bool verbose = true;
  bool tracing = true;
  double ueDist = 100;
  double ueBound = 1000;
  bool blockage = false;
  bool useEpc = true;
  double totalBandwidth = 200e6;
  double frequency = 26.0e9;
  double simTime = 60;
  std::string condition = "l";

  CommandLine cmd;
  cmd.AddValue ("verbose","Tell echo aplications to log if true", verbose);
  cmd.AddValue ("tracing","Enable pcap tracing", tracing);
  cmd.AddValue ("ueDist", "Distance between Enb and Ue [m]", ueDist);
  cmd.AddValue ("blockage", "If enabled blockage = true", blockage);
  cmd.AddValue ("frequency", "CC central frequency", frequency);
  cmd.AddValue ("totalBandwidth", "System bandwidth in Hz", totalBandwidth);
  cmd.AddValue ("simTime", "Simulation time", simTime);
  cmd.AddValue ("useEpc", "If enabled use EPC, else use RLC saturation mode", useEpc);
  cmd.AddValue ("condition", "Channel condition, l = LOS, n = NLOS, otherwise the condition is randomly determined", condition);
  cmd.Parse (argc, argv);
  
  Time::SetResolution (Time::NS);
  
  // Creating Objects
  Ptr<MmWavePhyMacCommon> phyMacConfig0 = CreateObject<MmWavePhyMacCommon> ();
  phyMacConfig0->SetBandwidth (totalBandwidth);
  phyMacConfig0->SetCentreFrequency (frequency);
  
  Ptr<MmWaveComponentCarrier> cc0 = CreateObject<MmWaveComponentCarrier> ();
  cc0->SetConfigurationParameters (phyMacConfig0);
  cc0->SetAsPrimary (true);
  
  std::map<uint8_t, MmWaveComponentCarrier> ccMap;
  ccMap [0] = *cc0;
  
    // create and set the helper
  
  Config::SetDefault ("ns3::MmWaveHelper::ChannelModel",StringValue ("ns3::ThreeGppSpectrumPropagationLossModel"));
  Config::SetDefault ("ns3::ThreeGppChannelModel::Scenario", StringValue ("UMa"));
  Config::SetDefault ("ns3::ThreeGppChannelModel::Blockage", BooleanValue (blockage)); // Enable/disable the blockage model  
  Config::SetDefault ("ns3::MmWaveHelper::PathlossModel",StringValue ("ns3::ThreeGppUmaPropagationLossModel"));

  // by default, isotropic antennas are used. To use the 3GPP radiation pattern instead, use the <ThreeGppAntennaArrayModel>
  // beware: proper configuration of the bearing and downtilt angles is needed
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
  
  // create the EPC
  Ipv4Address remoteHostAddr;
  Ptr<Node> remoteHost;
  InternetStackHelper internet;
  Ptr<MmWavePointToPointEpcHelper> epcHelper;
  Ipv4StaticRoutingHelper ipv4RoutingHelper;
  if (useEpc)
    {
      epcHelper = CreateObject<MmWavePointToPointEpcHelper> ();
      helper->SetEpcHelper (epcHelper);

      // create the Internet by connecting remoteHost to pgw. Setup routing too
      Ptr<Node> pgw = epcHelper->GetPgwNode ();

      // create remotehost
      NodeContainer remoteHostContainer;
      remoteHostContainer.Create (1);
      internet.Install (remoteHostContainer);
      Ipv4StaticRoutingHelper ipv4RoutingHelper;
      Ipv4InterfaceContainer internetIpIfaces;

      remoteHost = remoteHostContainer.Get (0);
      // create the Internet
      PointToPointHelper p2ph;
      p2ph.SetDeviceAttribute ("DataRate", DataRateValue (DataRate ("10Gb/s")));
      p2ph.SetDeviceAttribute ("Mtu", UintegerValue (1500));
      p2ph.SetChannelAttribute ("Delay", TimeValue (Seconds (0.001)));

      NetDeviceContainer internetDevices = p2ph.Install (pgw, remoteHost);

      Ipv4AddressHelper ipv4h;
      ipv4h.SetBase ("1.0.0.0", "255.255.0.0");
      internetIpIfaces = ipv4h.Assign (internetDevices);
      // interface 0 is localhost, 1 is the p2p device
      remoteHostAddr = internetIpIfaces.GetAddress (1);

      Ptr<Ipv4StaticRouting> remoteHostStaticRouting = ipv4RoutingHelper.GetStaticRouting (remoteHost->GetObject<Ipv4> ());
      remoteHostStaticRouting->AddNetworkRouteTo (Ipv4Address ("7.0.0.0"), Ipv4Mask ("255.255.0.0"), 1);
    }

  // create the enb node
  NodeContainer enbNodes;
  enbNodes.Create (1);

  // set mobility
  Ptr<ListPositionAllocator> enbPositionAlloc = CreateObject<ListPositionAllocator> ();
  enbPositionAlloc->Add (Vector (10.0, 10.0, 15.0));

  MobilityHelper enbmobility;
  enbmobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
  enbmobility.SetPositionAllocator (enbPositionAlloc);
  enbmobility.Install (enbNodes);
  BuildingsHelper::Install (enbNodes);

  // install enb device
  NetDeviceContainer enbNetDevices = helper->InstallEnbDevice (enbNodes);
  std::cout << "eNB device installed" << std::endl;


  
  LogComponentEnable("FlowMonitor", LOG_LEVEL_ALL);

  // create ue node
  NodeContainer ueNodes;
  ueNodes.Create (1);

  // set mobility
  MobilityHelper uemobility;
  uemobility.SetMobilityModel ("ns3::RandomWalk2dMobilityModel",
                               "Bounds", RectangleValue (Rectangle (-ueDist-ueBound, ueDist+ueBound, -ueDist-ueBound, ueDist+ueBound)));
  Config::SetDefault ("ns3::UniformDiscPositionAllocator::rho", DoubleValue (ueDist));
  Config::SetDefault ("ns3::UniformDiscPositionAllocator::Z", DoubleValue (1.6));
  Ptr<UniformDiscPositionAllocator> uePositionAlloc = CreateObject<UniformDiscPositionAllocator> ();
  uemobility.SetPositionAllocator (uePositionAlloc);
  uemobility.Install (ueNodes.Get (0));
  BuildingsHelper::Install (ueNodes);
  std::cout << "UE initial position :" << ueNodes.Get (0)->GetObject<MobilityModel> ()->GetPosition () << std::endl;

  // install ue device
  NetDeviceContainer ueNetDevices = helper->InstallUeDevice (ueNodes);
  std::cout << "UE device installed" << std::endl;
  
    if (useEpc)
    {
      // install the IP stack on the UEs
      internet.Install (ueNodes);
      Ipv4InterfaceContainer ueIpIface;
      ueIpIface = epcHelper->AssignUeIpv4Address (ueNetDevices);
      // assign IP address to UEs, and install applications
      // set the default gateway for the UE
      Ptr<Ipv4StaticRouting> ueStaticRouting = ipv4RoutingHelper.GetStaticRouting (ueNodes.Get (0)->GetObject<Ipv4> ());
      ueStaticRouting->SetDefaultRoute (epcHelper->GetUeDefaultGatewayAddress (), 1);

      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);

      // install and start applications on UEs and remote host
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
    }
  else
    {
      helper->AttachToClosestEnb (ueNetDevices, enbNetDevices);

      // activate a data radio bearer
      enum EpsBearer::Qci q = EpsBearer::GBR_CONV_VOICE;
      EpsBearer bearer (q);
      helper->ActivateDataRadioBearer (ueNetDevices, bearer);
    }
  
  helper->EnableTraces ();
  Traces ("./"); // enable UL MAC traces
  
  AnimationInterface anim("packet_5g.xml");

   Ptr<FlowMonitor> flowMonitor;
    FlowMonitorHelper flowMonitorHelper;
    flowMonitor = flowMonitorHelper.InstallAll();

    // Inicia a simulação
    Simulator::Stop(Seconds(10.0));
    Simulator::Run();
    Simulator::Destroy();

    // Calcula a vazão média
    CalculateThroughput(flowMonitor, flowMonitorHelper.GetClassifier());

    // Imprime a vazão média
    NS_LOG_INFO("Average Throughput: " << throughput << " Mbps");

    // Criação do gráfico de vazão
   AddDataset(0.0, 0.0);
   AddDataset(1.0, throughput);

  Gnuplot plot;
  plot.SetTitle("Throughput vs Time");
  plot.SetLegend("Throughput (Mbps)");
  plot.AddDataset(dataset);
  plot.GenerateOutput("throughput_graph.plt");
  plot.GenerateOutput("throughput_graph.png", "png", "Time (s)", "Throughput (Mbps)");

  
  //flowMonitor->SerializeToXmlFile("flow5g.xml", true, true);     
  
  return 0;
}
