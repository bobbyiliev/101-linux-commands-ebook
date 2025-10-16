# The `find` Command

The `find` command is one of the most powerful Linux utilities that lets you search for files and directories based on various conditions like name, size, modification time, permissions, and more.

## Basic Syntax

```
find [path] [options] [expression]
```

**In simple words:**  
> “Search starting from `[path]`, apply `[options or filters]`, and then perform an `[action]` on the result.”

Example:

```
find /home/user -name "*.log"
```
This searches for all `.log` files under `/home/user`.

## Common Use Cases

### 1. Search a File by Exact Name

```
find ./directory1 -name sample.txt
```

Finds `sample.txt` inside `directory1` and all its subdirectories.

Case-insensitive search:

```
find ./directory1 -iname "sample.txt"
```

### 2. Search Files by Pattern (Wildcard)

Find all `.txt` files under `directory1`.

```
find ./directory1 -name "*.txt"
```

More examples:
```
find /var/log -name "*.log"
find /etc -name "conf*"
```

### 3. Find Directories by Name

```
find / -type d -name test
```
Lists all directories named `test` from the root `/`.

### 4. Find Empty Files and Directories

```
find . -empty
```
Finds both empty files and directories in the current folder.

Only empty files:
```
find . -type f -empty
```

### 5. Find Files by Modification or Access Time

| Option | Description |
|--------|--------------|
| `-mtime n` | Modified *n* days ago |
| `-atime n` | Accessed *n* days ago |
| `-ctime n` | Changed *n* days ago |
| `-mmin n`  | Modified *n* minutes ago |

Examples:

Find files modified within the last 2 days.
```
find /var/log -mtime -2
```

Find files modified within the last hour.
```
find . -mmin -60
```

### 6. Find Files by Size

| Expression | Meaning |
|-------------|----------|
| `+n` | Greater than n |
| `-n` | Less than n |
| `n` | Exactly n |

Examples:

Find files larger than 100 MB.
```
find / -size +100M
```

Find files smaller than 10 KB.
```
find . -size -10k
```

### 7. Find Files Modified More Recently than Another File

```
find . -newer reference.txt
```
Lists files modified after `reference.txt`.

### 8. Find Files by Type

| Type | Description |
|------|--------------|
| `f` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `b` | Block device |
| `c` | Character device |

Example:

Find all block devices.
```
find /dev -type b
```

### 9. Find Files by Permission
Find files with exactly 644 permissions.
```
find /var/www -type f -perm 644
```

Find files executable by anyone.
```
find /usr -type f -perm /111
```

### 10. Execute Commands on Found Files

You can use the `-exec` option to run a command on each file found:

```
find . -type f -name "*.log" -exec rm -f {} \;
```
Deletes all `.log` files under the current directory.

**Alternative (faster):**

```
find . -type f -name "*.log" | xargs rm -f
```

### 11. Combine Multiple Conditions

You can combine filters together:

```
find /var/log -name "*.log" -size +50M -mtime -2
```
Finds `.log` files larger than 50 MB and modified within the last 2 days.

### 12. Print Only File Names (Quiet Output)
```
find /etc -type f -name "*.conf" -print
```
The `-print` flag ensures output is displayed (it’s the default in most systems).

## Quick Reference Table

| Task | Command |
|------|----------|
| Find files with specific name | `find . -name filename.txt` |
| Case-insensitive search | `find . -iname filename.txt` |
| Find directories only | `find . -type d` |
| Find empty files | `find . -type f -empty` |
| Find files > 1 GB | `find . -size +1G` |
| Find modified in last day | `find . -mtime -1` |
| Delete `.tmp` files | `find . -name "*.tmp" -delete` |
| Search and execute | `find . -name "*.log" -exec gzip {} \;` |

## Getting Help

To view the complete guide for the `find` command, run:

```
man find
```
