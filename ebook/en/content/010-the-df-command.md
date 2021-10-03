010-the-df-command.md

# The `df` command
The `df` command in Linux/Unix is used to show the disk usage & information.

# Usage

## Show available disk space

**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values are not human-readable (are in bytes)

**Command:**
```
df
```

## Show available disk space in human readable form

**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values ARE human-readable (are in GBs/MBs)

**Command:**
```
df -h
```

## Show available disk space for specific file system

**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values are only for the selected file system

**Command:**
```
df -hT file_system_name
```

## Show available inodes

**Action:**
--- Output the available inodes for all file systems

**Details:**
--- Outputted values are for inodes and not available space

**Command:**
```
df -i
```

## Show file system type

**Action:**
--- Output the file system types

**Details:**
--- Outputted values are for all file systems

**Command:**
```
df -T
```

## Exclude file system type from the output

**Action:**
--- Output the information while excluding the chosen file system type

**Details:**
--- Outputted values are for all file systems EXCEPT the chosen file system type

**Command:**
```
df -x file_system_type
```