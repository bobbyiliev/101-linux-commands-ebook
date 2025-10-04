# The `cpio` command

The `cpio` (copy in, copy out) command is a versatile archiving utility that can create and extract archives, copy files, and handle special file types. It's particularly useful for system backups, creating initramfs images, and working with tape archives.

## Syntax

```
cpio [options] < name-list
cpio [options] -i [patterns] < archive
cpio [options] -o > archive
cpio [options] -p destination-directory
```

## Operating Modes

### 1. Copy-out mode (-o)

```bash
# Create archive from file list
find . -name "*.txt" | cpio -o > archive.cpio

# Create compressed archive
find . -type f | cpio -o | gzip > archive.cpio.gz

# Verbose output
find . -name "*.conf" | cpio -ov > config_backup.cpio
```

### 2. Copy-in mode (-i)

```bash
# Extract archive
cpio -i < archive.cpio

# Extract to specific directory
cd /restore && cpio -i < /backup/archive.cpio

# Extract specific files
cpio -i "*.txt" < archive.cpio
```

### 3. Pass-through mode (-p)

```bash
# Copy files to another directory
find /source -type f | cpio -p /destination

# Preserve attributes while copying
find /etc -name "*.conf" | cpio -pdm /backup/configs
```

## Common Options

### Basic Options

```bash
# -o: Copy-out (create archive)
find . | cpio -o > archive.cpio

# -i: Copy-in (extract archive)
cpio -i < archive.cpio

# -p: Pass-through (copy files)
find . | cpio -p /destination

# -v: Verbose output
find . | cpio -ov > archive.cpio

# -t: List archive contents
cpio -tv < archive.cpio
```

### Advanced Options

```bash
# -d: Create directories as needed
cpio -id < archive.cpio

# -m: Preserve modification times
cpio -im < archive.cpio

# -u: Unconditional extraction (overwrite)
cpio -iu < archive.cpio

# -H: Specify archive format
cpio -oH newc > archive.cpio

# -B: Use 5120-byte blocks
cpio -oB > archive.cpio
```

## Archive Formats

### Available Formats

```bash
# Binary format (default, obsolete)
cpio -o > archive.cpio

# New ASCII format (recommended)
cpio -oH newc > archive.cpio

# Old ASCII format
cpio -oH odc > archive.cpio

# CRC format
cpio -oH crc > archive.cpio

# TAR format
cpio -oH tar > archive.tar

# USTAR format
cpio -oH ustar > archive.tar
```

## Practical Examples

### 1. System Backup

```bash
# Backup entire system (excluding certain directories)
find / -path /proc -prune -o -path /sys -prune -o -path /dev -prune -o -print | \
sudo cpio -oH newc | gzip > system_backup.cpio.gz

# Backup specific directories
find /etc /home /var -type f | cpio -oH newc > important_files.cpio

# Backup with verbose output
find /home/user -type f | cpio -ovH newc > user_backup.cpio
```

### 2. Creating initramfs

```bash
# Create initramfs image (common in Linux boot process)
cd /tmp/initramfs
find . | cpio -oH newc | gzip > /boot/initramfs.img

# Extract existing initramfs
cd /tmp/extract
zcat /boot/initramfs.img | cpio -id
```

### 3. Selective File Operations

```bash
# Archive only configuration files
find /etc -name "*.conf" -o -name "*.cfg" | cpio -oH newc > configs.cpio

# Archive files modified in last 7 days
find /home -type f -mtime -7 | cpio -oH newc > recent_files.cpio

# Archive files larger than 1MB
find /var/log -type f -size +1M | cpio -oH newc > large_logs.cpio
```

### 4. Working with Compressed Archives

```bash
# Create compressed archive
find . -type f | cpio -oH newc | gzip > archive.cpio.gz
find . -type f | cpio -oH newc | bzip2 > archive.cpio.bz2
find . -type f | cpio -oH newc | xz > archive.cpio.xz

# Extract compressed archives
zcat archive.cpio.gz | cpio -id
bzcat archive.cpio.bz2 | cpio -id
xzcat archive.cpio.xz | cpio -id
```

## Special File Types

### 1. Device Files and Special Files

```bash
# Archive including device files
find /dev -type c -o -type b | sudo cpio -oH newc > device_files.cpio

# Archive symbolic links
find . -type l | cpio -oH newc > symlinks.cpio

# Archive with all file types preserved
find . | sudo cpio -oH newc > complete_backup.cpio
```

### 2. Preserving Attributes

```bash
# Preserve ownership and permissions
find . | sudo cpio -oH newc > backup.cpio
sudo cpio -idm < backup.cpio

# Preserve modification times
cpio -im < archive.cpio

# Preserve all attributes in pass-through mode
find /source | sudo cpio -pdm /destination
```

## File Filtering and Selection

### 1. Pattern Matching

```bash
# Extract specific file patterns
cpio -i "*.txt" "*.conf" < archive.cpio

# Extract files in specific directory
cpio -i "etc/*" < archive.cpio

# Extract with shell globbing
cpio -i "*backup*" < archive.cpio
```

### 2. Exclude Patterns

```bash
# Create archive excluding certain files
find . -type f ! -name "*.tmp" ! -name "*.log" | cpio -oH newc > clean_archive.cpio

# Use grep to filter
find . -type f | grep -v -E '\.(tmp|log|cache)$' | cpio -oH newc > filtered.cpio
```

## Network Operations

### 1. Remote Backup

```bash
# Send archive over network
find /home | cpio -oH newc | ssh user@remote "cat > backup.cpio"

# Compressed network backup
find /data | cpio -oH newc | gzip | ssh user@remote "cat > data_backup.cpio.gz"

# Receive archive from network
ssh user@remote "cat backup.cpio" | cpio -id
```

### 2. Tape Operations

```bash
# Write to tape device
find /home | cpio -oH newc > /dev/st0

# Read from tape
cpio -itv < /dev/st0  # List contents
cpio -id < /dev/st0   # Extract

# Multi-volume archives
find /large_dataset | cpio -oH newc --split-at=700M > /dev/st0
```

## Archive Management

### 1. Listing Archive Contents

```bash
# List all files in archive
cpio -tv < archive.cpio

# List with detailed information
cpio -itv < archive.cpio

# Count files in archive
cpio -it < archive.cpio | wc -l

# Search for specific files
cpio -it < archive.cpio | grep "filename"
```

### 2. Verifying Archives

```bash
# Test archive integrity
cpio -it < archive.cpio > /dev/null

# Compare with filesystem
find . | cpio -oH newc | cpio -it | sort > archive_list.txt
find . | sort > filesystem_list.txt
diff archive_list.txt filesystem_list.txt
```

### 3. Updating Archives

```bash
# Append to existing archive (not directly supported)
# Workaround: extract, add files, recreate
mkdir /tmp/archive_work
cd /tmp/archive_work
cpio -id < /path/to/archive.cpio
# Add new files
find . | cpio -oH newc > /path/to/new_archive.cpio
```

## Performance Optimization

### 1. Block Size Tuning

```bash
# Use larger block size for better performance
cpio -oB > archive.cpio          # 5120 bytes
cpio -o --block-size=32768 > archive.cpio  # 32KB blocks

# For tape drives
cpio -o --block-size=65536 > /dev/st0  # 64KB blocks
```

### 2. Compression Strategies

```bash
# Different compression methods
find . | cpio -oH newc | gzip -1 > fast_compress.cpio.gz    # Fast
find . | cpio -oH newc | gzip -9 > best_compress.cpio.gz    # Best ratio
find . | cpio -oH newc | lz4 > lz4_compress.cpio.lz4        # Very fast
find . | cpio -oH newc | xz -9 > xz_compress.cpio.xz        # Best ratio
```

### 3. Parallel Processing

```bash
# Use parallel compression
find . | cpio -oH newc | pigz > parallel_compressed.cpio.gz

# Parallel decompression
pigz -dc archive.cpio.gz | cpio -id
```

## Integration with Other Tools

### 1. With find

```bash
# Complex find expressions
find /var/log -name "*.log" -size +10M -mtime +30 | cpio -oH newc > old_large_logs.cpio

# Execute commands during find
find . -name "*.txt" -exec grep -l "important" {} \; | cpio -oH newc > important_texts.cpio
```

### 2. With rsync

```bash
# Create incremental backups
rsync -av --link-dest=/backup/previous /source/ /backup/current/
find /backup/current -type f | cpio -oH newc > incremental.cpio
```

### 3. With tar compatibility

```bash
# Convert tar to cpio
tar -cf - files | cpio -oH tar > archive.tar

# Convert cpio to tar
cpio -it < archive.cpio | tar -cf archive.tar -T -
```

## Troubleshooting

### 1. Common Errors

```bash
# "Premature end of file" error
# Check if archive is complete or corrupted
file archive.cpio

# Permission denied errors
# Use sudo for system files
sudo cpio -id < archive.cpio

# "Cannot create directory" errors
# Use -d option
cpio -id < archive.cpio
```

### 2. Debugging

```bash
# Verbose mode for debugging
cpio -idv < archive.cpio

# Check archive format
file archive.cpio
hexdump -C archive.cpio | head

# Test archive before extraction
cpio -it < archive.cpio > /dev/null
echo $?  # Should return 0 for success
```

### 3. Recovery

```bash
# Partial archive recovery
dd if=damaged_archive.cpio of=partial.cpio bs=512 count=1000
cpio -id < partial.cpio

# Skip damaged portions
cpio -id --only-verify-crc < archive.cpio
```

## Scripting and Automation

### 1. Backup Scripts

```bash
#!/bin/bash
# Automated backup script
BACKUP_DIR="/backup/$(date +%Y%m%d)"
SOURCE="/home /etc /var/log"

mkdir -p "$BACKUP_DIR"
for dir in $SOURCE; do
    find "$dir" -type f | cpio -oH newc | gzip > "$BACKUP_DIR/$(basename $dir).cpio.gz"
done
```

### 2. Restoration Scripts

```bash
#!/bin/bash
# Automated restoration script
ARCHIVE="$1"
DEST="${2:-/restore}"

if [ ! -f "$ARCHIVE" ]; then
    echo "Archive not found: $ARCHIVE"
    exit 1
fi

mkdir -p "$DEST"
cd "$DEST"

if [[ "$ARCHIVE" =~ \.gz$ ]]; then
    zcat "$ARCHIVE" | cpio -idm
else
    cpio -idm < "$ARCHIVE"
fi
```

## Best Practices

### 1. Archive Naming

```bash
# Use descriptive names with dates
backup_$(hostname)_$(date +%Y%m%d_%H%M%S).cpio.gz

# Include source information
home_backup_$(date +%Y%m%d).cpio
etc_configs_$(date +%Y%m%d).cpio
```

### 2. Verification

```bash
# Always verify critical archives
find /important | cpio -oH newc > critical.cpio
cpio -it < critical.cpio | wc -l
find /important | wc -l
```

### 3. Documentation

```bash
# Document archive contents
cpio -itv < archive.cpio > archive_contents.txt
echo "Created: $(date)" >> archive_info.txt
echo "Source: /path/to/source" >> archive_info.txt
```

## Important Notes

- **Choose appropriate format**: Use `newc` format for modern systems
- **Preserve permissions**: Use `-m` and run as appropriate user
- **Test archives**: Always verify archive integrity
- **Use compression**: Combine with gzip/bzip2/xz for space efficiency
- **Handle special files**: Be careful with device files and symlinks
- **Network security**: Use secure channels for remote operations
- **Backup strategy**: Regular backups with verification

The `cpio` command is powerful for creating flexible archives and system backups, especially when combined with find and compression tools.

For more details, check the manual: `man cpio`
