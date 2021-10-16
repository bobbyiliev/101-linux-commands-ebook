# The `killall` command

`killall` sends a signal to **all** processes running any of the specified commands.  If no signal name is specified, `SIGTERM` is sent. In general, `killall` command kills all processes by knowing the name of the process.

Signals can be specified either by name (e.g. `-HUP` or `-SIGHUP`) or by number (e.g. `-1`) or by option `-s`.

If the command name is not a regular expression (option `-r`) and contains a slash (`/`), processes executing that particular file will be selected for killing, independent of their name.

`killall` returns a zero return code if at least one process has been killed for each listed command, or no commands were listed and at least one process matched the `-u` and `-Z` search criteria. `killall` returns non-zero otherwise.

A `killall` process never kills itself (but may kill other `killall` processes).

### Examples:

1. Kill all processes matching the name `conky` with `SIGTERM`:

```sh
killall conky
# OR
killall -SIGTERM conky
# OR
kilall -15 conky
```

I was able to kill Wine ( which are Windows exe files running on Linux ) applications this way too.

```sh
killall TQ.exe
```

2. List all the supported signals:

```sh
$ killall -l
HUP INT QUIT ILL TRAP ABRT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT
CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
```

As for the numbers.

```sh
$ for s in $(killall -l); do echo -n "$s " && kill -l $s; done
HUP 1
INT 2
QUIT 3
ILL 4
TRAP 5
ABRT 6
BUS 7
FPE 8
KILL 9
USR1 10
SEGV 11
USR2 12
PIPE 13
ALRM 14
TERM 15
STKFLT 16
CHLD 17
CONT 18
STOP 19
TSTP 20
TTIN 21
TTOU 22
URG 23
XCPU 24
XFSZ 25
VTALRM 26
PROF 27
WINCH 28
POLL 29
PWR 30
SYS 31
```

3. Ask before killing, to prevent unwanted kills:

```sh
$ killall -i conky
Kill conky(1685) ? (y/N)
```

4. Kill all processes and wait until the processes die.

```sh
killall -w conky
```

5. Kill based on time:

```sh
# Kill all firefox younger than 2 minutes
killall -y 2m  firefox

# Kill all firefox older than 2 hours
killall -o 2h  firefox
```

### Syntax:

```sh
killall [OPTION]... [--] NAME...
killall -l, --list
killall -V, --version
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-e`|`--exact`|require  an  exact  match for very long names|
|`-I`|`--ignore-case`|case insensitive process name match|
|`-g`|`--process-group`|kill process group instead of process|
|`-y`|`--younger-than`|kill processes younger than TIME|
|`-o`|`--older-than`|kill processes older than TIME|
|`-i`|`--interactive`|ask for confirmation before killing|
|`-l`|`--list`|list all known signal names|
|`-q`|`--quiet`|don't print complaints|
|`-r`|`--regexp`|interpret NAME as an extended regular expression|
|`-s`|`--signal SIGNAL`|send this signal instead of SIGTERM|
|`-u`|`--user USER`|kill only process(es) running as USER|
|`-v`|`--verbose`|report if the signal was successfully sent|
|`-w`|`--wait`|wait for processes to die|
|`-n`|`--ns PID`|match processes that belong to the same namespaces as PID
|`-Z`|`--context`|REGEXP kill only process(es) having context (must precede other arguments)

### Related commands

[kill](/ebook/en/content/034-the-kill-command.md), `pidof`
