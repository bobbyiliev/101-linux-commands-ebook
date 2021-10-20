# The `cd` command

The `cd` command is used to change the current working directory *(i.e., in which the current user is working)*. The "cd" stands for "**c**hange **d**irectory" and it is one of the most frequently used commands in the Linux terminal.

The `cd` command is often combined with the `ls` command (see chapter 1) when navigating through a system, however, you can also press the `TAB` key two times to list the contents of the new directory you just changed to.

### Examples of uses:

1. Change the current working directory:
```
cd <specified_directory_path>
```

2. Change the current working directory to the home directory:
```
cd ~
```
OR
```
cd
```

3. Change to the previous directory:
```
cd -
```
This will also echo the absolute path of the previous directory.

4. Change the current working directory to the system's root directory:
```
cd /
```

### &#x1F4A1; Quick Tips

Adding a `..` as a directory will allow you to move "up" from a folder:
```
cd ..
```
This can also be done multiple times! For example, to move up three folders:
```
cd ../../../
```

### Syntax:

```
cd [OPTIONS] directory
```

### Additional Flags and Their Functionalities

|**Short flag**   |**Long flag**   |**Description**   |
|:---|:---|:---|
|`-L`|<center>-</center>|Follow symbolic links. By default,`cd` behaves as if the `-L` option is specified.|
|`-P`|<center>-</center>|Don’t follow symbolic links.|
