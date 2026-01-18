
## Week 3 – Transport & Application Layers

### Big Picture

- **Transport layer** = gets data to the **right app**
    
- **Application layer** = apps actually talking in a format they understand
    

Everything here is about **process-to-process communication**, not just machine-to-machine.

---

## Transport Layer

### Multiplexing & Demultiplexing

This is how one machine can run tons of network apps at once.

- **Multiplexing**: sending traffic from many apps → one network connection
    
- **Demultiplexing**: receiving traffic → routing it to the correct app
    

This is done using **ports**.

---

### Ports

- A **port** is a 16-bit number (0–65535)
    
- IP = _which machine_
    
- Port = _which program_
    

Format:

- `IP:PORT` → socket address  
    Example: `10.1.1.100:80`
    

Servers **listen** on ports.  
Clients **connect** using ports.

---

### TCP (Reliable but Heavy)

TCP is:

- **Connection-oriented**
    
- Reliable
    
- Ordered
    
- Slower due to overhead
    

TCP is used when **accuracy matters** (websites, logins, file transfers).

---

### TCP Segments 

- TCP data = **TCP segment**
    
- Segment = header + payload
    
- Payload = app data
    

Important header ideas:

- **Source port / destination port** – who sent it, who should get it
    
- **Sequence number** – keeps data in order
    
- **Acknowledgement number** – confirms receipt
    
- **Window size** – flow control
    
- **Checksum** – data integrity
    

You do _not_ need to memorize the full header layout.

---

### TCP Control Flags (Know the Meaning, Not the Order)

Key ones:

- **SYN** – start a connection
    
- **ACK** – acknowledge data
    
- **FIN** – close connection
    
- **RST** – something broke, reset
    
- **PSH / URG** – mostly legacy / rarely used
    

---

### TCP Three-Way Handshake (Very Important)

How TCP connections start:

1. Client → **SYN**
    
2. Server → **SYN + ACK**
    
3. Client → **ACK**
    

Connection is now **established** and full-duplex.

Closing the connection uses a **four-way handshake** with FIN + ACKs.

---

### TCP Socket States

You’ll mostly see these when troubleshooting:

- **LISTEN** – server waiting
    
- **SYN_SENT** – client trying to connect
    
- **ESTABLISHED** – connection is active
    
- **FIN_WAIT / CLOSE_WAIT** – connection shutting down
    
- **CLOSED** – done
    

Ports are abstract.  
**Sockets are real**, created by programs.

---

### UDP (Fast, Dumb, Useful)

UDP is:

- **Connectionless**
    
- No acknowledgements
    
- No ordering
    
- No retries
    

Why it exists:

- Less overhead
    
- Faster
    
- Better for real-time stuff
    

Used for:

- Streaming
    
- Voice calls
    
- Games
    
- DNS
    

If a packet drops, UDP doesn’t care.

---

### Ports: Who Uses What

Port ranges (IANA-defined):

- **0** – unused
    
- **1–1023** → system / well-known ports
    
    - HTTP → 80
        
    - FTP → 21
        
- **1024–49151** → registered ports
    
    - Example: databases
        
- **49152–65535** → ephemeral ports
    
    - Used by clients for outbound connections
        

Clients use **ephemeral ports**.  
Servers listen on **fixed ports**.

---

### Firewalls (Practical Security)

- Firewalls block or allow traffic based on rules
    
- Most common rule: **block/allow ports**
    
- Can exist:
    
    - On routers
        
    - On servers
        
    - On personal computers
        

Most home routers = **router + firewall in one box**

---

## Application Layer 

- This is the **actual data apps care about**
    
- Web pages, videos, files, print jobs, etc.
    
- No single “application protocol”
    
    - HTTP, FTP, SMTP, DNS, etc.
        

Transport layer doesn’t care _what_ the data is.  
Application layer does.

---

### TCP/IP vs OSI

- TCP/IP = **5 layers** (practical)
    
- OSI = **7 layers** (academic)
    

OSI extra layers:

- **Session** – manages sessions between apps
    
- **Presentation** – formatting, encryption, compression
    

Real-world networking mostly thinks in **TCP/IP**, but certs love **OSI**.

---

### TL;DR 

- Transport layer = ports + TCP/UDP
    
- TCP = reliable, slow, ordered
    
- UDP = fast, unreliable, unordered
    
- Ports decide which app gets data
    
- Firewalls block traffic by rules
    
- Application layer = actual app data
