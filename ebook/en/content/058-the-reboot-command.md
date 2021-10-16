# The `reboot` Command

The `reboot` command is used to restart a linux system. However, it requires elevated permission using the [sudo](https://github.com/bobbyiliev/101-linux-commands-ebook/blob/main/ebook/en/content/051-the-sudo-command.md) command. Necessity to use this command usually arises after significant system or network updates have been made to the system.

## Syntax
```
reboot [OPTIONS...]
```

### Options
- **–help** : This option prints a short help text and exit.
- **-halt** : This command will stop the machine.
- **-w**, **–wtmp-only** : This option only writes wtmp shutdown entry, it do not actually halt, power-off, reboot.

### Examples
1. Basic Usage. Mainly used to restart without any further details
```
$ sudo reboot
```
However, alternatively the shutdown command with the `-r` option
```
$ sudo shutdown -r now
```

**Note** that the usage of the reboot, halt and power off is almost similar in syntax and effect. Run each of these commands with –help to see the details.

2. The `reboot` command has limited usage, and the `shutdown` command is being used instead of reboot command to fulfill much more advance reboot and shutdown requirements. One of those situations is a scheduled restart. Syntax is as follows
```
$ sudo shutdown –r [TIME] [MESSAGE]
```
Here the TIME has various formats. The simplest one is `now`, already been listed in the previous section, and tells the system to restart immediately. Other valid formats we have are +m, where m is the number of minutes we need to wait until restart and HH:MM which specifies the TIME in a 24hr clock.

**Example to reboot the system in 2 minutes**
```
$ sudo shutdown –r +2
```

**Example of a scheduled restart at 03:00 A.M**
```
$ sudo shutdown –r 03:00
```
3. Cancelling a Reboot. Usually happens in case one wants to cancel a scheduled restart

**Syntax**
```
$ sudo shutdown –c [MESSAGE]
```
**Usage**
```
$sudo shutdown -c "Scheduled reboot cancelled because the chicken crossed the road"
```

4. Checking your reboot logs
```
$ last reboot
```
