
# The `cut` command

The `cut` command lets you remove sections from each line of files. Print selected parts of lines from each FILE to standard output. With no FILE, or when FILE is -, read standard input.

### Usage and Examples:

1. Selecting specific fields in a file
```
cut -d "delimiter" -f (field number) file.txt
```

2. Selecting specific characters:
```
cut -c [(k)-(n)/(k),(n)/(n)] filename
```
Here, **k** denotes the starting position of the character and **n** denotes the ending position of the character in each line, if _k_ and _n_ are separated by “-” otherwise they are only the position of character in each line from the file taken as an input.

3. Selecting specific bytes:
```
cut -b 1,2,3 filename 			//select bytes 1,2 and 3
cut -b 1-4 filename				//select bytes 1 through 4
cut -b 1- filename				//select bytes 1 through the end of file
cut -b -4 filename				//select bytes from the beginning till the 4th byte
```
**Tabs and backspaces** are treated like as a character of 1 byte.

### Syntax:

```
cut OPTION... [FILE]...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-b`|`--bytes=LIST`|select only these bytes|
|`-c`|`--characters=LIST`|select only these characters|
|`-d`|`--delimiter=DELIM`|use DELIM instead of TAB for field delimiter|
|`-f`|`--fields`|select only these fields;  also print any line that contains no delimiter character, unless the -s option is specified|
|`-s`|`--only-delimited`|do not print lines not containing delimiters|
|`-z`|`--zero-terminated`|line delimiter is NUL, not newline|
