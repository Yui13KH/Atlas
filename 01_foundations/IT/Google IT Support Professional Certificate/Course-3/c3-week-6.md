# Week 6: Operating Systems in Practice

## Remote Access

### Remote Connection File Transfer (Linux)
- **SCP** (Secure Copy): copies files over network using SSH
  - Ex: `scp /home/user/file.txt user@IPADDRESS:/destination`

### Windows
- **pscp.exe** (from PuTTY): same as Linux SCP
- **Shared folders**:
  - Right-click folder → Share with → add users/groups
  - Access from other PCs: This PC → Computer tab → Map Network Drive
- CLI: `net share` → create shares with permissions

## Virtualization

- **Virtual instance**: just a single virtual machine (VM)

## Logging

### System Monitoring Basics
- **Logs**: system's diary – records events, errors, changes
- **Logging**: the act of writing those events

### Windows: Event Viewer
- Launch: Start Menu or `eventvwr.msc`
- **Custom Views**: filter across all logs for specific info

### Linux: Logs
- Stored in `/var/log` (variable stuff)
Key files:
- `/var/log/auth.log`: auth/security events
- `/var/log/kern.log`: kernel messages
- `/var/log/dmesg`: boot messages
- `/var/log/syslog`: catches almost everything (best first stop for troubleshooting, skips auth by default)

- **Log rotation**: auto-cleans old logs (handled by `logrotate`)

#### Reading a Log Line
- Timestamp (sometimes Unix/epoch)
- Hostname
- Service/process
- Event description

- Real-time view: `tail -f /var/log/syslog` (-f = follow)

## Operating System Deployment

### Imaging
- **Imaging**: format a machine with a full copy (OS + settings + apps) of another

### Deployment Methods
- **Disk cloning**: exact copy of a drive
  - Great for backups or quick setup of identical machines
  - Can clone to external drive via dock

- Linux: `dd` command → clones drives (everything is a file)

### Mobile Devices
- **Factory reset**: wipes back to original shipped state
  - Careful with expansion storage (SD cards) – might wipe or might not, depends on device
  - Always remove sensitive data before repurposing

- **OTA updates**: over-the-air, device downloads/installs itself
- **Re-flash**: connect to PC via USB, use software to manually install OS update/image
