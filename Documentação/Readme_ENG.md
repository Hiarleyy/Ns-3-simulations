# Ns-3-simulations

**Language / Idioma:** [🇺🇸 English](Readme_ENG.md) | [🇧🇷 Português](../README.md)

## Tasks

[Click here to see the tasks](../Tasks)

## Network simulator

[Ns-3](https://www.nsnam.org/) is a discrete-event network simulator for Internet systems, primarily aimed at research and educational use. Ns-3 is free and open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.

## mmWave: Ns-3 module

This is an ns-3 module for simulating 5G cellular networks operating in mmWaves.

Support for a wide range of channel models, including the 3GPP TR 38.901-based model for frequencies between 0.5 and 100 GHz. Ray tracing and measured traces can also be used.

Custom PHY and MAC classes supporting 3GPP NR frame structure and numerologies.

Custom schedulers for dynamic TDD format support.

Carrier aggregation in the MAC layer.

RLC layer improvements with packet re-segmentation for retransmissions.

Dual connectivity with LTE base stations, featuring fast secondary cell handover and channel tracking.

Core network elements simulation (also with MME as a real node).

For more information about this module, visit [mmWave-Ns3](https://github.com/nyuwireless-unipd/ns3-mmwave)

## RxPacketTrace
RxPacketTrace is responsible for monitoring the packets transmitted during the simulation. Each column of the file contains specific information about the packets transmitted (DL-Downlink) and packets received (UL-Uplink).

DL/UL - Indicates the packet state: Downlink (packet sent by the base station) or Uplink (packet sent by the user to the base station).

Time: Timestamp (in seconds) when the event (packet transmission or reception) occurred.

Frame: Frame number in which the transmission or reception occurred. Frames are units of time in LTE/5G structures.

subF: Subframe of the transmission or reception. A frame is divided into subframes.

slot: Slot in the subframe where the transmission or reception took place. Each subframe is divided into slots.

1stSym: First symbol of the transmission or reception in the slot.

symbol#: Number of symbols involved in the transmission or reception.

cellId: Cell ID associated with the transmission or reception. Each LTE/5G cell has a unique identifier.

rnti: Radio Network Temporary Identifier (RNTI), a temporary identifier used to identify the User Equipment (UE) in the network.

ccId: Component Carrier ID, used in carrier aggregation systems where multiple frequency carriers are used simultaneously.

tbSize: Transport Block Size, the size of the transport block in bits. Indicates the amount of data transmitted or received.

mcs: Modulation and Coding Scheme, indicating the modulation and coding used for transmission. MCS influences data rate and robustness against errors.

rv: Redundancy Version, used in HARQ (Hybrid Automatic Repeat Request) to identify redundant versions of the transport block for error correction.

SINR(dB): Signal to Interference plus Noise Ratio, in decibels. Measures the quality of the signal received by user nodes.

corrupt: Binary indicator (0 or 1) showing whether the packet was corrupted (1) or not (0).

TBler: Transport Block Error Rate, the proportion of transport blocks received with errors.

## DlRLcStats
The DlRlcStats file is used to analyze the performance of the RLC (Radio Link Control) layer in the downlink (DL) of a network simulation carried out with ns-3. It contains detailed metrics to evaluate and understand data transmission behavior in the network.

% start: Start of the time interval (in seconds) for the recorded statistics.

end: End of the time interval (in seconds).

CellId: Cell identification where the data was recorded.

IMSI: International Mobile Subscriber Identity of the user.

RNTI: Radio Network Temporary Identifier of the user.

LCID: Logical Channel Identifier, used to differentiate data flows.

nTxPDUs: Number of transmitted Protocol Data Units (PDUs).

TxBytes: Number of transmitted bytes.

nRxPDUs: Number of received PDUs.

RxBytes: Number of received bytes.

delay: Average PDU delay (in seconds).

stdDev: Standard deviation of PDU delay.

min: Minimum delay value (in seconds).

max: Maximum delay value (in seconds).

PduSize: Average PDU size (in bytes).

stdDev.1: Standard deviation of PDU size.

min.1: Minimum PDU size (in bytes).

max.1: Maximum PDU size (in bytes).

## Documentation
[Batman Algorithm](bat_ENG.md) || [NS3 Simulation in C++](packet5G_ENG.md) || [Results 10Nodes](10node_results_ENG.md) || [Docker NS3-MmWave](Docker-MmWave_ENG.md)

## Contact

### Marcos Hiarley
<div> <a href ="mailto:marcoshiarley.silva@gmail.com"><img src ="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a> <a href ="https://www.instagram.com/hiarley._/"><img src ="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a> <a href ="https://www.linkedin.com/in/marcos-hiarley/"><img src ="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" href="www.linkedin.com/in/marcos-hiarley-1853a7226"/></a> </div>
### Robert Gabriel
<div> <a href ="mailto:robertgabriel@disroot.org"><img src ="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a> <a href ="https://www.instagram.com/robertdsgabriel/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a> </div>
