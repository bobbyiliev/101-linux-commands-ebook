097-the-printf-command.md
# The `printf` command

This command lets you print the value of a variable by formatting it using rules. It is pretty similar to the printf in C language.

### Syntax:
```
$printf [-v variable_name] format [arguments]
```

### Options:

| OPTION      | Description                                                                                        |
| ---         | ---                                                                                                |
| `FORMAT`    | FORMAT controls the output, and defines the way that the ARGUMENTs will be expressed in the output |
| `ARGUMENT`  | An ARGUMENT will be inserted into the formatted output according to the definition of FORMAT       |
| `--help`    | Display help and exit |                                                                                      |
| `--version` | Output version information adn exit |                                                                        |

### Formats:

The anatomy of the FORMAT string can be extracted into three different parts,

- _ordinary characters_, which are copied exactly the same characters as were used originally to the output.
- _interpreted character_ sequences, which are escaped with a backslash ("\\").
- _conversion specifications_, this one will define the way the ARGUMENTs will be expressed as part of the output.


You can see those parts in this example,

```
printf " %s is where over %d million developers shape \"the future of sofware.\" " Github 65
```

The output:

```
Github is where over 65 million developers shape "the future of sofware."
```

The are two conversion specifications `%s` and `%d`, and there are two escaped characters which are the opening and closing double-quotes wrapping the words of _the future of software_. Other than that are the ordinary characters. 

### Conversion Specifications:

Each conversion specification begins with a `%` and ends with a `conversion character`. Between the `%` and the `conversion character` there may be, in order:

|     |     |
| --- | --- |
| `-`        | A minus sign. This tells printf to left-adjust the conversion of the argument |
| _number_   | An integer that specifies field width; printf prints a conversion of ARGUMENT in a field at least number characters wide. If necessary it will be padded on the left (or right, if left-adjustment is called for) to make up the field width |
| `.`	     | A period, which separates the field width from the precision |
| _number_   | An integer, the precision, which specifies the maximum number of characters to be printed from a string, or the number of digits after the decimal point of a floating-point value, or the minimum number of digits for an integer |
| `h` or `l` |	These differentiate between a short and a long integer, respectively, and are generally only needed for computer programming |

The conversion characters tell `printf` what kind of argument to print out, are as follows:

| Conversion char |	Argument type |
| --- | --- |
| `s`    | A string |
| `c`    | An integer, expressed as a character corresponds ASCII code |
| `d, i`    | An integer as a decimal number |
| `o`    | An integer as an unsigned octal number |
| `x, X`    | An integer as an unsigned hexadecimal number |
| `u`    | An integer as an unsigned decimal number |
| `f`    | A floating-point number with a default precision of 6 |
| `e, E`    | A floating-point number in scientific notation |
| `p`    | A memory address pointer |
| `%`    | No conversion |



Here is the list of some examples of the `printf` output the ARGUMENT. we can put any word but in this one we put a 'linuxcommand` word and enclosed it with quotes so we can see easier the position related to the whitespaces.

| FORMAT string | ARGUMENT string   | Output string   |
| ---           | ---               | ---             |
| `"%s"`	    | `"linuxcommand"`  | "linuxcommand"  | 
| `"%5s"`	    | `"linuxcommand"`	| "linuxcommand"  |
| `"%.5s"`	    | `"linuxcommand"`	| "linux"         |
| `"%-8s"`      | `"linuxcommand"`	| "linuxcommand"  |
| `"%-15s"`     | `"linuxcommand"`	| "linuxcommand " |
| `"%12.5s"`    | `"linuxcommand"`	| " linux"        |
| `"%-12.5"`    | `"linuxcommand"`	| "linux "        |
| `"%-12.4"`    | `"linuxcommand"`	| "linu "         |

Notes:

- `printf` requires the number of conversion strings to match the number of ARGUMENTs 
- `printf` maps the conversion strings one-to-one, and expects to find exactly one ARGUMENT for each conversion string
- Conversion strings are always interpreted from left to right.

Here's the example:

The input

```
printf "We know %f is %s %d" 12.07 "larger than" 12
```

The output:

```
We know 12.070000 is larger than 12
```

The example above shows 3 arguments, _12.07_, _larger than_, and _12_. Each of them interpreted from left to right one-to-one with the given 3 conversion strings (`%f`, `%d`, `%s`).

Character sequences which are interpreted as special characters by `printf`:

| Escaped char | Description   |
| ---     | ---    |
| `\a`    |	issues an alert (plays a bell). Usually ASCII BEL characters |
| `\b`    |	prints a backspace                    |
| `\c`    |	instructs `printf` to produce no further output |
| `\e`    |	prints an escape character (ASCII code 27) |
| `\f`    |	prints a form feed |
| `\n`    |	prints a newline |
| `\r`    |	prints a carriage return |
| `\t`    |	prints a horizontal tab |
| `\v`    |	prints a vertical tab |
| `\"`    | prints a double-quote (") |
| `\\`	  | prints a backslash (\) |
| `\NNN`  |	prints a byte with octal value `NNN` (1 to 3 digits)
| `\xHH`  |	prints a byte with hexadecimal value `HH` (1 to 2 digits)
| `\uHHHH`|	prints the unicode character with hexadecimal value `HHHH` (4 digits) |
| `\UHHHHHHHH` |	prints the unicode character with hexadecimal value `HHHHHHHH` (8 digits) |
| `%b`	  |	prints ARGUMENT as a string with "\\" escapes interpreted as listed above, with the exception that octal escapes take the form `\0` or `\0NN` |


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


#### More Examples:

The input:
```
printf 'Hello\nyoung\nman!'
```
The output:

```
hello 
young
man!
```

The two `\n` break the sentence into 3 parts of words.



The input:
```
printf "%f\n" 2.5 5.75
```

The output
```
2.500000
5.750000
```

The `%f` specifier combined with the `\n` interpreted the two arguments in the form of floating point in the seperated new lines.