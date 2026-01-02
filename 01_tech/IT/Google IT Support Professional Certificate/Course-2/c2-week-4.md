
# Week 4 – Networking Services 
## DNS (Domain Name System)

**Purpose**

- Maps domain names → IP addresses
    
- Allows IP changes without user impact
    
- Enables geo-routing (different IPs per region)
    

**Basic requirements for a host**

- IP address
    
- Subnet mask
    
- Default gateway
    
- DNS server
    

---

### DNS Server Types

- **Caching DNS**: stores results temporarily (TTL-based)
    
- **Recursive DNS**: performs full lookup on behalf of client
    
- **Root servers**: know TLD servers
    
- **TLD servers**: know authoritative servers
    
- **Authoritative servers**: give final answer
    

> One server can serve multiple roles.

---

### DNS Resolution

1. Client → recursive DNS
    
2. Recursive DNS → **root server**
    
3. Root → **TLD server**
    
4. TLD → **authoritative server**
    
5. Authoritative → final IP
    

**TTL (Time To Live)**

- How long DNS results may be cached (seconds)
    
- Longer TTL = slower global propagation of changes
    

---

### DNS Transport

- Uses **UDP port 53**
    
- TCP used only if response is too large
    
- No retransmission at DNS level (client retries)
    

---

### DNS Record Types

- **A** → IPv4 address
    
- **AAAA** → IPv6 address
    
- **CNAME** → alias to another domain
    
- **MX** → mail server
    
- **SRV** → service location
    
- **TXT** → arbitrary text (SPF, verification, config)
    
- **PTR** → reverse lookup (IP → name)
    

---

### Domain Structure

- **TLD**: `.com`, `.org`
    
- **Domain**: `example`
    
- **Subdomain**: `www`
    
- **FQDN**: `www.example.com`
    

Limits:

- Max 63 chars per label
    
- Max 255 chars total
    
- Up to 127 levels
    

---

### DNS Zones

- Authoritative servers manage **zones**
    
- Zones do **not overlap**
    
- Configured via **zone files**
    
- Must include:
    
    - **SOA record**
        
    - **NS records**
        
    - Resource records (A, AAAA, CNAME, etc.)
        

---

## DHCP (Dynamic Host Configuration Protocol)

**Purpose**

- Automatically assigns:
    
    - IP address
        
    - Subnet mask
        
    - Gateway
        
    - DNS server
        

**Runs at**

- Application layer
    
- Uses **UDP**
    
    - Server: port **67**
        
    - Client: port **68**
        

---

### DHCP Allocation Types

- **Dynamic**: random IP from pool
    
- **Automatic**: same IP reused if possible
    
- **Fixed**: MAC → IP mapping (manual)
    

---

### DHCP Process (DORA)

1. **DISCOVER** (broadcast, 0.0.0.0 → 255.255.255.255)
    
2. **OFFER**
    
3. **REQUEST**
    
4. **ACK**
    

- Result = **DHCP lease**
    
- Lease expires → process repeats
    

---

## NAT (Network Address Translation)

**What it is**

- Technique (not protocol)
    
- Rewrites **source IP** of outgoing packets
    

**Why**

- Hide internal IPs
    
- Save IPv4 addresses
    

---

### NAT Types / Concepts

- **One-to-many NAT**: many private IPs → one public IP
    
- **IP masquerading**: internal hosts invisible externally
    

---

### NAT + Transport Layer

- **Port preservation**: keeps same source port if possible
    
- If conflict → router picks new port
    
- Router tracks IP+port mappings
    

---

### Port Forwarding

- Maps external port → internal host
    
- Allows inbound access despite NAT
    

---

### IPv4 Address Exhaustion

- IPv4 exhausted at RIR level
    
- NAT + private IP ranges are temporary solutions
    
- IPv6 is the real fix
    

---

## VPNs (Virtual Private Networks)

**Purpose**

- Extend private networks over public networks
    
- Remote access or site-to-site connectivity
    

**How**

- Encrypted **tunnels**
    
- Encapsulate full packets inside payloads
    
- Create **virtual network interface**
    

**Notes**

- Strong authentication (often 2FA)
    
- Technique, not a single protocol
    

---

## Proxies

**Definition**

- Server acting on behalf of a client
    

**Uses**

- Anonymity
    
- Security
    
- Filtering
    
- Performance
    

---

### Proxy Types

- **Forward proxy**: client → proxy → internet
    
- **Reverse proxy**: internet → proxy → internal servers
    
    - Load balancing
        
    - TLS termination
        

---

## One-line exam reminders

- DNS = UDP 53
    
- DHCP = UDP 67/68
    
- NAT rewrites source IP
    
- TTL exists in DNS **and** IP (different meanings)
    
- VPN = encrypted tunnel
    
- Proxy ≠ VPN
    

---
