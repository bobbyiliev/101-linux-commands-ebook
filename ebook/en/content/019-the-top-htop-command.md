# The `top/htop` command

`top` is the default command-line utility that comes pre-installed on Linux distributions and Unix-like operating systems. It is used for displaying information about the system and its top CPU-consuming processes as well as RAM usage.

`htop` is interactive process-viewer and process-manager for Linux and Unix-like operating system based on ncurses. If you take top and put it on steroids, you get htop.

## Comparison between top and htop:

|**Feature**   |**top**   |**htop**   |
|:---|:---|:---|
|Type|Interactive system-monitor, process-viewer and process-manager|Interactive system-monitor, process-viewer and process-manager|
|Operating System|Linux distributions, macOS |Linux distributions, macOS |
|Installation|Built-in and is always there. Also has more adoption due to this fact.|Doesn't come preinstalled on most Linux distros. Manual installation is needed|
|User Interface|Basic text only|Colorful and nicer text-graphics interface|
|Scrolling Support|No|Yes, supports horizontal and vertical scrolling|
|Mouse Support|No|Yes|
|Process utilization|Displays processes but not in tree format|Yes, including user and kernel threads|
|Scrolling Support|No|Yes, supports horizontal and vertical scrolling|
|Mouse Support|No|Yes|
|Process utilization|Displays processes but not in tree format|Yes, including user and kernel threads|
|Network Utilization|No|No|
|Disk Utilization|No|No|
|Comments|Has a learning curve for some advanced options like searching, sending messages to processes, etc. It is good to have some knowledge of top because it is the default process viewer on many systems.|Easier to use and supports vi like searching with `/`. Sending messages to processes (kill, renice) is easier and doesn't require typing in the process number like top.|

## Examples:

###  `top`

1. To display dynamic real-time information about running processes:

```
top
```

2.  Sorting processes by internal memory size (default order - process ID):

```
top -o mem
```

3. Sorting processes first by CPU, then by running time:

```
top -o cpu -O time
```

4. Display only processes owned by given user:

```
top -user {user_name}
```

###  `htop`

1. Display dynamic real-time information about running processes. An enhanced version of `top`.

```
htop
```

2. displaying processes owned by a specific user:

```
htop --user {user_name}
```

3. Sort processes by a specified `sort_item` (use `htop --sort help` for available options):

```
htop --sort {sort_item}
```

## Syntax:

```
top [OPTIONS] 
```

```
htop [OPTIONS] 
```


## Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-a`|<center>-</center>|Sort by memory usage.|
|`-b`|<center>-</center>|Batch mode operation. Starts top in 'Batch mode', which could be useful for sending output from top to other programs or to a file. In this mode, top will not accept input and runs until the iterations limit you've set with the '-n' command-line option or until killed.|
|`-h`|<center>-</center>|`top --user {user_name}` Only display processes owned by user.|
|`-U`|<center>-user</center>|Help.|
|`-u`|<center>-</center>|This is an alias equivalent to: -o cpu -O time.|