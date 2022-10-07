# The `scp` command

SCP (secure copy) is a command-line utility that allows you to securely copy files and directories between two locations.

Both the files and passwords are encrypted so that anyone snooping on the traffic doesn't get anything sensitive.

### Different ways to copy a file or directory:

- From local system to a remote system.
- From a remote system to a local system.
- Between two remote systems from the local system.

### Examples:

1. To copy the files from a local system to a remote system:

```
scp /home/documents/local-file root@{remote-ip-address}:/home/
```

2. To copy the files from a remote system to the local system:
```
scp root@{remote-ip-address}:/home/remote-file /home/documents/
```

3. To copy the files between two remote systems from the local system.
```
scp root@{remote1-ip-address}:/home/remote-file root@{remote2-ip-address}/home/
```
4. To copy file though a jump host server. 
```
scp /home/documents/local-file -oProxyJump=<jump-host-ip> root@{remote-ip-address}/home/
```
On newer version of scp on some machines you can use the above command with a `-J` flag.
```
scp /home/documents/local-file -J <jump-host-ip> root@{remote-ip-address}/home/
```

### Syntax:
```
scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2
```
- `OPTION` - scp options such as cipher, ssh configuration, ssh port, limit, recursive copy …etc.
- `[user@]SRC_HOST:]file1` - Source file
- `[user@]DEST_HOST:]file2` - Destination file

Local files should be specified using an absolute or relative path, while remote file names should include a user and host specification.

scp provides several that control every aspect of its behaviour. The most widely used options are:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-P`|<center>-</center>|Specifies the remote host ssh port.|
|`-p`|<center>-</center>|Preserves files modification and access times.|
|`-q`|<center>-</center>|Use this option if you want to suppress the progress meter and non-error messages.|
|`-C`|<center>-</center>|This option forces scp to compresses the data as it is sent to the destination machine.|
|`-r`|<center>-</center>|This option tells scp to copy directories recursively.|

### Before you begin

The `scp` command relies on `ssh` for data transfer, so it requires an `ssh key` or `password` to authenticate on the remote systems.

The `colon (:)` is how scp distinguish between local and remote locations.

To be able to copy files, you must have at least read permissions on the source file and write permission on the target system.

Be careful when copying files that share the same name and location on both systems, `scp` will overwrite files without warning.

When transferring large files, it is recommended to run the scp command inside a `screen` or `tmux` session.
