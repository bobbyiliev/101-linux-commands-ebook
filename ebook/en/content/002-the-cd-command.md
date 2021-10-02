# The `cd` command


The `cd` command is used to change the current working directory *(i.e., in which the current user is working)*. 
The "cd" stands for 'change directory.' an it is one of the most frequently used commands in the Linux terminal.

### Examples of uses:


1. To change our current working directory, execute the command as follows:

```
cd <specified_directory_path>
```

3. To change the directory to home directory from the current working directory, execute the command as follows:

```
cd ~
```

4. To change to the previous directory from the current working directory, we can execute these two commands:

```
cd ..
```
or
```
cd -
```

The latter will show you the absolute path of your previous working directory

5. To navigate to the system's root directory from current working directory, execute the command as follows:

```
cd /
```

### Syntax:

```
cd [OPTIONS] directory
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-L`|<center>-</center>|Follow symbolic links. By default,`cd` behaves as if the `-L` option is specified.|
|`-P`|<center>-</center>|Don’t follow symbolic links.|