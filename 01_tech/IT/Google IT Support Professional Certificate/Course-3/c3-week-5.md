# Week 5: Process Management

## Life of a Process

### Programs vs Processes
- **Programs**: apps/executables (e.g., Chrome.exe)
- **Processes**: running instances of programs – take CPU/RAM
- Each gets a unique **process ID (PID)**
- Kernel allocates resources

**Background processes** (daemons): run silently, handle system stuff like networking, logging, scheduling

### Windows: Creation & Termination
- Boot: first user-mode process = `smss.exe` (Session Manager) → sets up OS
- Then starts `winlogon.exe` (login) and `csrss.exe` (GUI/console)
- Processes have parents but can run independently
- Kill: `taskkill /PID <number>`

### Linux: Creation & Termination
- All processes have parent-child relationship
- First process: **init** (PID 1) → starts everything else
- Processes usually terminate cleanly on finish, release resources
- If parent dies, children often become orphans (adopted by init)

## Managing Processes

### Windows: Viewing Info
- **Task Manager** (`Ctrl+Shift+Esc`): Processes tab → name, user, CPU/mem usage
  - Details tab → shows PID
  - End task to kill
- CLI:
  - `tasklist` (cmd)
  - `Get-Process` (PowerShell)

**Process Explorer** (download from MS):
- Tree view (shows parent-child)
- Bottom pane: open files/handles for selected process
- Options: Kill, Kill Tree, Restart, Suspend
- Restarted process → parent becomes Process Explorer

### Linux: Viewing Info
- `ps -x`: snapshot of your processes (PID, TTY, STAT, TIME, CMD)
  - STAT: R=running/runnable, S=sleeping, T=stopped, etc.
- `/proc`: virtual dir with process folders (not super practical for quick view)

### Signals (Both OS)
- **SIGINT** (interrupt): `Ctrl+C` → graceful stop

#### Linux Signals
- `kill <PID>` → default **SIGTERM** (ask nicely to quit, allows cleanup)
- `kill -KILL <PID>` or `kill -9 <PID>` → **SIGKILL** (force kill, no cleanup – last resort)
- `kill -TSTP <PID>` or `Ctrl+Z` → **SIGTSTP** (pause/suspend)
- `kill -CONT <PID>` → resume suspended process

## Mobile App Management
- **Foreground app**: the one you're using
- **Background apps**: suspended (paused, not fully closed)
- Open **App Switcher** → swipe to close background apps (frees RAM)

## Process Utilization / Resource Monitoring

### Windows
- **Resource Monitor** (search in Start): real-time CPU, mem, disk, network
- `Get-Process` in PowerShell → sort/filter for heavy users

### Linux
- **top**: live view of top resource hogs
  - Shows overall tasks, CPU%, mem%, per-process usage
  - Quit: `q`
- **uptime**: current time, system runtime, logged users, load averages (1/5/15 min)
  - Load avg tells how busy CPU has been
- **lsof**: list open files + which processes own them (great for debugging locked files)
