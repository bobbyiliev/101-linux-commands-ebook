# The `w` command

The `w`  command displays information about the users that are currently active on the machine and their [processes](https://www.computerhope.com/jargon/p/process.htm).

### Examples:

1. Running the `w` command without [arguments](https://www.computerhope.com/jargon/a/argument.htm) shows a list of logged on users and their processes.

```
w
```


2. Show information for the user named *hope*.

```
w hope
```

### Syntax:

```
finger [-l] [-m] [-p] [-s] [username]
```


### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-h`|`--no-header`|Don't print the header.|
|`-u`|`--no-current`|Ignores the username while figuring out the current process and cpu times. *(To see an example of this, switch to the root user with `su` and then run both `w` and `w -u`.)*|
|`-s`|`--short`|Display abbreviated output *(don't print the login time, JCPU or PCPU times).*|
|`-f`|`--from`|Toggle printing the from *(remote hostname)* field. The default as released is for the from field to not be printed, although your system administrator or distribution maintainer may have compiled a version where the from field is shown by default.|
|`--help`|<center>-</center>|Display a help message, and exit.|
|`-V`|`--version`|Display version information, and exit.|
|`-o`|`--old-style`|Old style output *(prints blank space for idle times less than one minute)*.|
|*`user`*|<center>-</center>|Show information about the specified the user only.|


### Additional Information

The  [header](https://www.computerhope.com/jargon/h/header.htm)  of the output shows (in this order): the current time, how long the system has been running, how many users are currently logged on, and the system  [load](https://www.computerhope.com/jargon/l/load.htm)  averages for the past 1, 5, and 15 minutes.

The following entries are displayed for each user: 
- login name the  [tty](https://www.computerhope.com/jargon/t/tty.htm) 
- name the  [remote](https://www.computerhope.com/jargon/r/remote.htm) 
- [host](https://www.computerhope.com/jargon/h/hostcomp.htm)  they are
- logged in from the amount of time they are logged in their 
- [idle](https://www.computerhope.com/jargon/i/idle.htm)  time JCPU
- PCPU 
- [command line](https://www.computerhope.com/jargon/c/commandi.htm)  of their current process

The JCPU time is the time used by all processes attached to the tty. It does not include past background jobs, but does include currently running background jobs.

The PCPU time is the time used by the current process, named in the "what" field.
