# Week 3: Package and Software Management

## Software Distribution

### Windows: Software Packages
- Usually `.exe` files (executables in Microsoft's PE format) – contain code, text, images, sometimes `.msi`
- **.msi** (Microsoft Installer): guides install/maintenance/removal via Windows Installer (handles uninstall too)
- Custom `.exe` installers: more control, but less automated
- **Microsoft Store** (since Win8): for APPX-packaged universal apps

### Linux: Software Packages
- Distro-specific: Red Hat = `.rpm`, Ubuntu/Debian = `.deb`
- Install `.deb`: `sudo dpkg -i SOFTWARE.deb`
- List installed: `dpkg -l` or `dpkg -l | grep SOFTWARE`

### Mobile App Packages
- Distributed via **app stores** (central trusted repos) – apps are signed by devs
- **App store app** = package manager; **service** = repo
- **Enterprise apps**: custom, signed with company cert
- **Side-loading**: direct install (risky, for devs)
- Apps are standalone (own deps/cache) – factory reset = clear app cache

### Archives (Compressed Files)
- **Archives**: multiple files squished into one (e.g., `.tar`, `.zip`, `.rar`)
- **Installing from source**: extract archive first
- Tools: **7-Zip** (Win/Linux: `7z -e FILE`), Linux `tar`

## Package Dependencies
Apps rely on other code (**dependencies**).

### Windows
- **DLLs** (dynamic-link libraries): shared code, loaded once for multiple apps (saves memory)
- **SxS** (side-by-side): manages shared libs in `C:\Windows\WinSxS` via manifests (handles multiple versions)
- Find packages/deps: PowerShell `Find-Package` (**cmdlet** = verb-noun command)

### Linux
- Standalone packages don't auto-install deps – need **package manager** for that

## Package Managers

### Windows
- **Chocolatey** (3rd-party): CLI install from its repo (uses PowerShell)

### Linux: APT (Advanced Package Tool)
- Handles install/remove/update/deps/cleanup
- **Repos**: central package servers (add via `/etc/apt/sources.list`)
- **PPA** (Personal Package Archive): user repos on Launchpad (use cautiously – could be sketchy)
- Commands:
  - `apt update`: refresh repo lists
  - `apt upgrade`: install updates
  - `apt --help`: more info

## What's Happening Under the Hood?

### Windows
- `.exe` install: custom or via Windows Installer (tracks actions for easy uninstall)
- **MSI files**: database of install tables + files/resources
- Tools: **Process Monitor** (tracks file/process activity), **Orca** (edit MSI, from SDK)

### Linux
- Often from source: extract → run setup script (compiles code, copies to `/bin`, etc.)
- Check **README** in archive for instructions

## Device Software Management

### Windows: Devices & Drivers
- **Device Manager**: console for all devices/drivers
- **Plug and Play (PnP)**: auto-detects hardware via **hardware ID** → finds driver (local, Windows Update, Driver Store)

### Linux: Devices & Drivers
- Everything's a file in `/dev`
- Types: **character** (keyboard/mouse, char-by-char), **block** (drives, block data)
- `ls -l` first char: `-` file, `d` dir, `b` block, `c` char
- Storage: `/dev/sda`, `/dev/sdb` etc. (a = first detected)
- Drivers: built into kernel or **kernel modules** (install like any package)

### OS Updates

**Windows**:
- **Windows Update Client**: background checks Microsoft servers
- Cumulative monthly patches (Win10+), includes **security patches**

**Linux**:
- Update kernel/packages: `sudo apt update && sudo apt upgrade`
- Check kernel: `uname -r`
