# The `tr` command

The tr command in UNIX is a command line utility for translating or deleting characters.
It supports a range of transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters and basic find and replace.
It can be used with UNIX pipes to support more complex translation. tr stands for translate.

### Examples:

1. Convert all lowercase letters in file1 to uppercase.

```
$ cat file1
foo
bar
baz
tr a-z A-Z < file1
FOO
BAR
BAZ
```

2. Make consecutive line breaks into one.

```
$ cat file1
foo


bar


baz
$ tr -s "\n" < file1
foo
bar
baz
```

3. Remove the newline code.

```
$ cat file1
foo
bar
baz
$ tr -d "\n" < file1
foobarbaz%
```

### Syntax:

The general syntax for the tr command is as follows:

```
tr [options] string1 [string2]
```

### Additional Flags and their Functionalities:

| **Short Flag** | **Long Flag** | **Description**                                                                                               |
| :------------- | :------------ | :------------------------------------------------------------------------------------------------------------ |
| `-C`           |               | Complement the set of characters in string1, that is `-C ab` includes every character except for `a` and `b`. |
| `-c`           |               | Same as -C.                                                                                                   |
| `-d`           |               | Delete characters in string1 from the input.                                                                  |
| `-s`           |               | If there is a sequence of characters in string1, combine them into one.                                       |
