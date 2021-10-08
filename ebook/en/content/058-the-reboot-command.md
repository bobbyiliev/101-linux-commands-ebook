# The `reboot` Command
---

  `halt`, `poweroff`, and `reboot` are commands you can run as root to stop the system hardware.

* `halt` instructs the hardware to stop all CPU functions.
* `poweroff` sends an ACPI signal which instructs the system to power down.
* `reboot` instructs the system to reboot.

These commands require superuser `privileges`. If you are not logged in as root, you need to prefix the command with `sudo` or the signal isn't sent.

These programs allow a system administrator to reboot, halt or poweroff the system.

When called with **--force** or when in `runlevel` 0 or 6, this tool invokes the `reboot` system call itself (with REBOOTCOMMAND argument passed) and directly reboots the system. Otherwise, this invokes the `shutdown` tool with the appropriate arguments without passing REBOOTCOMMAND argument.

Before invoking reboot, a shutdown time record is first written to **/var/log/wtmp**


## Examples: 

1. If you are logged in as root, issuing the reboot command will immediately initiate a reboot sequence. The system shuts down and then commence a **warm boot.**

```
reboot
```
2. Execute the reboot command as root.
```
sudo reboot
```


## Syntax
```
reboot [OPTION]... [REBOOTCOMMAND]
```

## Additional Flags and their Functionalities:

|Short Flag |	Long Flag |	Description|
|---|---|---|
|`-f `| `--force`	| Does not invoke shutdown and instead performs the actual action you would expect from the name.|
|`-p` | `--poweroff` |	Instructs the halt command to instead behave as poweroff.|
|`-w` | `--wtmp-only` |	Does not call shutdown or the reboot system call and instead only writes the shutdown record to /var/log/wtmp.|
|- |`--verbose`	|Outputs slightly more verbose messages when rebooting, which can be useful for debugging problems with shutdown.|


## Environment
|	ENV |	Description|
|---|---|
| `RUNLEVEL` |	reboot will read the current runlevel from this environment variable if set in preference to reading from /var/run/utmp.|
## Files
|	File |	Description|
|---|---|
| `/var/run/utmp` |	File where the current runlevel will be read from; this file also be updated with the runlevel record being replaced by a shutdown time record.|
| `/var/log/wtmp` |	A new runlevel record for the shutdown time will be appended to this file.|

