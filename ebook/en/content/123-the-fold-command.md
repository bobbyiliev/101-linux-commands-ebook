# The `fold` command

The `fold`  command in Linux wraps each line in an input file to fit a specified width and prints it to the standard output. 

By default, it wraps lines at a maximum width of 80 columns but this is configurable. 

To fold input using the fold command pass a file or standard input to the command.


### Syntax:

```
fold [OPTION]... [FILE]...
```

### Options

**-w** : By using this option in fold command, we can limit the width by number of columns.

By using this command we change the column width from default width of 80.
Syntax:

```
fold -w[n] [FILE]
```
 Example: wrap the lines of file1.txt to a width of 60 columns

```
fold -w60 file1.txt
```


**-b** : This option of fold command is used to limit the width of the output by the number of bytes rather than the number of columns. 

By using this we can enforce the width of the output to the number of bytes.

```
fold -b[n] [FILE]
```

Example: limit the output width of the file to 40 bytes and the command breaks the output at 40 bytes.

```
fold -b40 file1.txt
```

**-s** : This option is used to break the lines on spaces so that words are not broken. 

If a segment of the line contains a blank character within the first width column positions, break the line after the last such blank character meeting the width constraints.

```
fold -w[n] -s [FILE]
```


