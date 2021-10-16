# The `stat` command

The `stat` command lets you display file or file system status. It gives you useful information about the file (or directory) on which you use it.

### Examples:

1. Basic command usage

```
stat file.txt
```

2. Use the `-c` (or `--format`) argument to only display information you want to see (here, the total size, in bytes)

```
stat file.txt -c %s
```

### Syntax:

```
stat [OPTION] [FILE]
```

### Additional Flags and their Functionalities:

| Short Flag | Long Flag         | Description                                                                   |
| ---------- | ----------------- | ----------------------------------------------------------------------------- |
| `-L`       | `--dereference`   | Follow links                                                                  |
| `-f`       | `--file-system`   | Display file system status instead of file status                             |
| `-c`       | `--format=FORMAT` | Specify the format (see below)                                                |
| `-t`       | `--terse`         | Print the information in terse form                                           |
| -          | `--cached=MODE`   | Specify how to use cached attributes. Can be: `always`, `never`, or `default` |
| -          | `--printf=FORMAT` | Like `--format`, but interpret backslash escapes (`\n`, `\t`, ...)            |
| -          | `--help`          | Display the help and exit                                                     |
| -          | `--version`       | Output version information and exit                                           |


### Example of Valid Format Sequences for Files:

| Format | Description                                          |
| ------ | ---------------------------------------------------- |
| `%a`   | Permission bits in octal                             |
| `%A`   | Permission bits and file type in human readable form |
| `%d`   | Device number in decimal                             |
| `%D`   | Device number in hex                                 |
| `%F`   | File type                                            |
| `%g`   | Group ID of owner                                    |
| `%G`   | Group name of owner                                  |
| `%h`   | Number of hard links                                 |
| `%i`   | Inode number                                         |
| `%m`   | Mount point                                          |
| `%n`   | File name                                            |
| `%N`   | Quoted file name with dereference if symbolic link   |
| `%s`   | Total size, in bytes                                 |
| `%u`   | User ID of owner                                     |
| `%U`   | User name of owner                                   |
| `%w`   | Time of file birth, human-readable; - if unknown     |
| `%x`   | Time of last access, human-readable                  |
| `%y`   | Time of last data modification, human-readable       |
| `%z`   | Time of last status change, human-readable           |
