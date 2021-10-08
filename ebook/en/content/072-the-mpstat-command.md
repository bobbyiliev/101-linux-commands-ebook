# The `mpstat` command

The `mpstat` command is used to report processor related statistics. It accurately displays the statistics of the CPU usage of the system and information about CPU utilization and performance.

### Syntax:

```
mpstat [options] [<interval> [<count>]]

```

#### Note : It initializes the first processor with CPU 0, the second one with CPU 1, and so on.

### Options and their Functionalities:

|**Option**   |**Description**   |
|:---|:---|
|`-A`|to display all the detailed statistics|
|`-h`|to display mpstat help|
|`-I`|to display detailed interrupts statistics|
|`-n`|to report summary CPU statistics based on NUMA node placement|
|`-N`|to indicate the NUMA nodes for which statistics are to be reported|
|`-P`|to indicate the processors for which statistics are to be reported|
|`-o`|to display the statistics in JSON (Javascript Object Notation) format|
|`-T`|to display topology elements in the CPU report|
|`-u`|to report CPU utilization|
|`-v`|to display utilization statistics at the virtual processor level|
|`-V`|to display mpstat version|
|`-ALL`|to display detailed statistics about all CPUs|


### Examples:

1. To display processor and CPU statistics:
```
mpstat
```

2. To display processor number of all CPUs:
```
mpstat -P ALL
```

3. To get all the information which the tool may collect: 
```
mpstat -A
```

4. To display CPU utilization by a specific processor: 
```
mpstat -P 0
```

5. To display CPU usage with a time interval:
``` 
mpstat 1 5
```
**Note: This command will print 5 reports with 1 second time interval**
