# The `grep` command

The `grep` filter searches a file for a particular pattern of characters, and displays all lines that contain that pattern.
grep stands for globally search for regular expression and print out. The pattern that is searched in the file is referred to as the regular expression.

### Examples:

1. To search the contents of the destination.txt file for a string("KeY") case insensitively.

```
grep -i "KeY" destination.txt
```

2. Displaying the count of number of matches

```
grep -c "key" destination.txt
```

3. We can search multiple files and only display the files that contains the given string/pattern.

```
grep -l "key" destination1.txt destination2.txt destination3.xt destination4.txt
```

4. To show the line number of file with the line matched.

```
grep -n "key" destination.txt
```

5. If you want to grep the monitored log files, you can add the `--line-buffered` to search them in real time.

```
tail -f destination.txt | grep --line-buffered "key"
```

### Syntax:

The general syntax for the grep command is as follows:

```
grep [options] pattern [files]
```

### Additional Flags and their Functionalities:

| **Short Flag** | **Long Flag**          | **Description**                                                                                 |
| :------------- | :--------------------- | :---------------------------------------------------------------------------------------------- |
| `-c`           | `--count`              | print a count of matching lines for each input file                                             |
| `-h`           | `--no-filename`        | Display the matched lines, but do not display the filenames                                     |
| `-i`           | `--ignore-case`        | Ignores, case for matching                                                                      |
| `-l`           | `--files-with-matches` | Displays list of a filenames only.                                                              |
| `-n`           | `--line-number`        | Display the matched lines and their line numbers.                                               |
| `-v`           | `--invert-match`       | This prints out all the lines that do not matches the pattern                                   |
| `-e`           | `--regexp=`            | Specifies expression with this option. Can use multiple times                                   |
| `-f`           | `--file=`              | Takes patterns from file, one per line.                                                         |
| `-F`           | `--fixed-strings=`     | Interpret patterns as fixed strings, not regular expressions.                                   |
| `-E`           | `--extended-regexp`    | Treats pattern as an extended regular expression (ERE)                                          |
| `-w`           | `--word-regexp`        | Match whole word                                                                                |
| `-o`           | `--only-matching`      | Print only the matched parts of a matching line, with each such part on a separate output line. |
|                | `--line-buffered`      | Force output to be line buffered.                                                               |
