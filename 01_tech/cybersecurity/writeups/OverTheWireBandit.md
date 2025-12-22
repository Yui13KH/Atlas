# OverTheWire — Bandit Progress Notes

**Progress:** 19 / 34

## Core Concepts Learned (Organized by theme)

### **1. Shell Basics**

* `man` — lookup commands
* `echo` — quick output
* File inspection: `ls`, `ls -a`, `file`, `cat`
* Running weird filenames: `./filename`

### **2. Navigation & Search**

* `find` (filters):

  * `-type`
  * `-size`
  * `-user`, `-group`
* `grep` (+ regex) for pattern matching
* `sort`, `uniq`, `uniq -c` for filtering duplicates

### **3. Remote Access & Transfer**

* `ssh` (login)
* `scp` (remote file copy)
* SSH keys: `ssh -i keyfile`

### **4. Data Extraction & Encoding**

* `strings` — pull readable text from binaries
* Decoding:

  * `base64 -d`
  * `tr` (ROT13 / character translation)
  * `xxd -r`
* Archive handling:

  * `gzip -d`
  * `bzip2 -d`
  * `tar -xf`

### **5. Networking Tools**

* `nc` — netcat basics
* `nmap`, including:

  * `-p start-end`
  * `-sV` for service detection
* `openssl`:

  * `openssl s_client`
  * `openssl s_client -quiet`

### **6. System / Permissions**

* `diff` — compare files
* `setuid` / `setgid` behavior in binaries

---

## Next Steps

* Continue Bandit levels 20 → 34

respecting their terms and policies I wont be sharing neither the solutions nor the steps 