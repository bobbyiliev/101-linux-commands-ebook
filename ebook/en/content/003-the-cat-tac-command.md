# The `cat` command


The `cat` command allows us to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.

The "cat" stands for 'concatenate.' and it is one of the most frequently used commands in the Linux terminal.


### Examples of uses:


1. To display content of a file in terminal:

```
cd <specified_file_name>
```

2. To display content of multiple files in terminal:

```
cat file1 file2 ...
```

3. To create a file with cat command:

```
cat > filename
```

5. To display all the files in current directory:

```
cat *
```

6. To redirect a file to the other file:

```
cat oldfile > newfile
```
7. Use cat command with more and less options:

```
cat filename | more
cat filename | less
```

### Syntax:

```
cat [OPTION] [FILE]...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-T`|<center>-</center>|Display tab separated lines in file opened with ```cat``` command.|
|`-E`|<center>-</center>|To show $ at the end of each file.|
|`-E`|<center>-</center>|Display file with line numbers.|
