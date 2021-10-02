# The `uname` command

The `uname` command lets you print out system information and defaults to outputting the kernel name.

### Examples

1. Print out all system information

```
uname -a
```

2. Print out the kernel version

```
uname -v
```

### Syntax:

```
uname [OPTION]
```

### Additional Flags and their Functionalities

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-a`|`--all`|print all information, except omit processor and hardware platform if unknown|
|`-s`|`--kernel-name`|print the kernel name|
|`-n`|`--nodename`|print the network node hostname|
|`-r`|`--kernel-release`|print the kernel release|
|`-v`|`--kernel-version`|print the kernel version|
|`-m`|`--machine`|print the machine hardware name|
|`-p`|`--processor`|print the processor type (non-portable)|
|`-i`|`--hardware-platform`|print the hardware platform (non-portable)|
|`-o`|`--operating-system`|print the operating system|
