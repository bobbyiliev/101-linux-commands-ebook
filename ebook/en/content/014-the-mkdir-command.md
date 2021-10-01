# The `mkdir` command

The `mkdir` command in Linux/Unix is used to make a directory.

For example: 

```
mkdir name_of_directory
```

If you want to create a directory in a directory use path for that directory.

For example:

```
mkdir /home/test
```

You can also create sub-directories of a directory. It will create parent directory first, if it doesn't exist. But if it already exists, then it will not print an error message and will move further to create sub-directories.

For example:

```
mkdir -p /home/test/src/python
```
