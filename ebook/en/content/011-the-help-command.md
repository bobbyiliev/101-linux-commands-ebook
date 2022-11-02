# The `help` command
The `help` command displays information about builtin commands.
Display information about builtin commands.

If a `PATTERN` is specified, this command gives detailed help on all commands matching the `PATTERN`, otherwise the list of available help topics is printed.

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
```
2. We get a short description about the `pwd` command
```bash 	
$ help -d pwd
```
3. We get the syntax of the `cd` command
```bash
$ help -s cd
```
