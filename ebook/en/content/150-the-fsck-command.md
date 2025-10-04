# The `fsck` command

The `fsck` (file system check) command is used to check and repair Linux file systems. It can detect and fix various file system inconsistencies, corruption issues, and structural problems. It's an essential tool for maintaining file system integrity and recovering from system crashes.

## Syntax

```
fsck [options] [filesystem...]
```

## Key Features

- **Multiple File System Support**: Works with ext2, ext3, ext4, XFS, and more
- **Automatic Detection**: Can auto-detect file system type
- **Interactive Repair**: Prompts for confirmation before fixes
- **Batch Mode**: Can run automatically without user interaction
- **Read-Only Mode**: Check without making changes

## Basic Usage

### Simple File System Check

```bash
# Check specific partition
sudo fsck /dev/sdb1

# Check by mount point
sudo fsck /home

# Check with verbose output
sudo fsck -v /dev/sdb1
```

### Check All File Systems

```bash
# Check all file systems in /etc/fstab
sudo fsck -A

# Check all except root
sudo fsck -AR

# Check all with progress
sudo fsck -AV
```

## Common Options

### Basic Options

```bash
# -y: Answer "yes" to all questions
sudo fsck -y /dev/sdb1

# -n: Answer "no" to all questions (read-only)
sudo fsck -n /dev/sdb1

# -f: Force check even if file system seems clean
sudo fsck -f /dev/sdb1

# -v: Verbose output
sudo fsck -v /dev/sdb1
```

### Advanced Options

```bash
# -p: Automatically repair (preen mode)
sudo fsck -p /dev/sdb1

# -r: Interactive repair mode
sudo fsck -r /dev/sdb1

# -t: Specify file system type
sudo fsck -t ext4 /dev/sdb1

# -C: Show progress bar
sudo fsck -C /dev/sdb1
```

## File System Specific Commands

### 1. ext2/ext3/ext4 (e2fsck)

```bash
# Check ext4 file system
sudo fsck.ext4 /dev/sdb1

# Force check
sudo e2fsck -f /dev/sdb1

# Fix bad blocks
sudo e2fsck -c /dev/sdb1

# Thorough check with bad block scan
sudo e2fsck -cc /dev/sdb1
```

### 2. XFS (xfs_repair)

```bash
# Check XFS file system (read-only)
sudo xfs_repair -n /dev/sdb1

# Repair XFS file system
sudo xfs_repair /dev/sdb1

# Verbose repair
sudo xfs_repair -v /dev/sdb1
```

### 3. FAT32 (fsck.fat)

```bash
# Check FAT32 file system
sudo fsck.fat /dev/sdb1

# Repair FAT32
sudo fsck.fat -r /dev/sdb1

# Verbose check
sudo fsck.fat -v /dev/sdb1
```

## Practical Examples

### 1. Check Before Mounting

```bash
# Always check before mounting suspicious drives
sudo fsck -n /dev/sdb1

# If clean, mount normally
sudo mount /dev/sdb1 /mnt/usb

# If errors found, repair first
sudo fsck -y /dev/sdb1
sudo mount /dev/sdb1 /mnt/usb
```

### 2. System Recovery After Crash

```bash
# Boot from live CD/USB
# Check root file system
sudo fsck -f /dev/sda1

# Check other partitions
sudo fsck -f /dev/sda2
sudo fsck -f /dev/sda3

# Reboot if repairs were made
sudo reboot
```

### 3. Scheduled Maintenance

```bash
# Force check on all file systems
sudo fsck -Af

# Check with automatic repair
sudo fsck -Ap

# Check with progress indicators
sudo fsck -AVC
```

## Working with Different Scenarios

### 1. Read-Only Check

```bash
# Check without making changes
sudo fsck -n /dev/sdb1

# Verbose read-only check
sudo fsck -nv /dev/sdb1

# Generate report only
sudo fsck -n /dev/sdb1 > fsck_report.txt 2>&1
```

### 2. Automatic Repair

```bash
# Repair automatically (dangerous!)
sudo fsck -y /dev/sdb1

# Safer automatic repair
sudo fsck -p /dev/sdb1

# Batch mode for multiple file systems
sudo fsck -Ap
```

### 3. Interactive Repair

```bash
# Interactive mode (default)
sudo fsck /dev/sdb1

# Ask before each fix
sudo fsck -r /dev/sdb1

# Show detailed information
sudo fsck -rv /dev/sdb1
```

## Boot-Time File System Checks

### 1. Automatic Checks

```bash
# Configure automatic checks in /etc/fstab
# Sixth field controls fsck behavior:
# 0 = no check
# 1 = check first (root filesystem)
# 2 = check after root filesystem

# Example /etc/fstab entry:
# /dev/sda1 / ext4 defaults 1 1
# /dev/sda2 /home ext4 defaults 1 2
```

### 2. Force Check on Next Boot

```bash
# Create forcefsck file (traditional method)
sudo touch /forcefsck

# Or use tune2fs for ext filesystems
sudo tune2fs -C 1 -c 1 /dev/sda1

# Set maximum mount count
sudo tune2fs -c 30 /dev/sda1
```

### 3. Check Intervals

```bash
# Set check interval (ext filesystems)
sudo tune2fs -i 30d /dev/sda1  # Check every 30 days
sudo tune2fs -i 0 /dev/sda1    # Disable time-based checks

# Set mount count interval
sudo tune2fs -c 25 /dev/sda1   # Check every 25 mounts
sudo tune2fs -c 0 /dev/sda1    # Disable mount-based checks
```

## Troubleshooting Common Issues

### 1. Unmountable File System

```bash
# Try read-only check first
sudo fsck -n /dev/sdb1

# If errors found, try repair
sudo fsck -y /dev/sdb1

# For severe corruption
sudo fsck -f /dev/sdb1
```

### 2. Bad Superblock

```bash
# List backup superblocks
sudo mke2fs -n /dev/sdb1

# Use backup superblock
sudo e2fsck -b 32768 /dev/sdb1

# Try different backup
sudo e2fsck -b 98304 /dev/sdb1
```

### 3. Lost+Found Directory

```bash
# Recovered files appear in lost+found
ls -la /mnt/partition/lost+found/

# Files are numbered by inode
# Use file command to identify type
file /mnt/partition/lost+found/*

# Restore files based on content
```

## Advanced Repair Options

### 1. Bad Block Handling

```bash
# Scan for bad blocks during check
sudo e2fsck -c /dev/sdb1

# Thorough bad block scan
sudo e2fsck -cc /dev/sdb1

# Use existing bad block list
sudo badblocks -sv /dev/sdb1 > badblocks.list
sudo e2fsck -l badblocks.list /dev/sdb1
```

### 2. Journal Recovery

```bash
# ext3/ext4 journal recovery
sudo e2fsck -y /dev/sdb1

# Force journal recovery
sudo tune2fs -O ^has_journal /dev/sdb1
sudo e2fsck -f /dev/sdb1
sudo tune2fs -j /dev/sdb1
```

### 3. Inode Problems

```bash
# Check inode usage
sudo e2fsck -D /dev/sdb1

# Rebuild directory index
sudo e2fsck -D -f /dev/sdb1

# Fix inode count problems
sudo e2fsck -f /dev/sdb1
```

## Monitoring and Logging

### 1. Check Results

```bash
# View fsck results
dmesg | grep -i fsck

# Check system logs
journalctl | grep fsck
tail -f /var/log/messages | grep fsck
```

### 2. File System Status

```bash
# Check filesystem status
sudo tune2fs -l /dev/sda1 | grep -i "filesystem state"

# Check last fsck time
sudo tune2fs -l /dev/sda1 | grep -i "last checked"

# Check mount count
sudo tune2fs -l /dev/sda1 | grep -i "mount count"
```

### 3. Automated Monitoring

```bash
# Script to check filesystem health
#!/bin/bash
for fs in $(awk '$3 ~ /^ext[234]$/ && $2 != "/" {print $1}' /etc/fstab); do
    echo "Checking $fs..."
    sudo fsck -n "$fs" || echo "Errors found on $fs"
done
```

## Prevention and Best Practices

### 1. Regular Maintenance

```bash
# Schedule regular checks
# Add to crontab for non-critical systems
# 0 3 * * 0 /sbin/fsck -Ap > /var/log/fsck.log 2>&1
```

### 2. Proper Shutdown

```bash
# Always shutdown properly
sudo shutdown -h now

# Use sync before emergency shutdown
sync
sudo shutdown -h now
```

### 3. UPS Protection

```bash
# Install UPS monitoring
sudo apt install apcupsd  # For APC UPS
sudo apt install nut      # Network UPS Tools

# Configure automatic shutdown on power loss
```

## Recovery Scenarios

### 1. Boot Failure

```bash
# Boot from live USB/CD
# Mount root filesystem read-only
sudo mount -o ro /dev/sda1 /mnt

# Copy important data
sudo cp -r /mnt/home/user/important /backup/

# Unmount and check
sudo umount /mnt
sudo fsck -f /dev/sda1
```

### 2. Data Recovery

```bash
# Use ddrescue for severely damaged drives
sudo ddrescue /dev/sdb /backup/disk.img /backup/disk.log

# Then fsck the image
sudo fsck -f /backup/disk.img

# Mount and recover data
sudo mount -o loop /backup/disk.img /mnt/recovery
```

### 3. Multiple Errors

```bash
# Progressive repair approach
sudo fsck -n /dev/sdb1           # Check first
sudo fsck -p /dev/sdb1           # Auto-repair safe issues
sudo fsck -y /dev/sdb1           # Force repair remaining issues
sudo fsck -f /dev/sdb1           # Final thorough check
```

## Performance Considerations

### 1. Speed Optimization

```bash
# Use progress indicator
sudo fsck -C /dev/sdb1

# Parallel checking (careful with dependencies)
sudo fsck -A -P

# Skip time-consuming checks when appropriate
sudo fsck -p /dev/sdb1
```

### 2. System Impact

```bash
# Run during low-activity periods
# Schedule during maintenance windows
# Use ionice for lower priority
sudo ionice -c 3 fsck /dev/sdb1
```

## Important Safety Notes

- **Always unmount** file systems before checking
- **Backup important data** before repairs
- **Never interrupt** fsck during operation
- **Use read-only mode** first to assess damage
- **Understand risks** of automatic repair modes
- **Boot from live media** for root filesystem checks
- **Have recovery plan** ready before starting repairs

## Exit Codes

```bash
# fsck exit codes:
# 0: No errors
# 1: Filesystem errors corrected
# 2: System should be rebooted
# 4: Filesystem errors left uncorrected
# 8: Operational error
# 16: Usage or syntax error
# 32: Checking canceled by user request
# 128: Shared-library error
```

The `fsck` command is crucial for maintaining file system integrity and recovering from corruption issues.

For more details, check the manual: `man fsck`
