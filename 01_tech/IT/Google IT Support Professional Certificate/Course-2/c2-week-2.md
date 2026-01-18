
## Week 2 – Network Layer

### What the Network Layer Does

The network layer is about **getting data from one network to another**, not caring about cables or apps.  
Its main job is **IP addressing + routing**.

---

### IP Addresses 

- IP addresses are **32 bits**, written as **4 octets** (`x.x.x.x`)
    
- They belong to **networks**, not devices
    
- Devices usually get IPs automatically via **DHCP**
    
- **Static IPs** are mostly for servers / network gear
    
- **Dynamic IPs** are for normal clients
    

---

### IP Datagrams

- Network-layer packets are called **IP datagrams**
    
- An IP datagram = **header + payload**
    
- The payload is usually a **TCP or UDP packet**
    
- The whole IP datagram gets stuffed inside an **Ethernet frame** (this is **encapsulation**)
    

Header fields that actually matter conceptually:

- **Source IP / Destination IP** – where it’s from / where it’s going
    
- **TTL (Time To Live)** – prevents packets from looping forever
    
- **Protocol** – tells IP whether it’s TCP or UDP
    
- **Fragmentation stuff** – lets big packets get split if needed
    

You don’t need to memorize every header field, just know _why they exist_.

---

### IP Classes 

Old system split IPs into:

- **Class A** – huge networks
    
- **Class B** – medium
    
- **Class C** – small
    

This system sucked at scale, so it got replaced by **CIDR**.  
You still see classes mentioned for historical reasons.

---

### ARP

- **ARP = IP → MAC lookup**
    
- Devices keep an **ARP table**
    
- Needed because Ethernet needs MAC addresses, but apps use IPs
    
- ARP entries expire because networks change
    

That’s it. Don’t overthink it.

---

### Subnetting 
Subnetting = **splitting one big network into smaller ones**

Why it exists:

- Huge networks are unmanageable
    
- Routers need structure
    
- Smaller networks = easier routing
    

Key idea:

- IP address = **network part + subnet part + host part**
    
- Routers use subnetting to know **where packets belong**
    

---

### Subnet Masks 

- A subnet mask is just **a 32-bit filter**
    
- It uses **binary AND** to separate:
    
    - what part is the **network/subnet**
        
    - what part is the **host**
        

Rules:

- `1` = keep this bit (network/subnet)
    
- `0` = ignore this bit (host)
    

Example:

- `255.255.255.0` → last octet is hosts
    
- `/27` = shorthand for how many bits are network/subnet
    

Hosts per subnet:

- Always **2ⁿ**
    
- Technically 2 addresses are reserved (network + broadcast), but conceptually they still count
    

---

### Binary & AND Operator

- Computers think in **binary**
    
- **AND** is used to apply subnet masks
    
- `1 AND 1 = 1`
    
- Everything else = `0`
    

Subnet masks work _only_ because of AND logic. That’s the entire reason binary matters here.

---

### CIDR 
- CIDR = **no classes**
    
- Everything is defined by **IP + /number**
    
- Example: `192.168.1.0/24`
    
- Combines network + subnet into one clean concept
    
- Makes routing tables smaller and smarter
    

CIDR is why the internet didn’t collapse.

---

### Routing (How Packets Actually Move)

- Routers forward packets based on **destination IP**
    
- They use **routing tables**
    
- Routers always try to pick the **shortest / best path**
    
- Multiple paths exist in case something breaks
    

Basic router logic:

1. Receive packet
    
2. Check destination IP
    
3. Look it up in routing table
    
4. Forward it
    

---

### Routing Protocols

Routers talk to each other using routing protocols.

- **Interior Gateway Protocols** → inside one organization
    
    - Distance-vector (older, simpler)
        
    - Link-state (modern, smarter, heavier)
        
- **Exterior Gateway Protocol** → between organizations
    
    - **BGP** (this is how the internet works at scale)
        

You don’t need to configure these—just know _why they exist_.

---

### Private / Non-Routable IPs

Some IP ranges **don’t go on the public internet**:

- `10.0.0.0/8`
    
- `172.16.0.0/12`
    
- `192.168.0.0/16`
    

Used for internal networks.

- NAT lets them talk to the internet anyway
    
- This is why home networks work
    

---

### One Exam-Style Concept to Remember

**TTL exists to stop packets from looping forever if routing breaks.**

---

### TL;DR

- Network layer = IP + routing
    
- IPs belong to networks
    
- ARP maps IP → MAC
    
- Subnetting = organization
    
- Subnet masks use binary AND
    
- CIDR replaces classes
    
- Routers move packets using tables
    
- Private IPs exist for internal networks
    