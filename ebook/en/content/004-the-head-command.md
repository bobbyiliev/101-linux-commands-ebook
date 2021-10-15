# The `head` command

The `head` command prints the first 10 lines of a file by default.  
  
Example:

```
head filename.txt  
```

Syntax: 

```
head [OPTION] [FILENAME]  
```
  

### Get a specific number of lines:

Use the `-n` option with a number (should be an integer) of lines to display.

Example:
```
head -n 10 foo.txt  
```

This command will display the first 10 lines of file `foo.txt` .
  
Syntax:

```
head -n <~number> foo.txt
```
