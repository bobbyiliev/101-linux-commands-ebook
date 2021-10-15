#  The `kill` command

`kill` command in Linux (located in /bin/kill), is a built-in command which is used to terminate processes manually. The `kill` command sends a signal to a process which terminates the process. If the user doesn’t specify any signal which is to be sent along with kill command then default _TERM_ signal is sent that terminates the process.

Signals can be specified in three ways:
-   **By number (e.g. -5)**
-   **With SIG prefix (e.g. -SIGkill)**
-   **Without SIG prefix (e.g. -kill)**
  
### Syntax

```
kill [OPTIONS] [PID]...
```

###  Examples:
1. To display all the available signals you can use below command option:

```
kill -l
```

2. To show how to use a _PID_ with the _kill_ command.

```
$kill pid
```

3. To show how to send signal to processes.
```
kill {-signal | -s signal} pid
```

4. Specify Signal:
	
- using numbers as signals 
```
kill -9 pid
```
- using SIG prefix in signals
```
kill -SIGHUP pid
```
- without SIG prefix in signals
```
kill -HUP pid
```


###  Arguments:
The list of processes to be signaled can be a mixture of names and PIDs.

       pid    Each pid can be expressed in one of the following ways:

              n      where n is larger than 0.  The process with PID n is signaled.

              0      All processes in the current process group are signaled.

              -1     All processes with a PID larger than 1 are signaled.

              -n     where n is larger than 1.  All processes in process group  n  are  signaled.
                     When  an  argument  of  the  form '-n' is given, and it is meant to denote a
                     process group, either a signal must be specified first, or the argument must
                     be  preceded  by  a '--' option, otherwise it will be taken as the signal to
                     send.

       name   All processes invoked using this name will be signaled.
###  Options:
	   -s, --signal signal
              The signal to send.  It may be given as a name or a number.

       -l, --list [number]
              Print a list of signal names, or convert the given signal number to  a  name.   The
              signals can be found in /usr/include/linux/signal.h.

       -L, --table
              Similar to -l, but it will print signal names and their corresponding numbers.

       -a, --all
              Do  not  restrict the command-name-to-PID conversion to processes with the same UID
              as the present process.

       -p, --pid
              Only print the process ID (PID) of the named processes, do not send any signals.

       --verbose
              Print PID(s) that will be signaled with kill along with the signal.


