
# The `ionice` command


The `ionice` command is used to set or get process I/O scheduling class and priority.

### Examples of uses:


1.Sets process with PID 12 as an idle I/O process:

```
ionice -c 3 -p 12
```

2.   Prints the class and priority of the processes with PID 12 and 21.
```
ionice -p 12 21
```

### Syntax:

```
ionice [-c class] [-n level] [-t] command
```


### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-p`|`--pid`|Specify the process IDs of running processes for which scheduling parameters should be retrieved or set.|
|`-t`|`--ignore`|Ignore the request for a priority that hasn't been specified.|
|`-h`|`--help`|Dislay the help text|
|`-u`|`--uid`|Specify the user IDs of running processes for which to get or set the scheduling parameters|
