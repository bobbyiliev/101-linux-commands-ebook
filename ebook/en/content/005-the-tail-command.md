# The `tail` command

The `tail` command prints the last ten lines of a file.

Example:
```
tail filename.txt
```

Syntax:
```
tail [OPTION] [FILENAME]
```

### Get a specific number of lines with `tail`:

Use the `-n` option with a number(should be an integer) of lines to display.

Example:
```
tail -n 10 foo.txt
```

This command will display the last ten lines of the file `foo.txt`.

### Refresh the output on any new entry in a file

It is possible to let tail output any new line added to the file you are looking into. So, if a new line is written to the file, it will immediately be shown in your output. This can be done using the `--follow` or `-f` option. This is especially useful for monitoring log files.

Example:
```
tail -f foo.txt
```

Syntax:
```
tail -n <number> foo.txt
```