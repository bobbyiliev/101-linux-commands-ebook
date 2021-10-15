# The `who` command

The `who` command lets you print out a list of logged-in users, the current run level of the system and the time of last system boot.

### Examples

1. Print out all details of currently logged-in users

```
who -a  
```

2. Print out the list of all dead processes

```
who -d -H
```

### Syntax:

```
who [options] [filename] 
```

### Additional Flags and their Functionalities

|**Short Flag**    |**Description**   |
|---|---|
| `-r` |prints all the current runlevel  |
| `-d` |print all the dead processes  |
|`-q`|print all the login names and total number of logged on users |
|`-h`|print the heading of the columns displayed |
|`-b`|print the time of last system boot |