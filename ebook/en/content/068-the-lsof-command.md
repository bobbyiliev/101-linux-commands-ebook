# The `lsof` command

The `lsof` command shows **file infomation** of all the files opened by a running process. It's name is also derived from the fact that, list open files > `lsof`

An open file may be a regular file, a directory, a block special file, a character special file, an executing text reference, a library , a stream or a network file (Internet socket, NFS file or UNIX domain socket). A specific file or all the files in a file system may be selected by path.
### Syntax:

```
lsof [-OPTION] [USER_NAME]
```

### Examples:

1. To show all the files opened by all active processes:

```
lsof
```

2. To show the files opened by a particular user:

```
lsof -u [USER_NAME]
```


3. To list the processes with opened files under a specified directory:

```
lsof +d [PATH_TO_DIR]
```

### Options and their Functionalities:

|**Option**   |**Additional Options**   |**Description**   |
|:---|:---|:---|
|`-i`|`tcp`/ `udp`/ `:port`|List all network connections running, Additionally, on udp/tcp or on specified port.|
|`-i4`|<center>-</center>|List all processes with ipv4 connections.|
|`-i6`|<center>-</center>|List all processes with ipv6 connections.|
|`-c`|`[PROCESS_NAME]`|List all the files of a particular process with given name.|
|`-p`|`[PROCESS_ID]`|List all the files opened by a specified process id.|
|`-p`|`^[PROCESS_ID]`|List all the files that are not opened by a specified process id.|
|`+d`|`[PATH]`|List the processes with opened files under a specified directory|
|`+R`|<center>-</center>|List the files opened by parent process Id.|

### Help Command
Run below command to view the complete guide to `lsof` command.
```
man lsof
```
