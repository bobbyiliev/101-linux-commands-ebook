# The `ps` command

The `ps` command is used to identify programs and processes that are running on the system and the resources they are using. It is frequently [pipelined](<https://en.wikipedia.org/wiki/Pipeline_(Unix)>) with other commands like `grep` to search for a program/process or `less` so that the user can analyze the output one page at a time.

Lets say you have a program like openshot which is notorious for hogging system resources when exporting a video and you want to close it, but the GUI has become unresponsive.

### Example

You want to find the PID of openshot and kill it.

```
ps aux | grep openshot
kill - <openshot PID>
```

### Syntax

`ps [options]`

When run without any options, it's useless and will print: `CMD` - the executable processes/(program) running, their `PID` - process ID, `TTY` - terminal type and `Time` - How long the process has utilized the CPU or thread.

### Common Option

If you are going to remember only one thing from this page let it be these three letter `aux`:
`a` - which displays all processes running, including those being run by other users.
`u` - which shows the effective user of a process, i.e the person whose file access permissions are used by the process.
`x` - which shows processes that do not have a `TTY` associated with them.

For more options have a look at the man page or the cheat sheet.
`ps --help simple` with the basic options.
`ps --help all` with everything.

Another useful command which give a realtime snapshot of the processes and the resources they are using about every ten seconds is `top`.