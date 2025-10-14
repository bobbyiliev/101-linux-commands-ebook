# The `column` Command

The `column` command is used to format its input into multiple columns. It's particularly useful for making text-based tables and improving the readability of command output.

## Command Syntax
```bash
column [options] [file]...
```

## Command Options
- `-t`: Determine the number of columns automatically and create a table
- `-s`: Specify the column delimiter (default is whitespace)
- `-n`: Don't merge multiple adjacent delimiters
- `-c`: Output in column format with specified width
- `-x`: Fill columns before rows
- `-L`: Align all entries to the left
- `-R`: Align all entries to the right
- `-o`: Specify column separator for table output

## Examples

1. Basic Column Formatting
```bash
# Create a simple list and format it into columns
ls | column
```

2. Creating a Table from Delimited Data
```bash
# Format /etc/passwd entries into a neat table
cut -d: -f1,6,7 /etc/passwd | column -t -s:
```

3. Formatting Command Output
```bash
# Display mount information in a clean tabular format
mount | column -t
```

4. Custom Column Separator
```bash
# Format CSV data with custom separator
echo "Name,Age,City\nJohn,25,NYC\nJane,30,LA" | column -t -s,
```

5. Left-aligned Table
```bash
# Create a left-aligned table from space-separated data
ps aux | head -n 5 | column -t -L
```

## Additional Information
- The `column` command is part of the `util-linux` package
- It's particularly useful in shell scripts for formatting output
- Can handle both file input and standard input (stdin)
- Works well with other text processing commands like `cut`, `sort`, and `grep`

## See Also
- [`cut`](098-the-cut-command.md) - remove sections from files
- [`sort`](059-the-sort-command.md) - sort lines of text files
- [`paste`](060-the-paste-command.md) - merge lines of files
- [`tr`](119-the-tr-command.md) - translate or delete characters

## Further Reading
- `man column` - manual page for the column command
- [GNU Coreutils](https://www.gnu.org/software/coreutils/)