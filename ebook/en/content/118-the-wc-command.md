# The `wc` command

the `wc` command stands for word count. It's used to count the number of lines, words, and bytes *(characters)* in a file or standard input then prints the result to the standard output.


### Examples:

1. To count the number of lines, words and characters in a file in order:

```
wc file.txt
```

2. To count the number of directories in a directory:

```
ls -F | grep / | wc -l
```

### Syntax:

```bash
wc [OPTION]... [FILE]...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-c` | `--bytes` | print the byte counts|
|`-m` | `--chars` | print the character counts|
|`-l` | `--lines` | print the newline counts|
|<center>-</center> | `--files0-from=F` | read  input  from the files specified by NUL-terminated names in file F. If F is `-` then read names from standard input|
|`-L` | `--max-line-length` | print the maximum display width|
|`-w` | `--words` | print the word counts|



### Additional Notes:

* Passing more than one file to `wc` command prints the counts for each file and the total conuts of them.
* you can combine more whan one flag to print the result as you want. 
