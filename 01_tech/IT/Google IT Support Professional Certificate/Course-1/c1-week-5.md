
## Week 5 – Software (Trimmed, No BS)

### What software actually is

- **Software** = instructions that tell hardware what to do.
    
- Hardware is physical, software is not.
    
- Users interact with computers **through software**, not hardware.
    

---

### Coding vs scripting vs programming (don’t overthink it)

- **Coding** = translating instructions into something a computer understands.
    
- **Programming** = writing full programs in proper languages.
    
- **Scripting** = small programs for specific tasks (automation, fixes, shortcuts).
    
- Software = something that was programmed (one way or another).
    

---

### Types of software (only what matters)

- **Application software** → stuff you use (browser, editor, tools).
    
- **System software** → keeps the OS running.
    
- **Drivers** → let hardware talk to the OS.
    
- **Firmware** → software baked into hardware (BIOS/UEFI).
    
- **Open-source software (OSS)** → free to use, modify, share (Linux, Firefox, etc).
    

---

### Abstraction (important idea, not details)

- CPUs are different.
    
- Programming languages + abstraction let the _same code_ run on different hardware.
    
- Without abstraction, everything would be CPU-specific hell.
    

---

### How software execution evolved (simplified)

- Early days: binary → awful.
    
- **Assembly** → human-readable but still hardware-specific.
    
- **Compiled languages**
    
    - Code → compiler → machine instructions.
        
    - Faster, hardware-specific output.
        
- **Interpreted languages**
    
    - Code runs through an interpreter at runtime.
        
    - Slower, more flexible.
        
- Scripts = interpreted, great for quick tasks.
    

Key takeaway:

- **Compiled** = ahead of time
    
- **Interpreted** = just-in-time
    

---

### Why scripting actually matters (for IT / security)

- Automates boring or repetitive tasks.
    
- Solve a problem once → reuse forever.
    
- Used for log parsing, automation, troubleshooting, attacks, defense.
    

---

### Managing software (real-world stuff)

- Programs / apps / software = same idea.
    
- Always **test** before deploying.
    
- **Old software = security risk**.
    
- Bugs = unexpected behavior → often exploitable.
    
- Keep systems **updated**.
    

---

### Installing software (bare minimum)

**Windows**

- `.exe` = executable.
    
- Match **32-bit / 64-bit** with CPU.
    
- Reboot if asked.
    
- Verify installs via _Apps & Features_.
    

**Linux**

- Use package manager (`apt` on Ubuntu).
    
- Install: `sudo apt install <package>`
    
- Remove: `sudo apt remove <package>`
    
- `sudo` = admin privileges.
    

---

### Automation

- Managing one machine is easy.
    
- Managing many machines → **automation**.
    
- Scripts can:
    
    - Install software
        
    - Read logs
        
    - Detect errors
        
    - Fix issues automatically
        

This is where IT stops being manual labor.

---

### One-line takeaway

Software is layers of abstraction on top of hardware, and scripting is the shortcut that turns “doing work” into “letting machines do it for you”.
