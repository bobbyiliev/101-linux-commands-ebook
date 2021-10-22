# The `df` command
The `df` command in Linux/Unix is used to show the disk usage & information.
`df` is an abbreviation for "disk free".

`df` displays the amount of disk space available on the file system containing each file name argument. If no file name is given, the space available on all currently mounted file systems is shown.

### Syntax
```
df [OPTION]... [FILE]...
```

### Options
|**Short Flag**|**Long Flag**|**Description**|
|:--|:--|:--|
|`-a`|`--all`|Include pseudo, duplicate, inaccessible file systems.|
|`-B`|`--block-size=SIZE`|Scale sizes by SIZE before printing them; e.g., `-BM` prints sizes in units of 1,048,576 bytes; see SIZE format below.|
|`-h`|`--human-readable`|Print sizes in powers of 1024 (e.g., 1023M).|
|`-H`|`--si`|Print sizes in powers of 1000 (e.g., 1.1G).|
|`-i`|`--inodes`|List inode information instead of block usage.|
|`-k`|<center>-</center>|Like `--block-size=1K`.|
|`-l`|`--local`|Limit listing to local file systems.|
|<center>-</center>|`--no-sync`|Do not invoke `sync` before getting usage info (default).|
|<center>-</center>|`--output[=FIELD_LIST]`|Use the output format defined by `FIELD_LIST`, or print all fields if FIELD_LIST is omitted.|
|`-P`|`--portability`|Use the `POSIX` output format|
|<center>-</center>|`--sync`|Invoke sync before getting usage info.|
|<center>-</center>|`--total`|Elide all entries insignificant to available space, and produce a grand total.|
|`-t`|`--type=TYPE`|Limit listing to file systems of type `TYPE`.|
|`-T`|`--print-type`|Print file system type.|
|`-x`|`--exclude-type=TYPE`|Limit listing to file systems not of type `TYPE`.|
|`-v`|<center>-</center>|Ignored; included for compatibility reasons.|
|<center>-</center>|`--help`|Display help message and exit.|
|<center>-</center>|`--version`|Output version information and exit.|

### Examples:
1. Show available disk space
**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values are not human-readable (are in bytes)

**Command:**
```
df
```

2. Show available disk space in human-readable form
**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values ARE human-readable (are in GBs/MBs)

**Command:**
```
df -h
```

3. Show available disk space for the specific file system
**Action:**
--- Output the available disk space and where the directory is mounted

**Details:**
--- Outputted values are only for the selected file system

**Command:**
```
df -hT file_system_name
```

4. Show available inodes
**Action:**
--- Output the available inodes for all file systems

**Details:**
--- Outputted values are for inodes and not available space

**Command:**
```
df -i
```

5. Show file system type
**Action:**
--- Output the file system types

**Details:**
--- Outputted values are for all file systems

**Command:**
```
df -T
```

6. Exclude file system type from the output
**Action:**
--- Output the information while excluding the chosen file system type

**Details:**
--- Outputted values are for all file systems EXCEPT the chosen file system type

**Command:**
```
df -x file_system_type
```
