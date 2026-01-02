# Week 4: Filesystems

## Filesystem Types

### Quick Review
- **Filesystem**: organizes files on disk – without it, OS can't manage storage
- Windows default: **NTFS**
- Linux default: **ext4**
- Cross-compatible: **FAT32** (works on Win/Linux/Mac, but max file 4GB, max volume ~32GB)
- NTFS USB: readable/writable on both Win and modern Linux
- ext4 USB: Linux yes, Windows no (without extra drivers)

### Disk Anatomy
- Disks divided into **partitions** (logical sections)
- Format partition → becomes **volume** (people mix up partition/volume)
- **Partition table**: tells OS layout (bootable, sizes, etc.)

Two main types:
- **MBR** (old, Win-focused): max 2TB volumes, only 4 primary partitions (or extended + logical)
- **GPT** (new standard): >2TB, unlimited partitions, required for UEFI

## Windows: Partitioning & Formatting

### GUI
- **Disk Management** tool (right-click This PC → Manage → Disk Management)

Options:
- **Quick format**: fast, no bad sector scan
- **Full format**: scans for errors (slower)
- **Compression**: saves space but CPU cost when opening files

### CLI
- **Diskpart**: command-line disk manager
  - Run `diskpart` → `list disk` etc.

### Mounting/Unmounting
- Windows auto-mounts drives
- Always **safely eject** (unmounts properly)

## Linux: Partitioning & Formatting

- Tool: **parted** (supports MBR/GPT)
  - `sudo parted -l`: list disks/partitions (shows number, start/end, size, fs type, flags)
  - Interactive mode or one-liners
  - `mklabel`: set table type
  - `mkpart`: create partition (type, fs, start, end)

After partitioning:
- Format: `sudo mkfs -t ext4 /dev/PARTITION`

### Mounting/Unmounting
- Create dir first: `mkdir /my_usb`
- Mount: `sudo mount /dev/sdb1 /my_usb`
- Unmount: `sudo umount /my_usb` (always before unplugging)

Permanent mount: add to `/etc/fstab`
- Get UUID: `sudo blkid`
- Add line with UUID, mount point, fs type, etc.

## Swap Space (Virtual Memory)

### Concept
- **Virtual memory**: maps virtual → physical addresses
- Lets apps use more RAM than physically available
- Unused pages moved to disk (**swap**) – slower but prevents crashes

### Windows
- Called **paging file**
- Adjust size/location in System Properties

### Linux
- Dedicated **swap partition** or file
- Create in parted → set type linux-swap
- Format: `sudo mkswap /dev/PARTITION`
- Enable: `sudo swapon /dev/PARTITION`
- Auto-enable on boot: add to `/etc/fstab`

## How Files Are Stored

### Windows (NTFS)
- **Master File Table (MFT)**: database of all files (one record per file usually)
- Stores metadata: name, timestamps, permissions, location, etc.
- **File record number**: index in MFT

Links:
- **Shortcuts**: regular files pointing to target
- **Symbolic links**: filesystem-level, act like the real file
- **Hard links**: point to file record number (survive name changes)

### Linux
- **Inodes**: store metadata (not data or name)
- Inode table on filesystem
- Links:
  - **Softlinks/symlinks**: point to filename (`ln -s original link`) – can break if target moves
  - **Hardlinks**: point to inode (`ln original link`) – same file, no extra space, only deleted when link count hits 0 (shown in `ls -l` 2nd field)

## Disk Usage & Maintenance

### Windows
- Check: Disk Management → Properties on partition
- **Disk Cleanup**: `cleanmgr.exe` – deletes temp files, empties recycle bin, etc.
- **Defragmentation**: reorganizes files for HDD speed (less useful on SSD)
- SSDs use **trim** instead

### Linux
- **du -h [dir]**: disk usage of directory (human-readable)
- **df -h**: free space on whole system (human-readable)
- Linux handles fragmentation better

## Filesystem Repair

### Windows (NTFS)
- **Journaling**: logs metadata changes → can recover state
- **Self-healing**: fixes minor issues in background (no reboot)
- Check status: `fsutil repair query C:`

### Linux
- **fsck**: filesystem check/repair
  - Ex: `sudo fsck /dev/sdb`
  - NEVER run on mounted partition (will likely corrupt it)

Data often buffered in RAM → always unmount properly to avoid corruption

