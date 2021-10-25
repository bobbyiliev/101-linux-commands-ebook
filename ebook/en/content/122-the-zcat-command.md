# The `zcat` command

The `zcat` allows you to look at a compressed file.
  

### Examples:

1. To view the content of a compressed file:

```
~$ zcat test.txt.gz
Hello World
```

2. It can also Works with multiple files:

```
~$ zcat test2.txt.gz test.txt.gz
hello
Hello world
```

### Syntax:

The general syntax for the `zcat` command is as follows:

```
zcat [  -n ] [  -V ] [  File ... ]
```

