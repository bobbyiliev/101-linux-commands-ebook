# The `rm` command

`rm` which stands for "remove" is a command used to remove *(delete)* specific files. It can also be used to remove directories by using the appropriate flag.

### Example:
```
rm filename.txt
```
### Syntax
```
rm [OPTION] [FILE|DIRECTORY]
```

### Flags and their Functionalities:
|Short Flag|Long Flag|Description|
|:---|:---|:---|
|`-f`|`--force`|Ignore nonexistance of files or directories, never prompt|
|`-i`|<center>-</center>|Prompt before every removal|
|`-I`|<center>-</center>|Prompt once before removal of more than 3 files, or when removing recursively|
|`-d`|`--dir`|remove empty directories|
|`-v`|`--verbose`|explain what is being done|
|`-r` or `-R`|`--recursive`|remove directories and their contents recursively|
|<center>-</center>|`--help`|Display help then exit|
|<center>-</center>|`--version`|First, Print version Information, Then exit|
|<center>-</center>|`--no-preserve-root`|do not treat `/` specially|
|<center>-</center>|`-preserve-root[=all]`|do not remove `/` (default) <br>with 'all', reject any command line argument on a separate device from its parent|
|<center>-</center>|`--interactive[=WHEN]`|prompt according to WHEN, never, once `-I`, or always `-i`, without WHEN, prompt always|
|<center>-</center>|` --one-file-system`|when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument0|


***IMPORTANT NOTICE:***
1. `rm` doesn't remove directories by default, so use `-r`, `-R`, `--recursive` options to remove each listed directory, along with all of its contents.
2. To remove a file whose name starts with `-` such as `-foo`, use one of the following commands:
   - `rm -- -foo`
   - `rm ./-foo`
3. To ensure that files/directories being deleted are truly unrecoverable, consider using the `shred` command.