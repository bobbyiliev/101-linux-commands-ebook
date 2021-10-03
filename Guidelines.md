# Guidelines
This file contains some information and guidelines for contributing to the project.

## Why?
With multiple writers, editors, and PRs, keeping everything consistent for the reader should be a huge goal,
otherwise, going from page to page can lead the reader into more confusion rather than quickly helping them learn and grow.

## The Guidelines
*Obviously, this isn't a rulebook, and this itself should discuss everyone to ensure we get the best possible guidelines and design of the pages*

I've used the LS command by ZeusDes and BobbyIliev as an example as it has good formatting and information.

Commands and Flags outside of code blocks should be "highlighted" with inline code, like so \`ls`



- The start of the document should contain "The 'X' command"
- Below this a summary of what the command does
- Followed by some code block examples
- Next should be the syntax information, such as where flags, extra options, directories, and other information goes
- Afterwards, a table of more flags, including the short flag, long flag and descriptions, should be included
- Lastly, any more information can be included, perhaps such as video examples or interactive/useful sites


## Example



# The `ls` command

The `ls` command lets you see the files and directories inside a Specific directory *(current working directory by default)*.
It Normally Lists the files and directories in ascending alphabetical order.

### Examples:

1. To Show the files inside your current working directory:

```
ls
```

2. To Show the files and directory inside a specific directory:

```
ls {Directory_Path}
```

### Syntax:

```
ls [-OPTION] [DIRECTORY_PATH]
```

### Interactive training

In this interactive tutorial, you will learn the different ways to use the `ls` command:

[The ls command by Tony](https://devdojo.com/tnylea/ls-command)

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-l`|<center>-</center>|Show Results in long format|
|`-S`|<center>-</center>|Sort Results by file size|
|`-t`|<center>-</center>|Sort Results by modification time|
|`-r`|`--reverse`|Show files and directories in reverse order *(descending Alphabetical order)*|
|`-a`|`--all`|Show all files, Including hidden files *(file names which begin with period `.`)*|
|`-A`|`--almost-all`|Shows all like `-a` but without Showing `.`(Current Working Directory) and `..` (Parent Directory)|
|`-d`|`--directory`|Instead of listing the files and directories inside the directory, It Shows information about the directory itself, Can be used with `-l` to show long formatted information|
|`-F`|`--classify`|Appends an indicator character to the end of each listed name, as an example: `/` character is appended after each directory name listed|
|`-h`|`--human-readable`|like `-l` but displays file size in human-readable unit not in bytes
