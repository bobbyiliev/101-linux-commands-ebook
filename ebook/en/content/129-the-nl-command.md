# The `nl` command

The “nl” command enumerates lines in a file. A different way of viewing the contents of a file, the “nl” command can be very useful for many tasks.
## Syntax
```
nl [ -b Type ] [ -f Type ] [ -h Type ] [ -l Number ] [ -d Delimiter ] [ -i Number ] [ -n Format ] [ -v Number ] [ -w Number ] [ -p ] [ -s Separator ] [ File ]
```
## Examples:
1. To number all lines:
```
nl  -ba  chap1
```

2. Displays all the text lines:
```
[server@ssh ~]$ nl states
1 Alabama
2 Alaska
3 Arizona
4 Arkansas
5 California
6 Colorado
7 Connecticut.
8 Delaware
```

3. Specify a different line number format
```
nl  -i10  -nrz  -s::  -v10  -w4  chap1
```

You can name only one file on the command line. You can list the flags and the file name in any order.
