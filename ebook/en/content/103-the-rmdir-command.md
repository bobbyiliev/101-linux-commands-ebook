# The `rmdir` command

The **rmdir** command is used remove empty directories from the filesystem in Linux. The rmdir command removes each and every directory specified in the command line only if these directories are empty.

### Usage and Examples:

1. remove directory and its ancestors
```
rmdir -p a/b/c			// is similar to 'rmdir a/b/c a/b a'
```
2. remove multiple directories
```
rmdir a b c				// removes empty directories a,b and c
```

### Syntax:

```
rmdir [OPTION]... DIRECTORY...
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-`|`--ignore-fail-on-non-empty`|ignore each failure that is solely because a directory is non-empty|
|`-p`|`--parents`|remove DIRECTORY and its ancestors|
|`-d`|`--delimiter=DELIM`|use DELIM instead of TAB for field delimiter|
|`-v`|`--verbose`|output a diagnostic for every directory processed|
