# The `ncdu` Command
---

  `ncdu (NCurses Disk Usage)` is a curses-based version of the well-known 'du', and provides a fast way to see what directories are using your disk space.
  

## Example
1. Quiet Mode
```
ncdu -q
```

2. Omit mounted directories
```
ncdu -q -x
```



## Syntax 
```
ncdu [-hqvx] [--exclude PATTERN] [-X FILE] dir
```




## Additional Flags and their Functionalities:

|Short Flag |	Long Flag |	Description|
|---|---|---|
| `-h`| - |Print a small help message|
| `-q`| - |Quiet mode. While calculating disk space, ncdu will update the screen 10 times a second by default, this will be decreased to once every 2 seconds in quiet mode. Use this feature to save bandwidth over remote connections.|
| `-v`| - |Print version.|
| `-x`| - |Only count files and directories on the same filesystem as the specified dir.|
| - | `--exclude PATTERN`|Exclude files that match PATTERN. This argument can be added multiple times to add more patterns.|
| `-X FILE`| `--exclude-from FILE`| Exclude files that match any pattern in FILE. Patterns should be separated by a newline.|
