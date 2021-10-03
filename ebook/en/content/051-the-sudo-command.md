# The `sudo` command

The `sudo` ("switch user, do") command allows a user with proper permissions to execute a command as another user. By default, sudo executes commands as root.

### Syntax:

```
sudo [-OPTION] command
```

### Additional Flags and their Functionalities:

|**Flag**  |**Description**   |
|:---|:---|
|`-V`|The -V (version) option causes sudo to print the version number and exit. If the invoking user is already root, the -V option prints out a list of the defaults sudo was compiled with and the machine's local network addresses|
|`-l`|The -l (list) option prints out the commands allowed (and forbidden) the user on the current host.|
|`-L`|The -L (list defaults) option lists out the parameters set in a Defaults line with a short description for each. This option is useful in conjunction with grep.|
|`-h`|The -h (help) option causes sudo to print a usage message and exit.|
|`-v`|If given the `-v` (validate) option, `sudo` updates the user's timestamp, prompting for the user's password if necessary. This extends the sudo timeout for another 5 minutes (or whatever the timeout is set to in sudoers) but does not run a command.|
|`-K`|The -K (sure kill) option to sudo removes the user's timestamp entirely. Likewise, this option does not require a password.|
|`-u`|The -u (user) option causes sudo to run the specified command as a user other than root. To specify a uid instead of a username, use #uid.|
|`-s`|The -s (shell) option runs the shell specified by the SHELL environment variable if it's set or the shell as specified in the file passwd.|
|`--`|The -- flag indicates that sudo should stop processing command line arguments. It is most useful in conjunction with the -s flag.|
