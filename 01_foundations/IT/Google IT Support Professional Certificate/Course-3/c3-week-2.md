# Week 2: Users and Permissions

## Users and Groups

### Types of Users
- **Standard users**: limited access – can't install software or change key settings
- **Administrators**: full control over the machine

Users are organized into **groups** to manage permissions and access levels easier.

### Windows: Viewing & Managing Users/Groups
Use the **Computer Management** tool for everything admin-related.

Key sections:
- **Local Users and Groups**: where you add/remove/manage users and groups
- Task Scheduler: run stuff at specific times
- Event Viewer: system logs
- Shared Folders: shared stuff between users
- Performance: monitor CPU/RAM etc.
- Device Manager: hardware devices
- Services and Applications: manage running services

**Windows domain**: central database for managing multiple machines/users in enterprise.

**User Access Control (UAC)**: prompts for admin approval on big changes.

### Linux: Users & Superusers
- Standard users + admins
- **Root user**: the ultimate superuser (UID 0), created on install – has all privileges
- Dangerous to log in as root directly → use `sudo` for single commands ("superuser do")

View sudo access: check `/etc/group` file (groups listed with users)

View all users: `/etc/passwd` file  
Each line: username : encrypted password : UID (root = 0) : etc.

## Passwords

### Windows
Best practice: never set passwords for others directly (privacy + logs record commands)

- GUI: right-click user → "User must change password at next logon"
- PowerShell/CLI:
  - `net user USERNAME *` → prompts for password securely
  - `net user USERNAME /logonpasswordchg:yes` → forces change on next login

### Linux
- `passwd` → change your own password
- `sudo passwd -e USERNAME` → force a user to change password next login

## Adding & Removing Users

### Windows
- GUI: right-click → New User → set name, force password change
- CLI: `net user USERNAME * /add` then force change with `/logonpasswordchg:yes`

Remove: `net user USERNAME /del`

### Linux
- Add: `sudo useradd USERNAME` (creates home dir etc.)
- Then force password change: `sudo passwd -e USERNAME`
- Remove: `sudo userdel USERNAME`

## Mobile Users
- **Primary account**: set up during initial device config → creates your user profile
- **Single sign-on (SSO)**: log in once, apps use that auth
- **Biometrics**: fingerprint, face, etc. for unlock
- **Mobile Device Management (MDM)**: companies use to enforce rules and protect data

## Permissions

### Windows: File Permissions
Uses **Access Control Lists (ACLs)**:
- **DACLs** (Discretionary): who can do what
- **SACLs** (System): log access events

Main permissions:
- Read
- Read & Execute (includes Read)
- List folder contents (same as R&E for folders)
- Write
- Modify (read + execute + write)
- Full control (everything + change ownership/ACLs)

**Guest users**: no password, disabled by default  
**Authenticated Users**: anyone with credentials

Modify with `icacls` command (use single quotes in PowerShell)

**Simple permissions** are bundles of **special permissions** (e.g., Write Data, Append Data, Synchronize)

### Linux: File Permissions
Three basic: **read (r)**, **write (w)**, **execute (x)**

Shown in 10 characters:  
first = file type (`-` file, `d` directory)  
next 9 = permissions in trios: owner | group | others

Change with `chmod`:

**Symbolic**:  
`u` owner, `g` group, `o` others  
`+` add, `-` remove  
Ex: `chmod g+w file` → add write for group

**Numeric**:
- r = 4
- w = 2
- x = 1
Add them: 7 = rwx, 5 = rx, 4 = r, etc.  
Ex: `chmod 754 file` → owner rwx, group rx, others r

### Linux Special Bits
- **SetUID**: run as owner (`s` or +4000)
- **SetGID**: similar for group
- **Sticky bit**: only owner/root can delete (`t` or +1000)