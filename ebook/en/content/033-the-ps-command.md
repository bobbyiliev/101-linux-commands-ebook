# The `ps` command

The `ps` command (process status) is used to display information about running processes on a Linux system — such as their PID, memory usage, CPU time, and associated users.

It’s often **piped** with commands like `grep` to search for a specific process or `less` to scroll through large outputs.

## Why Use `ps`

Imagine your system feels slow or an app becomes unresponsive — you can use `ps` to:
- Identify processes consuming high CPU/memory
- Find a program’s PID (Process ID)
- Kill or debug a stuck process
- Check who’s running what on a shared system

## Basic Syntax

```
ps [options]
```

Without any options, `ps` only shows processes in the current terminal session.

Example:
```bash
ps
```

Output:
```
  PID TTY          TIME CMD
 4587 pts/0    00:00:00 bash
 4621 pts/0    00:00:00 ps
```

## Essential Usage

**The one combo to remember:** `ps aux`
- `a` = all processes (all users)
- `u` = show user/owner info
- `x` = include processes without terminals

```
ps aux
```

Output example:
```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168208  1100 ?        Ss   10:15   0:02 /sbin/init
myuser    2471  0.5  1.2 431204 24500 ?        Sl   10:17   1:05 code
myuser    2523  2.3  0.7 230940 14860 pts/0    R+   10:22   0:01 ps aux
```

## Some More Practical Day to Day Examples

### Finding and Killing a process

You want to stop a frozen **OpenShot** process.

```
ps aux | grep openshot
```

Output:
```
myuser   3625  99.9  6.1 1243924 252340 ?  Rl  10:30  25:17 openshot
myuser   3649   0.0  0.0   6348   740 pts/0  S+  10:31   0:00 grep --color=auto openshot
```

Now, kill it:
```
kill -9 3625
```

### Show Processes by User
```bash
ps -u username
```

Output:
```
  PID TTY          TIME CMD
 2284 ?        00:00:00 sshd
 2455 ?        00:00:02 bash
```

### Filtering & Sorting Output

Show top 10 memory-consuming processes:
```
ps aux --sort=-%mem | head -10
```

Show top 10 CPU-consuming processes:
```
ps aux --sort=-%cpu | head -10
```

### Checking Parent/Child Process Hierarchy
```bash
ps -ef --forest
```
This gives a tree-like structure showing parent-child relationships — useful when debugging service spawns.

### Custom Output Format
To Show only PID, user, memory, and command:
```
ps -eo pid,user,%mem,cmd
```

## Real-Life DevOps Examples

### 1. Checking which process uses a specific port
```
sudo ps -fp $(sudo lsof -t -i:8080)
```

### 2. Monitoring Jenkins, Nginx, or Docker processes
```
ps aux | grep nginx
ps aux | grep jenkins
ps aux | grep docker
```

### 3. Find Zombie Processes
```
ps aux | awk '{ if ($8 == "Z") print $0; }'
```

## Key Options for Quick Reference

| Option | Description |
|:-------|:------------|
| `aux` | All processes with detailed info |
| `-ef` | Full listing (alternative to aux) |
| `-eo format` | Custom output columns |
| `--sort` | Sort by column (-%mem, -%cpu) |
| `-p PID` | Show specific PID |
| `-C name` | Show processes by command name |
| `-u user` | Show user's processes |
| `f` | ASCII art process tree |

### Additional Options:

|**Option**   |**Description**   |
|:---|:---|
|`a`|Shows list all processes with a terminal (tty)|
|`-A`|Lists all processes. Identical to `-e`|
|`-a`|Shows all processes except both session leaders and processes not associated with a terminal|
|`-d`|Select all processes except session leaders|
|`--deselect`|Shows all processes except those that fulfill the specified conditions. Identical to `-N`|
|`-e`|Lists all processes. Identical to `-A`|
|`-N`|Shows all processes except those that fulfill the specified conditions. Identical to `-deselect`|
|`T`|Select all processes associated with this terminal. Identical to the `-t` option without any argument|
|`r`|Restrict the selection to only running processes|
|`--help simple`|Shows all the basic options|
|`--help all`|Shows every available options|

## Related Tools

If you need **real-time** monitoring, use:
```
top
```
or the more user-friendly modern version:
```
htop
```


