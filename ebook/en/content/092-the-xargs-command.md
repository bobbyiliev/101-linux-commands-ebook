# The `xargs` command

`xargs` is used to build and execute command lines from standard input

Some commands like grep can accept input as parameters, but some commands accepts arguments, this is place where xargs came into picture.
### Syntax:

```
xargs [options] [command [initial-arguments]]
```

### Options: 

```
-0, --null
```

Input  items  are terminated by a null character instead of by whitespace, and the quotes and backslash are not special (every character is taken literal‐ly).  Disables the end of file string, which is treated like any other argument.  Useful when input items might contain white space, quote marks, or back‐slashes. 


```
-a file, --arg-file=file
```

Read  items  from  file instead of standard input.  If you use this option, stdin remains unchanged when commands are run.  Otherwise, stdin is redirected
from /dev/null.


```
-o, --open-tty
```

Reopen stdin as /dev/tty in the child process before executing the command.  This is useful if you want xargs to run an interactive application.


```
--delimiter=delim, -d delim
```

Input items are terminated by the specified character.  The specified delimiter may be a single character, a C-style character escape such as  \n,  or  an
octal  or hexadecimal escape code.  Octal and hexadecimal escape codes are understood as for the printf command.   Multibyte characters are not supported.
When processing the input, quotes and backslash are not special; every character in the input is taken literally.  The -d option disables any  end-of-file
string,  which  is treated like any other argument.  You can use this option when the input consists of simply newline-separated items, although it is al‐
most always better to design your program to use --null where this is possible.

```
-p, --interactive
```

Prompt  the  user  about whether to run each command line and read a line from the terminal.  Only run the command line if the response starts with `y' or
`Y'.  Implies -t.


### Examples:


 ```
 find /tmp -name core -type f -print | xargs /bin/rm -f
 ```
Find files named core in or below the directory /tmp and delete them.  Note that this will work incorrectly if there are any  filenames  containing  newlines  or
spaces.


```
find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f
```
Find  files  named core in or below the directory /tmp and delete them, processing filenames in such a way that file or directory names containing spaces or new‐
lines are correctly handled.


```
find /tmp -depth -name core -type f -delete
```

Find files named core in or below the directory /tmp and delete them, but more efficiently than in the previous example (because we avoid the need to use fork(2)
and exec(2) to launch rm and we don't need the extra xargs process).


```
cut -d: -f1 < /etc/passwd | sort | xargs echo
```

Generates a compact listing of all the users on the system.


### Help Command
Run below command to view the complete guide to `xargs` command.
```
man xargs
```