
# The `basename` command

The `basename` is a command-line utility that strips directory from given file names. Optionally, it can also remove any trailing suffix. It is a simple command that accepts only a few options.

### Examples

The most basic example is to print the file name with the leading directories removed:

```bash
basename /etc/bar/foo.txt
```

The output will include the file name:

```bash
foo.txt
```

If you run basename on a path string that points to a directory, you will get the last segment of the path. In this example, /etc/bar is a directory.

```bash
basename /etc/bar
```

Output

```bash
bar
```

The basename command removes any trailing `/` characters:

```bash
basename /etc/bar/foo.txt/
```

Output

```bash
foo.txt
```

### Options

1. By default, each output line ends in a newline character. To end the lines with NUL, use the -z (--zero) option.

```bash
$ basename -z /etc/bar/foo.txt
foo.txt$
```

2. The `basename` command can accept multiple names as arguments. To do so, invoke the command with the `-a` (`--multiple`) option, followed by the list of files separated by space. For example, to get the file names of `/etc/bar/foo.txt` and `/etc/spam/eggs.docx` you would run:

```bash
basename -a /etc/bar/foo.txt /etc/spam/eggs.docx
```

```bash
foo.txt
eggs.docx
```

### Syntax

The basename command supports two syntax formats:

```bash
basename NAME [SUFFIX]
basename OPTION... NAME...
```

### Additional functionalities

**Removing a Trailing Suffix**: To remove any trailing suffix from the file name, pass the suffix as a second argument:

```bash
basename /etc/hostname name
host
```

Generally, this feature is used to strip file extensions

### Help Command

Run the following command to view the complete guide to `basename` command.

```bash
man basename
```
