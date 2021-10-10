# The ``lsblk`` command

## Summary
The ``lsblk`` command displays the block and loop devices on the system. It is especially useful when you want to format disks, write filesystems, check the filesystem and know the mount point of a device.


## Examples 

1. Basic usage is fairly simple - just execute 'lsblk' sans any option.
```
lsblk
```

2. Make lsblk display empty devices as well
```
lsblk -a
```

3. Make lsblk print size info in bytes
```
lsblk -b
```

4. Make lsblk print zone model for each device
```
lsblk -z
```

5. Make lsblk skip entries for slaves
```
lsblk -d
```

6. Make lsblk use ascii characters for tree formatting
```
lsblk -i
```

7. Make lsblk display info about device owner, group, and mode
```
lsblk -m
```

8. Make lsblk output select columns

```
lsblk -o NAME,SIZE
```

## Syntax
```
lsblk [options] [<device> ...]
```

## Reading information given by ``lsblk``
On running ``lsblk`` with no flags or command-line arguments, it writes general disk information to the STDOUT.
Here is a table that interpretes that information:

| Column Name | Meaning                           | Interpretation                                              |
|:-----------:|:----------------------------------|:------------------------------------------------------------|
| NAME        | Name of the device.               | Shows name of the device.                                   |
| RM          | Removable.                        | Shows 1 if the device is removable, 0 if not.               |
| SIZE        | Size of the device.               | Shows size of the device.                                   |
| RO          | Read-Only.                        | Shows 1 if read-only, 0 if not.                             |
| TYPE        | The type of block or loop device. | Shows ``disk`` for entire disk and ``part`` for partitions. |
| MOUNTPOINTS | Where the device is mounted.      | Shows where the device is mounted. Empty if not mounted.    |

## Reading information of a specific device
``lsblk`` can display information of a specific device when the device's absolute path is passed to it.
For example, ``lsblk`` command for displaying the information of the ``sda`` disk is:
```
lsblk /dev/sda
```

## Useful flags for ``lsblk``
Here is a table that show some of the useful flags that can be used with lsblk

| **Short Flag**             | **Long Flag**          | **Description**                              |
|:--------------------------:|:-----------------------|:---------------------------------------------|
| ``-a``                     | ``--all``              | `lsblk` does not list empty devices by default. This option disables this restriction.      |
| ``-b``                     | ``--bytes``            | Print the SIZE column in bytes rather than in human-readable format.      |
| ``-d``                     | ``--nodeps``           | Don't print device holders or slaves.        |
| ``-D``                     | ``--discard``          | Print information about the discard (TRIM, UNMAP) capabilities for each device.        |
| ``-E``                     | ``--dedup column``     | Use column as a de-duplication key to de-duplicate output tree. If the key is not available for the device, or the device is a partition and parental whole-disk device provides the same key than the device is always printed.|
| ``-e``                     | ``--exclude list``     | xclude the devices specified by a comma-separated list of major device numbers. Note that RAM disks (major=1) are excluded by default. The filter is applied to the top-level devices only.|
| ``-f``                     | ``--fs``               | Displays information about filesystem.       |
| ``-h``                     | ``--help``             | Print a help text and exit.|
| ``-l``                     | ``--include list``     | Displays all the information in List Format. |
| ``-J``                     | ``--json``             | Displays all the information in JSON Format. |
| ``-l``                     | ``--list``             | Displays all the information in List Format. |
| ``-m``                     | ``--perms``            | Displays info about device owner, group and mode.                 |
| ``-M``                     | ``--merge``            | Group parents of sub-trees to provide more readable output for RAIDs and Multi-path devices. The tree-like output is required.|
| ``-n``                     | ``--noheadings``       | Do not print a header line.                  |
| ``-o``                     | ``--output list``      | Specify which output columns to print. Use `--help` to get a list of all supported columns.              |
| ``-O``                     | ``--output-all``       | Displays all available columns.              |
| ``-p``                     | ``--paths``            | Displays absolute device paths.              |
| ``-P``                     | ``--pairs``            | Use key="value" output format. All potentially unsafe characters are hex-escaped (\x<code>)             |
| ``-r``                     | ``--raw``              | Use the raw output format. All potentially unsafe characters are hex-escaped (\x<code>) in NAME, KNAME, LABEL, PARTLABEL and MOUNTPOINT columns.|
| ``-S``                     | ``--scsi``             | Output info about SCSI devices only. All partitions, slaves and holder devices are ignored.|
| ``-s``                     | ``--inverse``          | Print dependencies in inverse order.                   |
| ``-t``                     | ``--topology``         | Output info about block device topology. This option is equivalent to "-o NAME,ALIGNMENT,MIN-IO,OPT-IO,PHY-SEC,LOG-SEC,ROTA,SCHED,RQ-SIZE".|
| ``-T``                     | ``--tree[=column]``             | Displays all the information in Tree Format. |
| ``-V``                     | ``--version``          | Output version information and exit.         |
| ``-w``                     | ``--width``            |pecifies output width as a number of characters. The default is the number of the terminal columns, and if not executed ona terminal, then output width is not restricted at all by default.|
| ``-x``                     | ``--sort [column]``    | Sort output lines by column. This option enables `--list` output format by default. It is possible to use the option `--tree` to force tree-like output and than the tree branches are sorted by the column.|
| ``-z``                     | ``--zoned``            | Print the zone model for each device.   |
| ``-``                      | ``--sysroot directory``| Gather data for a Linux instance other than the instance from which the lsblk command is issued. The specified directory is the system root of the Linux instance to be inspected.|

## Exit Codes
Like every Unix / Linux Program, ``lslbk`` returns an exit code to the environment.
Here is a table of all the exit codes.

| Exit Code | Meaning                                                    |
|:---------:|:-----------------------------------------------------------|
| 0         | Exit with success.                                         |
| 1         | Exit with failure.                                         |
| 32        | Specified device(s) not found.                             |
| 64        | Some of the specified devices were found while some not.   |
