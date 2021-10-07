
# The `pstree` command

The `pstree` command is similar to `ps`, but instead of listing the running processes, it shows them as a tree. The tree-like format is sometimes more suitable way to display the processes hierarchy which is a much simpler way to visualize running processes. The root of the tree is either init or the process with the given pid. 

### Examples

1. To display a hierarchical tree structure of all running processes:

```
pstree
```

2. To display a tree with the given process as the root of the tree:

```
pstree [pid]
```

3. To show only those processes that have been started by a user:

```
pstree [USER]
```

4. To show the parent processes of the given process:

```
pstree -s [PID]
```

5. To view the output one page at a time, pipe it to the `less` command:

```
pstree | less
```


### Syntax

`ps [OPTIONS] [USER or PID]`


### Additional Flags and their Functionalities


|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-a`|`--arguments`|Show command line arguments|
|`-A`|`--ascii`|use ASCII line drawing characters|
|`-c`|`--compact`|Don't compact identical subtrees|
|`-h`|`--highlight-all`|Highlight current process and its ancestors|
|`-H PID`|`--highlight-pid=PID`|highlight this process and its ancestors|
|`-g`|`--show-pgids`|show process group ids; implies `-c`|
|`-G`|`--vt100`|use VT100 line drawing characters|
|`-l`|`--long`|Don't truncate long lines|
|`-n`|`--numeric-sort`|Sort output by PID|
|`-N type`|`--ns-sort=type`|Sort by namespace type (cgroup, ipc, mnt, net, pid, user, uts)|
|`-p`|`--show-pids`|show PIDs; implies -c|
|`-s`|`--show-parents`|Show parents of the selected process|
|`-S`|`--ns-changes`|show namespace transitions|
|`-t`|`--thread-names`|Show full thread names|
|`-T`|`--hide-threads`|Hide threads, show only processes|
|`-u`|`--uid-changes`|Show uid transitions|
|`-U`|`--unicode`|Use UTF-8 (Unicode) line drawing characters|
|`-V`|`--version`|Display version information|
|`-Z`|`--security-context`|Show SELinux security contexts|


