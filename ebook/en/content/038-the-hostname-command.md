# The `hostname` command

`hostname`  is used to display the system's DNS name, and to display or set its hostname or NIS domain name.
### Syntax:

```
hostname [-a|--alias] [-d|--domain] [-f|--fqdn|--long] [-A|--all-fqdns] [-i|--ip-address] [-I|--all-ip-addresses] [-s|--short] [-y|--yp|--nis]
```

### Examples:

1. ``` hostname -a, hostname --alias ```
    Display the alias name of the host (if used). This option is deprecated and should not be used anymore.

2. ```hostname -s, hostname --short```
    Display the short host name. This is the host name cut at the first dot.

3.  ```hostname -V, hostname --version```
    Print version information on standard output and exit successfully.


### Help Command
Run below command to view the complete guide to `hostname` command.
```
man hostname
```