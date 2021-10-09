# The `chmod` command

The `chmod` command allows you to change the permissions on a file using either a symbolic or numeric mode or a reference file.

### Examples:

1. Change the permission of a file using symbolic mode:

```
chmod u=rwx,g=rx,o=r myfile
```

The command above means :

- user can read, write, execute `myfile`
- group can read, execute `myfile`
- other can read `myfile`

2. Change the permission of a file using numeric mode

```
chmod 754 myfile user:group file.txt
```

The command above means :

- user can read, write, execute `myfile`
- group can read, execute `myfile`
- other can read `myfile`

3. Change the permission of a folder recursively

```
chmod -R 754 folder
```

### Syntax:

```
chmod [OPTIONS] MODE FILE(s)
```

- `[OPTIONS]` :
  -R: recursive, mean all file inside directory

- `MODE`: different way to set permissions:

- **symbolic mode explained**

  - u: user
  - g: group
  - o: other
  - =: set the permission
  - r: read
  - w: write
  - x: execute
  - example `u=rwx` means user can read write and execute

- **numeric mode explained**:

  - 4 stands for "read",
  - 2 stands for "write",
  - 1 stands for "execute", and
  - 0 stands for "no permission."
  - example 7 mean read + write + execute
