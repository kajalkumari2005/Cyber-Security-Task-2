# Cyber Security & Ethical Hacking Internship – Task 2

## Reconnaissance, Information Gathering, Network Scanning & Enumeration

### 1. Introduction

Network reconnaissance is the process of collecting information about a computer or network before performing security assessment activities. It can include discovering active hosts, identifying open ports, detecting services, gathering DNS information and observing network traffic.

This project was performed in an authorized Kali Linux lab environment. The practical work included Nmap scanning, DNS enumeration, WHOIS lookup, traceroute, Wireshark traffic analysis, Netcat testing and Python-based network reconnaissance.

### 2. Objectives

The main objectives of this task were:

- To understand passive and active reconnaissance.
- To discover hosts in a network.
- To identify open and closed ports.
- To perform service and version detection.
- To perform basic OS detection.
- To understand DNS and WHOIS information gathering.
- To analyze network traffic using Wireshark.
- To understand Netcat-based connectivity and banner testing.
- To automate basic reconnaissance tasks using Python.
- To generate CSV, JSON and HTML reports.

### 3. Lab Environment

The practical work was performed using:

- Operating System: Kali Linux
- Network Interface: eth0
- Kali Linux IP: 10.0.2.15
- Network: 10.0.2.0/24
- VirtualBox NAT Gateway: 10.0.2.2
- Tools: Nmap, Wireshark, Netcat, DNS utilities, Traceroute and Python 3.

All testing of network services was performed on the authorized local laboratory system.

### 4. Host Discovery

Nmap was used to perform host discovery on the local network.

Command:

nmap -sn 10.0.2.0/24

The scan was used to identify hosts responding on the local network.

### 5. Port Scanning

A local HTTP server was started on port 8000 for authorized testing.

Command:

python3 -m http.server 8000 --bind 0.0.0.0

The port was then scanned using Nmap.

Command:

nmap -p 8000 10.0.2.15

The scan identified port 8000 as open.

Additional ports were tested using the Python port scanner.

| Port | Status |
|---|---|
| 22 | CLOSED |
| 80 | CLOSED |
| 443 | CLOSED |
| 8000 | OPEN |
| 9000 | CLOSED |

### 6. Service and Version Detection

Nmap service detection was performed on the locally hosted HTTP service.

Command:

nmap -sV -p 8000 10.0.2.15

This demonstrated how Nmap can identify information about services running on an open port.

### 7. OS Detection

Basic operating system detection was tested using:

sudo nmap -O 10.0.2.15

OS detection results can depend on network conditions and available responses. Therefore, the result was treated as a demonstration of the Nmap OS detection technique rather than a definitive identification.

### 8. DNS Enumeration

DNS utilities were used to obtain information about domain names.

Commands used:

nslookup example.com

dig example.com

dig example.com A

Reverse DNS was also tested:

dig -x 8.8.8.8

These commands demonstrate forward DNS lookup, DNS record retrieval and reverse DNS lookup.

### 9. WHOIS Lookup

WHOIS was used to obtain publicly available registration information.

Command:

whois example.com

WHOIS information can contain domain registration and administrative information depending on the domain and registrar.

### 10. Traceroute

Traceroute was used to observe the network path toward a destination.

Command:

traceroute example.com

Some intermediate hops displayed asterisks. This can occur when network devices do not respond to traceroute probes or filter them.

### 11. Wireshark Traffic Analysis

Wireshark was used to capture and analyze network traffic on the eth0 interface.

The following traffic types were observed:

- DNS traffic
- TCP traffic
- UDP traffic
- ICMP traffic

Example display filters used:

dns

tcp

udp

icmp

DNS traffic was generated using nslookup, TCP traffic was generated using HTTP requests, and ICMP traffic was generated using ping.

### 12. Netcat Testing

Netcat was used to test local TCP connectivity.

A listening service was started using:

nc -lvnp 9000

A second terminal connected to it using:

nc 127.0.0.1 9000

A test message was transmitted between the terminals.

Netcat was also used to interact with the local HTTP service on port 8000 for basic banner/response testing.

### 13. Python Automation

Python scripts were created to automate basic reconnaissance tasks.

The project includes scripts for:

- Host discovery
- TCP port scanning
- Banner grabbing
- CSV report generation
- JSON report generation
- HTML report generation

The Python port scanner tested selected ports and identified port 8000 as open.

### 14. Banner Grabbing

A Python banner-grabbing script connected to the local HTTP service and sent an HTTP HEAD request.

The script demonstrated how a response from a network service can provide information about the service.

### 15. Report Generation

The Python scripts generated three report formats:

- CSV
- JSON
- HTML

The reports contain the target address and port scanning results.

### 16. Project Structure

The project is organized as follows:

Task-2/

├── README.md

├── requirements.txt

├── src/

├── reports/

├── screenshots/

├── captures/

├── diagrams/

└── report/

The src directory contains Python scripts. The reports directory contains generated reports. Screenshots contains practical evidence, while captures is intended for Wireshark capture files. The diagrams directory contains the network topology representation.

### 17. Results

The practical exercises demonstrated the basic process of network reconnaissance and enumeration.

The main local scanning result was:

- Target: 10.0.2.15
- Port 8000: OPEN
- Ports 22, 80, 443 and 9000: CLOSED

DNS queries successfully demonstrated domain-name resolution and DNS record retrieval.

Wireshark demonstrated how network packets can be captured and filtered according to protocols.

Netcat demonstrated basic TCP listening and connectivity.

Python demonstrated how reconnaissance activities can be partially automated and converted into structured reports.

### 18. Limitations

The practical environment contained a limited number of authorized hosts. Therefore, testing was mainly performed against the local Kali Linux system and its locally created HTTP service.

The Python host-discovery demonstration was basic and should not be considered a complete production-grade host discovery system. A more advanced implementation could use ICMP, TCP probes or Nmap integration and could accept a user-provided IP range.

### 19. Ethical and Legal Considerations

Network reconnaissance must only be performed on systems for which permission has been obtained.

Unauthorized scanning or traffic capture may violate organizational policies or applicable laws. During this project, scanning and service testing were restricted to the authorized laboratory environment.

### 20. Conclusion

This task provided practical experience with network reconnaissance, information gathering, scanning and enumeration.

Nmap was used for host discovery, port scanning, service detection and OS detection. DNS utilities and WHOIS demonstrated information gathering. Traceroute showed network paths, while Wireshark provided practical packet analysis. Netcat demonstrated TCP connectivity and banner testing.

Python automation demonstrated how repetitive reconnaissance activities can be converted into scripts and structured reports.

The project provided a foundation for understanding network security assessment and responsible reconnaissance in an authorized environment.
