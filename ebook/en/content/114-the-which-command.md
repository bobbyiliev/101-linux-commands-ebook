# The `which` command

`which` command identifies the executable binary that launches when you issue a command to the shell. 
If you have different versions of the same program on your computer, you can use which to find out which one the shell will use.

It has 3 return status as follows:

    0 : If all specified commands are found and executable.
    1 : If one or more specified commands is nonexistent or not executable.
    2 : If an invalid option is specified.

### Syntax

```
which [filename1] [filename2] ...
```

You can pass multiple programs and commands to which, and it will check them in order. 

For example:

```which ping cat uptime date head```

### Options

-a : List all instances of executables found (instead of just the first
one of each).

-s : No output, just return 0 if all the executables are found, or 1
if some were not found