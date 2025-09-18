# Ns-3-simulations

**English | [Português](README.md)**
### Tasks
[Click here to view the tasks](Tasks)

## Network simulator
[Ns-3](https://www.nsnam.org/) is a discrete-event network simulator for Internet systems, primarily targeted for research and educational use. ns-3 is free and open-source software, licensed under the GNU GPLv2 license and maintained by a worldwide community.

## mmWave: ns-3 Module
- This is an ns-3 module for simulation of 5G cellular networks operating on mmWaves.
- Support for a wide range of channel models, including the 3GPP TR 38.901-based model for frequencies between 0.5 and 100 GHz. Ray tracing and measured traces can also be used.
- Custom PHY and MAC classes that support 3GPP NR frame structure and numerologies.
- Custom schedulers for dynamic TDD format support
- Carrier aggregation at the MAC layer
- RLC layer enhancements with packet re-segmentation for retransmissions
- Dual connectivity with LTE base stations, with fast secondary cell handover and channel tracking
- Core network element simulation (also with MME as a real node)

For more information about the ns3 module, you can find it at [mmWave-Ns3](https://github.com/nyuwireless-unipd/ns3-mmwave)

## RxPacketTrace
### RxPacketTrace is responsible for monitoring the packets that are transmitted in the simulation. Each column of the file contains specific information about the packets that were transmitted (DL-Downlink) and the packets received (UL-Uplink)

- **DL/UL** - Indicates the packet state, whether it is in Downlink or Uplink. Downlink is packet transmission by the base station and Uplink is packet transmission by the user to the base station
- **Time**: The timestamp (in seconds) when the event (packet transmission or reception) occurred.
- **Frame**: The frame number in which the transmission or reception occurred. Frames are time units in the LTE/5G time structure.
- **subF**: Subframe in which the transmission or reception occurred. A frame is divided into subframes.
- **slot:** Slot in the subframe where the transmission or reception occurred. Each subframe is divided into slots.
- **1stSym:** First symbol of transmission or reception in the slot.
- **symbol#:** Number of symbols involved in the transmission or reception.
- **cellId:** ID of the cell to which the transmission or reception is associated. In LTE/5G networks, each cell has a unique identifier.
- **rnti:** Radio Network Temporary Identifier (RNTI), which is a temporary identifier used to identify the user equipment (UE) in the network.
- **ccId:** Component Carrier ID, used in carrier aggregation systems where multiple frequency carriers can be used simultaneously.
- **tbSize:** Transport Block Size, which is the size of the transport block in bits. This value indicates the amount of data transmitted or received.
- **mcs:** Modulation and Coding Scheme, which indicates the modulation and coding scheme used for transmission. MCS is a parameter that influences the data transmission rate and robustness against errors.
- **rv:** Redundancy Version, which is used to identify different redundant versions of the transport block in HARQ (Hybrid Automatic Repeat Request) for error correction.
- **SINR(dB):** Signal to Interference plus Noise Ratio in decibels. It is the measure of signal quality that was received by the user nodes.
- **corrupt:** Binary indicator (0 or 1) that shows whether the packet was corrupted (1) or not (0) during transmission.
- **TBler:** Transport Block Error Rate, which is the transport block error rate. Indicates the proportion of transport blocks that were received with error.

![image](https://github.com/Hiarleyy/Ns-3-simulations/assets/111695591/2177e459-496d-4d2d-a01d-f03cea067d53)

## DlRLcStats
### The DlRlcStats file is used to analyze the performance of the RLC (Radio Link Control) layer on the downlink (DL - Downlink) in a network simulation performed with ns-3. It contains detailed metrics that allow evaluating and understanding the data transmission behavior in the network.

- **% start**: Start of the time interval (in seconds) for the recorded statistics. **end**: End of the time interval (in seconds) for the recorded statistics.
- **CellId**: Identification of the cell where the data was recorded.
- **IMSI**: International Mobile Subscriber Identity of the user.
- **RNTI**: Radio Network Temporary Identifier of the user.
- **LCID**: Logical Channel Identifier, used to differentiate different data flows.
- **nTxPDUs**: Number of transmitted protocol data units (PDUs).
- **TxBytes**: Number of bytes transmitted.
- **nRxPDUs**: Number of received PDUs.
- **RxBytes**: Number of bytes received.
- **delay**: Average delay (in seconds) of the PDUs.
- **stdDev**: Standard deviation of PDU delay.
- **min**: Smallest delay value (in seconds) recorded.
- **max**: Largest delay value (in seconds) recorded.
- **PduSize**: Average size of PDUs (in bytes).
- **stdDev.1**: Standard deviation of PDU size.
- **min.1**: Smallest PDU size recorded (in bytes).
- **max.1**: Largest PDU size recorded (in bytes).

![image](https://github.com/Hiarleyy/Ns-3-simulations/assets/111695591/cd2436ee-cf0b-4368-8434-176ba3ec8eb5)

## Documentation
#### [Batman Algorithm](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/Documenta%C3%A7%C3%A3o/bat.md) || [NS3 Simulation in C++](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/Documenta%C3%A7%C3%A3o/packet5G.md) || [Results 10Nodes](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/Documenta%C3%A7%C3%A3o/10node_results.md) || [Docker NS3-MmWave](https://github.com/Hiarleyy/Ns-3-simulations/blob/main/Documenta%C3%A7%C3%A3o/Docker-MmWave.md)


## Contact

### Marcos Hiarley
<div>
<a href ="mailto:marcoshiarley.silva@gmail.com"><img src ="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href ="https://www.instagram.com/hiarley._/"><img src ="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href ="https://www.linkedin.com/in/marcos-hiarley/"><img src ="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" href="www.linkedin.com/in/marcos-hiarley-1853a7226"/></a>
</div>


### Robert Gabriel
<div>
<a href ="mailto:robertgabriel@disroot.org"><img src ="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href ="https://www.instagram.com/robertdsgabriel/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
</div>