# The `hostnamectl` command

The `hostnamectl` command provides a proper API used to control Linux system hostname and change its related settings. The command also helps to change the hostname without actually locating and editing the `/etc/hostname` file on a given system.

## Syntax
```
$ hostnamectl [OPTIONS...] COMMAND ...
```
where **COMMAND** can be any of the following

**status**: Used to check the current hostname settings

**set-hostname NAME**: Used to set system hostname 

**set-icon-name NAME**: Used to set icon name for host



## Example

1. Basic usage to view the current hostnames
```
$ hostnamectl 
```
or 
```
$ hostnamectl status
```

2. To change the static host name to _myhostname_. It may or may not require root access
```
$ hostnamectl set-hostname myhostname --static
```

3. To set or change a transient hostname
```
$ hostnamectl set-hostname myotherhostname --transient
```

4. To set the pretty hostname. The name that is to be set needs to be in the double quote(” “).
```
$ hostname set-hostname "prettyname" --pretty
```

