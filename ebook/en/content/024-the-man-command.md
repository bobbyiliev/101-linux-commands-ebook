# The `man` command

The `man` command is used to display the manual of any command that we can run on the terminal.
It provides information like: DESCRIPTION, OPTIONS, AUTHORS and more.

### Examples:

1. Man page for printf:

```
man printf
```

2. Man page section 2 for intro:

```
man 2 intro
```
3. Viewing the Manual for a Local File (using the -l flag):

```
man -l [LOCAL-FILE]
```

### Syntax:

```
man [SECTION-NUM] [COMMAND NAME]
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-f`|<center>-</center>|Return the sections of an command|
|`-a`|<center>-</center>|Display all the manual pages of an command|
|`-k`|<center>-</center>|Searches the given command with RegEx in all man pages|
|`-w`|<center>-</center>|Returns the location of a given command man page|
|`-I`|<center>-</center>|Searches the command manual case sensitive|
