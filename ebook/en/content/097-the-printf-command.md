097-the-printf-command.md
# The `printf` command

This command lets you print the value of a variable by formatting it using rules. It is pretty similar to the printf in C language.

### Syntax:
```
$printf [-v variable_name] format [arguments]
```

### Examples:
The format specifiers usually used with printf are stated in the examples below:

- %s

```
$printf "%s\n" "Printf command documentation!"
```
This will print `Printf command documentation!` in the shell.

### Other important attributes of printf command:

- `%b` - Prints arguments by expanding backslash escape sequences.
- `%q` - Prints arguments in a shell-quoted format which is reusable as input.
- `%d` , `%i` - Prints arguments in the format of signed decimal integers.
- `%u` - Prints arguments in the format of unsigned decimal integers.
- `%o` - Prints arguments in the format of unsigned octal(base 8) integers.
- `%x`, `%X` - Prints arguments in the format of unsigned hexadecimal(base 16) integers. %x prints lower-case letters and %X prints upper-case letters.
- `%e`, `%E` - Prints arguments in the format of floating-point numbers in exponential notation. %e prints lower-case letters and %E prints upper-case.
- `%a`, `%A` - Prints arguments in the format of floating-point numbers in hexadecimal(base 16) fractional notation. %a prints lower-case letters and %A prints upper-case.
- `%g`, `%G` - Prints arguments in the format of floating-point numbers in normal or exponential notation, whichever is more appropriate for the given value and precision. %g prints lower-case letters and %G prints upper-case.
- `%c` - Prints arguments as single characters.
- `%f` - Prints arguments as floating-point numbers.
- `%s` - Prints arguments as strings.
- `%%` - Prints a "%" symbol.


