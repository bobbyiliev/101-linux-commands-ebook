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
|`-a`|`--all`|Show all files, including hidden files *(file names which begin with period `.`)*|
|`-A`|`--almost-all`|Shows all like `-a` but without showing `.`(current working directory) and `..` (parent directory)|
|`-d`|`--directory`|Instead of listing the files and directories inside the directory, it shows any information about the directory itself, it can be used with `-l` to show long formatted information|
|`-F`|`--classify`|Appends an indictaor character to the end of each listed name, as an example: `/` character is appended after each directory name listed|
|`-h`|`--human-readable`|like `-l` but displays file size in human-readable unit not in bytes|


### Setting Persistent Options:

Using the alias command it's possible to set persistent options for various commands, including ls.
This alias command sets color to auto, lists in long format, and show human-readable file sizes

```
alias ls="ls --color=auto -lh"
``` 

This alias will be active only on the current session until it ends.  For this alias to be active for all new sessions, 
add the command to your user rc file for example for bash : ~/.bashrc 


