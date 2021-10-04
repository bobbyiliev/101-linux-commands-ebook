# The `tail` command

The `tail` command prints the last 10 lines by default of a file.
  
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

This command will display the first 10 lines of file `foo.txt`.

You can also omit the `n` flag, this example will also give same result as above command:

```
tail -10 foo.txt  
```

### Refresh the output on any new entry in a file

It is possible to let tail output any new line added to the file you are looking into. So if a new log entry is written to the file, it will immediately be shown in your output. This can be done via `--follow` or `-f` as an option.

Example:

```
tail -f foo.txt
```

Syntax:

```
tail -n <~number> foo.txt
```
