
## Week 4 – Networking (Only the Stuff That Matters)

### What networking actually is

- A **network** = computers connected together.
    
- **Internet ≠ Web**
    
    - Internet = physical infrastructure (cables, routers, servers).
        
    - Web = websites + data on top of the Internet.
        
- IT networking = building, managing, fixing those connections.
    

---

### Clients, servers, ISPs

- **Servers** connect directly to the Internet and provide stuff (websites, services).
    
- **Clients** (your laptop/phone) request stuff from servers.
    
- You don’t connect “to the Internet” directly — you go through an **ISP**.
    

---

### Addresses (this part actually matters)

- **IP address** → logical network address (where you are).
    
- **MAC address** → hardware address (who you are).
    
- You need **both** for communication.
    
- Data moves as **packets**, gets reassembled at the destination.
    

Good mental model:

- IP = street address
    
- MAC = person’s name at that address
    

---

### Networking hardware (don’t memorize, understand)

- **Ethernet** = wired
    
- **Wi-Fi** = wireless
    
- **Fiber** = very fast, light-based
    
- **Router** = connects networks, decides where traffic goes
    
- **Switch** = connects devices inside a network
    
- **Hub** = dumb, broadcasts to everyone (basically obsolete)
    

If something breaks:  
device → cable → switch → router → ISP → Internet

---

### Protocols (language of the Internet)

- Protocols = rules for how data moves.
    
- **TCP/IP** is the core of the Internet.
    
    - **IP** → addressing + routing
        
    - **TCP** → reliable delivery (order, retransmission)
        

That’s enough for now.

---

### The Web basics

- Websites = **HTML** documents.
    
- **URL** = address of a resource.
    
- **Domain name** = human-friendly name.
    
- **DNS** = phonebook that maps domain → IP.
    
- Every website visit = DNS lookup + server logs your IP.
    

---

### Why IPv4 is a problem

- IPv4 = 32 bits → ~4.3 billion addresses.
    
- Not enough anymore.
    
- **IPv6** = 128 bits → basically unlimited (slow adoption).
    
- **NAT** exists to cheat the system:
    
    - One public IP
        
    - Many private internal IPs
        

Receptionist analogy works, keep that.

---

### Internet history (only the takeaway)

- ARPANET → early networking.
    
- TCP/IP → allowed networks to talk to each other.
    
- WWW → made the Internet usable for humans.
    

---

### Impact / security angle

- Internet = globalization.
    
- **IoT** = everything online (often insecure).
    
- Privacy isn’t personal anymore — it’s political.
    
- Security isn’t optional.
    
- Everyone gets hacked eventually → plan for it.
    

---

### One-line takeaway

Networking is about **addresses, packets, protocols, and routing**, and most problems come down to IPs, DNS, or broken links in the chain.

---
