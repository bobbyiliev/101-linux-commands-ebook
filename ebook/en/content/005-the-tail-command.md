# The `tail` command

The `tail` command prints the last ten lines of a file.

Example:
```
tail filename.txt
```

Syntax:
```
tail [OPTION] [FILENAME]
```

### Get a specific number of lines with `tail`:

Use the `-n` option with a number(should be an integer) of lines to display.

Example:
```
tail -n 10 foo.txt
```

This command will display the last ten lines of the file `foo.txt`.

### Refresh the output on any new entry in a file

It is possible to let tail output any new line added to the file you are looking into. So, if a new line is written to the file, it will immediately be shown in your output. This can be done using the `--follow` or `-f` option. This is especially useful for monitoring log files.

Example:
```
tail -f foo.txt
```

Syntax:
```
tail -n <number> foo.txt
```

### Additional Flags and their Functionalities

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-c`|`--bytes=[+]NUM`|Output the last NUM bytes;<br> or use -c +NUM to <br>output starting with byte NUM of each file|
|`-f`|<code>--follow[={name&#124;descriptor}]</code>|Output appended data as the file grows;<br>an absent option argument means 'descriptor'|
|`-F`||Same as --follow=name --retry|
|`-n`|`--lines=[+]NUM`|Output the last NUM lines, instead of the last 10;<br>or use -n +NUM to output starting with line NUM|
||`--max-unchanged-stats=N`|with --follow=name, reopen a FILE which has not<br>changed size after N (default 5) iterations<br>to see if it has been unlinked or rename<br>(this is the usual case of rotated log files);<br>with inotify, this option is rarely useful|
||`--pid=PID`|with -f, terminate after process ID, PID dies|
|`-q`|`--quiet, --silent`|Never output headers giving file names|
|``|`--retry`|keep trying to open a file if it is inaccessible|
|`-s`|`--sleep-interval=N`|With -f, sleep for approximately N seconds<br>(default 1.0) between iterations;<br>with inotify and --pid=P, check process P at<br>least once every N seconds|
|`-v`|`--verbose`|Always output headers giving file names|
|`-z`|`--zero-terminated`|Line delimiter is NUL, not newline|
||`--help`|Display this help and exit|
||`--version`|Output version information and exit|
