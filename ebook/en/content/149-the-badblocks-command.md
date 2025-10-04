# The `badblocks` command

The `badblocks` command is used to search for bad blocks on a storage device. It can scan hard drives, SSDs, USB drives, and other storage media to identify sectors that cannot reliably store data. This is essential for maintaining data integrity and system reliability.

## Syntax

```
badblocks [options] device [last-block] [first-block]
```

## Key Features

- **Non-destructive Testing**: Read-only tests by default
- **Destructive Testing**: Write tests for thorough checking
- **Pattern Testing**: Uses specific patterns to detect errors
- **Progress Reporting**: Shows scan progress and results
- **Output Options**: Various formats for different use cases

## Basic Usage

### Simple Read Test

```bash
# Basic read test (non-destructive)
sudo badblocks /dev/sdb

# Test specific partition
sudo badblocks /dev/sdb1

# Verbose output
sudo badblocks -v /dev/sdb
```

### Show Progress

```bash
# Show progress during scan
sudo badblocks -s /dev/sdb

# Show progress with verbose output
sudo badblocks -sv /dev/sdb
```

## Testing Modes

### 1. Read-Only Test (Default)

```bash
# Non-destructive read test
sudo badblocks /dev/sdb

# Read test with verbose output
sudo badblocks -v /dev/sdb

# Read test showing progress
sudo badblocks -sv /dev/sdb
```

### 2. Non-Destructive Read-Write Test

```bash
# Non-destructive read-write test
sudo badblocks -n /dev/sdb

# Backup original data, test, then restore
sudo badblocks -nv /dev/sdb
```

### 3. Destructive Write Test

```bash
# WARNING: This will destroy all data!
sudo badblocks -w /dev/sdb

# Destructive test with verbose output
sudo badblocks -wv /dev/sdb

# Write test with progress
sudo badblocks -wsv /dev/sdb
```

## Common Options

### Basic Options

```bash
# -v: Verbose output
sudo badblocks -v /dev/sdb

# -s: Show progress
sudo badblocks -s /dev/sdb

# -o: Output bad blocks to file
sudo badblocks -o badblocks.txt /dev/sdb

# -b: Specify block size (default 1024)
sudo badblocks -b 4096 /dev/sdb
```

### Advanced Options

```bash
# -c: Number of blocks to test at once
sudo badblocks -c 65536 /dev/sdb

# -p: Number of passes (for write tests)
sudo badblocks -w -p 2 /dev/sdb

# -t: Test pattern for write tests
sudo badblocks -w -t 0xaa /dev/sdb

# -f: Force operation even if mounted
sudo badblocks -f /dev/sdb
```

## Practical Examples

### 1. Basic Drive Health Check

```bash
# Unmount the device first
sudo umount /dev/sdb1

# Run basic read test
sudo badblocks -sv /dev/sdb

# Save results to file
sudo badblocks -sv -o badblocks_sdb.txt /dev/sdb
```

### 2. Thorough Drive Testing

```bash
# Full destructive test (destroys data!)
# Make sure to backup first!
sudo badblocks -wsv /dev/sdb

# Multiple pass destructive test
sudo badblocks -wsv -p 3 /dev/sdb
```

### 3. Testing Specific Range

```bash
# Test blocks 1000 to 2000
sudo badblocks -sv /dev/sdb 2000 1000

# Test first 1GB (assuming 4K blocks)
sudo badblocks -sv -b 4096 /dev/sdb 262144 0
```

### 4. Integration with fsck

```bash
# Create bad blocks file
sudo badblocks -sv -o /tmp/badblocks /dev/sdb1

# Use with fsck to mark bad blocks
sudo fsck.ext4 -l /tmp/badblocks /dev/sdb1

# For new filesystem
sudo mke2fs -l /tmp/badblocks /dev/sdb1
```

## Different Block Sizes

### Choosing Block Size

```bash
# 1KB blocks (default)
sudo badblocks -b 1024 /dev/sdb

# 4KB blocks (common for modern drives)
sudo badblocks -b 4096 /dev/sdb

# 512 byte blocks (traditional sector size)
sudo badblocks -b 512 /dev/sdb

# Match filesystem block size
sudo tune2fs -l /dev/sdb1 | grep "Block size"
sudo badblocks -b 4096 /dev/sdb1
```

## Test Patterns

### Write Test Patterns

```bash
# Alternating pattern (0xaa = 10101010)
sudo badblocks -w -t 0xaa /dev/sdb

# All ones pattern
sudo badblocks -w -t 0xff /dev/sdb

# All zeros pattern
sudo badblocks -w -t 0x00 /dev/sdb

# Random pattern
sudo badblocks -w -t random /dev/sdb
```

### Multiple Patterns

```bash
# Test with multiple patterns
sudo badblocks -w -t 0xaa -t 0x55 -t 0xff -t 0x00 /dev/sdb

# Four-pass test with different patterns
sudo badblocks -wsv -p 4 -t 0xaa -t 0x55 -t 0xff -t 0x00 /dev/sdb
```

## Output and Reporting

### Standard Output

```bash
# Basic output (just bad block numbers)
sudo badblocks /dev/sdb

# Verbose output with details
sudo badblocks -v /dev/sdb

# Progress indicator
sudo badblocks -s /dev/sdb
```

### Save Results to File

```bash
# Save bad blocks list
sudo badblocks -o badblocks.txt /dev/sdb

# Append to existing file
sudo badblocks -o badblocks.txt /dev/sdb >> all_badblocks.txt

# Save with verbose output to different files
sudo badblocks -v -o badblocks.txt /dev/sdb 2> scan_log.txt
```

## Working with Different Storage Types

### 1. Traditional Hard Drives

```bash
# Standard test for HDDs
sudo badblocks -sv /dev/sda

# Thorough test with multiple passes
sudo badblocks -wsv -p 4 /dev/sda
```

### 2. Solid State Drives

```bash
# Read-only test (preferred for SSDs)
sudo badblocks -sv /dev/sdb

# Non-destructive test
sudo badblocks -nsv /dev/sdb

# Avoid excessive write tests on SSDs
```

### 3. USB Drives

```bash
# Test USB drive
sudo badblocks -sv /dev/sdc

# Fast test for quick verification
sudo badblocks -sv -c 65536 /dev/sdc
```

### 4. SD Cards

```bash
# Test SD card
sudo badblocks -sv /dev/mmcblk0

# Write test for fake capacity detection
sudo badblocks -wsv /dev/mmcblk0
```

## Integration with File Systems

### 1. ext2/ext3/ext4

```bash
# Create filesystem with bad block check
sudo mke2fs -c /dev/sdb1

# Check existing filesystem
sudo fsck.ext4 -c /dev/sdb1

# Thorough check
sudo fsck.ext4 -cc /dev/sdb1
```

### 2. Using with e2fsck

```bash
# Create bad blocks list
sudo badblocks -sv -o /tmp/badblocks /dev/sdb1

# Apply to filesystem
sudo e2fsck -l /tmp/badblocks /dev/sdb1
```

## Monitoring and Automation

### 1. Scheduled Checking

```bash
# Create script for regular checking
#!/bin/bash
DEVICE="/dev/sdb"
LOGFILE="/var/log/badblocks_$(date +%Y%m%d).log"

sudo badblocks -sv -o /tmp/badblocks "$DEVICE" > "$LOGFILE" 2>&1

if [ -s /tmp/badblocks ]; then
    echo "Bad blocks found on $DEVICE!" | mail -s "Bad Blocks Alert" admin@domain.com
fi
```

### 2. SMART Integration

```bash
# Check SMART status first
sudo smartctl -a /dev/sdb

# Run badblocks if SMART shows issues
sudo smartctl -t short /dev/sdb
sleep 300
sudo smartctl -a /dev/sdb
sudo badblocks -sv /dev/sdb
```

## Performance Considerations

### 1. Speed Optimization

```bash
# Increase block count for faster scanning
sudo badblocks -c 65536 /dev/sdb

# Use larger block size
sudo badblocks -b 4096 -c 16384 /dev/sdb

# Combine options for maximum speed
sudo badblocks -sv -b 4096 -c 65536 /dev/sdb
```

### 2. System Impact

```bash
# Run with lower priority
sudo nice -n 19 badblocks -sv /dev/sdb

# Limit I/O impact
sudo ionice -c 3 badblocks -sv /dev/sdb

# Combine nice and ionice
sudo nice -n 19 ionice -c 3 badblocks -sv /dev/sdb
```

## Interpreting Results

### 1. No Bad Blocks

```bash
# Output: "Pass completed, 0 bad blocks found."
# This indicates a healthy drive
```

### 2. Bad Blocks Found

```bash
# Output shows block numbers of bad sectors
# Example:
# Pass completed, 5 bad blocks found. (0/0/5 errors)
# 1024
# 2048
# 4096
# 8192
# 16384
```

### 3. Understanding Block Numbers

```bash
# Convert block numbers to byte offsets
# Block 1024 with 4KB block size = 1024 * 4096 = 4,194,304 bytes
# This helps locate physical position on drive
```

## Troubleshooting

### 1. Permission Denied

```bash
# Must run as root
sudo badblocks /dev/sdb

# Check device permissions
ls -l /dev/sdb
```

### 2. Device Busy

```bash
# Unmount all partitions first
sudo umount /dev/sdb1
sudo umount /dev/sdb2

# Check for active processes
lsof /dev/sdb*

# Use force option if necessary
sudo badblocks -f /dev/sdb
```

### 3. Slow Performance

```bash
# Increase block count
sudo badblocks -c 65536 /dev/sdb

# Use appropriate block size
sudo badblocks -b 4096 /dev/sdb

# Check system load
iostat 1
```

## Safety Considerations

### 1. Data Backup

```bash
# Always backup before destructive tests
sudo dd if=/dev/sdb of=/backup/sdb_backup.img bs=1M

# Or use filesystem-level backup
sudo rsync -av /mount/point/ /backup/location/
```

### 2. Drive Health Assessment

```bash
# Check SMART data first
sudo smartctl -a /dev/sdb

# Look for reallocated sectors
sudo smartctl -A /dev/sdb | grep Reallocated
```

### 3. When to Replace Drive

```bash
# Replace if:
# - Many bad blocks found (>50-100)
# - Bad blocks increasing over time
# - SMART indicates drive failure
# - Critical system drive affected
```

## Alternative Tools

### 1. SMART Tools

```bash
# Use smartctl for health monitoring
sudo smartctl -t long /dev/sdb
sudo smartctl -a /dev/sdb
```

### 2. Manufacturer Tools

```bash
# Many manufacturers provide specific tools
# - Western Digital: WD Data Lifeguard
# - Seagate: SeaTools
# - Samsung: Samsung Magician
```

## Important Notes

- Read tests are safe and non-destructive
- Write tests destroy all data on the device
- Always unmount devices before testing
- Test results should be interpreted with other health indicators
- Regular testing helps prevent data loss
- Consider drive replacement if many bad blocks are found
- Modern drives have spare sectors for bad block management

The `badblocks` command is an essential tool for maintaining storage device health and preventing data loss.

For more details, check the manual: `man badblocks`
