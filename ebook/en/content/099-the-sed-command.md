# The `sed` command

`sed` command stands for stream editor. A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline). For instance, it can perform lot’s of functions on files like searching, find and replace, insertion or deletion. While in some ways it is similar to an editor which permits scripted edits (such as `ed`), `sed` works by making only one pass over the input(s), and is consequently more efficient. But it is sed's ability to filter text in a pipeline that particularly distinguishes it from other types of editors.

The most common use of `sed` command is for a substitution or for find and replace. By using sed you can edit files even without opening it, which is a much quicker way to find and replace something in the file. It supports basic and extended regular expressions that allow you to match complex patterns. Most Linux distributions come with GNU and `sed` is pre-installed by default. 

### Examples:

1. To Find and Replace String with `sed`
```
sed -i 's/{search_regex}/{replace_value}/g' input-file
```

2. For Recursive Find and Replace *(along with `find`)*

> Sometimes you may want to recursively search directories for files containing a string and replace the string in all files. This can be done using commands such as find to recursively find files in the directory and piping the file names to `sed`.
The following command will recursively search for files in the current working directory and pass the file names to `sed`. It will recursively search for files in the current working directory and pass the file names to `sed`.

```
find . -type f -exec sed -i 's/{search_regex}/{replace_value}/g' {} +
```

### Syntax:

```
sed [OPTION]... {script-only-if-no-other-script} [INPUT-FILE]... 
```

- `OPTION` - sed options in-place, silent, follow-symlinks, line-length, null-data ...etc.
- `{script-only-if-no-other-script}` - Add the script to command if available.
- `INPUT-FILE` - Input Stream, A file or input from a pipeline.

If no option is given, then the first non-option argument is taken as the sed script to interpret. All remaining arguments are names of input files; if no input files are specified, then the standard input is read.

GNU sed home page: [http://www.gnu.org/software/sed/](http://www.gnu.org/software/sed/)

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-i[SUFFIX]`|<center>--in-place[=SUFFIX]</center>|Edit files in place (makes backup if SUFFIX supplied).|
|`-n`|<center>--quiet, --silent</center>|Suppress automatic printing of pattern space.|
|`-e script`|<center>--expression=script</center>|Add the script to the commands to be executed.|
|`-f script-file`|<center>--file=script-file</center>|Add the contents of script-file to the commands to be executed.|
|`-l N`|<center>--line-length=N</center>|Specify the desired line-wrap length for the `l` command.|
|`-r`|<center>--regexp-extended</center>|Use extended regular expressions in the script.|
|`-s`|<center>--separate</center>|Consider files as separate rather than as a single continuous long stream.|
|`-u`|<center>--unbuffered</center>|Load minimal amounts of data from the input files and flush the output buffers more often.|
|`-z`|<center>--null-data</center>|Separate lines by NULL characters.|

### Before you begin

It may seem complicated and complex at first, but searching and replacing text in files with sed is very simple.

To find out more: [https://www.gnu.org/software/sed/manual/sed.html](https://www.gnu.org/software/sed/manual/sed.html)