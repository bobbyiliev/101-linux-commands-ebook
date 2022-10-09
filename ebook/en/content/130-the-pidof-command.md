# The `pidof` command

The `pidof` is a command-line utility that allows you to find the process ID of a running program.

## Syntax
```
pidof [OPTIONS] PROGRAM_NAME
```

To view the help message and all options of the command:
```
[user@home ~]$ pidof -h

 -c           Return PIDs with the same root directory
 -d <sep>     Use the provided character as output separator
 -h           Display this help text
 -n           Avoid using stat system function on network shares
 -o <pid>     Omit results with a given PID
 -q           Quiet mode. Do not display output
 -s           Only return one PID
 -x           Return PIDs of shells running scripts with a matching name
 -z           List zombie and I/O waiting processes. May cause pidof to hang.
```

## Examples:
To find the PID of the SSH server, you would run:

```
pidof sshd
```

If there are running processes with names matching `sshd`, their PIDs will be displayed on the screen. If no matches are found, the output will be empty.

```
# Output
4382 4368 811
```

`pidof` returns `0` when at least one running program matches with the requested name. Otherwise, the exit code is `1`. This can be useful when writing shell scripts.

To be sure that only the PIDs of the program you are searching for are displayed, use the full pathname to the program as an argument. For example, if you have two running programs with the same name located in two different directories pidof will show PIDs of both running programs.

By default, all PIDs of the matching running programs are displayed. Use the `-s` option to force pidof to display only one PID:

```
pidof -s program_name
```

The `-o` option allows you to exclude a process with a given PID from the command output:

```
pidof -o pid program_name
```

When pidof is invoked with the `-o` option, you can use a special PID named %PPID that represents the calling shell or shell script.

To return only the PIDs of the processes that are running with the same root directory, use the `-c` option.
This option works only pidof is run as `root` or `sudo` user:

```
pidof -c pid program_name
```

## Conclusion

The `pidof` command is used to find out the PIDs of a specific running program.

`pidof` is a simple command that doesn’t have a lot of options. Typically you will invoke pidof only with the name of the program you are searching for.
