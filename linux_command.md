# Basic Linux Command Line

---

## Introduction to Linux CLI

The Command Line Interface (CLI) is a powerful way to interact with Linux systems.

**Why use CLI?**
- More efficient for many tasks
- Automation through scripts
- Remote server management
- Essential for DevOps and system administration

---

## Navigation Commands

### pwd - Print Working Directory
```bash
pwd
# Shows current directory path
```

### cd - Change Directory
```bash
cd /home/user          # Absolute path
cd Documents           # Relative path
cd ..                  # Go up one level
cd ~                   # Go to home directory
cd -                   # Go to previous directory
```

### ls - List Directory Contents
```bash
ls                     # List files
ls -l                  # Long format with details
ls -la                 # Include hidden files
ls -lh                 # Human-readable file sizes
```

---

## File Operations

### Creating Files and Directories
```bash
touch file.txt         # Create empty file
mkdir mydir            # Create directory
mkdir -p dir1/dir2     # Create nested directories
```

### Copying and Moving
```bash
cp file1.txt file2.txt       # Copy file
cp -r dir1 dir2              # Copy directory recursively
mv file.txt newname.txt      # Rename/move file
mv file.txt /path/to/dest/   # Move to directory
```

### Deleting
```bash
rm file.txt            # Remove file
rm -r directory        # Remove directory recursively
rm -rf directory       # Force remove (use carefully!)
rmdir emptydir         # Remove empty directory
```

---

## Viewing File Contents

### cat - Concatenate and Display
```bash
cat file.txt           # Display entire file
cat file1.txt file2.txt # Display multiple files
```

### less and more - Paginated Viewing
```bash
less file.txt          # View file with navigation
more file.txt          # Simple pager
# Press 'q' to quit, space for next page
```

### head and tail
```bash
head file.txt          # First 10 lines
head -n 20 file.txt    # First 20 lines
tail file.txt          # Last 10 lines
tail -f logfile.log    # Follow file updates (logs)
```

---

## File Permissions

### Understanding Permissions
```
-rwxr-xr--
 │││││││││
 ││││└┴┴┴┴─── Others (r--)
 │││└┴┴┴───── Group (r-x)
 ││└┴┴─────── Owner (rwx)
 │└───────── File type (- = file, d = directory)
```

### chmod - Change Mode
```bash
chmod 755 script.sh    # rwxr-xr-x
chmod +x script.sh     # Add execute permission
chmod -w file.txt      # Remove write permission
chmod u+x,g-w file     # User add execute, group remove write
```

### chown - Change Owner
```bash
chown user file.txt           # Change owner
chown user:group file.txt     # Change owner and group
```

---

## Searching

### find - Find Files
```bash
find . -name "*.txt"           # Find by name
find /home -type f -size +10M  # Files larger than 10MB
find . -mtime -7               # Modified in last 7 days
```

### grep - Search Text
```bash
grep "pattern" file.txt        # Search in file
grep -r "pattern" .            # Recursive search
grep -i "pattern" file.txt     # Case insensitive
grep -n "pattern" file.txt     # Show line numbers
grep -v "pattern" file.txt     # Invert match (exclude)
```

### which and whereis
```bash
which python           # Find command location
whereis ls            # Find binary, source, manual
```

---

## Process Management

### Viewing Processes
```bash
ps                     # Show current processes
ps aux                 # All processes (detailed)
top                    # Interactive process viewer
htop                   # Enhanced process viewer (if installed)
```

### Managing Processes
```bash
command &              # Run in background
jobs                   # List background jobs
fg                     # Bring to foreground
bg                     # Continue in background
kill PID               # Terminate process
kill -9 PID            # Force kill
killall name           # Kill by name
```

---

## Input/Output Redirection

### Redirection Operators
```bash
command > file.txt     # Redirect output (overwrite)
command >> file.txt    # Append output
command < file.txt     # Input from file
command 2> error.log   # Redirect errors
command &> all.log     # Redirect both output and errors
```

### Pipes
```bash
command1 | command2    # Pipe output to another command
ls -l | grep ".txt"    # List and filter
cat file | sort | uniq # Chain multiple commands
```

---

## System Information

### Disk Usage
```bash
df -h                  # Disk space (human-readable)
du -sh directory       # Directory size
du -h --max-depth=1    # Size of subdirectories
```

### System Info
```bash
uname -a               # System information
whoami                 # Current user
hostname               # Machine name
uptime                 # System uptime
free -h                # Memory usage
```

### Date and Time
```bash
date                   # Current date and time
cal                    # Calendar
```

---

## Network Commands

### Basic Networking
```bash
ping google.com        # Test connectivity
ifconfig               # Network interfaces (older)
ip addr                # Network interfaces (newer)
netstat -tuln          # Network connections
ss -tuln               # Socket statistics (modern)
```

### File Transfer
```bash
wget url               # Download file
curl url               # Transfer data
scp file user@host:    # Secure copy to remote
```

---

## Package Management

### Debian/Ubuntu (apt)
```bash
sudo apt update        # Update package list
sudo apt upgrade       # Upgrade packages
sudo apt install pkg   # Install package
sudo apt remove pkg    # Remove package
```

### RedHat/CentOS (yum/dnf)
```bash
sudo yum update        # Update packages
sudo yum install pkg   # Install package
sudo dnf install pkg   # Install (newer systems)
```

---

## Archive and Compression

### tar - Tape Archive
```bash
tar -czf archive.tar.gz dir/   # Create compressed archive
tar -xzf archive.tar.gz        # Extract archive
tar -tzf archive.tar.gz        # List contents
```

### zip and unzip
```bash
zip -r archive.zip dir/        # Create zip
unzip archive.zip              # Extract zip
```

---

## Text Processing

### sed - Stream Editor
```bash
sed 's/old/new/' file.txt      # Replace first occurrence
sed 's/old/new/g' file.txt     # Replace all occurrences
```

### awk - Pattern Scanning
```bash
awk '{print $1}' file.txt      # Print first column
awk -F: '{print $1}' /etc/passwd  # Custom delimiter
```

### sort and uniq
```bash
sort file.txt                  # Sort lines
sort -r file.txt               # Reverse sort
uniq file.txt                  # Remove duplicates
sort file.txt | uniq -c        # Count occurrences
```

---

## Useful Tips

### Command History
```bash
history                # Show command history
!123                   # Run command #123 from history
!!                     # Run last command
!$                     # Last argument of previous command
Ctrl+R                 # Search history (interactive)
```

### Keyboard Shortcuts
- `Ctrl+C` - Cancel current command
- `Ctrl+D` - Exit shell / EOF
- `Ctrl+L` - Clear screen
- `Ctrl+A` - Move to line start
- `Ctrl+E` - Move to line end
- `Ctrl+U` - Clear line before cursor
- `Tab` - Auto-complete

---

## Man Pages and Help

### Getting Help
```bash
man command            # Manual page
command --help         # Help option
info command           # Info documentation
whatis command         # Brief description
apropos keyword        # Search man pages
```

### Example
```bash
man ls                 # Read ls manual
ls --help              # Quick help for ls
```

---

## Best Practices

1. **Always double-check before using:**
   - `rm -rf` (can delete everything)
   - Commands with `sudo` (run as root)

2. **Use tab completion** to avoid typos

3. **Read man pages** for detailed options

4. **Test commands** in safe environment first

5. **Use version control** for important files

6. **Regular backups** before major changes

---

## Thank You!

**Practice makes perfect!**

Start with basic commands and gradually explore more advanced features.

**Resources:**
- `man` pages
- Online tutorials
- Linux communities
- Practice on virtual machines

---
