# The `head` command

The `head` command prints the first ten lines of a file.

Example:
```
head filename.txt
```

Syntax:
```
head [OPTION] [FILENAME]
```

### Get a specific number of lines:

Use the `-n` option with a number (should be an integer) of lines to display.

Example:
```
head -n 10 foo.txt
```

This command will display the first ten lines of the file `foo.txt`.

Syntax:
```
head -n <number> foo.txt
```
### Additional Flags and their Functionalities


|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-c`|`--bytes=[-]NUM`|Print the first NUM bytes of each file; <br>with the leading '-', <br>print all but the last NUM bytes of each file|
|`-n`|`--lines=[-]NUM`|Print the first NUM lines instead of the first 10;<br> with the leading '-', <br>print all but the last NUM lines of each file|
|`-q`|`--quiet, --silent`|Never print headers giving file names|
|`-v`|`--verbose`|Always print headers giving file names|
|`-z`|`--zero-terminated`|Line delimiter is NUL, not newline|
|` `|`--help`| Display this help and exit|
|` `|`--version`|Output version information and exit|