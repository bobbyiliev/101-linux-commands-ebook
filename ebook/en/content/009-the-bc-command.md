# The `bc` command

The `bc` command provides the functionality of being able to perform mathematical calculations through the command line.

### Examples:

1. To calculate the sum of two numbers:

```
echo "2021 + 10" | bc
```

2. To calculate the square root of a number:

```
echo "2^2" | bc
```

3. To check whether one value is greater than the other or not:

```
echo "10>5" | bc
```

4. To calculate the remainder (modulo):
```
echo "2999%9" | bc
```

### Syntax:

```
bc [ -hlwsqv ] [long-options] [  file ... ]
```

### Additional Flags and their Functionalities:

*Note: This does not include an exhaustive list of options.*

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-i`|`--interactive`|Force interactive mode|
|`-l`|`--mathlib`|Use the predefined math routines|
|`-q`|`--quiet`|Opens the interactive mode for bc without printing the header|
|`-s`|`--standard`|Treat non-standard bc constructs as errors|
|`-w`|`--warn`|Provides a warning if non-standard bc constructs are used|

### Notes:

1. The capabilities of `bc` can be further appreciated if used within a script. Aside from basic arithmetic operations, `bc` supports increments/decrements, complex calculations, logical comparisons, etc.
2. Two of the flags in `bc` refer to non-standard constructs. If you evaluate `100>50 | bc` for example, you will get a strange warning. According to the POSIX page for bc, relational operators are only valid if used within an `if`, `while`, or `for` statement.