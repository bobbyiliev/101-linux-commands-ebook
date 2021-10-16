# The `ifconfig` command

`ifconfig` is used to configure the kernel-resident network interfaces.  It is used at boot time to set up interfaces as necessary.  After that, it is usually only needed when debugging or when system tuning is needed.


If no arguments are given, `ifconfig` displays the status of the currently active interfaces.  If a single interface argument is given, it displays the  status  of the  given interface only; if a single -a argument is given, it displays the status of all interfaces, even those that are down.  Otherwise, it configures an interface.
### Syntax:

```
ifconfig [-v] [-a] [-s] [interface]
```

### Examples:

1. To display the currently active interfaces:

```
ifconfig
```

2. To show all the active interface:

```
ifconfig -a
```

3. To show all the error conditions:

```
ifconfig -v
```

4. To show a shortlist:

```
ifconfig -s
```

### Help Command
Run below command to view the complete guide to `ifconfig` command.
```
man ifconfig
```