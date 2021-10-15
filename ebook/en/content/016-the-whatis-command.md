# The `whatis` command

The `whatis` command is used to display one-line manual page descriptions for commands. 
It can be used to get a basic understanding of what a (unknown) command is used for.

### Examples of uses:

1. To display what `ls` is used for:

```
whatis ls
```

2. To display the use of all commands which start with `make`, execute the following:

```
whatis -w make*
```

### Syntax:

```
whatis [-OPTION] [KEYWORD]
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-d`|`--debug`|Show debugging messages|
|`-r`|`--regex`|Interpret each keyword as a regex|
|`-w`|`--wildcard`|The keyword(s) contain wildcards|