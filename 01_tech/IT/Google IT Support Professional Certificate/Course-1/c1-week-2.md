## Week 2 – Hardware (Cut to the Point)

### Big picture

You don’t really understand systems or infra unless you understand hardware **at a basic level**.  
Not to repair PCs for a living — just to know what’s going on under the hood.

---

## Core components (remember these)

### CPU

- The brain. Does calculations and runs instructions.
    
- Each CPU has an **instruction set** (depends on architecture).
    
- Must match the motherboard socket (LGA / PGA).
    
- Gets hot → needs a heat sink + fan.
    

---

### RAM

- Short-term memory.
    
- **Volatile** (data disappears when power is off).
    
- Used for running programs.
    
- DDR SDRAM is standard (DDR4-DDR5 is common).
    

---

### Storage

- HDD = cheaper, slower, moving parts.
    
- SSD = faster, more stable, more expensive.
    
- SATA is common.
    
- NVMe = very fast (uses PCIe).
    
- _Hot-swappable_ = can plug/unplug while running.
    

---

### Motherboard

- Connects everything.
    
- **Chipset** controls how parts talk:
    
    - Northbridge: CPU ↔ RAM / GPU
        
    - Southbridge: I/O (USB, storage, etc.)
        
- Uses **PCIe** for expansion cards.
    
- Common sizes:
    
    - ATX (standard)
        
    - ITX (smaller)
        

---

### Power Supply (PSU)

- Converts wall AC → low-voltage DC.
    
- Wattage = how much power it can deliver.
    
- 500W is enough for most normal PCs.
    
- Bigger is usually safer than barely enough.
    

---

## How data actually moves (high level)

- **Programs** = instructions.
    
- CPU works with:
    
    - **Registers** (tiny + super fast)
        
    - **Cache** (fast, smaller than RAM)
        
    - **RAM** (slower, bigger)
        
- **Buses** move data:
    
    - Address bus → where data is
        
    - Data bus → actual data
        
- **Clock cycle** tells CPU when to act.
    
- Overclocking = faster clocks (more heat, less stability).
    

I don’t need electrical details — just the flow.

---

## Ports & peripherals (don’t overthink)

- **Peripherals** = external devices (keyboard, mouse, display, storage).
    
- USB is king:
    
    - USB 2.0 / 3.0 / 3.1
        
    - Type-C is becoming universal.
        
- Video:
    
    - HDMI, DisplayPort (audio + video)
        
    - VGA / DVI (older)
        

**Important gotcha**

- MB ≠ Mb
    
    - 1 byte = 8 bits
        
    - Transfer speeds are in _bits_, file sizes in _bytes_.
        

---

## Mobile devices (same idea, compact)

- Phones are computers too.
    
- Use **SoC** (CPU + RAM on one chip).
    
- Components aren’t replaceable.
    
- Use batteries → limited charge cycles.
    
- Wrong charger = damage or fire risk.
    

---

## Booting & firmware (important)

### BIOS / UEFI

- Initializes hardware.
    
- Starts the OS.
    
- Stored on motherboard (ROM, not disk).
    
- UEFI = modern BIOS.
    

### POST

- Happens before BIOS.
    
- Checks hardware.
    
- Beep codes = errors.
    

### CMOS battery

- Stores time + boot settings.
    
- Dead battery = wrong time, boot issues.
    

---

## Assembly & safety (bare minimum)

- Static electricity can kill components → ground yourself.
    
- Use anti-static bags.
    
- Align CPU markers correctly.
    
- Apply thermal paste before heat sink.
    
- Good airflow matters.
    
- Cable management prevents damage.
    

---

## Mobile repair basics

- Check RMA policy first.
    
- Factory reset wipes everything.
    
- Use proper tools.
    
- Keep parts organized.
    
- Test after repair.
    

---

## Stuff I don’t need to memorize

- Exact USB speeds
    
- Every port color
    
- Detailed bus wiring
    
- IT helpdesk procedures
    

---

### One-line takeaway

Hardware is layered, data moves through buses and memory, firmware starts the system, and most problems come from power, heat, compatibility, or bad assumptions.

---
