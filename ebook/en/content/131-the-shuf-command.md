# The `shuf` command

The `shuf` command in Linux writes a random permutation of the input lines to standard output. It pseudo randomizes an input in the same way as the cards are shuffled. It is a part of GNU Coreutils and is not a part of POSIX. This command reads either from a file or standard input in bash and randomizes those input lines and displays the output.

## Syntax
```
# file shuf
shuf [OPTION] [FILE]

# list shuf
shuf -e [OPTION]... [ARG]

# range shuf
shuf -i LO-HI [OPTION]
```

Like other Linux commands, `shuf` command comes with `-–help` option:
```
[user@home ~]$ shuf --help
Usage: shuf [OPTION]... [FILE]
  or:  shuf -e [OPTION]... [ARG]...
  or:  shuf -i LO-HI [OPTION]...
Write a random permutation of the input lines to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -e, --echo                treat each ARG as an input line
  -i, --input-range=LO-HI   treat each number LO through HI as an input line
  -n, --head-count=COUNT    output at most COUNT lines
  -o, --output=FILE         write result to FILE instead of standard output
      --random-source=FILE  get random bytes from FILE
  -r, --repeat              output lines can be repeated
  -z, --zero-terminated     line delimiter is NUL, not newline
```

## Examples:

### shuf command without any option or argument.

```
shuf
```

When `shuf` command is used without any argument in the command line, it takes input from the user until `CTRL-D` is entered to terminate the set of inputs. It displays the input lines in a shuffled form. If `1, 2, 3, 4 and 5` are entered as input lines, then it generates `1, 2, 3, 4 and 5` in random order in the output as seen in the illustration below:

```
[user@home ~]$ shuf
1
2
3
4
5

4
5
1
2
3
```

Consider an example where Input is taken  from the pipe:

```
{
seq 5 | shuf
}
```

`seq 5` returns the integers sequentially from `1` to `5` while the `shuf` command takes it as input and shuffles the content i.e, the integers from `1` to `5`. Hence, `1` to `5` is displayed as output in random order.

```
[user@home ~]$ {
> seq 5 | shuf
> }
5
4
2
3
1
```

### File shuf

When `shuf` command is used without `-e` or `-i` option, then it operates as a file shuf i.e, it shuffles the contents of the file. The `<file_name>` is the last parameter of the `shuf` command and if it is not given, then input has to be provided from the shell or pipe. 

Consider an example where input is taken from a file:

```
shuf file.txt
```

Suppose file.txt contains 6 lines, then the shuf command displays the input lines in random order as output.

```
[user@home ~]$ cat file.txt
line-1
line-2
line-3
line-4
line-5

[user@home ~]$ shuf file.txt
line-5
line-4
line-1
line-3
line-2
```

Any number of lines can be randomized by using `-n` option.

```
shuf -n 2 file.txt
```

This will display any two random lines from the file.

```
line-5
line-2
```

### List shuf

When `-e` option is used with shuf command, it works as a list shuf. The arguments of the command are taken as the input line for the shuf.

Consider an example:

```
shuf -e A B C D E
```

It will take `A, B, C, D, E` as input lines, and will shuffle them to display the output.

```
A
C
B
D
E
```

Any number of input lines can be displayed using the `-n` option along with `-e` option.

```
shuf -e -n 2 A B C D E
```

This will display any two of the inputs.

```
E
A
```

### Range shuf

When `-i` option is used along with `shuf` command, it acts as a `range shuf`. It requires a range of input as input where `L0` is the lower bound while `HI` is the upper bound. It displays integers from `L0-HI` in shuffled form.

```
[user@home ~]$ shuf -i 1-5
4
1
3
2
5
```

## Conclusion

The `shuf` command helps you randomize input lines. And there are features to limit the number of output lines, repeat lines and even generate random positive integers. Once you're done practicing whatever we've discussed here, head to the tool's [man page](https://linux.die.net/man/1/shuf) to know more about it.