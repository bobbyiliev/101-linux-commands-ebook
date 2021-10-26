# The `uname` command
The `uname` command lets you print out system information and defaults to outputting the kernel name.

## Syntax:
```bash
$ uname [OPTION]
```

## Examples
1. Print out all system information.
```bash
$ uname -a
```

2. Print out the kernel version.
```bash
$ uname -v
```

## Options
|**Short Flag**|**Long Flag**|**Description**|
|:-|:-|:-|
|`-a`|`--all`|Print all information, except omit processor and hardware platform if unknown.|
|`-s`|`--kernel-name`|Print the kernel name.|
|`-n`|`--nodename`|Print the network node hostname.|
|`-r`|`--kernel-release`|Print the kernel release.|
|`-v`|`--kernel-version`|Print the kernel version.|
|`-m`|`--machine`|Print the machine hardware name.|
|`-p`|`--processor`|Print the processor type (non-portable).|
|`-i`|`--hardware-platform`|Print the hardware platform (non-portable).|
|`-o`|`--operating-system`|Print the operating system.|
