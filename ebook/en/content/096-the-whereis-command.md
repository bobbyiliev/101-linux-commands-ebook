# The `whereis` command

The `whereis` command is used to find the location of source/binary file of a command and manuals sections for a specified file in Linux system. If we compare `whereis` command with find command they will appear similar to each other as both can be used for the same purposes but `whereis` command produces the result more accurately by consuming less time comparatively.

#### Points to be kept on mind while using the whereis command:

Since the `whereis` command uses chdir(change directory 2V) to give you the result in the fastest possible way, the pathnames given with the -M, -S, or -B must be full and well-defined i.e. they must begin with a `/` and should be a valid path that exist in the system’s directories, else it exits without any valid result.
`whereis` command has a hard-coded(code which is not dynamic and changes with specification) path, so you may not always find what you’re looking for.

### Syntax

```
whereis [options] [filename]
```

### Options

-b : This option is used when we only want to search for binaries.
-m : This option is used when we only want to search for manual sections.
-s : This option is used when we only want to search for source files.
-u: This option search for unusual entries. A source file or a binary file is said to be unusual if it does not have any existence in system as per [-bmsu] described along with “–u”. Thus `whereis -m -u *‘ asks for those files in the current directory which have unsual entries.

-B : This option is used to change or otherwise limit the places where whereis searches for binaries.
-M : This option is used to change or otherwise limit the places where whereis searches for manual sections.
-S : This option is used to change or otherwise limit the places where whereis searches for source files.

-f : This option simply terminate the last directory list and signals the start of file names. This must be used when any of the -B, -M, or -S options are used.
-V: Displays version information and exit.
-h: Displays the help and exit.