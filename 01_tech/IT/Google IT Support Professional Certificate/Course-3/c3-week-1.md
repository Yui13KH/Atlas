# Week 1: Navigating the System

## Basic Commands
- The command line interpreter in **Linux** is called a **shell**, and we'll use **Bash** to interact with it.

#### Directories & Paths
- Files and folders are organized in a hierarchical tree structure.
- Locations are called **paths**.
- **Absolute path**: starts from the main/root directory.
- **Relative path**: from your current directory.

### Windows
- Main directory: **C Drive** (C:\)
- Subdirectories use backslashes `\`
- **Wildcard**: `*` for pattern matching
- **Alias**: nickname for a command
- **Parameters**: add options to commands (go after destination, unlike Bash)
- Key commands:
  - `rm <folder> -Recurse` → delete folder and contents
  - `rm <file> -Force` → remove protected files
  - `-Recurse`: list/copy into subdirectories
  - `-Verbose`: show details during operations

### Linux
- Main directory: **root** (`/`)
- Everything is in a tree rooted at `/`
- File names are **case sensitive**
- **Flags**: add options (e.g., `--help` shows command info)
- You can combine flags: `ls -la` same as `ls -l -a`
- To delete folder and contents: `rm -r <folder>`

## File and Text Manipulation

#### PowerShell
- `-Head` and `-Tail`: view first/last lines of a file
- `Get-Alias <command>`: check if something is an alias
- PowerShell commands are long and descriptive (extra typing tho)
- Three ways to run stuff: PowerShell commands, aliases (Bash-style), or cmd.exe (`/?` for help)
- `Select-String`: search text (great with wildcards)
- `-Filter *.exe`: filter by file pattern
- `echo` is alias for `Write-Output`

#### Bash
- `less <file>`: view large files (navigate with arrows, page up/down, `g` to start, `G` to end, `/search`, `q` to quit)
- `head` and `tail`: same as PowerShell
- `grep`: search for text in files (super powerful)

## I/O Streams (same idea in both)

Each process has:
- **stdin**: input (usually keyboard)
- **stdout**: normal output (screen)
- **stderr**: error output

#### Windows/PowerShell
- `>` : redirect stdout to file (overwrites)
- `>>`: append to file
- `|` : pipe output of one command to input of another  
  Ex: `cat words.txt | Select-String st > st_words.txt`
- Redirect errors to black hole: `2> $null`

#### Linux/Bash
- `<` : get input from file
- `>` : redirect stdout (overwrites)
- `>>`: append stdout
- `2>` : redirect stderr
- `/dev/null`: the Linux black hole for discarding output

## Create, Modify, Remove Files/Folders in Linux

#### Creating directories
- `mkdir <name>` → make one or more dirs  
  Ex: `mkdir dir1 dir2 dir3`
- `-p`: create parents if needed
- `-m`: set permissions on creation
- `-v`: verbose mode

#### Removing empty directories
- `rmdir <name>` → remove one or more empty dirs
- `-p`: remove parent dirs if empty too

#### Creating files
- `touch <file>` → create empty file (or update timestamp if exists)
- `-c`: don't create if it doesn't exist

#### Copying/Moving
- Use `.` to mean current directory  
  Ex: `mv /home/user/Images/Vacation.jpg .`

#### Searching in files (grep flags)
- `-r`: recursive
- `-w`: whole word only
- `-n`: show line numbers
- `-e`: specify pattern
- `--include` / `--exclude`: filter file types
- `--include-dir` / `--exclude-dir`: filter directories  
  Ex: `grep -rw /home/user/Downloads -e "vacation"`