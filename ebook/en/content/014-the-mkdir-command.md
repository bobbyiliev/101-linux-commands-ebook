# The `mkdir` command

The `mkdir` command in Linux/Unix is used to make a directory.

For example: 

```
mkdir name_of_directory
```

If you want to create a subdirectory within a directory you can use the path to that directory.

For example:

```
mkdir /home/test
```

You can also create sub-directories of a directory. It will create the parent directory first, if it doesn't exist. 
Ff it already exists, then it will not print an error message and will move further to create the sub-directories.

For example:

```
mkdir -p /home/test/src/python
```
