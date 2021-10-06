
# The `diff/sdiff` command
This command is used to display the differences in the files by comparing the files line by line.
### Syntax:

```
diff [options] File1 File2 
```

### Example

1. Lets say we have two files with names a.txt and b.txt containing 5 Indian states as follows-:
```
$ cat a.txt
Gujarat
Uttar Pradesh
Kolkata
Bihar
Jammu and Kashmir

$ cat b.txt
Tamil Nadu
Gujarat
Andhra Pradesh
Bihar
Uttar pradesh

```
On typing the diff command we will get below output.
```
$ diff a.txt b.txt
0a1
> Tamil Nadu
2,3c3
< Uttar Pradesh
 Andhra Pradesh
5c5
 Uttar pradesh
```

### Flags and their Functionalities

|**Short Flag**    |**Description**   |
|--|--|
| `-c`|To view differences in context mode, use the -c option.  |
| `-u`|To view differences in unified mode, use the -u option. It is similar to context mode  |
|`-i`|By default this command is case sensitive. To make this command case in-sensitive use -i option with diff. |
|`-version`|This option is used to display the version of diff which is currently running on your system.  |
