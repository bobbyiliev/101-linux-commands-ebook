
# The `mount` command

The `mount` command is used to mount 'attach' a filesystem and make it accessible by an existing directory structure tree.
### Examples:

1. Displays version information:

```
mount -V
```

2. Attaching filesystem found on device and of type type at the directory dir:

```
mount -t type device dir
```

### Syntax Forms:

```
mount [-lhV]
```
```
mount -a [-fFnrsvw] [-t vfstype] [-O optlist]
```
```
mount [-fnrsvw] [-t fstype] [-o options] device dir
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-h`|<center>`--help`</center>|Dispaly a  help message and exists|
|`-n`|<center>`--no-mtab`</center>|Mount without writing in /etc/mtab|
|`-a`|<center>`--all`</center>|Mount all filesystems (of the given types) mentioned in fstab|
|`-r`|`--read-only`|Mount the filesystem read-only|
|`-w`|`--rw`|Mount the filesystem as read/write.|
|`-M`|`--move`|Move a subtree to some other place.|
|`-B`|`--bind`|Remount a subtree somewhere else *(so that its contents are available in both places)*.|



