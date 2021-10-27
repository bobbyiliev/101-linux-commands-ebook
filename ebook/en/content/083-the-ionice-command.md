# The `ionice` command

The `ionice` command is used to set or get process I/O scheduling class and priority.

If no arguments are given , `ionice` will query the current I/O scheduling class and priority for that process.

## Usage

 ```
ionice [options] -p <pid>
```
 
```
ionice [options] -P <pgid>
```

```
ionice [options] -u <uid>
```

```
ionice [options] <command>
```

## A process can be of three scheduling classes:
- ### Idle
		
	A program with idle I/O priority will only get disk time when `no other program has asked for disk I/O for a defined grace period`.
	
	The impact of idle processes on normal system actively should be `zero`.
	
	This scheduling class `doesn’t take priority` argument.
	
	Presently this scheduling class is permitted for an `ordinary user (since kernel 2.6.25)`.
- ### Best Effort
		
	This is `effective` scheduling class for any process that has `not asked for a specific I/O priority`.
	
	This class `takes priority argument from 0-7`, with `lower` number being `higher priority`.
	
	Programs running at the same best effort priority are served in `round- robbin fashion`.
	
	Note that before kernel 2.6.26  a process that has not asked for an I/O priority formally uses “None” as scheduling class , but the io schedular will treat such processes as if it were in the best effort class. 
	
	The priority within best effort class will be dynamically derived form the CPU nice level of the process : io_priority = ( cpu_nice + 20 ) / 5/
	for kernels after 2.6.26 with CFQ I/O schedular a process that has not asked for sn io priority inherits CPU scheduling class.
	
	`The I/O priority is derived from the CPU nice level of the process` ( smr sd before kernel 2.6.26 ).

- ### Real Time
		
	The real time schedular class is `given first access to disk, regardless of what else is going on in the system`.
	
	Thus the real time class needs to be used with some care, as it cans tarve other processes .
	
	As with the best effort class, `8 priority levels are defined denoting how big a time slice a given process will receive on each scheduling window`.	
	
	This scheduling class is `not permitted for an ordinary user(non-root)`.

## Options
| Options | Description |
|---|---|
| -c, --class <class>   | name or number of scheduling class, 0: none, 1: realtime, 2: best-effort, 3: idle|
| -n, --classdata <num> | priority (0..7) in the specified scheduling class,only for the realtime and best-effort classes|
| -p, --pid <pid>...    | act on these already running processes|
| -P, --pgid <pgrp>...  | act on already running processes in these groups|
| -t, --ignore          | ignore failures|
| -u, --uid <uid>...    | act on already running processes owned by these users|
| -h, --help            | display this help|
| -V, --version         | display version|

For more details see ionice(1).


## Examples
| Command | O/P |Explanation|
|---|---|---|
|`$ ionice` |*none: prio 4*|Running alone `ionice` will give the class and priority of current process |
|`$ ionice -p 101`|*none : prio 4*|Give the details(*class : priority*) of the process specified by given process id|
|`$ ionice -p 2` |*none: prio 4*| Check the class and priority of process with pid 2 it is none and 4 resp.|
|`$ ionice    -c2    -n0    -p2`|2 ( best-effort )	priority 0	process 2 | Now lets set process(pid) 2 as a best-effort program with highest priority|
|$ `ionice` -p 2|best-effort : prio 0| Now if I check details of Process 2 you can see the updated one|
|$ `ionice` /bin/ls||get priority and class info of bin/ls |
|$ `ionice` -n4 -p2||set priority 4 of process with pid 2 |
|$ `ionice` -p 2|  best-effort: prio 4| Now observe the difference between the command ran above and this one we have changed priority from 0 to 4|
|$ `ionice` -c0 -n4 -p2|ionice: ignoring given class data for none class|(Note that before kernel 2.6.26  a process that has not asked for an I/O priority formally uses “None” as scheduling class , |
|||but the io schedular will treat such processes as if it were in the best effort class. )|
|||-t option : ignore failure|
|$ `ionice` -c0 -n4 -p2 -t| | For ignoring the warning shown above we can use -t option so it will ignore failure |

## Conclusion
  
 Thus we have successfully learnt about `ionice` command.
