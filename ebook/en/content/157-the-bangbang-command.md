# The `!!` command (History Expansion)

The `!!` command is a bash history expansion feature that repeats the last command. It's part of a broader set of history expansion capabilities that allow you to quickly re-execute, modify, or reference previous commands. This is extremely useful for correcting mistakes, adding sudo, or repeating complex commands.

## Syntax

```
!!
!<event>
!<string>
!?<string>?
```

## Key Features

- **Last Command Repetition**: Quickly re-run the previous command
- **Command Modification**: Modify and re-execute previous commands
- **Argument Extraction**: Extract specific arguments from previous commands
- **Pattern Matching**: Find commands by pattern
- **Time Saving**: Avoid retyping complex commands

## Basic Usage

### Simple History Expansion

```bash
# Run a command
ls -la /home/user

# Repeat the last command
!!

# Add sudo to the last command
sudo !!

# This is equivalent to:
sudo ls -la /home/user
```

### Common Scenarios

```bash
# Forgot sudo
apt update
# Permission denied

# Fix with sudo
sudo !!
# Executes: sudo apt update

# Wrong directory
cd /var/logs
# No such file or directory

# Fix the path
cd /var/log
# Then repeat with correct path
!!
```

## History Expansion Patterns

### 1. Event Designators

```bash
# !! - Last command
!!

# !n - Command number n
!123

# !-n - nth command back
!-2    # Two commands ago
!-5    # Five commands ago

# !string - Most recent command starting with 'string'
!ls    # Last command starting with 'ls'
!git   # Last command starting with 'git'

# !?string? - Most recent command containing 'string'
!?config?   # Last command containing 'config'
!?file?     # Last command containing 'file'
```

### 2. Word Designators

```bash
# Previous command: git commit -m "Fix bug" --amend

# !^ - First argument
echo !^        # echo commit

# !$ - Last argument
echo !$        # echo --amend

# !* - All arguments
echo !*        # echo commit -m "Fix bug" --amend

# !:n - nth argument (0-based)
echo !:0       # echo git
echo !:1       # echo commit
echo !:2       # echo -m

# !:n-m - Range of arguments
echo !:1-3     # echo commit -m "Fix bug"
```

### 3. Modifiers

```bash
# Previous command: ls /home/user/documents/file.txt

# :h - Remove trailing pathname component (head)
echo !!:h      # echo /home/user/documents

# :t - Remove leading pathname components (tail)
echo !!:t      # echo file.txt

# :r - Remove trailing suffix
echo !!:r      # echo /home/user/documents/file

# :e - Remove all but trailing suffix
echo !!:e      # echo txt

# :s/old/new/ - Substitute first occurrence
!!:s/user/admin/   # ls /home/admin/documents/file.txt

# :gs/old/new/ - Global substitution
!!:gs/o/0/         # ls /h0me/user/d0cuments/file.txt
```

## Practical Examples

### 1. Error Correction

```bash
# Typo in command
ct /etc/hosts
# Command not found

# Correct and re-run
cat /etc/hosts

# Then if you need to edit it
sudo vi !!    # Becomes: sudo vi /etc/hosts
```

### 2. Adding Missing Options

```bash
# Run command without verbose
tar -czf backup.tar.gz /home/user

# Add verbose flag
!!:s/-czf/-czvf/
# Becomes: tar -czvf backup.tar.gz /home/user

# Or simpler approach
tar -czvf backup.tar.gz /home/user
```

### 3. File Operations

```bash
# Create file
touch /tmp/test_file.txt

# Edit the same file
vi !!:$     # vi /tmp/test_file.txt

# Copy to different location
cp !!:$ /home/user/
# Becomes: cp /tmp/test_file.txt /home/user/

# Previous command: find /var/log -name "*.log" -size +10M
# Copy found files
cp !!:3 !!:4 !!:5 /backup/
# Using specific arguments from find command
```

### 4. Directory Navigation

```bash
# Change to a directory
cd /usr/local/bin

# List contents
ls !!:$     # ls /usr/local/bin

# Go back and then to related directory
cd /usr/local/src
# ... later ...
cd !!:h/bin    # cd /usr/local/bin
```

## Advanced History Expansion

### 1. Complex Substitutions

```bash
# Previous: rsync -av /home/user/docs/ backup@server:/backup/user/docs/

# Change source directory
!!:s/docs/pictures/
# Becomes: rsync -av /home/user/pictures/ backup@server:/backup/user/docs/

# Change both source and destination
!!:s/docs/pictures/:s/user\/docs/user\/pictures/
# Global changes
!!:gs/docs/pictures/
```

### 2. Combining with Other Features

```bash
# Previous: find /var/log -name "*.log" -type f -exec ls -l {} \;

# Modify to use different action
!!:s/-exec ls -l/-exec wc -l/
# Count lines instead of listing

# Extract just the find portion
!:0-4    # find /var/log -name "*.log" -type f

# Use arguments with different command
grep "error" !!:3  # grep "error" "*.log"
```

### 3. Working with Multiple Commands

```bash
# Pipeline command
ps aux | grep apache | grep -v grep

# Modify the grep pattern
!!:s/apache/nginx/
# Becomes: ps aux | grep nginx | grep -v grep

# Extract just part of pipeline
!:0-2     # ps aux | grep apache

# Add to existing pipeline
!! | wc -l    # Count the results
```

## Interactive Features

### 1. History Verification

```bash
# Enable history verification (before execution)
set +H    # Disable history expansion
set -H    # Enable history expansion

# Show command before execution
shopt -s histverify
# Now !! will show the command and wait for Enter
```

### 2. History Search

```bash
# Ctrl+R - Reverse search
# Type to search through history
# Ctrl+R again to find previous matches

# Search for specific command
!?git commit?    # Find last command containing "git commit"
!?ssh?           # Find last command containing "ssh"
```

## Configuration and Settings

### 1. History Settings

```bash
# History size
export HISTSIZE=1000        # Commands in memory
export HISTFILESIZE=2000    # Commands in file

# History control
export HISTCONTROL=ignoreboth    # Ignore duplicates and spaces
export HISTCONTROL=ignoredups    # Ignore duplicates only

# History ignore patterns
export HISTIGNORE="ls:cd:cd -:pwd:exit:date:* --help"

# Timestamp in history
export HISTTIMEFORMAT="%F %T "
```

### 2. History Expansion Settings

```bash
# Check if history expansion is enabled
set +o | grep histexpand

# Enable history expansion
set -H
# or
set -o histexpand

# Disable history expansion
set +H
# or
set +o histexpand
```

## Safety and Best Practices

### 1. Verification Before Execution

```bash
# Enable command verification
shopt -s histverify

# This makes !! show the command first, requiring Enter to execute

# Check what command will be executed
history | tail -1    # See last command
echo !!             # See what !! would execute (without running it)
```

### 2. Safe Practices

```bash
# Be careful with destructive commands
rm -rf /tmp/*
# Don't blindly run !! after such commands

# Use history to verify
history | tail -5    # Check recent commands

# For critical operations, type commands fully
# Don't rely on history expansion for:
# - rm commands
# - chmod commands
# - System configuration changes
```

### 3. Debugging

```bash
# See history expansion in action
set -x    # Enable command tracing
!!        # You'll see the expanded command
set +x    # Disable tracing

# Check history before using
history 10    # Show last 10 commands
!-2           # Run 2nd to last command
```

## Common Patterns and Shortcuts

### 1. Frequent Combinations

```bash
# Add sudo to last command
sudo !!

# Redirect last command output
!! > output.txt
!! 2>&1 | tee log.txt

# Background last command
!! &

# Time last command
time !!

# Run last command in different directory
(cd /tmp && !!)
```

### 2. File and Directory Operations

```bash
# Previous: vi /etc/apache2/sites-available/default

# Test the configuration
apache2ctl -t

# Copy the file
cp !!:$ !!:$:r.backup    # cp /etc/apache2/sites-available/default /etc/apache2/sites-available/default.backup

# Edit related file
vi !!:h/sites-enabled/default    # vi /etc/apache2/sites-enabled/default
```

### 3. Network and System Commands

```bash
# Check service status
systemctl status apache2

# Restart if needed
sudo !!:s/status/restart/    # sudo systemctl restart apache2

# Check multiple services
systemctl status nginx
!!:s/nginx/mysql/           # systemctl status mysql
!!:s/mysql/postgresql/      # systemctl status postgresql
```

## Integration with Scripts

### 1. History in Scripts

```bash
#!/bin/bash
# Note: History expansion doesn't work in scripts by default
# Enable it explicitly if needed

set -H    # Enable history expansion in script

# Use variables instead of history expansion in scripts
last_command="$1"
echo "Re-running: $last_command"
eval "$last_command"
```

### 2. Interactive Scripts

```bash
#!/bin/bash
# Interactive script using history concepts

while true; do
    read -p "Command: " cmd

    if [ "$cmd" = "!!" ]; then
        echo "Re-running: $last_cmd"
        eval "$last_cmd"
    elif [ "$cmd" = "exit" ]; then
        break
    else
        eval "$cmd"
        last_cmd="$cmd"
    fi
done
```

## Alternatives and Related Commands

### 1. fc (Fix Command)

```bash
# Edit last command in editor
fc

# Edit specific command number
fc 123

# List recent commands
fc -l

# Re-run range of commands
fc -s 100 105
```

### 2. history command

```bash
# Show command history
history

# Show last 10 commands
history 10

# Execute specific command number
!123

# Search and execute
history | grep git
!456
```

## Troubleshooting

### 1. History Expansion Not Working

```bash
# Check if enabled
set +o | grep histexpand

# Enable it
set -H

# Check in current shell
echo $-    # Should contain 'H'
```

### 2. Unexpected Expansions

```bash
# Escape ! to prevent expansion
echo "The price is \$5\!"

# Use single quotes
echo 'The price is $5!'

# Disable temporarily
set +H
echo "Commands with ! work normally"
set -H
```

### 3. Complex Command Issues

```bash
# For very complex commands, use variables
complex_cmd="find /var/log -name '*.log' -exec grep 'error' {} \;"
eval "$complex_cmd"

# Then modify variable instead of using history expansion
complex_cmd="${complex_cmd/error/warning}"
eval "$complex_cmd"
```

## Important Notes

- **Interactive Only**: History expansion primarily works in interactive shells
- **Not in Scripts**: Usually disabled in scripts for safety
- **Shell Specific**: This is a bash/zsh feature, not available in all shells
- **Verification**: Use `histverify` option for safety with destructive commands
- **Case Sensitive**: History expansion is case-sensitive
- **Immediate Execution**: !! executes immediately; use caution with destructive commands

The `!!` command and history expansion features are powerful tools for efficient command-line work, but they require understanding and careful use to avoid mistakes.

For more details, check the bash manual: `man bash` (search for "History Expansion")
