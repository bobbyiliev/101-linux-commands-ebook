# The `mv` command

The `mv` command lets you **move one or more files or directories** from one place to another in a file system like UNIX.
It can be used for two distinct functions:

-   To rename a file or folder.
-   To move a group of files to a different directory.

_**Note:** No additional space is consumed on a disk during renaming, and the mv command doesn't provide a prompt for confirmation_

### Syntax:

```[linux]
mv [options] source (file or directory)  destination
```

### Examples:

1. To rename a file called old_name.txt:

```[linux]
mv old_name.txt new_name.txt
```

2. To move a file called _essay.txt_ from the current directory to a directory called _assignments_ and rename it _essay1.txt_:

```[linux]
mv essay.txt assignments/essay1.txt
```

3. To move a file called _essay.txt_ from the current directory to a directory called _assignments_ without renaming it

```[linux]
mv essay.txt assignments
```

### Additional Flags and their Functionalities:

| **Short Flag** | **Long Flag**   | **Description**                                                                                           |
| :------------- | :-------------- | :-------------------------------------------------------------------------------------------------------- |
| `-f`           | `--force`       | Force move by overwriting destination file without prompt                                                 |
| `-i`           | `--interactive` | Interactive prompt before overwrite                                                                       |
| `-u`           | `--update`      | Move only when the source file is newer than the destination file or when the destination file is missing |
| `-n`           | `--no-clobber`  | Do not overwrite an existing file                                                                         |
| `-v`           | `--verbose`     | Print source and destination files                                                                        |
| `-b`           | `--backup`      | Create a Backup of Existing Destination File                                                              |
