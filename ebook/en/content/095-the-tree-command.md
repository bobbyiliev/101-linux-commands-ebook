# The `tree` command

The `tree` command in Linux recursively lists directories as tree structures. Each listing is indented according to its depth relative to root of the tree.

### Examples:

1. Show a tree representation of the current directory.

```
tree
```

2. -L NUMBER limits the depth of recursion to avoid display very deep trees.

```
tree -L 2 /
```

### Syntax:

```
tree  [-acdfghilnpqrstuvxACDFQNSUX]  [-L  level [-R]] [-H baseHREF] [-T title]
      [-o filename] [--nolinks] [-P pattern] [-I  pattern]  [--inodes]
      [--device] [--noreport] [--dirsfirst] [--version] [--help] [--filelimit #]
      [--si] [--prune] [--du] [--timefmt  format]  [--matchdirs]  [--from-file]
      [--] [directory ...]
```


### Additional Flags and their Functionalities:

|**Flag**   |**Description**   |
|:---|:---|
|`-a`|Print all files, including hidden ones.|
|`-d`|Only list directories.|
|`-l`|Follow symbolic links into directories.|
|`-f`|Print the full path to each listing, not just its basename.|
|`-x`|Do not move across file-systems.|
|`-L #`|Limit recursion depth to #.|
|`-P REGEX`|Recurse, but only list files that match the REGEX.|
|`-I REGEX`|Recurse, but do not list files that match the REGEX.|
|`--ignore-case`|Ignore case while pattern-matching.|
|`--prune`|Prune empty directories from output.|
|`--filelimit #`|Omit directories that contain more than # files.|
|`-o FILE`|Redirect STDOUT output to FILE.|
|`-i`|Do not output indentation.|
