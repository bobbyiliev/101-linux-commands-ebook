# The `pwd` command

The `pwd` stands for Print Working Directory. It prints the path of the current working directory, starting from the root.

Example:
```
pwd
```

The output would be your current directory:

```
/home/your_user/some_directory
```

Syntax:
```
pwd [OPTION]
```

Tip:
You can also check this by printing out the `$PWD` variable:

```
echo $PWD
```

The output would be the same as of the `pwd` command.

### Options:


|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
| `-L` | `--logical` | If the environment variable $PWD contains an absolute name of the current directory with no "." or ".." components, then output those contents, even if they contain symbolic links. Otherwise, fall back to default (-P) behavior. |
| `-P`| `--physical` | Print a fully resolved name for the current directory, where all components of the name are actual directory names, and not symbolic links. |
| ` ` | `--help`| Display a help message, and exit. |
| ` ` | `--version`| Display version information, and exit. |

By default, `pwd' behaves as if `-L' were specified.
