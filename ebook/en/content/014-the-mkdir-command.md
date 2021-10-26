# The `mkdir` command
The `mkdir` command in Linux/Unix is used to create a directory.


## Syntax
```bash
$ mkdir [-m=mode] [-p] [-v] [-Z=context] directory [directory ...]
```

## Examples
1. Make a directory named **myfiles**.
```bash
$ mkdir myfiles
```

2. Create a directory named **myfiles** at the home directory:
```bash
$ mkdir ~/myfiles
```

3. Create the **mydir** directory, and set its file mode (`-m`) so that all users (`a`) may read (`r`), write (`w`), and execute (`x`) it.
```bash
$ mkdir -m a=rwx mydir
```

You can also create sub-directories of a directory. It will create the parent directory first, if it doesn't exist. 
If it already exists, then it move further to create the sub-directories without any error message.

For directories, this means that any user on the system may view ("read"), and create/modify/delete ("write") files in the directory. Any user may also change to ("execute") the directory, for example with the `cd` command.

4. Create the directory **/home/test/src/python**. If any of the parent directories **/home**, **/home/test**, or **/home/test/src** do not already exist, they are automatically created.
```bash
$ mkdir -p /home/test/src/python
```

## Options
|**Short Flags**|**Long Flags**|**Descriptions**|
|:-|:-|:-|
|`-m`|`--mode=MODE`|Set file mode (as in chmod), not `a=rwx - umask`.|
|`-p`|`--parents`|No error if existing, make parent directories as needed.|
|`-v`|`--verbose`|Print a message for each created directory.|
|`-Z`|`--context=CTX`|Set the SELinux security context of each created directory to CTX.|
|<center>-</center>|`--help`|Display a help message and exit.|
|<center>-</center>|`--version`|Output version information and exit.|
