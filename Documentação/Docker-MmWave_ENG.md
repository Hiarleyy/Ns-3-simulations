tags: #fleeting #5g #ns3 #project 
Created:2024-06-20, Thu Jun 4 - 19:31
Week-number:25


## Summary:

- A Docker image was developed to facilitate the use of the Ns3 simulator. You can access the project's custom image at: https://hub.docker.com/r/hiarley/ns3-mmwave/tags
- Mmwave Version: (mmwave-8.0)
- Ns-3 Version: (Ns-3 3.42) 

## How to use the image?
- After checking all the requirements for using Docker Desktop, you can use the following command to access this image:

```Bash
docker pull hiarley/ns3-mmwave
```
- To start a container using this image, you need to use the `docker run` command as follows:

```bash
docker run --name ns3-container -it hiarley/ns3-mmwave
```

- This way you will create a container named ns3-container, and to execute it, you can use:
```bash
docker exec -it ns3-container bash
```

## **Compilers and Development Tools**:

- **GCC**: GNU Compiler Collection (GCC) version 4.9 or higher. The recommended version is GCC 9.3.0 or higher.
- **G++**: C++ compiler associated with GCC.
- **Python**: Python 3.6 or higher for configuration and execution scripts.
- **Ranger:** Custom terminal to facilitate file viewing and changing
- **Fish**: Terminal used to complete Linux commands
- **Vim**: Text editor for code changes - (Can be replaced by Nano)

## **Required Libraries**:

- **GNU C Library** (glibc) version 2.27 or higher.
- **CMake** version 3.10 or higher to build some optional modules.
- **pkg-config** to facilitate configuration of dependent libraries.
- **libsqlite3-dev** for SQLite support.
- **libxml2-dev** for XML support.
- **libgtk-3-dev** and **libgtk2.0-0** for graphical interface (optional).
- **libpcap-dev** for packet capture support.
- **libgsl-dev** for GNU Scientific Library libraries.
- **libbz2-dev** for bzip2 compression support.
- **libboost-all-dev** for various support functionalities (optional).

## **Optional Tools**:

- **Netanim**: For simulation animation, requires Qt4 or Qt5 library.
- **GNUplot**: For graph generation.
- **Tcpdump**: For packet capture and analysis.
## Shell Scripts for NS3
- The project image also adds two files to facilitate program usage:
	reload.sh -- Refreshes the Packet.cc file to be built again
	move-files.sh -- Moves output files to a folder called dataframe
## **Development Modules**
- Ns3-Mmwave: (https://github.com/nyuwireless-unipd/ns3-mmwave) -- **Version 8.0** 
- ---
Reference:

https://ieeexplore.ieee.org/document/8344116/