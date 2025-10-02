# The `help` command
The `help` command displays information about builtin commands.
Display information about builtin commands.

If a `PATTERN` is specified, this command gives detailed help on all commands matching the `PATTERN`, otherwise the list of available help topics is printed.

> **Quick Tip:** The `help` command only works for commands that are "built-in" to the Bash shell itself (like `cd`, `pwd`, `echo`, `read`). It will not work for standalone programs like `ls`, `grep`, or `find`. To get help for those, you should use the `man` command (e.g., `man ls`).

## Syntax
```bash
$ help [-dms] [PATTERN ...]
```

## Options
|**Option**|**Description**|
|:--|:--|
|`-d`|Output short description for each topic.|
|`-m`|Display usage in pseudo-manpage format.|
|`-s`|Output only a short usage synopsis for each topic matching the provided `PATTERN`.|

## Examples of uses:
1. We get the complete information about the `cd` command
```bash
$ help cd
cd: cd [-L|[-P [-e]] [-@]] [dir]
    Change the shell working directory.

    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable.
...
(additional details about options and exit status follow)
```
2. We get a short description about the `pwd` command
```bash 	
$ help -d pwd
pwd: pwd [-LP]
    Print the name of the current working directory.
```
3. We get the syntax of the `cd` command
```bash
$ help -s cd
cd [-L|[-P [-e]] [-@]] [dir]
```
