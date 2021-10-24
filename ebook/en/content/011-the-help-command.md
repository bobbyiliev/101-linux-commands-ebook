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

## Example
```bash
$ help ls
```
