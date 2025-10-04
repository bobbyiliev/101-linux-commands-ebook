# The `cd` command

The `cd` command is used to change the current working directory *(i.e., the directory in which the current user is working)*. The "cd" stands for "**c**hange **d**irectory" and it is one of the most frequently used commands in the Linux terminal.

The `cd` command is often combined with the `ls` command (see chapter 1) when navigating through a system. You can also press the `TAB` key to auto-complete directory names, or press `TAB` twice to list available directories in the current location.

### Syntax:

```
cd [OPTIONS] [directory]
```

### Basic Examples:

1. **Change to a specific directory:**
```
cd /path/to/directory
```

2. **Change to your home directory:**
```
cd ~
```
OR simply:
```
cd
```

3. **Change to the previous directory:**
```
cd -
```
This will also print the absolute path of the previous directory.

4. **Change to the system's root directory:**
```
cd /
```

5. **Move up one directory level (parent directory):**
```
cd ..
```

6. **Move up multiple directory levels:**
```
cd ../../..
```
This example moves up three levels.

### Practical Examples:

**Using relative paths:**
```
cd Documents/Projects/MyApp
```

**Using absolute paths:**
```
cd /usr/local/bin
```

**Combining with home directory shortcut:**
```
cd ~/Downloads
```

**Navigate to a directory with spaces in the name:**
```
cd "My Documents"
```
OR
```
cd My\ Documents
```

**Switch between two directories:**
```
cd /var/log
cd /etc
cd -  # Returns to /var/log
cd -  # Returns to /etc
```

### Additional Flags and Their Functionalities

|**Short flag**   |**Long flag**   |**Description**   |
|:---|:---|:---|
|`-L`|<center>-</center>|Follow symbolic links (default behavior). The `cd` command will follow symlinks and update the working directory to the target location.|
|`-P`|<center>-</center>|Use the physical directory structure without following symbolic links. Shows the actual path instead of the symlink path.|

**Example of `-L` vs `-P` with symbolic links:**
```
# Assume /var/www is a symlink to /home/user/web
cd -L /var/www      # Working directory shows as /var/www
pwd                 # Outputs: /var/www

cd -P /var/www      # Working directory resolves to actual path
pwd                 # Outputs: /home/user/web
```

### Common Errors and Troubleshooting

**Permission denied:**
```
cd /root
# bash: cd: /root: Permission denied
```
Solution: You need appropriate permissions to access the directory. Try using `sudo` if necessary.

**No such file or directory:**
```
cd /invalid/path
# bash: cd: /invalid/path: No such file or directory
```
Solution: Verify the path exists using `ls` or check for typos. Remember that paths are case-sensitive.

**Not a directory:**
```
cd /etc/passwd
# bash: cd: /etc/passwd: Not a directory
```
Solution: Ensure you're navigating to a directory, not a file.

### Important Notes:

- **Case sensitivity:** Linux file systems are case-sensitive. `cd Documents` is different from `cd documents`.
- **Special characters:** Directory names with spaces or special characters need to be quoted or escaped.
- **The `cd` command is a shell built-in:** It's not an external program, which is why it can change the shell's current directory.
- **No output on success:** By default, `cd` produces no output when successful (except `cd -` which prints the new path).
