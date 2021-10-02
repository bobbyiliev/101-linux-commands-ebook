# The `chown` command

The `chown` command makes it possible to change the ownership of a file or directory.  Users and groups are fundamental in Linux, with `chown` you can 
change the owner of a file or directory. It's also possible to change ownership on folders recursively

### Examples:

1. Change the owner of a file 

```
chown user file.txt
```

2. Change the group of a file

```
chown :group file.txt
```

3. Change the user and group in one line

```
chown user:group file.txt
```

4. Change to ownership on a folder recursively

```
chown -R user:group folder
```

### Syntax:

```
chown [-OPTION] [DIRECTORY_PATH]
```