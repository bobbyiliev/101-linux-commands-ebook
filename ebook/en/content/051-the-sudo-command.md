# The `sudo` command

The `sudo` ("substitute user do" or "super user do") command allows a user with proper permissions to execute a command as another user, such as the superuser.

This is the equivalent of "run as administrator" option in Windows. The `sudo` command allows you to elevate your current user account to have root privileges. Also, the root privilege in `sudo` is only valid for a temporary amount of time. Once that time expires, you have to enter your password again to regain root privilege.

> WARNING: Be very careful when using the `sudo` command. You can cause irreversible and catastrophic changes while acting as root!

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

## Examples
This command switches your command prompt to the BASH shell as a root user:

```
sudo bash
```
Your command line should change to:

```
root@hostname:/home/[username]
```

Adding a string of text to a file is often used to add the name of a software repository to the sources file, without opening the file for editing. Use the following syntax with echo, sudo and tee command:


```
echo ‘string-of-text’ | sudo tee -a [path_to_file]
```

Example:

````
echo "deb http://nginx.org/packages/debian `lsb_release -cs` nginx" \ | sudo tee /etc/apt/sources.list.d/nginx.list
````
