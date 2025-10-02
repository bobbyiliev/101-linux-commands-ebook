# The `ls` command

The `ls` command lets you see the files and directories inside a specific directory *(current working directory by default)*.
It normally lists the files and directories in ascending alphabetical order.

### Examples:

1. To show the files inside your current working directory:

```
ls
```

2. To show the files and directory inside a specific Directory:

```
ls {Directory_Path}
```

### Syntax:

```
ls [-OPTION] [DIRECTORY_PATH]
```

### Interactive training

In this interactive tutorial, you will learn the different ways to use the `ls` command:

[The ls command by Tony](https://devdojo.com/tnylea/ls-command)

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-l`|<center>-</center>|Show results in long format|
|`-S`|<center>-</center>|Sort results by file size|
|`-t`|<center>-</center>|Sort results by modification time|
|`-r`|`--reverse`|Show files and directories in reverse order *(descending alphabetical order)*|
|`-a`|`--all`|Show all files, including hidden files *(file names which begin with a period `.`)*|
|`-la`|<center>-</center>|Show long format files and directories including hidden files|
|`-lh`|<center>-</center>|list long format files and directories with readable size|
|`-A`|`--almost-all`|Shows all like `-a` but without showing `.`(current working directory) and `..` (parent directory)|
|`-d`|`--directory`|Instead of listing the files and directories inside the directory, it shows any information about the directory itself, it can be used with `-l` to show long formatted information|
|`-F`|`--classify`|Appends an indicator character to the end of each listed name, as an example: `/` character is appended after each directory name listed|
|`-h`|`--human-readable`|like `-l` but displays file size in human-readable unit not in bytes|


### SELinux Support on Red Hat-Based Systems:

On Red Hat-based distributions (RHEL, CentOS, Fedora, Rocky Linux, AlmaLinux) that use SELinux, the `ls` command provides additional options to display SELinux security context information:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-Z`|`--context`|Display SELinux security context for files and directories|
|`-lZ`|<center>-</center>|Show long format with SELinux security context|

**Example Output:**

```bash
ls -Z
unconfined_u:object_r:user_home_t:s0 file.txt
unconfined_u:object_r:user_home_t:s0 directory
```

```bash
ls -lZ
-rw-rw-r--. 1 user user unconfined_u:object_r:user_home_t:s0 1234 Jan 15 10:30 file.txt
drwxrwxr-x. 2 user user unconfined_u:object_r:user_home_t:s0 4096 Jan 15 10:25 directory
```

The SELinux context format is: `user:role:type:level`

**Note:** The `-Z` option is only functional on systems with SELinux enabled. On non-SELinux systems, this option may not be available or will show no additional information.


### Setting Persistent Options:


Customizing command behavior in Linux is easy using the `alias` command. To make these changes permanent, follow these steps:

1. **Create the Alias**: Define your alias with the desired options. For example, to enhance the `ls` command:

    ```bash
    alias ls="ls --color=auto -lh"
    ```

2. **Persistence**: This alias is effective only for the current session. To make it permanent, add the alias to your shell's configuration file:

    - **Bash**: Append the alias to `~/.bashrc`:

        ```bash
        echo 'alias ls="ls --color=auto -lh"' >> ~/.bashrc
        source ~/.bashrc
        ```

3. **Verification**: Open a new terminal session, and the `ls` command will display files as configured.


