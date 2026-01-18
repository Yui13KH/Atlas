
## Course 2 – Networking

### Week 1: Intro to Networking 

### What networking actually is

- **Networking** = how computers talk to each other.
    
- They do that using **protocols** (agreed rules).
    
- The Internet = networks connected together.  
    The Web = stuff _on top_ of the Internet.
    

---

## TCP/IP Five-Layer Model

Used to understand _where_ things break and _what_ does what.

1. **Physical** – wires, cables, signals, electricity/light
    
2. **Data Link** – Ethernet, MAC addresses, frames (local delivery)
    
3. **Network** – IP, routers, moving data between networks
    
4. **Transport** – TCP / UDP, which app gets the data
    
5. **Application** – HTTP, DNS, etc. (what users actually see)
    

> Network layer = “get it to the right computer”  
> Transport layer = “get it to the right program”

Mail analogy is fine but honestly: **just remember the job of each layer**.

---

## Networking devices

### Cables

- **Copper (Cat5e / Cat6)**
    
    - Sends data as voltage changes
        
    - Cheap, common
        
    - Crosstalk = signal bleeding → errors
        
- **Fiber**
    
    - Sends data as light
        
    - Faster, longer distances, no EMI
        
    - Expensive + fragile
        
    - Mostly data centers / backbone stuff
        

---

### Hubs vs Switches 

- **Hub** (Layer 1)
    
    - Sends everything to everyone
        
    - One big collision domain
        
    - Basically obsolete
        
- **Switch** (Layer 2)
    
    - Looks at **MAC addresses**
        
    - Sends data only where it’s needed
        
    - Faster, fewer collisions  
        → **This is why hubs died**
        

---

### Routers (Layer 3)

- Connect **different networks**
    
- Look at **IP addresses**
    
- Home router = LAN ↔ ISP
    
- ISP core routers = Internet backbone
    
- Routers talk to each other using **BGP**
    
    - BGP decides best paths across the Internet
        

---

## Servers & clients

- **Server** = provides data
    
- **Client** = requests data
    
- A machine can be _both_ depending on context
    
- The name usually refers to **primary role**, not exclusivity
    

---

## Physical Layer

- Data = **bits (0s and 1s)**
    
- Copper cables carry constant charge
    
- Bits are sent via **modulation (line coding)**  
    → voltage changes = 0 or 1
    

### Duplex

- **Simplex** – one direction (baby monitor)
    
- **Duplex** – both directions
    
- **Full-duplex** – both talk at once (normal)
    
- **Half-duplex** – only one at a time (usually a problem)
    

---

### Ports & patch panels

- **RJ45** = standard Ethernet plug
    
- Ports have LEDs:
    
    - Link light = connected
        
    - Activity light = traffic
        
- **Patch panels** = cable organization only  
    (no logic, no routing)
    

---

## Data Link Layer (Ethernet & MACs)

### Ethernet

- Most common Layer 2 protocol
    
- Handles local delivery
    
- Uses **CSMA/CD** (old-school collision handling)
    
    - Mostly irrelevant now because switches exist
        

---

### MAC addresses 

- 48 bits = 6 bytes = **6 octets**
    
- Written in hex (0–9, A–F)
    
- First 3 octets = **OUI** (manufacturer)
    
- Last 3 = unique per device
    
- Globally unique (huge address space)
    

---

### Traffic types

- **Unicast** – one → one
    
- **Multicast** – one → selected group
    
- **Broadcast** – one → everyone
    
    - Ethernet broadcast = FF:FF:FF:FF:FF:FF
        
    - Used for discovery (ARP, etc.)
        

---

## Ethernet frame 

Ethernet sends **frames** (Layer 2 packets).

Main idea:

- **Headers** identify who it’s for and what it is
    
- **Payload** = actual data (IP, TCP, app stuff)
    
- **CRC** checks integrity
    

Key parts:

- Preamble + SFD → sync
    
- Destination MAC
    
- Source MAC
    
- EtherType / VLAN tag
    
- Payload (46–1500 bytes)
    
- Frame Check Sequence (CRC)
    

Ethernet:

- Detects corruption
    
- Does **not** fix it  
    (higher layers decide retransmission)
    

---

## VLANs 

- **VLAN** = multiple logical networks on same hardware
    
- Traffic separated by tags
    
- Common use:
    
    - Phones on one VLAN
        
    - PCs on another
        
- Improves security + organization
    

---

## TL;DR — what actually matters

- TCP/IP layers and what each one does
    
- Switch = MAC, Router = IP
    
- Ethernet + MAC addresses = local delivery
    
- Fiber vs copper (why/when)
    
- Frames carry data, CRC checks integrity
    
- VLANs = logical separation
    

