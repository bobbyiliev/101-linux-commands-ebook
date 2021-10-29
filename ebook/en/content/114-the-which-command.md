# The `which` command

`which` command identifies the executable binary that launches when you issue a command to the shell. 
If you have different versions of the same program on your computer, you can use which to find out which one the shell will use.

It has 3 return status as follows:

    0 : If all specified commands are found and executable.
    1 : If one or more specified commands is nonexistent or not executable.
    2 : If an invalid option is specified.

### Examples

1. To find the full path of the ls command, type the following:

```
which ls
```

2. We can provide more than one arguments to the which command:

```
which netcat uptime ping
```

 The which command searches from left to right, and if more than one matches are found in the directories listed in the PATH path variable, which will print only the first one.

3. To display all the paths for the specified command:

```
which [filename] -a
```

4. To display the path of node executable files, execute the command:

```
which node
```

5. To display the path of Java executable files, execute:

```
which java  
```

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