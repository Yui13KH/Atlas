Alright, same treatment again — **hard cut, high-signal, written like you wrote it**, no fluff.

---

## Week 3 – Operating Systems 

### What an OS is (real definition)

- The OS is the thing that **manages hardware** and lets users/apps interact with it.
    
- Two parts:
    
    - **Kernel** → talks directly to hardware.
        
    - **User space** → shells, GUIs, system tools, apps.
        

Windows, macOS, Linux — same ideas, different implementations.

---

## Remote access

### SSH

- Used to control another machine remotely.
    
- Needs:
    
    - SSH client (your machine)
        
    - SSH server (remote machine)
        
- SSH server = background service, not hardware.
    
- You need:
    
    - A user account on the target
        
    - IP / hostname
        
- Password auth exists but **keys are better**.
    
- SSH keys = public/private pair.
    
    - Public locks, private unlocks.
        
- Linux: OpenSSH
    
- Windows: PuTTY (and Plink)
    

### Other remote stuff

- **RDP** = Windows remote desktop (GUI).
    
- **VPN** = puts you _inside_ another network.
    

---

## Kernel responsibilities (remember this list)

The kernel handles:

- **Process management**
    
- **Memory management**
    
- **File management**
    
- **I/O management**
    

That’s basically it.

---

## Processes

- **Program** = app on disk.
    
- **Process** = program that’s running.
    
- CPU doesn’t run everything at once.
    
- Uses **time slices** (milliseconds).
    
- Feels simultaneous, isn’t.
    

---

## Memory (important conceptually)

- RAM is limited → **virtual memory** exists.
    
- Virtual memory = RAM + disk.
    
- Programs are split into **pages**.
    
- Pages not in use go to disk (**swap**).
    
- Disk is slower than RAM → heavy swapping = slow system.
    

---

## Files & file systems

File =

- Data
    
- Metadata (owner, perms, size, timestamps)
    
- File system
    

Common file systems:

- Windows → **NTFS**
    
- macOS → **APFS**
    
- Linux → **ext4**
    

Stick to what the OS expects.

---

## I/O (why systems feel slow)

- I/O = keyboards, disks, screens, network, etc.
    
- Kernel manages device communication via drivers.
    
- “System is slow” is usually:
    
    - Not enough RAM
        
    - CPU bottleneck
        
    - Disk or I/O congestion
        

---

## User interaction

- **GUI** = clicks, windows, abstraction.
    
- **Shell / CLI** = text commands.
    
- Linux → **BASH**
    
- Windows → **PowerShell**
    

Security people live in the CLI.

---

## Logs

- Logs = system diary.
    
- Used for debugging, auditing, incident response.
    
- If something broke → logs first.
    

---

## Boot process (high-level)

1. Power on
    
2. BIOS/UEFI runs POST
    
3. Boot device selected
    
4. Bootloader loads OS
    
5. Kernel loads
    
6. Drivers + system services start
    
7. User space starts (login, desktop)
    

UEFI = modern BIOS.

---

## Virtual machines

- VM = software computer.
    
- Used for:
    
    - Testing
        
    - Isolation
        
    - Malware analysis
        
    - Labs
        

Very relevant for security.

---

## Mobile OS (quick)

- Optimized for battery.
    
- Less features than desktop OS.
    
- Touch/voice require extra drivers.
    
- Same OS ideas, just constrained.
    

---

## Chrome OS 

- Browser-centric OS.
    
- Most data lives in the cloud.
    
- No admin rights for users.
    
- Auto-updates + rollback.
    
- Strong security by design.
    

---

## Stuff I don’t need to memorize

- Exact install steps
    
- GUI-only workflows
    
- OS marketing differences
    

---

### One-line takeaway

The OS is a resource manager: kernel controls hardware, user space interacts with it, and everything boils down to processes, memory, I/O, and files.

---
