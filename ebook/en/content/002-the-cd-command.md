# The `cd` command


The `cd` command is used to change the current working directory *(i.e., in which the current user is working)*. 
The "cd" stands for 'change directory.' an it is one of the most frequently used commands in the Linux terminal.

The `cd` command stands for `chdir` (**Ch**ange **Dir**ectory), Often combined with the `ls` command that shows files and folders, `cd` allows you to navigate through folders/directorys, Much like navigating through chapters and pages in a book.

It Normally Lists the files and directories in ascending alphabetical order after typing `cd` and pressing `TAB` 2 times.

### Examples of uses:


1. To change our current working directory, execute the command as follows:

```
cd <specified_directory_path>
```

2. To change the directory to home directory from the current working directory, execute the command as follows:

```
cd ~
```

or simply

```
cd
```

3. To change to the previous directory from the current working directory, we can execute this command:

```
cd -
```

It will also show you the absolute path of your previous working directory

4. To navigate to the system's root directory from current working directory, execute the command as follows:

```
cd /
```

5. To navigate through multiple folders:

```
cd {Directory_Path}
cd /home/user/101-linux-commands-ebook/ebook/en/content/
```

### Quick Tips

Adding a `..` as a directory will allow you to move "up" from a folder, this can be done multiple times too!
eg. `cd ..` to move up one folder or `cd ../../../` to move up 3!

### Syntax:

```
cd [OPTIONS] directory
```

### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-L`|<center>-</center>|Follow symbolic links. By default,`cd` behaves as if the `-L` option is specified.|
|`-P`|<center>-</center>|Don’t follow symbolic links.|
