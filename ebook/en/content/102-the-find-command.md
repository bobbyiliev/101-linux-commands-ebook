# The `find` command

The `find` command lets you **search for files in a directory hierarchy** 

-   Search a file with specific name.
-   Search a file with pattern
- 	Search for empty files and directories.


### Examples:

1.  Search a file with specific name:

```[linux]
find ./directory1 -name sample.txt
```

2. Search a file with pattern:

```[linux]
find ./directory1 -name '*.txt' 
```

3. To find all directories whose name is test in / directory.

```[linux]
find / -type d -name test
```

4. Searching empty files in current directory

```[linux]
find . -size 0k
```

### Syntax:

```[linux]          
find [options] [paths] [expression]
```
**In Simple words** 
```[linux]
find [where to start searching from]
 [expression determines what to find] [-options] [what to find]
```

### Additional Flags and their Functionalities:

Commonly-used primaries include:
- `name` pattern - tests whether the file name matches the shell-glob pattern given.
- `type` type - tests whether the file is a given type. Unix file types accepted include:

| **options** |  **Description**                                                                                           |
| :-------------  | :-------------------------------------------------------------------------------------------------------- |
| `b`           | block device (buffered)                                                 |
| `d`            | directory                                                                      |
| `f`           | regular file |
| `l`             | Symbolic link                                                                        |
| `-print`              | always returns true; prints the name of the current file plus a newline to the stdout.  |
| `-mtime n`              | find's all the files which are modified n days back. |
| `-atime n`              | find's all the files which are accessed 50 days back. |
| `-cmin n` |              find's all the files which are modified in the last 1 hour.|
| ` -newer file` |              find's   file was modified more recently than file.|
| `-size n` |             File uses n units of space, rounding up.|

### Help Command
Run below command to view the complete guide to `find` command or [click here](https://en.wikipedia.org/wiki/Find_(Unix)).
```[linux]
man find
```
