# The `mkdir` command

The `mkdir` command in Linux/Unix is used to create a directory.

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
If it already exists, then it move further to create the sub-directories without any error message.

For example:

```
mkdir -p /home/test/src/python
```
