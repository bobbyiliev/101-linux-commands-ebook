# The `cat` command
---

The `cat` command allows us to create single or multiple files, to view the content of a file or to concatenate files and redirect the output to the terminal or files.

The "cat" stands for 'concatenate.' and it's one of the most frequently used commands in the Linux terminal.


### Examples of uses:


1. To display the content of a file in terminal:

```
cat <specified_file_name>
```

2. To display the content of multiple files in terminal:

```
cat file1 file2 ...
```

3. To create a file with the cat command:

```
cat > filename
```

5. To display the content of all the files in current directory:

```
cat *
```

6. To put the output of a given file into another file:

```
cat oldfile > newfile
```
7. Use cat command with `more` and `less` options:

```
cat filename | more
cat filename | less
```

8. Append the contents of file1.txt to file2.txt

```
cat file1.txt >> file2.txt
```

9. Some implementations of cat, with option -n, it's possible to show line numbers

```
cat -n file1.txt file2.txt > newnumberedfile.txt
```


### Syntax:

```
cat [OPTION] [FILE]...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-A`| `--show-all` |equivalent to -vET|
|`-b`| `--number-nonblank` |number nonempty output lines, overrides -n|
|`-e`|<center>-</center>| equivalent to -vE|
|`-T`|<center>-</center>|Display tab separated lines in file opened with ```cat``` command.|
|`-E`|<center>-</center>|To show $ at the end of each file.|
|`-E`|<center>-</center>|Display file with line numbers.|
|`-n`| `--number`|number all output lines|
|`-s`| `--squeeze-blank`|suppress repeated empty output lines|
|`-u`|<center>-</center>|(ignored)|
|`-v`| `--show-nonprinting`|use ^ and M- notation, except for LFD and TAB|
|<center>-</center>|`--help` |display this help and exit|
|<center>-</center>|`--version`|output version information and exit|


---


# The `tac` command

`tac` is a Linux command that allows you to view files line-by-line, beginning from the last line. (tac doesn't reverse the contents of each individual line, only the order in which the lines are presented.) It is named by analogy with `cat`.


### Examples of uses:


1. To display the content of a file in terminal:

```
tac <specified_file_name>
```

2. This option attaches the separator before instead of after.

```
tac -b concat.txt tacexample.txt
```
3. This option will interpret the separator as a regular expression.
```
tac -r concat.txt tacexample.txt
```
4. This option uses STRING as the separator instead of newline.
```
tac -s concat.txt tacexample.txt
```

5. This option will display the help text and exit.

```
tac --help
```
6. This option will give the version information and exit.

```
tac --version
```

### Syntax:

```
tac [OPTION]... [FILE]...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-b`|`--before`|attach the separator before instead of after|
|`-r`| `--regex`|interpret the separator as a regular expression|
|`-s`| `--separator=STRING`|use STRING as the separator instead of newline|
|<center>-</center>|`--help`|display this help and exit|
|<center>-</center>|`--version`|output version information and exit|
