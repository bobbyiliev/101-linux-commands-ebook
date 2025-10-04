# The `cfdisk` command

The `cfdisk` command is a curses-based disk partitioning tool for Linux. It provides a user-friendly, text-based interface for creating, deleting, and managing disk partitions. Unlike `fdisk`, `cfdisk` offers a more intuitive menu-driven approach.

## Syntax

```
cfdisk [options] [device]
```

## Key Features

- **Interactive Interface**: Menu-driven partition management
- **Real-time Display**: Shows current partition table
- **Safe Operations**: Requires explicit write command to save changes
- **Multiple File Systems**: Supports various partition types
- **Resize Support**: Can resize existing partitions

## Basic Usage

### Starting cfdisk

```bash
# Open cfdisk on primary disk
sudo cfdisk /dev/sda

# Open cfdisk on secondary disk
sudo cfdisk /dev/sdb

# Auto-detect and use first available disk
sudo cfdisk
```

### Navigation

- **Up/Down Arrows**: Navigate between partitions
- **Left/Right Arrows**: Navigate between menu options
- **Enter**: Select menu option
- **Tab**: Move between interface elements

## Menu Options

### Main Operations

- **New**: Create a new partition
- **Delete**: Delete selected partition
- **Resize**: Resize selected partition
- **Type**: Change partition type
- **Write**: Write changes to disk
- **Quit**: Exit without saving (if no changes written)

### Additional Options

- **Bootable**: Toggle bootable flag
- **Verify**: Check partition table consistency
- **Print**: Display partition information

## Common Tasks

### 1. Creating a New Partition

```bash
# Start cfdisk
sudo cfdisk /dev/sdb

# Steps in cfdisk:
# 1. Select "New" from menu
# 2. Choose partition size
# 3. Select partition type (primary/extended)
# 4. Choose partition type (Linux, swap, etc.)
# 5. Select "Write" to save changes
# 6. Type "yes" to confirm
# 7. Select "Quit" to exit
```

### 2. Deleting a Partition

```bash
# In cfdisk interface:
# 1. Navigate to partition to delete
# 2. Select "Delete" from menu
# 3. Confirm deletion
# 4. Select "Write" to save changes
# 5. Type "yes" to confirm
```

### 3. Changing Partition Type

```bash
# In cfdisk interface:
# 1. Navigate to target partition
# 2. Select "Type" from menu
# 3. Choose new partition type from list
# 4. Select "Write" to save changes
```

## Common Partition Types

### Linux Partition Types

- **83**: Linux filesystem
- **82**: Linux swap
- **8e**: Linux LVM
- **fd**: Linux RAID autodetect

### Other Common Types

- **07**: NTFS/HPFS
- **0c**: FAT32 LBA
- **ef**: EFI System Partition
- **01**: FAT12

## Command Line Options

```bash
# Show help
cfdisk --help

# Show version
cfdisk --version

# Use alternative device
cfdisk /dev/sdc

# Start with specific partition table type
cfdisk -t gpt /dev/sdb
cfdisk -t dos /dev/sdb
```

## Practical Examples

### 1. Partitioning a New USB Drive

```bash
# Insert USB drive (assume it's /dev/sdc)
# Check device name
lsblk

# Start cfdisk
sudo cfdisk /dev/sdc

# Create new partition table if needed
# Create partitions as needed
# Write changes and quit
```

### 2. Adding Swap Partition

```bash
# Start cfdisk on target disk
sudo cfdisk /dev/sda

# Create new partition
# Set type to "82" (Linux swap)
# Write changes

# Format as swap
sudo mkswap /dev/sda3

# Enable swap
sudo swapon /dev/sda3
```

### 3. Preparing Disk for LVM

```bash
# Start cfdisk
sudo cfdisk /dev/sdb

# Create partition
# Set type to "8e" (Linux LVM)
# Write changes

# Create physical volume
sudo pvcreate /dev/sdb1
```

## Safety Features

### 1. Change Tracking

```bash
# cfdisk tracks all changes
# Shows asterisk (*) next to modified partitions
# Changes only applied when "Write" is selected
```

### 2. Confirmation Required

```bash
# Writing changes requires typing "yes"
# Provides final warning before applying changes
# Can quit without saving if no "Write" performed
```

### 3. Verification

```bash
# Built-in partition table verification
# Warns about potential issues
# Suggests corrections for problems
```

## Working with Different Partition Tables

### 1. GPT (GUID Partition Table)

```bash
# Create GPT partition table
sudo cfdisk -t gpt /dev/sdb

# Features:
# - Supports >2TB disks
# - Up to 128 partitions
# - Backup partition table
# - 64-bit LBA addressing
```

### 2. MBR/DOS Partition Table

```bash
# Create MBR partition table
sudo cfdisk -t dos /dev/sdb

# Limitations:
# - 4 primary partitions maximum
# - 2TB disk size limit
# - Extended partitions for >4 partitions
```

## Integration with Other Tools

### 1. After Partitioning

```bash
# Verify partition creation
lsblk /dev/sdb
fdisk -l /dev/sdb

# Format partitions
sudo mkfs.ext4 /dev/sdb1
sudo mkfs.xfs /dev/sdb2

# Mount partitions
sudo mkdir /mnt/partition1
sudo mount /dev/sdb1 /mnt/partition1
```

### 2. Backup Before Changes

```bash
# Backup partition table before changes
sudo sfdisk -d /dev/sdb > sdb_partition_backup.txt

# Restore if needed
sudo sfdisk /dev/sdb < sdb_partition_backup.txt
```

## Troubleshooting

### 1. Permission Issues

```bash
# Must run as root or with sudo
sudo cfdisk /dev/sdb

# Check device permissions
ls -l /dev/sdb
```

### 2. Device Busy

```bash
# Unmount all partitions on device first
sudo umount /dev/sdb1
sudo umount /dev/sdb2

# Check for active processes
lsof /dev/sdb*
```

### 3. Partition Table Corruption

```bash
# Verify partition table
sudo cfdisk /dev/sdb

# If corrupted, recreate partition table
# (This will destroy all data!)
sudo cfdisk -t gpt /dev/sdb  # For GPT
sudo cfdisk -t dos /dev/sdb  # For MBR
```

## Best Practices

### 1. Always Backup

```bash
# Backup important data before partitioning
# Create partition table backup
sudo sfdisk -d /dev/sdb > partition_backup.txt
```

### 2. Verify Device

```bash
# Double-check device name before starting
lsblk
fdisk -l

# Ensure you're working on correct disk
```

### 3. Plan Partition Layout

```bash
# Plan your partition scheme:
# - Root partition (/)
# - Swap partition
# - Home partition (/home)
# - Boot partition (/boot) if needed
```

### 4. Consider Alignment

```bash
# Modern cfdisk handles alignment automatically
# Uses 1MB alignment by default
# Optimal for SSDs and advanced format drives
```

## Comparison with Other Tools

### vs fdisk

- **cfdisk**: Menu-driven, user-friendly
- **fdisk**: Command-driven, more scriptable

### vs parted

- **cfdisk**: Simpler interface, basic operations
- **parted**: More advanced features, command-line scriptable

### vs gparted

- **cfdisk**: Text-based, lightweight
- **gparted**: Graphical interface, requires X11

## Important Notes

- Always unmount partitions before modifying them
- Changes are not written until you explicitly choose "Write"
- Backup important data before making partition changes
- Some operations may require a system reboot to take effect
- Be extremely careful when working with system disks
- Consider using LVM for more flexible partition management

The `cfdisk` command provides an excellent balance between ease of use and functionality for disk partitioning tasks.

For more details, check the manual: `man cfdisk`
