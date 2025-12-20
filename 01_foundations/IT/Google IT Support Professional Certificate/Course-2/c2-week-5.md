# Week 5 – Networking Services
## POTS and Dial-Up
### Dial-Up, Modems and Point-to-Point Protocols
- Early Internet used **Plain Old Telephone Service (POTS)** / **Public Switched Telephone Network (PSTN)** for data.
- **USENET** pioneered data over phone lines (late 1970s).
- **Dial-up connection**: dials a phone number to establish link.
- **Modem** (modulator/demodulator): converts digital data → audio tones for POTS.
- Baud rates evolved: 110 bps (1950s) → 300 bps (USENET era) → 14.4 kbps (1990s household).
- Still used in some rural areas today.

---
## Broadband Connections
### What is Broadband?
- Any high-speed, **always-on** connection (no dialing needed).
- Unlike dial-up, not easily oversaturated.
- Businesses used **T-carrier technologies** (originally for multiple phone calls over one line).

### T-Carrier Technologies
- Invented by AT&T.
- **T1**: 24 channels × 64 kbps = 1.544 Mbps (originally voice, repurposed for data).
- "T1 line" now means any ~1.544 Mbps twisted-pair connection.
- **T3**: 28 T1 lines multiplexed = 44.7 Mbps.
- Dedicated, expensive; mainly business use.

### Digital Subscriber Lines (DSL)
- Uses existing phone twisted-pair at higher frequencies (no interference with voice).
- Simultaneous voice + data on same line.
- **DSLAM** (Digital Subscriber Line Access Multiplexer): establishes long-running connection.
- Types:
  - **ADSL**: Asymmetric (faster download than upload).
  - **SDSL**: Symmetric speeds (up to ~1.544 Mbps; business/original use).
  - **HDSL**: Higher speeds than SDSL.

### Cable Broadband
- Uses coaxial cable (originally TV).
- Deregulation (1984 Cable Act) → widespread infrastructure.
- Shares bandwidth with TV signals using unused frequencies.
- **Shared bandwidth model**: multiple users share until ISP core (unlike point-to-point DSL).
- Devices:
  - **Cable modem** (customer side).
  - **CMTS** (Cable Modem Termination System) at ISP.

### Fiber Connections
- Light signals → much longer distance without degradation vs copper.
- Expensive, so long used only in core networks; now reaching end users.
#### FTTX (Fiber to the X)
- **FTTN**: Fiber to neighborhood cabinet → copper/coax last leg.
- **FTTB**: Fiber to building → copper inside.
- **FTTH/FTTP**: Fiber direct to home/premises.
- **ONT** (Optical Network Terminator): converts fiber signals → Ethernet (replaces modem).

---
## WANs
### Wide Area Network Technologies
- Connects multiple sites as one logical network.
- Uses special ISP links (e.g., local loop → ISP core).
- Data link layer protocols similar to Internet routing (not Ethernet).
- High-speed; suited for large data across sites.
- Expensive vs consumer broadband.

### Point-to-Point VPNs
- **Site-to-site VPN**: encrypted tunnel between locations.
- Alternative to traditional WAN (cheaper with cloud growth).
- Handled by network devices (no per-user setup needed).

---
## Wireless Networking
### Introduction to Wireless Networking Technologies
- **Wi-Fi** = IEEE 802.11 family standards.
- Operates mainly on **2.4 GHz** (longer range, more interference) and **5 GHz** (faster, shorter range) bands.
- Newer standards (b → a → g → n → ac → ...) improve speed/range.
- 802.11 covers physical + data link layers.

#### 802.11 Frames
- Frame control (protocol info)
- Duration (transmission length)
- 4 address fields (source, destination, receiver, transmitter MACs)
- Sequence control (ordering)
- Data payload
- Frame check sequence (CRC checksum)

### Wireless Network Configurations
- **Ad-hoc**: Devices connect directly (peer-to-peer, no infrastructure).
- **WLAN** (Wireless LAN): Access points bridge wireless ↔ wired LAN.
- **Mesh**: Wireless APs interconnect (extends range without cabling each AP).

### Wireless Channels
- Subsections of frequency band to reduce interference/collisions.
- Overlapping channels cause issues; non-overlapping preferred.
- Many APs auto-select least congested channel (static or dynamic).

### Wireless Security
- No physical security → encryption needed.
- **WEP**: Weak (40-bit), deprecated.
- **WPA**: Improved (128-bit).
- **WPA2**: Current standard (256-bit).
- **MAC filtering**: Allow only approved device MACs.

### Cellular Networking
- Long-range radio (miles vs Wi-Fi).
- Divided into **cells** with non-overlapping frequencies (like WLAN channels).
- Cell towers = access points.
- Used by phones, tablets, laptops, cars.

### Mobile Device Networks
- Prefer **non-metered** (Wi-Fi) over cellular to save costs.
- **Bluetooth**: Short-range pairing for peripherals (exchange keys/PIN → auto-connect).

---
## One-line exam reminders
- Dial-up → modem + POTS (audio tones)
- Broadband = always-on, high-speed
- T1 = 1.544 Mbps (24 × 64 kbps)
- DSL = simultaneous voice + data on phone line
- Cable = shared bandwidth + CMTS
- Fiber = longest distance, ONT at premises
- WAN = multi-site logical network (expensive links)
- Site-to-site VPN = cheaper WAN alternative
- Wi-Fi = 802.11, 2.4/5 GHz bands
- WLAN needs access points; ad-hoc does not
- Channels reduce wireless collisions
- WPA2 = current Wi-Fi security standard
- Cellular = cells with reused frequencies