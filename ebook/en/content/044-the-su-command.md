# The `su` command

In linux, `su` allows you to run commands with a substitute user and group ID.

When called without arguments, `su` defaults to running an interactive shell as root. 

## Example :

```bash
$ su
```

In case that you wanted to switch to a user called `devdojo`, you could do that by running the following command:

```
$ su devdojo
```

## The syntax of the `su` command is :

```bash
$ su [options] [-] [<user>[<argument>...]]

```

## Options :

```bash
-m, -p         --> do not reset environment variables
-w             --> do not reset specified variables
-g             --> specify the primary group
-G             --> specify a supplemental group
-l             --> make the shell a login shell
-f             --> pass -f to the shell (for csh or tcsh)
-s             --> run <shell> if /etc/shell allows it 
-p             --> create a new pseudo terminal
-h             --> display this help
-v             --> display version
```
