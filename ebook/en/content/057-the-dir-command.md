# The `dir` command

The `dir` command lists the contents of a directory(_the current directory by default_). **It differs from ls command in the format of listing the content**. By default, the dir command lists the files and folders in columns, sorted vertically and special characters are represented by backslash escape sequences.

### Syntax:

```[linux]
dir [OPTIONS] [FILE]
```

### Examples:

1. To list files in the current directory:

```[linux]
dir
```

2. To list even the hidden files in the current directory:

```[linux]
dir -a
```

3. To list the content with detailed information for each entry

```[linux]
dir -l
```

### Additional Flags and their Functionalities:

| **Short Flag**     | **Long Flag**               | **Description**                                                                                                                   |
| :----------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `-a`               | `--all`                     | It displays all the hidden files(starting with `.`) along with two files denoted by `.` and `..`                                  |
| `-A`               | `--almost-all`              | It is **similar to -a** option except that it _does not display files that signals the current directory and previous directory._ |
| `-l`               | <center>-</center>          | Display detailed information for each entry                                                                                       |
| `-s`               | `--size`                    | Print the allocated size of each file, in blocks File                                                                             |
| `-h`               | `--human-readable`          | Used with with -l and -s, to print sizes like in human readable format like 1K, 2M and so on                                      |
| `-F`               | <center>-</center>          | Classifies entries into their type based on appended symbol (`/`, `*`, `@`, `%`, `=`)                                             |
| `-v`               | `--verbose`                 | Print source and destination files                                                                                                |
| <center>-</center> | `--group-directories-first` | To group directories before files                                                                                                 |
| `-R `              | `--recursive`               | To List subdirectories recursively.                                                                                               |
| `-S `              | <center>-</center>          | sort by file size, display largest first                                                                                          |
