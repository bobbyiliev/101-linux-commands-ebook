# The `iostat` command

The `iostat` command in Linux is used for monitoring system input/output statistics for devices and partitions. It monitors system input/output by observing the time the devices are active in relation to their average transfer rates. The iostat produce reports may be used to change the system configuration to raised balance the input/output between the physical disks. iostat is being included in sysstat package. If you don’t have it, you need to install first.

### Syntax:

```[linux]
iostat [ -c ] [ -d ] [ -h ] [ -N ] [ -k | -m ] [ -t ] [ -V ] [ -x ]
       [ -z ] [ [ [ -T ] -g group_name ] { device [...] | ALL } ]
       [ -p [ device [,...] | ALL ] ] [ interval [ count ] ]
```

### Examples:

1. Display a single history-since-boot report for all CPU and Devices:
```[linux]
iostat -d 2
```

2. Display a continuous device report at two-second intervals:
```[linux]
iostat -d 2 6
```

3.Display, for all devices, six reports at two-second intervals:
```[linux]
iostat -x sda sdb 2 6
```

4.Display, for devices sda and sdb, six extended reports at two-second intervals:
```[linux]
iostat -p sda 2 6
```

### Additional Flags and their Functionalities:

| **Short Flag**                  | **Description**                                            |                                                                      
| :------------------------------ | :--------------------------------------------------------- |
| `-x`                            | Show more details statistics information.                  |                                                                      
| `-c`                            | Show only the cpu statistic.                               |                                                                      
| `-d`                            | Display only the device report                             |                                                                       
| `-xd                            | Show extended I/O statistic for device only.               |                                                           
| `-k`                            | Capture the statistics in kilobytes or megabytes.          |                                                                      
| `-k23`                          | Display cpu and device statistics with delay.              |
| `-j ID mmcbkl0 sda6 -x -m 2 2`  | Display persistent device name statistics.                 |                                                                      
| `-p `                           | Display statistics for block devices.                      |                                                                
| `-N `                           |  Display lvm2 statistic information.                       | 
