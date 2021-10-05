# The `printenv` command

The `printenv` prints the values of the specified [environment  _VARIABLE(s)_](https://www.computerhope.com/jargon/e/envivari.htm). If no [_VARIABLE_](https://www.computerhope.com/jargon/v/variable.htm) is specified, print name and value pairs for them all.

### Examples:

1. Display the values of all environment variables.

```
printenv
```

2. Display the location of the current user's [home directory](https://www.computerhope.com/jargon/h/homedir.htm).
```
printenv HOME
```

3. To use the `--null` command line option as the terminating character between output entries.
```
printenv --null SHELL HOME
```
*NOTE: By default, the* `printenv` *command uses newline as the terminating character between output entries.*


### Syntax:

```
printenv [OPTION]... PATTERN...
```


### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-0`|`--null`|End each output line with **0** byte rather than [newline](https://www.computerhope.com/jargon/n/newline.htm).|
|`--help`|<center>-</center>|Display a help message, and exit.|
