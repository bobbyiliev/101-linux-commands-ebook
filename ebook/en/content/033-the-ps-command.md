# The `ps` command

The `ps` command is used to identify programs and processes that are running on the system and the resources they are using. It is frequently [pipelined](<https://en.wikipedia.org/wiki/Pipeline_(Unix)>) with other commands like `grep` to search for a program/process or `less` so that the user can analyze the output one page at a time.

Lets say you have a program like openshot which is notorious for hogging system resources when exporting a video and you want to close it, but the GUI has become unresponsive.

### Example

1. You want to find the PID of openshot and kill it.

```
ps aux | grep openshot
kill - <openshot PID>
```

2. To Show all the running processes:

```
ps -A
```


### Syntax

`ps [options]`

When run without any options, it's useless and will print: `CMD` - the executable processes/(program) running, their `PID` - process ID, `TTY` - terminal type and `Time` - How long the process has utilized the CPU or thread.

### Common Option

If you are going to remember only one thing from this page let it be these three letter `aux`:
`a` - which displays all processes running, including those being run by other users.
`u` - which shows the effective user of a process, i.e the person whose file access permissions are used by the process.
`x` - which shows processes that do not have a `TTY` associated with them.

### Additional Options:

|**Option**   |**Description**   |
|:---|:---|
|`a`|Shows list all processes with a terminal (tty)|
|`-A`|Lists all processes. Identical to `-e`|
|`-a`|Shows all processes except both session leaders and processes not associated with a terminal|
|`-d`|Select all processes except session leaders|
|`--deselect`|Shows all processes except those that fulfill the specified conditions. Identical to `-N`|
|`-e`|Lists all processes. Identical to `-A`|
|`-N`|Shows all processes except those that fulfill the specified conditions. Identical to `-deselect`|
|`T`|Select all processes associated with this terminal. Identical to the `-t` option without any argument|
|`r`|Restrict the selection to only running processes|
|`--help simple`|Shows all the basic options|
|`--help all`|Shows every available options|

Another useful command which give a realtime snapshot of the processes and the resources they are using about every ten seconds is `top`.
