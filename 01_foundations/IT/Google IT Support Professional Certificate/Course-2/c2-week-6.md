# Week 6: Troubleshooting and the Future of Networking

### Intro
- **Error detection**: Protocol/program detects something went wrong.
- **Error recovery**: Protocol/program attempts to fix the issue.

---
## Verifying Connectivity

### Ping: Internet Control Message Protocol (ICMP)
- ICMP reports transmission failures (e.g., destination unreachable, time exceeded).
- ICMP packet structure:
  - **Type** (8 bits): Message category.
  - **Code** (8 bits): Specific reason.
  - **Checksum** (16 bits).
  - **Rest of header** (optional 32 bits).
  - **Data payload**: Includes original IP header + first 8 bytes of offending packet.
- **Ping**: Sends ICMP **Echo Request** → expects **Echo Reply**.
  - Windows: Defaults to 4 pings.
  - macOS/Linux: Runs indefinitely until interrupted (`Ctrl+C`).

### Traceroute
- Maps path between nodes; shows info per hop (network layer).
- Exploits **TTL** field: Starts at 1, increments per packet.
  - Linux/macOS: Uses UDP to high ports.
  - Windows (`tracert`): Uses ICMP Echo Request.
- Similar tools:
  - `mtr` (Linux/macOS): Real-time updates.
  - `pathping` (Windows): Runs ~50s, then shows aggregate data.

### Testing Port Connectivity
#### Netcat (`nc`) – Linux/macOS
- `nc <host> <port>`: Opens connection (interactive if successful).
- `-z`: Scan mode (no data sent, just checks if open).
- `-v`: Verbose output (human-readable success/failure).

#### Test-NetConnection – Windows (PowerShell)
- Without port: Performs enhanced ping (shows more details).
- With `-Port <port>`: Tests specific TCP port connectivity.

---
## Digging into DNS

### Name Resolution Tools
- **nslookup**: Universal tool (Windows, macOS, Linux).
  - `nslookup <hostname>`: Shows resolver used + result.
  - Interactive mode (`nslookup` alone): 
    - `set type=A/AAAA/MX/TXT` etc.
    - `set debug`: Full packet details.

### Public DNS Servers
- Free recursive resolvers anyone can use.
- Common examples:
  - Level 3: `4.2.2.1` – `4.2.2.6`
  - Google: `8.8.8.8`, `8.8.4.4`
- Most respond to ping → good for basic Internet connectivity tests.
- Caution: Research before using (risk of DNS hijacking).

### DNS Registration and Expiration
- **Registrar**: Organization that assigns domain names.
- Originally dominated by Network Solutions; now many accredited registrars.

### Hosts Files
- Legacy local mapping: IP → hostname (one per line).
- Processed **before** DNS queries on most OSes.
- Always includes loopback:
  - `127.0.0.1 localhost`
  - `::1 localhost` (IPv6)
- **Loopback address**: Traffic to self (never leaves device).
- Common malware vector: Redirects legitimate domains to malicious IPs.

---
## The Cloud

### What is The Cloud?
- **Cloud computing**: Shared, on-demand provisioning of computing resources.
- Core technology: **Hardware virtualization**.
  - **Host**: Physical machine.
  - **Guests**: Virtual machines.
  - **Hypervisor**: Software managing VMs (presents virtual hardware).

#### Cloud Types
- **Public cloud**: Run by third-party provider.
- **Private cloud**: Single org, usually on-premises.
- **Hybrid cloud**: Mix of private (sensitive) + public (general).

### Everything as a Service
- **IaaS** (Infrastructure as a Service): Rent servers/network/storage.
- **PaaS** (Platform as a Service): Rent execution environment for apps.
- **SaaS** (Software as a Service): Centrally hosted apps (e.g., Gmail, Office 365).

### Cloud Storage
- Provider handles security, availability, redundancy.
- Geographic distribution → disaster protection.
- Pay for actual usage; scales automatically.

---
## IPv6

### IPv6 Addressing and Subnetting
- 128-bit addresses (vs IPv4 32-bit).
- Written as 8 groups of 4 hex digits (e.g., 2001:0db8:0000:0000:0000:0000:1234:5678).
- Shortening rules:
  1. Drop leading zeros in groups.
  2. Replace one sequence of all-zero groups with `::` (once only).
- Loopback: `::1`.
- Reserved:
  - `2001:0db8::` → documentation.
  - `FF00::` → multicast.
  - `FE80::` → link-local unicast (auto-configured from MAC).
- No address classes; first 64 bits = network, last 64 bits = host.
- Subnetting: CIDR notation (e.g., /64).

### IPv6 Headers
- Simplified and shorter than IPv4:
  - Version (4 bits)
  - Traffic class (8 bits) – QoS
  - Flow label (20 bits) – QoS tagging
  - Payload length (16 bits)
  - Next header (8 bits) – chains optional headers
  - Hop limit (8 bits) – like TTL
  - Source + Destination addresses (128 bits each)
- Optional fields chained via Next Header.

### IPv6 and IPv4 Harmony
- **IPv4-mapped IPv6 addresses**: `::FFFF:<IPv4>` (e.g., `::FFFF:192.168.1.1`).
- **IPv6 tunneling**: Encapsulate IPv6 in IPv4 datagrams.
- **Tunnel brokers**: Third-party services providing tunnel endpoints.

---
## One-line exam reminders
- Ping = ICMP Echo Request/Reply
- Traceroute uses increasing TTL to reveal hops
- Netcat `-z -v` = quick port check
- nslookup interactive → set type=MX/TXT etc.
- Hosts file overrides DNS; contains 127.0.0.1 localhost
- Hypervisor manages virtual machines
- IaaS → infrastructure, PaaS → platform, SaaS → software
- IPv6 = 128-bit, :: shortening, no classes
- FE80:: = link-local, FF00:: = multicast
- IPv6 tunnels encapsulate over IPv4 Internet