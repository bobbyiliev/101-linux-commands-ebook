072-the-mpstat-command.md
# The `mpstat` command

`mpstat` is a command that is used to report processor related statistics. It accurately displays the statistics of the CPU usage of the system. It displays information about CPU utilization and performance. It initializes the first processor with CPU 0, the second one with CPU 1, and so on.

### Syntax:

```[linux]
mpstat [OPTIONS]
```

### Examples:

1. To display processor and CPU statistics.

```[linux]
mpstat
```

2. To display processor number of all CPUs.

```[linux]
mpstat -P ALL
```

3. To get all the information which the tool may collect.

```[linux]
mpstat -A
```

4. To display CPU utilization by a specific processor.

```[linux]
mpstat -P [PROCESSOR]
```

5. To display CPU usage with a time interval.

```[linux]
mpstat [TIME INTERVAL] [NUMBER OF PRINTS]
```

6. To display mpstat version.

```[linux]
mpstat -V 
```

# Cheat sheet

| Item | Description |
| --- | --- |
| `-a` | Displays all the statistics. |
| `-d` | Displays detailed affinity and migration statistics for AIX® threads and dispatching statistics for logical processors.  |
| `-i` | Displays detailed interrupts statistics. |
| `-s` | Displays simultaneous multithreading threads utilization, this flag is available only when `mpstat` runs in a simultaneous multithreading enabled partition.|
| `-h` | Displays pc and processor switches, with stolen and donation statistics for dedicated partitions. |
| `-w` | Displays wide column output, switches to wide output mode. Default is 80 column output mode. |
| `@wparname` | Displays the statistics for the specified WPAR. |
| `-X` | Generates the XML output. The default file name is *mpstat_DDMMYYHHMM.xml* unless you specify a different file name by using with the –o option. |
| `-o` | Specifies the file name for the XML output. |
| `-v` | Displays utilization statistics at the virtual processor level. |
