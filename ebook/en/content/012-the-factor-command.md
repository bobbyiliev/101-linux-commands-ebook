# The `factor` command
The `factor` command prints the prime factors of each specified integer `NUMBER`. If none are specified on the command line, it will read them from the standard input.

## Syntax
```bash
$ factor [NUMBER]...
```
OR:
```bash
$ factor OPTION
```

## Options
|**Option**|**Description**|
|:--|:--|
|`--help`|Display this a help message and exit.|
|`--version`|Output version information and exit.|

## Examples

1. Print prime factors of a prime number.
```bash
$ factor 50
```

2. Print prime factors of a non-prime number.
```bash
$ factor 75
```
